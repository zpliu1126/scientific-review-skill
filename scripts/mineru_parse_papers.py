#!/usr/bin/env python3
"""Batch-parse local PDFs with the MinerU Precision Extract API.

Token handling is intentionally narrow: the script reads MINERU_TOKEN from the
process environment and never writes it to files or logs.
"""

from __future__ import annotations

import argparse
import csv
import http.client
import json
import os
import re
import shutil
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


API_BASE = "https://mineru.net/api/v4"
MODEL_VERSION = "vlm"
LANGUAGE = "en"
EXTRA_FORMATS = ["html"]
MAX_BATCH_SIZE = 50


@dataclass
class IndexRecord:
    file_name: str
    data_id: str
    state: str
    full_md_path: str
    content_list_path: str
    error_message: str = ""


def make_data_id(pdf_path: Path) -> str:
    """Return a MinerU data_id from the PDF basename without spaces."""
    stem = pdf_path.stem.strip()
    data_id = re.sub(r"\s+", "_", stem)
    data_id = re.sub(r"[^\w.\-\u4e00-\u9fff]+", "_", data_id, flags=re.UNICODE)
    data_id = re.sub(r"_+", "_", data_id).strip("_.")
    return data_id or "pdf"


def parsed_dir_for(pdf_path: Path, output_root: Path) -> Path:
    return output_root / pdf_path.stem


def is_already_parsed(pdf_path: Path, output_root: Path) -> bool:
    parsed_dir = parsed_dir_for(pdf_path, output_root)
    meta_path = parsed_dir / "meta.json"
    full_md_path = parsed_dir / "full.md"
    if not meta_path.is_file() or not full_md_path.is_file():
        return False
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    return meta.get("state") == "done"


def chunks(items: Sequence[Any], size: int) -> Iterator[list[Any]]:
    for start in range(0, len(items), size):
        yield list(items[start : start + size])


def find_pdfs(input_dir: Path) -> list[Path]:
    return sorted(path for path in input_dir.rglob("*.pdf") if path.is_file())


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
        raise RuntimeError(f"HTTP {exc.code}: {body}") from exc


def upload_file(upload_url: str, pdf_path: Path) -> None:
    parsed = urllib.parse.urlsplit(upload_url)
    if parsed.scheme != "https":
        raise RuntimeError(f"Expected HTTPS upload URL for {pdf_path.name}")
    body = pdf_path.read_bytes()
    path = urllib.parse.urlunsplit(("", "", parsed.path, parsed.query, ""))
    connection = http.client.HTTPSConnection(parsed.netloc, timeout=300)
    try:
        connection.request("PUT", path, body=body, headers={})
        response = connection.getresponse()
        response_body = response.read().decode("utf-8", errors="replace")
        if response.status not in (200, 201, 204):
            raise RuntimeError(f"Upload failed for {pdf_path.name}: HTTP {response.status}: {response_body}")
    finally:
        connection.close()


def request_batch(token: str, pdfs: Sequence[Path]) -> dict[str, Any]:
    payload = {
        "files": [{"name": pdf.name, "data_id": make_data_id(pdf)} for pdf in pdfs],
        "model_version": MODEL_VERSION,
        "language": LANGUAGE,
        "enable_table": True,
        "enable_formula": True,
        "extra_formats": EXTRA_FORMATS,
    }
    result = _json_request("POST", f"{API_BASE}/file-urls/batch", token, payload)
    if result.get("code") != 0:
        raise RuntimeError(f"MinerU batch request failed: {result.get('msg') or result}")
    return result


def poll_batch(token: str, batch_id: str, poll_seconds: int, timeout_minutes: int) -> dict[str, Any]:
    deadline = time.time() + timeout_minutes * 60
    result_url = f"{API_BASE}/extract-results/batch/{batch_id}"
    latest: dict[str, Any] = {}
    while time.time() < deadline:
        latest = _json_request("GET", result_url, token)
        extract_results = latest.get("data", {}).get("extract_result", [])
        states = [item.get("state", "unknown") for item in extract_results]
        print(f"{datetime.now(timezone.utc).isoformat()} batch_id={batch_id} states={','.join(states)}")
        if extract_results and all(state in {"done", "failed"} for state in states):
            return latest
        time.sleep(poll_seconds)
    raise RuntimeError(f"Timed out waiting for batch {batch_id}")


