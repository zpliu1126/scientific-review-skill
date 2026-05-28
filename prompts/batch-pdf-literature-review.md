# Batch PDF Literature Review Prompt

Use this prompt when the user provides a folder of PDFs and wants batch close reading, evidence cards, cited-reference mining, or evidence-matrix preparation.

```text
Use scientific-review-skill for batch PDF literature review.

Before reading the papers, run the PDF Structure Parsing Module.

Input:
- PDF directory:
- Topic:
- Output directory:
- Backend: auto / grobid / docling / marker / pymupdf4llm

Step 1. Parse PDF structure.

Default command:
python scripts/parse_pdf_structure.py \
  --input papers/ \
  --output literature-notes/pdf-structure/ \
  --backend auto

For a topic workflow:
python scripts/parse_pdf_structure.py \
  --input papers/ \
  --output literature-notes/plant-gene-network-curation/{topic}/pdf_structure/ \
  --backend auto

Step 2. Check parsing_manifest.csv.

Confirm every PDF has:
- parser_used
- parser_status
- fallback_used
- has_text_layer
- page_count
- Introduction / Methods / Results / Discussion / References status
- confidence
- need_manual_review

Step 3. Use parsed_text/{paper_slug}.md or .json for reading.

If confidence is high or medium:
- use the detected sections as reading anchors.

If Introduction or other major sections are not stable:
- label the source basis as section-uncertain full-text reading.
- keep reading if full text is available.
- write [Introduction 标题未稳定识别，正文结构需人工复核] when Introduction is uncertain.
- do not pretend uncertain section boundaries are confirmed.

Step 4. Generate one full-text paper card per paper.

Use templates/fulltext-paper-card.md and keep parser metadata in Source Basis.

Step 5. Run cited-reference mining when requested or when full-text close reading requires it.

Use prompts/cited-relevant-literature-mining.md after the parsed full-text reading, not before parsing.

Step 6. Build downstream outputs.

Depending on the user goal, generate:
- evidence matrix
- cited-reference inventory
- plant functional gene inventory
- regulatory edge table
- review outline
- review paragraph draft

Final quality check:
1. Every PDF has parser_used.
2. fallback_used is recorded.
3. scanned/image-only PDFs are marked.
4. parsed_text exists for successful parses.
5. structure_report exists.
6. Introduction / Methods / Results / Discussion / References statuses are explicit.
7. Uncertain sections are not presented as confirmed.
8. fulltext-paper-card keeps section uncertainty.
9. Original PDFs were not deleted or moved.
```
