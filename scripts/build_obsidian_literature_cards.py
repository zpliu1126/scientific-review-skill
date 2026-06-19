from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURATED = ROOT / "01_Curated"
PAPER_CARDS = CURATED / "Paper-Cards"
CLAIMS = CURATED / "Claim-Evidence"
METHODS = CURATED / "Method-Summaries"
OUT_DIR = ROOT / "02_Literature" / "Cards"
INDEX = ROOT / "02_Literature" / "literature-index.md"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end].strip().splitlines()
    body = text[end + 4 :].lstrip()
    meta: dict[str, str] = {}
    current_key = ""
    current_values: list[str] = []
    for line in raw:
        if not line.strip():
            continue
        if re.match(r"^[A-Za-z_][A-Za-z0-9_]*:", line):
            if current_key:
                meta[current_key] = "\n".join(current_values).strip()
            key, value = line.split(":", 1)
            current_key = key.strip()
            current_values = [value.strip()]
        elif current_key:
            current_values.append(line.rstrip())
    if current_key:
        meta[current_key] = "\n".join(current_values).strip()
    return meta, body


def section(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^##\s+|\Z)",
        re.MULTILINE,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line and not line.startswith(">"):
            return clean_bullet(line)
    return "unknown"


def clean_bullet(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^[-*]\s+", "", line)
    return line.strip()


def parse_listish(value: str) -> list[str]:
    value = value.strip()
    if not value or value == "unknown":
        return []
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    parts = re.split(r"[,;]\s*", value)
    return [p.strip().strip("'\"") for p in parts if p.strip().strip("'\"")]


def yaml_scalar(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""
    if re.search(r"[:\[\]\n,]", value):
        value = value.replace('"', '\\"')
        return f'"{value}"'
    return value


def yaml_list(values: list[str]) -> str:
    values = [v.strip() for v in values if v and v.strip()]
    if not values:
        return "[]"
    return "\n" + "\n".join(f"  - {yaml_scalar(v)}" for v in values)


def wikilink(name: str) -> str:
    name = clean_bullet(name)
    name = re.sub(r"^[A-Za-z ]+:\s*", "", name).strip()
    return f"[[{name}]]" if name else ""


def extract_reusable_block(card_body: str) -> dict[str, list[str]]:
    block = section(card_body, "12. Reusable knowledge")
    out: dict[str, list[str]] = defaultdict(list)
    current = ""
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("- "):
            content = clean_bullet(line)
            if ":" in content:
                key, value = content.split(":", 1)
                current = key.strip()
                vals = re.split(r";|,", value)
                out[current].extend(v.strip().strip(".") for v in vals if v.strip())
            elif current:
                out[current].append(content.strip("."))
        elif current:
            out[current].append(line.strip("."))
    return out


def extract_methods(method_text: str, claim_rows: list[dict[str, str]]) -> list[str]:
    names: list[str] = []
    for line in method_text.splitlines():
        line = line.strip()
        if line.startswith("### "):
            name = line[4:].strip()
            if name.lower() != "method name":
                names.append(name)
        elif line.startswith("- Method name:"):
            names.append(line.split(":", 1)[1].strip())
    for row in claim_rows:
        method = row.get("method", "").strip()
        if method:
            for part in re.split(r";", method):
                if part.strip():
                    names.append(part.strip())
    seen: set[str] = set()
    unique: list[str] = []
    for name in names:
        name = name.strip().strip(".")
        if name and name.lower() not in seen:
            seen.add(name.lower())
            unique.append(name)
    return unique


def read_claims(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def most_common(rows: list[dict[str, str]], key: str, default: str = "") -> str:
    vals = [row.get(key, "").strip() for row in rows if row.get(key, "").strip()]
    if not vals:
        return default
    return Counter(vals).most_common(1)[0][0]


def confidence_summary(rows: list[dict[str, str]], evidence_strength: str) -> str:
    vals = [row.get("confidence_level", "").strip() for row in rows if row.get("confidence_level", "").strip()]
    if not vals:
        return evidence_strength or "unknown"
    return "; ".join(v for v, _ in Counter(vals).most_common(3))


def output_name(meta: dict[str, str], paper_id: str) -> str:
    year = meta.get("year", "unknown").strip() or "unknown"
    short = paper_id
    first = "Unknown"
    match = re.match(r"^\d{4}-([^-]+)-(.+)$", paper_id)
    if match:
        first = match.group(1).strip()
        short = match.group(2).replace("-", " ")
    short = re.sub(r"\s+", " ", short).strip()
    safe = re.sub(r'[<>:"/\\|?*]', "-", f"{year} - {first} - {short}")
    return f"{safe}.md"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build_findings(rows: list[dict[str, str]]) -> str:
    parts: list[str] = []
    for idx, row in enumerate(rows[:6], 1):
        parts.append(
            "\n".join(
                [
                    f"### Finding {idx}",
                    "> [!info] Source-reported content",
                    f"> {row.get('source_reported_content', '').strip() or row.get('scientific_claim', '').strip() or 'unknown'}",
                    "",
                    f"- Evidence type: {row.get('evidence_type', '').strip() or 'unknown'}",
                    f"- Method: {row.get('method', '').strip() or 'unknown'}",
                    f"- Data type: {row.get('data_type', '').strip() or 'unknown'}",
                    f"- Figure/table anchor: {row.get('figure_or_table_anchor', '').strip() or 'unknown'}",
                    f"- Confidence: {row.get('confidence_level', '').strip() or 'unknown'}",
                    f"- Limitation: {row.get('limitation', '').strip() or 'unknown'}",
                ]
            )
        )
    return "\n\n".join(parts) if parts else "unknown"


def bullet_block(text: str) -> str:
    text = text.strip()
    if not text:
        return "- unknown"
    lines = [line.rstrip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def build_note(card_path: Path) -> tuple[Path, str, dict[str, str]]:
    card_text = read_text(card_path)
    meta, body = split_frontmatter(card_text)
    paper_id = card_path.name.removesuffix(".review.md")
    claim_path = CLAIMS / f"{paper_id}.claims.tsv"
    method_path = METHODS / f"method-summary.{paper_id}.md"
    claim_rows = read_claims(claim_path) if claim_path.exists() else []
    method_text = read_text(method_path) if method_path.exists() else ""
    methods = extract_methods(method_text, claim_rows)
    reusable = extract_reusable_block(body)
    concepts = reusable.get("Concepts", [])
    datasets = reusable.get("Datasets", [])
    frameworks = reusable.get("Analytical frameworks", [])
    designs = reusable.get("Experimental designs", [])
    topics = parse_listish(meta.get("topics", ""))
    data_types = sorted({row.get("data_type", "").strip() for row in claim_rows if row.get("data_type", "").strip()})
    systems = sorted({row.get("study_system", "").strip() for row in claim_rows if row.get("study_system", "").strip()})
    confidence = confidence_summary(claim_rows, meta.get("evidence_strength", "unknown"))
    title = meta.get("title", "unknown").strip() or "unknown"
    today = date.today().isoformat()
    filename = output_name(meta, paper_id)
    out_path = OUT_DIR / filename

    source_basis = section(body, "2. Source basis")
    takeaway = first_nonempty_line(section(body, "3. One-sentence takeaway"))
    question = section(body, "4. Research question") or "unknown"
    design = section(body, "5. Study design") or "unknown"
    conclusions = section(body, "8. Author conclusions") or "unknown"
    inference = section(body, "9. Reasonable inference") or "unknown"
    synthesis = section(body, "10. Model synthesis") or "unknown"
    limitations = section(body, "11. Limitations and missing controls") or "unknown"
    open_questions = section(body, "13. Open questions") or "unknown"

    frontmatter = "\n".join(
        [
            "---",
            "type: literature-note",
            "source: mineru",
            "curation: scientific-review-skill",
            "status: curated",
            f"title: {yaml_scalar(title)}",
            f"authors: {yaml_scalar(meta.get('authors', 'unknown'))}",
            f"year: {yaml_scalar(meta.get('year', 'unknown'))}",
            f"journal: {yaml_scalar(meta.get('journal', 'unknown'))}",
            f"doi: {yaml_scalar(meta.get('doi', 'unknown'))}",
            f"field: {yaml_scalar(meta.get('field', 'unknown'))}",
            f"topics: {yaml_list(topics)}",
            f"study_type: {yaml_scalar(meta.get('study_type', 'unknown'))}",
            f"methods: {yaml_list(methods)}",
            f"data_types: {yaml_list(data_types)}",
            f"study_system: {yaml_list(systems)}",
            f"evidence_strength: {yaml_scalar(meta.get('evidence_strength', 'unknown'))}",
            f"confidence_level: {yaml_scalar(confidence)}",
            f"paper_id: {paper_id}",
            f"mineru_dir: {yaml_scalar(meta.get('mineru_dir', 'unknown'))}",
            f"curated_card: {rel(card_path)}",
            f"claim_evidence_table: {rel(claim_path) if claim_path.exists() else ''}",
            f"created: {today}",
            f"updated: {today}",
            "---",
        ]
    )

    concept_links = [wikilink(c) for c in concepts if c]
    method_links = [wikilink(m) for m in methods[:12] if m]
    concept_body = "\n".join(f"- {x}" for x in concept_links) if concept_links else "- unknown"
    method_body = "\n".join(f"- {x}" for x in method_links) if method_links else "- unknown"
    dataset_body = "\n".join(f"- {clean_bullet(x)}" for x in datasets if x) or "- unknown"
    framework_body = "\n".join(f"- {clean_bullet(x)}" for x in frameworks if x) or "- unknown"
    design_body = "\n".join(f"- {clean_bullet(x)}" for x in designs if x) or "- unknown"
    evidence_links = "\n".join(f"- [[{paper_id} claims]]") if claim_path.exists() else "- unknown"
    question_links = "\n".join(f"- [[{paper_id} open questions]]")

    content = f"""{frontmatter}

# {title}

> [!summary] 一句话结论
> {takeaway}

## 基本信息
- Authors: {meta.get('authors', 'unknown') or 'unknown'}
- Year: {meta.get('year', 'unknown') or 'unknown'}
- Journal: {meta.get('journal', 'unknown') or 'unknown'}
- DOI: {meta.get('doi', 'unknown') or 'unknown'}
- Study type: {meta.get('study_type', 'unknown') or 'unknown'}
- Source basis: {rel(card_path)}; {rel(claim_path) if claim_path.exists() else 'unknown'}; {rel(method_path) if method_path.exists() else 'unknown'}

## 核心科学问题
{bullet_block(question)}

## 研究设计
{bullet_block(design)}

## 主要发现

{build_findings(claim_rows)}

## 作者结论
{bullet_block(conclusions)}

## 谨慎推断
> [!caution] Reasonable inference
{blockquote(inference)}

## 模型综合
> [!abstract] Model synthesis
{blockquote(synthesis)}

## 可复用知识

### Concepts
{concept_body}

### Methods
{method_body}

### Datasets
{dataset_body}

### Analytical frameworks
{framework_body}

### Experimental designs
{design_body}

## 局限性
{bullet_block(limitations)}

## 开放问题
{bullet_block(open_questions)}

## 关联笔记
- Concepts: {', '.join(concept_links) if concept_links else 'unknown'}
- Methods: {', '.join(method_links) if method_links else 'unknown'}
- Evidence: [[{paper_id} claims]]
- Questions: [[{paper_id} open questions]]
"""
    return out_path, content, {"paper_id": paper_id, "title": title, "year": meta.get("year", "unknown"), "authors": meta.get("authors", "unknown")}


def blockquote(text: str) -> str:
    text = text.strip() or "unknown"
    lines = [line.rstrip() for line in text.splitlines()]
    return "\n".join(f"> {line}" if line else ">" for line in lines)


def build_index(records: list[dict[str, str]]) -> str:
    rows = [
        "---",
        "type: literature-index",
        "source: 01_Curated",
        f"updated: {date.today().isoformat()}",
        "---",
        "",
        "# Literature Index",
        "",
        "> [!note]",
        "> This index tracks Obsidian literature cards generated from `01_Curated/` outputs.",
        "",
        "| Year | Title | Card | Curated Paper ID |",
        "| --- | --- | --- | --- |",
    ]
    for record in sorted(records, key=lambda r: (r.get("year", ""), r.get("title", ""))):
        card_stem = Path(record["path"]).stem
        rows.append(f"| {record.get('year', 'unknown')} | {record.get('title', 'unknown')} | [[{card_stem}]] | `{record.get('paper_id', '')}` |")
    return "\n".join(rows) + "\n"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, str]] = []
    created: list[Path] = []
    skipped: list[Path] = []
    for card in sorted(PAPER_CARDS.glob("*.review.md")):
        out_path, content, record = build_note(card)
        record["path"] = rel(out_path)
        records.append(record)
        if out_path.exists():
            skipped.append(out_path)
            continue
        out_path.write_text(content, encoding="utf-8", newline="\n")
        created.append(out_path)
    INDEX.write_text(build_index(records), encoding="utf-8", newline="\n")
    print(f"created={len(created)} skipped_existing={len(skipped)} index={rel(INDEX)}")
    for path in created:
        print(f"created\t{rel(path)}")
    for path in skipped:
        print(f"skipped\t{rel(path)}")


if __name__ == "__main__":
    main()