def download_file(url: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=300) as response:
        output_path.write_bytes(response.read())


def _copy_first_zip_member(zip_path: Path, output_path: Path, selectors: Iterable[str]) -> str:
    selector_list = list(selectors)
    with zipfile.ZipFile(zip_path) as archive:
        names = archive.namelist()
        selected = ""
        for selector in selector_list:
            for name in names:
                if Path(name).name == selector:
                    selected = name
                    break
            if selected:
                break
        if not selected:
            for name in names:
                basename = Path(name).name
                if basename.endswith("_content_list.json") and not basename.endswith("_content_list_v2.json"):
                    selected = name
                    break
        if not selected:
            for name in names:
                if "content_list" in Path(name).name and name.endswith(".json"):
                    selected = name
                    break
        if not selected:
            return ""
        output_path.write_bytes(archive.read(selected))
        return selected


def store_success(
    pdf_path: Path,
    output_root: Path,
    batch_id: str,
    result: dict[str, Any],
    downloaded_zip: Path,
    model_version: str,
    language: str,
) -> IndexRecord:
    parsed_dir = parsed_dir_for(pdf_path, output_root)
    parsed_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(pdf_path, parsed_dir / "source.pdf")
    shutil.copy2(downloaded_zip, parsed_dir / "result.zip")

    full_md_path = parsed_dir / "full.md"
    content_list_path = parsed_dir / "content_list.json"
    full_member = _copy_first_zip_member(downloaded_zip, full_md_path, ["full.md"])
    content_member = _copy_first_zip_member(downloaded_zip, content_list_path, ["content_list.json"])

    if not full_member:
        raise RuntimeError(f"full.md not found in MinerU result zip for {pdf_path.name}")
    if not content_member:
        raise RuntimeError(f"content_list.json not found in MinerU result zip for {pdf_path.name}")

    meta = {
        "original_pdf": str(pdf_path),
        "source_pdf": str(parsed_dir / "source.pdf"),
        "data_id": result.get("data_id", make_data_id(pdf_path)),
        "batch_id": batch_id,
        "state": result.get("state", "done"),
        "full_zip_url": result.get("full_zip_url", ""),
        "parsed_time": datetime.now(timezone.utc).isoformat(),
        "model_version": model_version,
        "language": language,
        "full_md_zip_member": full_member,
        "content_list_zip_member": content_member,
    }
    (parsed_dir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return IndexRecord(
        file_name=pdf_path.name,
        data_id=str(meta["data_id"]),
        state=str(meta["state"]),
        full_md_path=str(full_md_path),
        content_list_path=str(content_list_path),
    )


def record_for_skipped(pdf_path: Path, output_root: Path) -> IndexRecord:
    parsed_dir = parsed_dir_for(pdf_path, output_root)
    meta_path = parsed_dir / "meta.json"
    data_id = make_data_id(pdf_path)
    if meta_path.is_file():
        try:
            data_id = str(json.loads(meta_path.read_text(encoding="utf-8")).get("data_id", data_id))
        except json.JSONDecodeError:
            pass
    return IndexRecord(
        file_name=pdf_path.name,
        data_id=data_id,
        state="done",
        full_md_path=str(parsed_dir / "full.md"),
        content_list_path=str(parsed_dir / "content_list.json"),
    )


def write_index(output_root: Path, records: Sequence[IndexRecord]) -> None:
    output_root.mkdir(parents=True, exist_ok=True)
    with (output_root / "index.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "file_name",
                "data_id",
                "state",
                "full_md_path",
                "content_list_path",
                "error_message",
            ],
            delimiter="\t",
        )
        writer.writeheader()
        for record in records:
            writer.writerow(record.__dict__)


def write_failures(output_root: Path, failures: Sequence[IndexRecord]) -> None:
    if not failures:
        return
    output_root.mkdir(parents=True, exist_ok=True)
    with (output_root / "failed.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["file_name", "data_id", "state", "error_message"],
            delimiter="\t",
        )
        writer.writeheader()
        for failure in failures:
            writer.writerow(
                {
                    "file_name": failure.file_name,
                    "data_id": failure.data_id,
                    "state": failure.state,
                    "error_message": failure.error_message,
                }
            )


