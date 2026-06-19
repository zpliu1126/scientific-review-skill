#!/usr/bin/env python3
"""Run MinerU Precision Extract API for one local file.

The script expects MINERU_API_TOKEN in the environment. It uploads the input
file through MinerU's signed URL flow, polls until completion, downloads the
result zip, and extracts it into the output directory.
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import sys
import time
import urllib.error
import urllib.request
import urllib.parse
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


API_BASE = "https://mineru.net/api/v4"


def _json_request(method: str, url: str, token: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {
        "Accept": "*/*",
        "Authorization": f"Bearer {token}",
    }
    if payload is not None:
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from {url}: {body}") from exc


def _upload_file(upload_url: str, file_path: Path) -> None:
    parsed = urllib.parse.urlsplit(upload_url)
    if parsed.scheme != "https":
        raise RuntimeError(f"Expected an HTTPS upload URL, got: {upload_url}")
    body = file_path.read_bytes()
    path = urllib.parse.urlunsplit(("", "", parsed.path, parsed.query, ""))
    connection = http.client.HTTPSConnection(parsed.netloc, timeout=300)
    try:
        connection.request("PUT", path, body=body, headers={})
        response = connection.getresponse()
        response_body = response.read().decode("utf-8", errors="replace")
        if response.status not in (200, 201, 204):
            raise RuntimeError(f"Upload failed with HTTP {response.status}: {response_body}")
    finally:
        connection.close()


def _download(url: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=300) as response:
        output_path.write_bytes(response.read())


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run MinerU precision parsing for one local PDF/document.")
    parser.add_argument("--input", required=True, help="Local PDF/document path.")
    parser.add_argument("--output", required=True, help="Directory for downloaded and extracted results.")
    parser.add_argument("--model-version", default="vlm", choices=("vlm", "pipeline", "MinerU-HTML"))
    parser.add_argument("--language", default="en", help="MinerU language code, for example en or ch.")
    parser.add_argument("--ocr", action="store_true", help="Enable OCR for scanned/image PDFs.")
    parser.add_argument("--poll-seconds", type=int, default=15)
    parser.add_argument("--timeout-minutes", type=int, default=60)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = os.environ.get("MINERU_API_TOKEN") or os.environ.get("MINERU_TOKEN")
    if not token:
        print("MINERU_API_TOKEN or MINERU_TOKEN is not set.", file=sys.stderr)
        return 2

    input_path = Path(args.input).resolve()
    if not input_path.is_file():
        print(f"Input file does not exist: {input_path}", file=sys.stderr)
        return 2

    output_dir = Path(args.output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    data_id = input_path.stem

    payload = {
        "files": [{"name": input_path.name, "data_id": data_id, "is_ocr": bool(args.ocr)}],
        "model_version": args.model_version,
        "enable_formula": True,
        "enable_table": True,
        "language": args.language,
    }

    submit_url = f"{API_BASE}/file-urls/batch"
    submit_result = _json_request("POST", submit_url, token, payload)
    _write_json(output_dir / "mineru_submit_response.json", submit_result)
    if submit_result.get("code") != 0:
        print(f"MinerU submit failed: {submit_result}", file=sys.stderr)
        return 1

    batch_id = submit_result["data"]["batch_id"]
    upload_urls = submit_result["data"]["file_urls"]
    if len(upload_urls) != 1:
        print(f"Expected one upload URL, got {len(upload_urls)}", file=sys.stderr)
        return 1

    _upload_file(upload_urls[0], input_path)

    result_url = f"{API_BASE}/extract-results/batch/{batch_id}"
    deadline = time.time() + args.timeout_minutes * 60
    final_result: dict[str, Any] | None = None
    while time.time() < deadline:
        result = _json_request("GET", result_url, token)
        _write_json(output_dir / "mineru_latest_result.json", result)
        extract_results = result.get("data", {}).get("extract_result", [])
        state = extract_results[0].get("state") if extract_results else "unknown"
        print(f"[{datetime.now(timezone.utc).isoformat()}] state={state}")
        if state == "done":
            final_result = result
            break
        if state == "failed":
            print(f"MinerU parse failed: {extract_results[0].get('err_msg')}", file=sys.stderr)
            return 1
        time.sleep(args.poll_seconds)

    if final_result is None:
        print("Timed out waiting for MinerU parse result.", file=sys.stderr)
        return 1

    extract_result = final_result["data"]["extract_result"][0]
    zip_url = extract_result.get("full_zip_url")
    if not zip_url:
        print(f"Done response did not include full_zip_url: {final_result}", file=sys.stderr)
        return 1

    zip_path = output_dir / f"{input_path.stem}_mineru_result.zip"
    _download(zip_url, zip_path)
    extract_dir = output_dir / "extracted"
    extract_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as archive:
        archive.extractall(extract_dir)

    manifest = {
        "input": str(input_path),
        "output_dir": str(output_dir),
        "model_version": args.model_version,
        "language": args.language,
        "ocr": bool(args.ocr),
        "batch_id": batch_id,
        "zip_path": str(zip_path),
        "extract_dir": str(extract_dir),
        "final_result": final_result,
    }
    _write_json(output_dir / "mineru_parse_manifest.json", manifest)
    print(f"Downloaded: {zip_path}")
    print(f"Extracted: {extract_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
