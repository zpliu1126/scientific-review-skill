# PDF Parsing Backends

Use this reference when selecting or installing PDF parsing backends for the PDF 结构化解析模块.

## Backend Priority

1. **GROBID**
   - Best first choice for scientific papers.
   - Produces TEI/XML with title, authors, abstract, body sections, references, and sometimes figure/table captions.
   - Requires a running service.

2. **Docling**
   - Use for complex layouts, tables, mixed figure/text pages, and PDFs where visual layout matters.
   - Produces Markdown/JSON/structured document output.

3. **Marker**
   - Use for PDF-to-Markdown/JSON conversion with equations, tables, images, and section cues.
   - Useful when GROBID is unavailable or layout conversion matters more than bibliographic TEI.

4. **PyMuPDF4LLM**
   - Lightweight fallback for Markdown conversion.
   - Faster and simpler, but lower confidence for scientific section structure than GROBID/Docling/Marker.

5. **OCRmyPDF**
   - Use only for scanned or image-only PDFs.
   - It creates a searchable PDF first; then parse that searchable PDF with GROBID, Docling, Marker, or PyMuPDF4LLM.

## Installation Notes

Use a virtual environment when installing Python backends.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### GROBID

Run GROBID as a local service:

```bash
docker run --rm --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.9.0-crf
```

For higher accuracy and a machine that can support it:

```bash
docker run --rm --gpus all --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.9.0-full
```

Then parse with:

```bash
python scripts/parse_pdf_structure.py \
  --input papers/ \
  --output literature-notes/pdf-structure/ \
  --backend grobid \
  --grobid-url http://localhost:8070
```

### Docling

```bash
python -m pip install docling
```

CPU-only Linux installs may need a PyTorch CPU wheel index:

```bash
python -m pip install docling --extra-index-url https://download.pytorch.org/whl/cpu
```

### Marker

```bash
python -m pip install marker-pdf
```

Marker may download models on first use. For CLI testing:

```bash
marker_single papers/example.pdf --output_format markdown --output_dir /tmp/marker-out
```

### PyMuPDF4LLM

```bash
python -m pip install pymupdf4llm
```

The script also tries plain PyMuPDF as a last local extraction path if PyMuPDF4LLM is missing:

```bash
python -m pip install pymupdf
```

### OCRmyPDF

Install OCRmyPDF and OCR language data through the operating system package manager when possible:

```bash
sudo apt-get update
sudo apt-get install ocrmypdf tesseract-ocr tesseract-ocr-eng
```

For simplified Chinese OCR:

```bash
sudo apt-get install tesseract-ocr-chi-sim
```

Run OCR only for scanned PDFs:

```bash
python scripts/parse_pdf_structure.py \
  --input papers/ \
  --output literature-notes/pdf-structure/ \
  --backend auto \
  --ocr \
  --ocr-language eng+chi_sim
```

## Backend Selection Rules

- Use `--backend auto` for routine batches.
- Use `--backend grobid` when GROBID is running and the PDFs are standard scientific articles.
- Use `--backend docling` for complex layouts, heavy tables, mixed image/text pages, or poor reading order.
- Use `--backend marker` when Markdown/JSON with equations, tables, and images is more useful than TEI/XML.
- Use `--backend pymupdf4llm` for fast low-cost fallback or quick screening.
- Enable `--ocr` only when `has_text_layer=no` or the text layer is unusable.

## Output Interpretation

- `parser_used`: backend that produced the accepted output.
- `parser_status`: `success`, `failed`, or `skipped_existing`.
- `fallback_used`: `no` if the first attempted backend succeeded; otherwise records the failed backend chain.
- `confidence`: section-structure confidence, not scientific evidence strength.
- `need_manual_review=yes`: section boundaries, reading order, captions, or metadata require human checking.

Do not upgrade evidence strength because a parser succeeded. Parser confidence only describes extraction quality.