def process_batch(
    token: str,
    pdfs: Sequence[Path],
    output_root: Path,
    poll_seconds: int,
    timeout_minutes: int,
) -> tuple[list[IndexRecord], list[IndexRecord]]:
    records: list[IndexRecord] = []
    failures: list[IndexRecord] = []
    batch_response = request_batch(token, pdfs)
    batch_id = batch_response["data"]["batch_id"]
    upload_urls = batch_response["data"]["file_urls"]
    if len(upload_urls) != len(pdfs):
        raise RuntimeError(f"MinerU returned {len(upload_urls)} upload URLs for {len(pdfs)} PDFs")

    for pdf, upload_url in zip(pdfs, upload_urls):
        print(f"Uploading {pdf.name}")
        upload_file(upload_url, pdf)

    final_response = poll_batch(token, batch_id, poll_seconds, timeout_minutes)
    extract_results = final_response.get("data", {}).get("extract_result", [])
    result_by_data_id = {item.get("data_id"): item for item in extract_results}

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        for pdf in pdfs:
            data_id = make_data_id(pdf)
            result = result_by_data_id.get(data_id)
            if not result:
                failure = IndexRecord(pdf.name, data_id, "failed", "", "", "No result returned by MinerU")
                records.append(failure)
                failures.append(failure)
                continue
            state = result.get("state", "unknown")
            if state != "done":
                failure = IndexRecord(pdf.name, data_id, str(state), "", "", str(result.get("err_msg", "")))
                records.append(failure)
                failures.append(failure)
                continue
            try:
                zip_url = result.get("full_zip_url")
                if not zip_url:
                    raise RuntimeError("Missing full_zip_url")
                downloaded_zip = temp_path / f"{data_id}.zip"
                download_file(zip_url, downloaded_zip)
                records.append(store_success(pdf, output_root, batch_id, result, downloaded_zip, MODEL_VERSION, LANGUAGE))
            except Exception as exc:
                failure = IndexRecord(pdf.name, data_id, "failed", "", "", str(exc))
                records.append(failure)
                failures.append(failure)
    return records, failures


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parse PDFs through the MinerU Precision Extract API.")
    parser.add_argument("--input-dir", default="papers/smallRNA")
    parser.add_argument("--output-dir", default="mineru-parsed")
    parser.add_argument("--limit", type=int, help="Process only the first N unparsed PDFs.")
    parser.add_argument("--force", action="store_true", help="Re-submit PDFs even when meta.json says done.")
    parser.add_argument("--poll-seconds", type=int, default=15)
    parser.add_argument("--timeout-minutes", type=int, default=60)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    token = os.environ.get("MINERU_TOKEN")
    if not token:
        print("MINERU_TOKEN is not set.", file=sys.stderr)
        return 2

    input_dir = Path(args.input_dir)
    output_root = Path(args.output_dir)
    pdfs = find_pdfs(input_dir)
    output_root.mkdir(parents=True, exist_ok=True)

    records: list[IndexRecord] = []
    failures: list[IndexRecord] = []
    to_process: list[Path] = []
    for pdf in pdfs:
        if not args.force and is_already_parsed(pdf, output_root):
            records.append(record_for_skipped(pdf, output_root))
        else:
            to_process.append(pdf)

    if args.limit is not None:
        limited = to_process[: args.limit]
        deferred = to_process[args.limit :]
        to_process = limited
        for pdf in deferred:
            records.append(IndexRecord(pdf.name, make_data_id(pdf), "pending", "", "", "Not processed due to --limit"))

    for batch in chunks(to_process, MAX_BATCH_SIZE):
        batch_records, batch_failures = process_batch(
            token=token,
            pdfs=batch,
            output_root=output_root,
            poll_seconds=args.poll_seconds,
            timeout_minutes=args.timeout_minutes,
        )
        records.extend(batch_records)
        failures.extend(batch_failures)
        write_index(output_root, records)
        write_failures(output_root, failures)

    write_index(output_root, records)
    write_failures(output_root, failures)
    print(f"Indexed {len(records)} PDFs at {output_root / 'index.tsv'}")
    if failures:
        print(f"Failures: {len(failures)} at {output_root / 'failed.tsv'}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
