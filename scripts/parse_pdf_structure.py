#!/usr/bin/env python3
"""Parse scientific PDFs into structured Markdown, JSON, and TEI when available."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unicodedata
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

try:
    from check_pdf_text_layer import check_pdf_text_layer, find_pdfs
except ImportError:  # pragma: no cover - supports package-style imports
    from scripts.check_pdf_text_layer import check_pdf_text_layer, find_pdfs  # type: ignore


MANIFEST_FIELDS = [
    "file_path",
    "paper_slug",
    "parser_used",
    "parser_status",
    "has_text_layer",
    "page_count",
    "detected_title",
    "detected_abstract",
    "detected_sections",
    "introduction_detected",
    "methods_detected",
    "results_detected",
    "discussion_detected",
    "references_detected",
    "figure_caption_detected",
    "table_caption_detected",
    "confidence",
    "fallback_used",
    "need_manual_review",
    "notes",
]

SECTION_SYNONYMS = {
    "introduction": [
        "introduction",
        "background",
        "background and aims",
        "background introduction",
        "research background",
        "general introduction",
    ],
    "methods": [
        "materials and methods",
        "material and methods",
        "methods",
        "experimental procedures",
        "experimental design",
        "plant materials and growth conditions",
        "sample preparation",
        "rna extraction and sequencing",
        "statistical analysis",
    ],
    "results": [
        "results",
        "results and analysis",
        "findings",
        "results and discussion",
    ],
    "discussion": [
        "discussion",
        "results and discussion",
        "conclusions",
        "conclusion",
        "general discussion",
    ],
    "references": [
        "references",
        "literature cited",
        "bibliography",
    ],
}


@dataclass
class ParseResult:
    backend: str
    status: str
    markdown: str = ""
    data: Dict[str, Any] = field(default_factory=dict)
    tei_xml: str = ""
    notes: str = ""


@dataclass
class SectionStatus:
    introduction: str
    methods: str
    results: str
    discussion: str
    references: str
    detected_sections: List[str]
    figure_caption_detected: str
    table_caption_detected: str
    confidence: str
    need_manual_review: str
    notes: List[str]


def slugify_pdf(pdf_path: Path) -> str:
    stem = unicodedata.normalize("NFKD", pdf_path.stem)
    ascii_stem = stem.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^A-Za-z0-9]+", "-", ascii_stem).strip("-").lower()
    digest = hashlib.sha1(str(pdf_path).encode("utf-8")).hexdigest()[:8]
    if not slug:
        return f"paper-{digest}"
    return f"{slug[:90]}-{digest}"


def normalize_heading(text: str) -> str:
    value = " ".join(text.strip().split())
    value = re.sub(r"^\s*(section\s*)?([0-9]+|[ivxlcdm]+)(\.[0-9]+)*[\.)]?\s+", "", value, flags=re.I)
    value = value.replace("/", " ")
    value = re.sub(r"[^A-Za-z0-9 ]+", " ", value)
    return " ".join(value.lower().split())


def compact_text(text: str) -> str:
    return " ".join(text.split())


def detect_caption(markdown: str, kind: str) -> str:
    if kind == "figure":
        pattern = r"(?im)^\s*(fig(?:ure)?\.?|图)\s*[\divxlcdm]+[\.:：\s]"
    else:
        pattern = r"(?im)^\s*(table|表)\s*[\dixvlcdm]+[\.:：\s]"
    return "yes" if re.search(pattern, markdown) else "no"


def extract_markdown_headings(markdown: str) -> List[str]:
    headings: List[str] = []
    for line in markdown.splitlines():
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", line)
        if match:
            headings.append(match.group(1).strip())
    return headings


def detect_sections(markdown: str, data: Dict[str, Any]) -> SectionStatus:
    headings: List[str] = []
    for section in data.get("sections", []) or []:
        if isinstance(section, dict) and section.get("heading"):
            headings.append(str(section["heading"]))
    headings.extend(extract_markdown_headings(markdown))

    normalized = [(heading, normalize_heading(heading)) for heading in headings]
    statuses = {
        "introduction": "missing",
        "methods": "missing",
        "results": "missing",
        "discussion": "missing",
        "references": "missing",
    }
    notes: List[str] = []

    for heading, normalized_heading in normalized:
        for canonical, synonyms in SECTION_SYNONYMS.items():
            if normalized_heading in synonyms:
                statuses[canonical] = "confirmed"
        if normalized_heading == "results and discussion":
            statuses["results"] = "combined_results_discussion"
            statuses["discussion"] = "combined_results_discussion"
            notes.append("Results and Discussion is combined; mark combined_results_discussion.")

    references = data.get("references", []) or []
    if references and statuses["references"] == "missing":
        statuses["references"] = "confirmed"

    article_hint = " ".join(
        str(data.get(key, "")) for key in ("title", "abstract", "article_type")
    ).lower()
    if statuses["methods"] == "missing" and re.search(r"\breview\b|综述|meta-analysis", article_hint):
        statuses["methods"] = "not_applicable"
        notes.append("Methods may be not_applicable for a review or synthesis article.")

    body_text = compact_text(markdown)
    if statuses["introduction"] == "missing" and len(body_text) > 1000:
        before_methods = body_text
        method_match = re.search(r"(?i)\b(materials?\s+and\s+methods|methods|experimental procedures)\b", body_text)
        if method_match:
            before_methods = body_text[: method_match.start()]
        if len(before_methods) > 700:
            statuses["introduction"] = "probable_introduction"
            notes.append(
                "Introduction heading was not stable, but early body text appears to provide background."
            )

    figure_caption = "yes"
    if not data.get("figures") and detect_caption(markdown, "figure") == "no":
        figure_caption = "no"
    table_caption = "yes"
    if not data.get("tables") and detect_caption(markdown, "table") == "no":
        table_caption = "no"

    confirmed_count = sum(
        1
        for key in ("introduction", "methods", "results", "discussion", "references")
        if statuses[key] in ("confirmed", "combined_results_discussion", "not_applicable")
    )
    if confirmed_count >= 4:
        confidence = "high"
    elif confirmed_count >= 2 or statuses["introduction"] == "probable_introduction":
        confidence = "medium"
    else:
        confidence = "low"

    need_manual = "yes" if confidence == "low" else "no"
    if statuses["introduction"] != "confirmed":
        need_manual = "yes"
        notes.append("[Introduction 标题未稳定识别，正文结构需人工复核]")
    for key in ("methods", "results", "discussion", "references"):
        if statuses[key] == "missing":
            need_manual = "yes"
            notes.append(f"[需要人工复核] {key} section was not confidently detected.")

    return SectionStatus(
        introduction=statuses["introduction"],
        methods=statuses["methods"],
        results=statuses["results"],
        discussion=statuses["discussion"],
        references=statuses["references"],
        detected_sections=sorted(set(headings)),
        figure_caption_detected=figure_caption,
        table_caption_detected=table_caption,
        confidence=confidence,
        need_manual_review=need_manual,
        notes=notes,
    )


def text_from_element(element: Optional[ET.Element]) -> str:
    if element is None:
        return ""
    return compact_text(" ".join(element.itertext()))


def parse_tei(tei_xml: str) -> Dict[str, Any]:
    ns = {"tei": "http://www.tei-c.org/ns/1.0"}
    root = ET.fromstring(tei_xml)
    title = ""
    for xpath in [
        ".//tei:titleStmt/tei:title[@type='main']",
        ".//tei:titleStmt/tei:title",
        ".//tei:sourceDesc//tei:analytic/tei:title",
    ]:
        title = text_from_element(root.find(xpath, ns))
        if title:
            break

    authors: List[str] = []
    for author in root.findall(".//tei:teiHeader//tei:sourceDesc//tei:analytic//tei:author", ns):
        name = text_from_element(author.find(".//tei:persName", ns)) or text_from_element(author)
        if name:
            authors.append(name)

    abstract = text_from_element(root.find(".//tei:profileDesc/tei:abstract", ns))

    sections: List[Dict[str, str]] = []
    for div in root.findall(".//tei:text/tei:body//tei:div", ns):
        head = text_from_element(div.find("./tei:head", ns))
        if not head:
            continue
        paragraphs = [text_from_element(p) for p in div.findall("./tei:p", ns)]
        sections.append({"heading": head, "text": "\n\n".join(p for p in paragraphs if p)})

    references: List[Dict[str, str]] = []
    for bibl in root.findall(".//tei:listBibl/tei:biblStruct", ns):
        ref_title = text_from_element(bibl.find(".//tei:analytic/tei:title", ns))
        monogr_title = text_from_element(bibl.find(".//tei:monogr/tei:title", ns))
        date = bibl.find(".//tei:date", ns)
        year = date.attrib.get("when", "") if date is not None else ""
        references.append({"title": ref_title, "source": monogr_title, "year": year})

    figures: List[str] = []
    tables: List[str] = []
    for figure in root.findall(".//tei:figure", ns):
        label = text_from_element(figure.find("./tei:label", ns))
        desc = text_from_element(figure.find("./tei:figDesc", ns))
        head = text_from_element(figure.find("./tei:head", ns))
        caption = compact_text(" ".join(part for part in [label, head, desc] if part))
        figure_type = figure.attrib.get("type", "").lower()
        if caption:
            if figure_type == "table" or caption.lower().startswith("table"):
                tables.append(caption)
            else:
                figures.append(caption)

    return {
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "sections": sections,
        "references": references,
        "figures": figures,
        "tables": tables,
        "parser_native_format": "tei_xml",
    }


def structured_to_markdown(data: Dict[str, Any]) -> str:
    lines: List[str] = []
    title = data.get("title") or "Untitled"
    lines.append(f"# {title}")
    authors = data.get("authors") or []
    if authors:
        lines.append("")
        lines.append("**Authors:** " + "; ".join(str(author) for author in authors))
    if data.get("abstract"):
        lines.extend(["", "## Abstract", str(data["abstract"])])
    for section in data.get("sections", []) or []:
        if not isinstance(section, dict):
            continue
        heading = section.get("heading") or "Untitled Section"
        lines.extend(["", f"## {heading}"])
        if section.get("text"):
            lines.append(str(section["text"]))
    if data.get("figures"):
        lines.extend(["", "## Figures"])
        for caption in data["figures"]:
            lines.append(f"- {caption}")
    if data.get("tables"):
        lines.extend(["", "## Tables"])
        for caption in data["tables"]:
            lines.append(f"- {caption}")
    if data.get("references"):
        lines.extend(["", "## References"])
        for index, reference in enumerate(data["references"], start=1):
            if isinstance(reference, dict):
                ref_text = compact_text(
                    " ".join(str(reference.get(key, "")) for key in ("title", "source", "year"))
                )
            else:
                ref_text = str(reference)
            lines.append(f"{index}. {ref_text or '[unparsed reference]'}")
    return "\n".join(lines).rstrip() + "\n"


def parse_with_grobid(pdf_path: Path, grobid_url: str, timeout: int) -> ParseResult:
    endpoint = grobid_url.rstrip("/") + "/api/processFulltextDocument"
    boundary = "----codexpdfstructure" + hashlib.sha1(str(pdf_path).encode()).hexdigest()
    pdf_bytes = pdf_path.read_bytes()
    body = b"".join(
        [
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="input"; filename="{pdf_path.name}"\r\n'.encode(),
            b"Content-Type: application/pdf\r\n\r\n",
            pdf_bytes,
            b"\r\n",
            f"--{boundary}--\r\n".encode(),
        ]
    )
    request = urllib.request.Request(
        endpoint,
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            tei_xml = response.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return ParseResult("grobid", "failed", notes=f"GROBID request failed: {exc}")
    if "<TEI" not in tei_xml and "<tei" not in tei_xml:
        return ParseResult("grobid", "failed", notes="GROBID did not return TEI XML")
    try:
        data = parse_tei(tei_xml)
    except Exception as exc:
        return ParseResult("grobid", "failed", tei_xml=tei_xml, notes=f"TEI parse failed: {exc}")
    markdown = structured_to_markdown(data)
    return ParseResult("grobid", "success", markdown=markdown, data=data, tei_xml=tei_xml)


def parse_with_docling(pdf_path: Path) -> ParseResult:
    try:
        from docling.document_converter import DocumentConverter  # type: ignore
    except ImportError as exc:
        return ParseResult("docling", "failed", notes=f"Docling is not installed: {exc}")
    try:
        converter = DocumentConverter()
        result = converter.convert(str(pdf_path))
        document = result.document
        markdown = document.export_to_markdown()
        if hasattr(document, "export_to_dict"):
            native = document.export_to_dict()
        elif hasattr(document, "model_dump"):
            native = document.model_dump()
        else:
            native = {"repr": repr(document)}
        data = {
            "title": infer_title_from_markdown(markdown),
            "authors": [],
            "abstract": infer_abstract_from_markdown(markdown),
            "sections": [{"heading": heading, "text": ""} for heading in extract_markdown_headings(markdown)],
            "references": infer_references_from_markdown(markdown),
            "figures": infer_captions_from_markdown(markdown, "figure"),
            "tables": infer_captions_from_markdown(markdown, "table"),
            "parser_native_format": "docling",
            "native": native,
        }
        return ParseResult("docling", "success", markdown=markdown, data=data)
    except Exception as exc:  # pragma: no cover - optional backend
        return ParseResult("docling", "failed", notes=f"Docling failed: {exc}")


def parse_with_marker(pdf_path: Path) -> ParseResult:
    try:
        from marker.converters.pdf import PdfConverter  # type: ignore
        from marker.models import create_model_dict  # type: ignore
        from marker.output import text_from_rendered  # type: ignore

        converter = PdfConverter(artifact_dict=create_model_dict())
        rendered = converter(str(pdf_path))
        markdown, _, _ = text_from_rendered(rendered)
        native: Any
        if hasattr(rendered, "model_dump"):
            native = rendered.model_dump()
        else:
            native = {"repr": repr(rendered)}
        data = markdown_to_basic_structure(markdown, "marker", native)
        return ParseResult("marker", "success", markdown=markdown, data=data)
    except ImportError:
        return parse_with_marker_cli(pdf_path)
    except Exception as exc:  # pragma: no cover - optional backend
        return ParseResult("marker", "failed", notes=f"Marker failed: {exc}")


def parse_with_marker_cli(pdf_path: Path) -> ParseResult:
    marker_single = shutil.which("marker_single")
    if not marker_single:
        return ParseResult("marker", "failed", notes="Marker is not installed and marker_single is not on PATH")
    try:
        with tempfile.TemporaryDirectory(prefix="marker-output-") as tmpdir:
            command = [
                marker_single,
                str(pdf_path),
                "--output_format",
                "markdown",
                "--output_dir",
                tmpdir,
            ]
            completed = subprocess.run(command, capture_output=True, text=True, check=False)
            if completed.returncode != 0:
                return ParseResult("marker", "failed", notes=completed.stderr.strip() or "marker_single failed")
            md_files = list(Path(tmpdir).rglob("*.md"))
            if not md_files:
                return ParseResult("marker", "failed", notes="marker_single produced no Markdown")
            markdown = md_files[0].read_text(encoding="utf-8", errors="replace")
            data = markdown_to_basic_structure(markdown, "marker_cli", {})
            return ParseResult("marker", "success", markdown=markdown, data=data)
    except Exception as exc:  # pragma: no cover - optional backend
        return ParseResult("marker", "failed", notes=f"marker_single failed: {exc}")


def parse_with_pymupdf4llm(pdf_path: Path) -> ParseResult:
    try:
        import pymupdf4llm  # type: ignore
    except ImportError:
        return parse_with_pymupdf_plain(pdf_path)
    try:
        markdown = pymupdf4llm.to_markdown(str(pdf_path))
        data = markdown_to_basic_structure(markdown, "pymupdf4llm", {})
        return ParseResult("pymupdf4llm", "success", markdown=markdown, data=data)
    except Exception as exc:  # pragma: no cover - optional backend
        return ParseResult("pymupdf4llm", "failed", notes=f"PyMuPDF4LLM failed: {exc}")


def parse_with_pymupdf_plain(pdf_path: Path) -> ParseResult:
    try:
        try:
            import fitz  # type: ignore
        except ImportError:
            import pymupdf as fitz  # type: ignore
    except ImportError as exc:
        return ParseResult("pymupdf4llm", "failed", notes=f"PyMuPDF4LLM/PyMuPDF not installed: {exc}")
    try:
        doc = fitz.open(str(pdf_path))
        lines: List[str] = [f"# {pdf_path.stem}", ""]
        for index, page in enumerate(doc, start=1):
            lines.append(f"## Page {index}")
            lines.append(page.get_text("text"))
        doc.close()
        markdown = "\n".join(lines)
        data = markdown_to_basic_structure(markdown, "pymupdf_plain", {})
        return ParseResult("pymupdf_plain", "success", markdown=markdown, data=data)
    except Exception as exc:  # pragma: no cover - optional backend
        return ParseResult("pymupdf_plain", "failed", notes=f"PyMuPDF plain extraction failed: {exc}")


def infer_title_from_markdown(markdown: str) -> str:
    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
        if len(stripped) > 8:
            return stripped[:250]
    return ""


def infer_abstract_from_markdown(markdown: str) -> str:
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        if normalize_heading(line.lstrip("# ")) == "abstract":
            collected: List[str] = []
            for next_line in lines[index + 1 :]:
                if next_line.strip().startswith("#"):
                    break
                if next_line.strip():
                    collected.append(next_line.strip())
            return compact_text(" ".join(collected))
    match = re.search(r"(?is)\babstract\b[:\s]+(.{100,2000}?)(\n\s*(keywords?|introduction|1\.?\s+introduction)\b)", markdown)
    return compact_text(match.group(1)) if match else ""


def infer_references_from_markdown(markdown: str) -> List[str]:
    match = re.search(r"(?is)(^|\n)\s*#{0,6}\s*(references|literature cited|bibliography)\s*\n(.+)$", markdown)
    if not match:
        return []
    text = match.group(3)
    refs = []
    for chunk in re.split(r"\n(?=\s*(\[\d+\]|\d+\.|\w.+\(\d{4}\)))", text):
        cleaned = compact_text(chunk)
        if len(cleaned) > 20:
            refs.append(cleaned)
    return refs[:500]


def infer_captions_from_markdown(markdown: str, kind: str) -> List[str]:
    if kind == "figure":
        pattern = r"(?im)^\s*((?:fig(?:ure)?\.?|图)\s*[\divxlcdm]+[\.:：\s].+)$"
    else:
        pattern = r"(?im)^\s*((?:table|表)\s*[\dixvlcdm]+[\.:：\s].+)$"
    return [compact_text(match.group(1)) for match in re.finditer(pattern, markdown)]


def markdown_to_basic_structure(markdown: str, parser_native_format: str, native: Any) -> Dict[str, Any]:
    return {
        "title": infer_title_from_markdown(markdown),
        "authors": [],
        "abstract": infer_abstract_from_markdown(markdown),
        "sections": [{"heading": heading, "text": ""} for heading in extract_markdown_headings(markdown)],
        "references": infer_references_from_markdown(markdown),
        "figures": infer_captions_from_markdown(markdown, "figure"),
        "tables": infer_captions_from_markdown(markdown, "table"),
        "parser_native_format": parser_native_format,
        "native": native,
    }


def run_ocrmypdf(pdf_path: Path, parsed_text_dir: Path, slug: str, language: str) -> Tuple[Path, str]:
    output_pdf = parsed_text_dir / f"{slug}.searchable.pdf"
    if output_pdf.exists():
        return output_pdf, "existing searchable PDF"
    ocrmypdf = shutil.which("ocrmypdf")
    if not ocrmypdf:
        return pdf_path, "OCRmyPDF requested but ocrmypdf is not on PATH"
    command = [
        ocrmypdf,
        "--skip-text",
        "--language",
        language,
        str(pdf_path),
        str(output_pdf),
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode != 0:
        return pdf_path, "OCRmyPDF failed: " + (completed.stderr.strip() or completed.stdout.strip())
    return output_pdf, f"OCRmyPDF generated {output_pdf}"


def backend_sequence(backend: str) -> List[str]:
    if backend == "auto":
        return ["grobid", "docling", "marker", "pymupdf4llm"]
    return [backend]


def parse_pdf(pdf_path: Path, args: argparse.Namespace, parsed_text_dir: Path, slug: str, has_text_layer: str) -> Tuple[ParseResult, str, str]:
    parse_input = pdf_path
    ocr_note = ""
    if has_text_layer == "no" and args.ocr:
        parse_input, ocr_note = run_ocrmypdf(pdf_path, parsed_text_dir, slug, args.ocr_language)

    attempts: List[ParseResult] = []
    for backend in backend_sequence(args.backend):
        if backend == "grobid":
            result = parse_with_grobid(parse_input, args.grobid_url, args.timeout)
        elif backend == "docling":
            result = parse_with_docling(parse_input)
        elif backend == "marker":
            result = parse_with_marker(parse_input)
        elif backend == "pymupdf4llm":
            result = parse_with_pymupdf4llm(parse_input)
        else:
            result = ParseResult(backend, "failed", notes=f"Unknown backend {backend}")
        attempts.append(result)
        if result.status == "success":
            failed = [f"{attempt.backend}: {attempt.notes}" for attempt in attempts[:-1]]
            fallback_used = "no" if len(attempts) == 1 else "yes: " + " | ".join(failed)
            notes = "; ".join(part for part in [ocr_note, result.notes] if part)
            result.notes = notes
            return result, fallback_used, " -> ".join(attempt.backend for attempt in attempts)

    notes = "; ".join(
        part
        for part in [ocr_note] + [f"{attempt.backend}: {attempt.notes}" for attempt in attempts]
        if part
    )
    failed_backend = attempts[-1].backend if attempts else args.backend
    return ParseResult(failed_backend, "failed", notes=notes), "yes" if len(attempts) > 1 else "no", " -> ".join(attempt.backend for attempt in attempts)


def write_outputs(
    pdf_path: Path,
    slug: str,
    result: ParseResult,
    section_status: SectionStatus,
    text_layer: Any,
    output_dir: Path,
    parsed_text_dir: Path,
    reports_dir: Path,
    fallback_used: str,
    force: bool,
) -> Dict[str, str]:
    md_path = parsed_text_dir / f"{slug}.md"
    json_path = parsed_text_dir / f"{slug}.json"
    tei_path = parsed_text_dir / f"{slug}.tei.xml"
    report_path = reports_dir / f"{slug}_structure_report.md"

    parsed_payload = {
        "source_pdf": str(pdf_path),
        "paper_slug": slug,
        "parser_used": result.backend,
        "parser_status": result.status,
        "text_layer": asdict(text_layer),
        "section_status": asdict(section_status),
        "data": result.data,
        "notes": result.notes,
    }

    if force or not md_path.exists():
        md_path.write_text(result.markdown or "", encoding="utf-8")
    if force or not json_path.exists():
        json_path.write_text(json.dumps(parsed_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if result.tei_xml and (force or not tei_path.exists()):
        tei_path.write_text(result.tei_xml, encoding="utf-8")
    if force or not report_path.exists():
        report_path.write_text(
            render_structure_report(
                pdf_path=pdf_path,
                slug=slug,
                result=result,
                section_status=section_status,
                text_layer=text_layer,
                output_dir=output_dir,
                md_path=md_path,
                json_path=json_path,
                tei_path=tei_path if result.tei_xml else None,
                fallback_used=fallback_used,
            ),
            encoding="utf-8",
        )

    return {
        "md_path": str(md_path),
        "json_path": str(json_path),
        "tei_path": str(tei_path) if result.tei_xml else "",
        "report_path": str(report_path),
    }


def write_failure_outputs(
    pdf_path: Path,
    slug: str,
    result: ParseResult,
    section_status: SectionStatus,
    text_layer: Any,
    parsed_text_dir: Path,
    force: bool,
) -> None:
    md_path = parsed_text_dir / f"{slug}.md"
    json_path = parsed_text_dir / f"{slug}.json"
    if force or not md_path.exists():
        md_path.write_text(
            "\n".join(
                [
                    "# PDF Structure Parsing Failed",
                    "",
                    f"- Source PDF: `{pdf_path}`",
                    f"- Parser used: {result.backend}",
                    f"- Parser status: {result.status}",
                    f"- Has text layer: {text_layer.has_text_layer}",
                    f"- Page count: {text_layer.page_count}",
                    f"- Notes: {result.notes}",
                    "",
                    "[需要人工复核] Parsing failed before reliable structured text could be produced.",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    if force or not json_path.exists():
        payload = {
            "source_pdf": str(pdf_path),
            "paper_slug": slug,
            "parser_used": result.backend,
            "parser_status": result.status,
            "text_layer": asdict(text_layer),
            "section_status": asdict(section_status),
            "data": {},
            "notes": result.notes,
        }
        json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def render_structure_report(
    pdf_path: Path,
    slug: str,
    result: ParseResult,
    section_status: SectionStatus,
    text_layer: Any,
    output_dir: Path,
    md_path: Path,
    json_path: Path,
    tei_path: Optional[Path],
    fallback_used: str,
) -> str:
    data = result.data
    lines = [
        "# PDF Structure Report",
        "",
        "## Source",
        "",
        f"- File path: `{pdf_path}`",
        f"- Paper slug: `{slug}`",
        f"- Output root: `{output_dir}`",
        f"- Has text layer: {text_layer.has_text_layer}",
        f"- Page count: {text_layer.page_count}",
        f"- Parser used: {result.backend}",
        f"- Parser status: {result.status}",
        f"- Fallback used: {fallback_used}",
        f"- Confidence: {section_status.confidence}",
        f"- Need manual review: {section_status.need_manual_review}",
        "",
        "## Parsed Outputs",
        "",
        f"- Markdown: `{md_path}`",
        f"- JSON: `{json_path}`",
        f"- TEI/XML: `{tei_path}`" if tei_path else "- TEI/XML: not available from selected parser",
        "",
        "## Metadata",
        "",
        f"- Detected title: {data.get('title') or '[需要人工复核]'}",
        f"- Authors: {'; '.join(data.get('authors') or []) or '[需要人工复核]'}",
        f"- Abstract detected: {'yes' if data.get('abstract') else 'no'}",
        "",
        "## Section Detection",
        "",
        "| Section | Status |",
        "|---|---|",
        f"| Introduction | {section_status.introduction} |",
        f"| Methods | {section_status.methods} |",
        f"| Results | {section_status.results} |",
        f"| Discussion | {section_status.discussion} |",
        f"| References | {section_status.references} |",
        "",
        "## Captions",
        "",
        f"- Figure captions detected: {section_status.figure_caption_detected}",
        f"- Table captions detected: {section_status.table_caption_detected}",
        "",
        "## Detected Headings",
        "",
    ]
    if section_status.detected_sections:
        lines.extend(f"- {heading}" for heading in section_status.detected_sections)
    else:
        lines.append("- [需要人工复核] No stable section headings detected.")
    lines.extend(["", "## Section Uncertainty Notes", ""])
    if section_status.notes or result.notes:
        for note in section_status.notes:
            lines.append(f"- {note}")
        if result.notes:
            lines.append(f"- Parser notes: {result.notes}")
    else:
        lines.append("- No major section uncertainty detected.")
    if section_status.introduction != "confirmed":
        lines.extend(
            [
                "",
                "[Introduction 标题未稳定识别，正文结构需人工复核]",
                "",
                "Reading should continue as `section-uncertain full-text reading` if full text is available.",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def load_manifest(manifest_path: Path) -> Dict[Tuple[str, str], Dict[str, str]]:
    if not manifest_path.exists():
        return {}
    with manifest_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = {}
        for row in reader:
            rows[(row.get("file_path", ""), row.get("paper_slug", ""))] = row
        return rows


def write_manifest(manifest_path: Path, rows: Iterable[Dict[str, str]]) -> None:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in MANIFEST_FIELDS})


def write_failures(output_dir: Path, rows: Iterable[Dict[str, str]]) -> None:
    failures = [row for row in rows if row.get("parser_status") not in ("success", "skipped_existing")]
    path = output_dir / "parsing_failures.md"
    lines = ["# Parsing Failures", ""]
    if not failures:
        lines.append("No parsing failures recorded in the latest manifest.")
    else:
        for row in failures:
            lines.extend(
                [
                    f"## {row.get('paper_slug') or row.get('file_path')}",
                    "",
                    f"- File path: `{row.get('file_path')}`",
                    f"- Parser used: {row.get('parser_used')}",
                    f"- Parser status: {row.get('parser_status')}",
                    f"- Has text layer: {row.get('has_text_layer')}",
                    f"- Fallback used: {row.get('fallback_used')}",
                    f"- Need manual review: {row.get('need_manual_review')}",
                    f"- Notes: {row.get('notes')}",
                    "",
                ]
            )
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def make_manifest_row(
    pdf_path: Path,
    slug: str,
    result: ParseResult,
    text_layer: Any,
    section_status: Optional[SectionStatus],
    fallback_used: str,
    notes: str,
) -> Dict[str, str]:
    section_status = section_status or SectionStatus(
        introduction="missing",
        methods="missing",
        results="missing",
        discussion="missing",
        references="missing",
        detected_sections=[],
        figure_caption_detected="no",
        table_caption_detected="no",
        confidence="low",
        need_manual_review="yes",
        notes=["[需要人工复核] Parser failed before section detection."],
    )
    data = result.data or {}
    return {
        "file_path": str(pdf_path),
        "paper_slug": slug,
        "parser_used": result.backend,
        "parser_status": result.status,
        "has_text_layer": text_layer.has_text_layer,
        "page_count": str(text_layer.page_count),
        "detected_title": str(data.get("title") or ""),
        "detected_abstract": "yes" if data.get("abstract") else "no",
        "detected_sections": "; ".join(section_status.detected_sections),
        "introduction_detected": section_status.introduction,
        "methods_detected": section_status.methods,
        "results_detected": section_status.results,
        "discussion_detected": section_status.discussion,
        "references_detected": section_status.references,
        "figure_caption_detected": section_status.figure_caption_detected,
        "table_caption_detected": section_status.table_caption_detected,
        "confidence": section_status.confidence,
        "fallback_used": fallback_used,
        "need_manual_review": section_status.need_manual_review,
        "notes": notes,
    }


def existing_outputs_present(parsed_text_dir: Path, reports_dir: Path, slug: str) -> bool:
    return (
        (parsed_text_dir / f"{slug}.md").exists()
        and (parsed_text_dir / f"{slug}.json").exists()
        and (reports_dir / f"{slug}_structure_report.md").exists()
    )


def process_pdf(pdf_path: Path, args: argparse.Namespace, output_dir: Path, existing_rows: Dict[Tuple[str, str], Dict[str, str]]) -> Dict[str, str]:
    parsed_text_dir = output_dir / "parsed_text"
    reports_dir = output_dir / "structure_reports"
    parsed_text_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify_pdf(pdf_path)
    text_layer = check_pdf_text_layer(pdf_path, args.sample_pages)
    if existing_outputs_present(parsed_text_dir, reports_dir, slug) and not args.force:
        result = ParseResult("existing", "skipped_existing", notes="Existing parsed_text and structure_report kept; use --force to overwrite.")
        section_status = None
        row = existing_rows.get((str(pdf_path), slug))
        if row:
            row = dict(row)
            row["parser_status"] = "skipped_existing"
            row["notes"] = result.notes
            return row
        return make_manifest_row(pdf_path, slug, result, text_layer, section_status, "no", result.notes)

    result, fallback_used, attempt_chain = parse_pdf(pdf_path, args, parsed_text_dir, slug, text_layer.has_text_layer)
    if result.status == "success":
        section_status = detect_sections(result.markdown, result.data)
        write_outputs(
            pdf_path=pdf_path,
            slug=slug,
            result=result,
            section_status=section_status,
            text_layer=text_layer,
            output_dir=output_dir,
            parsed_text_dir=parsed_text_dir,
            reports_dir=reports_dir,
            fallback_used=fallback_used,
            force=args.force,
        )
        notes = "; ".join(part for part in [result.notes, f"attempt_chain={attempt_chain}"] if part)
        return make_manifest_row(pdf_path, slug, result, text_layer, section_status, fallback_used, notes)

    notes = "; ".join(part for part in [result.notes, f"attempt_chain={attempt_chain}"] if part)
    failure_status = SectionStatus(
        introduction="missing",
        methods="missing",
        results="missing",
        discussion="missing",
        references="missing",
        detected_sections=[],
        figure_caption_detected="no",
        table_caption_detected="no",
        confidence="low",
        need_manual_review="yes",
        notes=["[需要人工复核] Parsing failed."],
    )
    write_failure_outputs(
        pdf_path=pdf_path,
        slug=slug,
        result=result,
        section_status=failure_status,
        text_layer=text_layer,
        parsed_text_dir=parsed_text_dir,
        force=args.force,
    )
    report_path = reports_dir / f"{slug}_structure_report.md"
    if args.force or not report_path.exists():
        report_path.write_text(
            render_structure_report(
                pdf_path=pdf_path,
                slug=slug,
                result=result,
                section_status=failure_status,
                text_layer=text_layer,
                output_dir=output_dir,
                md_path=parsed_text_dir / f"{slug}.md",
                json_path=parsed_text_dir / f"{slug}.json",
                tei_path=None,
                fallback_used=fallback_used,
            ),
            encoding="utf-8",
        )
    return make_manifest_row(pdf_path, slug, result, text_layer, failure_status, fallback_used, notes)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Parse PDFs into structured text before scientific close reading.",
        epilog=textwrap.dedent(
            """\
            Examples:
              python scripts/parse_pdf_structure.py --input papers/ --output literature-notes/pdf-structure/ --backend auto
              python scripts/parse_pdf_structure.py --input papers/ --output literature-notes/pdf-structure/ --backend grobid --grobid-url http://localhost:8070
            """
        ),
    )
    parser.add_argument("--input", required=True, help="PDF file or directory to scan recursively.")
    parser.add_argument(
        "--output",
        default="literature-notes/pdf-structure/",
        help="Output directory. Topic workflows may use literature-notes/plant-gene-network-curation/{topic}/pdf_structure/.",
    )
    parser.add_argument(
        "--backend",
        choices=("auto", "grobid", "docling", "marker", "pymupdf4llm"),
        default="auto",
        help="Parser backend. auto tries GROBID, Docling, Marker, then PyMuPDF4LLM.",
    )
    parser.add_argument("--grobid-url", default="http://localhost:8070", help="Base URL for a running GROBID service.")
    parser.add_argument("--timeout", type=int, default=120, help="Backend timeout in seconds where supported.")
    parser.add_argument("--sample-pages", type=int, default=5, help="Pages sampled for text-layer detection.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing parsed outputs for matching paper slugs.")
    parser.add_argument("--ocr", action="store_true", help="For scanned PDFs only, run OCRmyPDF before parser fallback.")
    parser.add_argument("--ocr-language", default="eng", help="OCRmyPDF language code, e.g. eng or eng+chi_sim.")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    input_path = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = output_dir / "parsing_manifest.csv"
    existing_rows = load_manifest(manifest_path)

    pdfs = find_pdfs(input_path)
    rows_by_key = dict(existing_rows)
    for pdf_path in pdfs:
        row = process_pdf(pdf_path, args, output_dir, existing_rows)
        rows_by_key[(row["file_path"], row["paper_slug"])] = row

    rows = list(rows_by_key.values())
    rows.sort(key=lambda row: (row.get("file_path", ""), row.get("paper_slug", "")))
    write_manifest(manifest_path, rows)
    write_failures(output_dir, rows)
    print(f"Processed {len(pdfs)} PDF(s). Manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
