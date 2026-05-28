# PDF Structure Parsing Prompt

Use this prompt before single-paper close reading, batch PDF close reading, cited-reference mining, or functional gene evidence curation.

中文名称：PDF 结构化解析模块

```text
Use scientific-review-skill and run the PDF Structure Parsing Module before reading or curating the PDF content.

Goal:
Convert PDFs into structured text first, then use the structured output for close reading, cited-reference mining, evidence matrices, or plant functional gene network curation.

Input:
- PDF file or directory:
- Topic workflow, if any:
- Preferred backend: auto / grobid / docling / marker / pymupdf4llm
- GROBID URL, if running as a service:
- Whether OCR is allowed for scanned PDFs only:

Default output:
literature-notes/pdf-structure/

Topic workflow output:
literature-notes/plant-gene-network-curation/{topic}/pdf_structure/

Required output structure:
pdf_structure/
├── parsed_text/
│   ├── {paper_slug}.md
│   ├── {paper_slug}.json
│   └── {paper_slug}.tei.xml
├── structure_reports/
│   └── {paper_slug}_structure_report.md
├── parsing_manifest.csv
└── parsing_failures.md

Backend priority when backend=auto:
1. GROBID for scientific paper structure parsing and TEI/XML.
2. Docling for complex layout, tables, and mixed figure/text PDFs.
3. Marker for Markdown/JSON conversion with sections, equations, tables, and image cues.
4. PyMuPDF4LLM as lightweight Markdown fallback.
5. OCRmyPDF only for scanned/image-only PDFs, before handing the searchable PDF to a parser.

Do not rely only on pypdf plain-text extraction. pypdf-style text extraction can lose section headings, reading order, double-column order, captions, and table context.

For each PDF, record:
- parser_used
- parser_status
- has_text_layer
- page_count
- fallback_used
- detected_title
- detected_abstract
- detected_sections
- Introduction / Methods / Results / Discussion / References status
- figure/table caption status
- confidence
- need_manual_review
- notes

Section uncertainty rule:
If Introduction is not stably detected, write:
[Introduction 标题未稳定识别，正文结构需人工复核]

If full text is available, continue close reading as:
section-uncertain full-text reading

Do not pretend uncertain sections are confirmed. Mark [需要人工复核] whenever section headings or reading order are unstable.
```

Command examples:

```bash
python scripts/parse_pdf_structure.py \
  --input papers/ \
  --output literature-notes/pdf-structure/ \
  --backend auto
```

```bash
python scripts/parse_pdf_structure.py \
  --input papers/ \
  --output literature-notes/pdf-structure/ \
  --backend grobid \
  --grobid-url http://localhost:8070
```

For a plant topic workflow:

```bash
python scripts/parse_pdf_structure.py \
  --input papers/ \
  --output literature-notes/plant-gene-network-curation/flavonoid/pdf_structure/ \
  --backend auto
```
