#!/usr/bin/env python3
"""Check whether PDFs contain an extractable text layer.

This script intentionally uses optional PDF libraries. It prefers PyMuPDF
because it reports page count and page text quickly, then falls back to pypdf.
If neither library is installed, the text-layer status is reported as unknown.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, List, Optional


@dataclass
class TextLayerResult:
    file_path: str
    has_text_layer: str
    page_count: str
    sampled_pages: int
    sampled_text_chars: int
    scanned_or_image_pdf: str
    checker_used: str
    notes: str


def find_pdfs(input_path: Path) -> List[Path]:
    if input_path.is_file():
        return [input_path] if input_path.suffix.lower() == ".pdf" else []
    return sorted(path for path in input_path.rglob("*.pdf") if path.is_file())


def _clean_text(text: Optional[str]) -> str:
    if not text:
        return ""
    return " ".join(text.split())


def _check_with_pymupdf(pdf_path: Path, sample_pages: int) -> Optional[TextLayerResult]:
    try:
        try:
            import fitz  # type: ignore
        except ImportError:
            import pymupdf as fitz  # type: ignore
    except ImportError:
        return None

    try:
        doc = fitz.open(str(pdf_path))
        page_count = len(doc)
        pages_to_sample = min(page_count, sample_pages)
        char_count = 0
        for index in range(pages_to_sample):
            char_count += len(_clean_text(doc[index].get_text("text")))
        doc.close()
        has_text = char_count >= 50
        return TextLayerResult(
            file_path=str(pdf_path),
            has_text_layer="yes" if has_text else "no",
            page_count=str(page_count),
            sampled_pages=pages_to_sample,
            sampled_text_chars=char_count,
            scanned_or_image_pdf="no" if has_text else "yes",
            checker_used="pymupdf",
            notes="" if has_text else "sampled pages contain too little extractable text",
        )
    except Exception as exc:  # pragma: no cover - depends on local PDFs
        return TextLayerResult(
            file_path=str(pdf_path),
            has_text_layer="unknown",
            page_count="unknown",
            sampled_pages=0,
            sampled_text_chars=0,
            scanned_or_image_pdf="unknown",
            checker_used="pymupdf",
            notes=f"PyMuPDF failed: {exc}",
        )


def _check_with_pypdf(pdf_path: Path, sample_pages: int) -> Optional[TextLayerResult]:
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        return None

    try:
        reader = PdfReader(str(pdf_path))
        page_count = len(reader.pages)
        pages_to_sample = min(page_count, sample_pages)
        char_count = 0
        for index in range(pages_to_sample):
            char_count += len(_clean_text(reader.pages[index].extract_text()))
        has_text = char_count >= 50
        return TextLayerResult(
            file_path=str(pdf_path),
            has_text_layer="yes" if has_text else "no",
            page_count=str(page_count),
            sampled_pages=pages_to_sample,
            sampled_text_chars=char_count,
            scanned_or_image_pdf="no" if has_text else "yes",
            checker_used="pypdf",
            notes="" if has_text else "sampled pages contain too little extractable text",
        )
    except Exception as exc:  # pragma: no cover - depends on local PDFs
        return TextLayerResult(
            file_path=str(pdf_path),
            has_text_layer="unknown",
            page_count="unknown",
            sampled_pages=0,
            sampled_text_chars=0,
            scanned_or_image_pdf="unknown",
            checker_used="pypdf",
            notes=f"pypdf failed: {exc}",
        )


def check_pdf_text_layer(pdf_path: Path, sample_pages: int = 5) -> TextLayerResult:
    """Return text-layer status for one PDF."""
    for checker in (_check_with_pymupdf, _check_with_pypdf):
        result = checker(pdf_path, sample_pages)
        if result is not None:
            return result
    return TextLayerResult(
        file_path=str(pdf_path),
        has_text_layer="unknown",
        page_count="unknown",
        sampled_pages=0,
        sampled_text_chars=0,
        scanned_or_image_pdf="unknown",
        checker_used="none",
        notes="Install pymupdf or pypdf to check text layers",
    )


def _write_csv(results: Iterable[TextLayerResult], output_path: Optional[Path]) -> None:
    rows = [asdict(result) for result in results]
    fieldnames = list(asdict(TextLayerResult("", "", "", 0, 0, "", "", "")).keys())
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        handle = output_path.open("w", newline="", encoding="utf-8")
    else:
        handle = sys.stdout
    try:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    finally:
        if output_path:
            handle.close()


def _write_json(results: Iterable[TextLayerResult], output_path: Optional[Path]) -> None:
    payload = [asdict(result) for result in results]
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check whether PDFs have an extractable text layer."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="PDF file or directory to scan recursively.",
    )
    parser.add_argument(
        "--output",
        help="Optional output file. Defaults to stdout.",
    )
    parser.add_argument(
        "--format",
        choices=("csv", "json"),
        default="csv",
        help="Output format.",
    )
    parser.add_argument(
        "--sample-pages",
        type=int,
        default=5,
        help="Number of leading pages to sample.",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    input_path = Path(args.input)
    pdfs = find_pdfs(input_path)
    results = [check_pdf_text_layer(path, args.sample_pages) for path in pdfs]
    output_path = Path(args.output) if args.output else None
    if args.format == "json":
        _write_json(results, output_path)
    else:
        _write_csv(results, output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
