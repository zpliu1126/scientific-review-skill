# PDF Structure Parsing Example

Example command:

```bash
python scripts/parse_pdf_structure.py \
  --input papers/ \
  --output literature-notes/plant-gene-network-curation/flavonoid/pdf_structure/ \
  --backend auto
```

Expected files:

```text
literature-notes/plant-gene-network-curation/flavonoid/pdf_structure/
├── parsed_text/
│   ├── zhang-2024-flavonoid-biosynthesis.json
│   ├── zhang-2024-flavonoid-biosynthesis.md
│   └── zhang-2024-flavonoid-biosynthesis.tei.xml
├── structure_reports/
│   └── zhang-2024-flavonoid-biosynthesis_structure_report.md
├── parsing_manifest.csv
└── parsing_failures.md
```

Example manifest row:

| file_path | paper_slug | parser_used | parser_status | has_text_layer | page_count | detected_title | detected_abstract | detected_sections | introduction_detected | methods_detected | results_detected | discussion_detected | references_detected | figure_caption_detected | table_caption_detected | confidence | fallback_used | need_manual_review | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| papers/Zhang_2024_flavonoid.pdf | zhang-2024-flavonoid-biosynthesis | grobid | success | yes | 12 | Flavonoid biosynthesis regulates... | yes | Introduction; Materials and Methods; Results; Discussion; References | confirmed | confirmed | confirmed | confirmed | confirmed | yes | yes | high | no | no | attempt_chain=grobid |

Example section-uncertain row:

| file_path | paper_slug | parser_used | parser_status | has_text_layer | page_count | detected_title | detected_abstract | detected_sections | introduction_detected | methods_detected | results_detected | discussion_detected | references_detected | figure_caption_detected | table_caption_detected | confidence | fallback_used | need_manual_review | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| papers/Old_scan.pdf | old-scan | pymupdf4llm | success | no | 9 |  | no | Page 1; Page 2 | probable_introduction | missing | missing | missing | missing | no | no | low | yes: grobid failed; docling failed; marker failed | yes | [Introduction 标题未稳定识别，正文结构需人工复核]; [需要人工复核] methods section was not confidently detected. |

Downstream full-text card source basis:

```text
- PDF parser used: pymupdf4llm
- Parser confidence: low
- Section detection status: section-uncertain full-text reading
- Introduction detected: probable_introduction
- Methods detected: missing
- Results detected: missing
- Discussion detected: missing
- References detected: missing
- Section uncertainty notes: [Introduction 标题未稳定识别，正文结构需人工复核]; [需要人工复核]
```

Reading should continue if the full text is usable, but claims must not pretend that uncertain section boundaries are confirmed.
