# Scientific Review Skill

Scientific Review Skill helps an AI agent read life science literature, compare evidence across papers, and draft review materials without fabricating citations or blurring source-reported content, reasonable inference, and model synthesis. It is a general life science review skill with domain-specific support for plant and crop science, population and evolutionary genomics, molecular biology, omics studies, animal models, human genetics, and biomedical evidence.

## What It Supports

- Single-paper close reading
- PDF structure parsing before full-text close reading
- Full-text PDF close reading with cited-reference mining
- Batch PDF literature review with parser manifest and section uncertainty tracking
- Multi-paper evidence matrices
- Review outlines organized by scientific claims
- Review paragraph drafting with citation traceability
- Plant literature discovery and full-text prioritization when PDFs have not been collected
- Backward citation mining through the Cited Relevant Literature Mining Module
- Journal metrics enrichment for candidate paper screening, with strict separation from evidence strength
- Plant trait and stress functional gene network curation with source-traceable gene and edge tables
- Yuque MCP / API cloud document upload workflow with TOC verification and troubleshooting
- Explicit separation of source-reported content, reasonable inference, and model synthesis
- General review scoping, evidence grouping, controversy synthesis, and gap analysis
- Plant and omics evidence interpretation, including RNA-seq, DEG, GO/KEGG, WGCNA, qRT-PCR/qPCR, population genomics, comparative genomics, and functional validation boundaries
- Animal and human evidence interpretation, including cell models, animal models, cohorts, iPSC, organoids, and clinical validation boundaries

## Core Safety Rules

- Never invent references, DOI, PMID, author names, journal names, years, figures, species, cultivars, treatments, methods, statistics, results, pathways, or conclusions.
- Mark missing support as `[source needed]`; mark unverified but available support as `[needs verification]`.
- Distinguish source-reported content, reasonable inference, and model synthesis.
- State whether the analysis is based on full text, abstract, metadata, user notes, or searched sources.
- Preserve uncertainty, limitations, conflicting findings, and evidence quality.

## Directory Structure

```text
scientific-review-skill/
├── SKILL.md
├── README.md
├── agents/
├── assets/
├── prompts/
├── scripts/
├── templates/
├── examples/
└── references/
```

`scripts/` contains deterministic helpers for PDF text-layer checks and structured PDF parsing. `assets/` is reserved for future reusable assets.

## Suggested Use

Ask the agent to use this skill when working with life science papers, plant science, crop science, molecular biology, genetics, population genomics, evolutionary genomics, comparative genomics, stress physiology, transcriptomics, omics studies, animal or human functional genetics, candidate genes, functional validation, or review writing.

Example:

```text
Use scientific-review-skill to create an evidence matrix for these five papers on drought-responsive transcription factors in rice transcriptome studies.
```

## PDF Structure Parsing Module

Use the PDF Structure Parsing Module, 中文名“PDF 结构化解析模块”, before single-paper PDF close reading, batch PDF close reading, cited-reference mining, or plant functional gene evidence curation.

It converts PDFs into structured Markdown/JSON/TEI when possible and records parser confidence, fallback, text-layer status, detected sections, captions, and manual-review needs. This avoids relying only on pypdf-style plain text extraction, which can lose headings, two-column reading order, figure/table captions, and reference context.

Default output:

```text
literature-notes/pdf-structure/
```

Topic workflow output:

```text
literature-notes/plant-gene-network-curation/{topic}/pdf_structure/
```

Expected output structure:

```text
pdf_structure/
├── parsed_text/
│   ├── {paper_slug}.md
│   ├── {paper_slug}.json
│   └── {paper_slug}.tei.xml
├── structure_reports/
│   └── {paper_slug}_structure_report.md
├── parsing_manifest.csv
└── parsing_failures.md
```

Run:

```bash
python scripts/parse_pdf_structure.py \
  --input papers/ \
  --output literature-notes/pdf-structure/ \
  --backend auto
```

If GROBID is running as a service:

```bash
python scripts/parse_pdf_structure.py \
  --input papers/ \
  --output literature-notes/pdf-structure/ \
  --backend grobid \
  --grobid-url http://localhost:8070
```

For scanned PDFs, enable OCR only for image-only files:

```bash
python scripts/parse_pdf_structure.py \
  --input papers/ \
  --output literature-notes/pdf-structure/ \
  --backend auto \
  --ocr \
  --ocr-language eng+chi_sim
```

Backend priority for `--backend auto`:

1. GROBID
2. Docling
3. Marker
4. PyMuPDF4LLM
5. OCRmyPDF only for scanned/image-only PDFs before parser fallback

Optional backend installation:

```bash
# GROBID service, CPU-friendly
docker run --rm --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.9.0-crf

# Python backends
python -m pip install docling
python -m pip install marker-pdf
python -m pip install pymupdf4llm

# OCRmyPDF on Debian/Ubuntu
sudo apt-get install ocrmypdf tesseract-ocr tesseract-ocr-eng
sudo apt-get install tesseract-ocr-chi-sim
```

If Introduction is not stably detected, downstream full-text cards must include:

```text
[Introduction 标题未稳定识别，正文结构需人工复核]
```

Do not stop reading if full text is available. Continue as `section-uncertain full-text reading` and do not present uncertain section boundaries as confirmed.

## Cited Relevant Literature Mining Module

Use the Cited Relevant Literature Mining Module, 中文名“被引相关文献挖掘模块”, during single-paper PDF/full-text close reading when you want the reading card to also surface topic-relevant papers cited by the current paper.

This module is designed for backward citation mining:

- recover classic or core papers missed by keyword search
- identify original research cited by high-quality papers
- expand candidate_papers.csv and need_fulltext.md with seed papers
- support functional gene curation, regulatory network curation, mechanism reviews, and evidence matrices

It reads the current paper's Introduction, Results, Discussion, and References, then keeps only cited papers relevant to the current topic. It does not mechanically copy the full References section. Cited papers are literature discovery leads, not verified full-text evidence.

Default output:

```text
literature-notes/cited-literature/
```

Topic workflow output:

```text
literature-notes/plant-gene-network-curation/{topic}/cited_references/
├── per_paper/
│   └── {paper_slug}_cited_relevant_literature.md
├── cited_reference_inventory.csv
├── cited_reference_inventory.md
├── cited_reference_priority_list.md
└── need_reference_verification.md
```

Workflow chain:

```text
PDF Structure Parsing
-> Full-text Paper Reading
-> Cited Relevant Literature Mining
-> cited_reference_inventory.csv
-> merge into candidate_papers.csv
-> update need_fulltext.md
-> next-round full-text evidence curation
```

Example:

```text
Use scientific-review-skill.
Read this PDF in full-text close-reading mode.
Also run the Cited Relevant Literature Mining Module.

Topic: nitrogen use efficiency genes and breeding in wheat.
Output:
literature-notes/plant-gene-network-curation/nitrogen-use-efficiency/cited_references/
```

To merge cited-reference leads into candidate discovery, import Priority A/B rows from `cited_reference_inventory.csv`, deduplicate by DOI, PMID, or normalized title plus year, mark the source basis as `cited-reference lead`, and add papers with `need_fulltext = yes` or `maybe` to `need_fulltext.md`.

## Plant Gene Network Curation Workflow

Use the Plant Trait and Stress Functional Gene Network Curation Workflow when you need to curate plant genes and regulatory relationships for a trait, stress response, hormone pathway, developmental process, gene family, or molecular-breeding topic.

Default output directory:

```text
literature-notes/plant-gene-network-curation/
```

If you only have a topic and have not collected PDFs, run the Literature Discovery and Prioritization Module first. It writes:

```text
literature-notes/plant-gene-network-curation/literature_discovery/
├── search_strategy.md
├── candidate_papers.csv
├── candidate_papers.md
├── fulltext_priority_list.md
├── journal_metrics_summary.md
├── need_journal_metric_verification.md
└── need_fulltext.md
```

This module ranks candidate papers for full-text acquisition. Candidate paper metadata and abstracts are not full-text evidence; they must be labeled `metadata-level` or `abstract-level`. Paywalled papers should be marked `need user/institutional access`, and illegal full-text sources must not be used.

When Journal Metrics Enrichment is enabled, the candidate paper inventory can include JCR Impact Factor, JCR category/quartile, CiteScore, SJR, ISSN/eISSN, metric year, metric source, and access status. These metrics are only auxiliary screening metadata. They must not replace evidence type, experimental design, full-text verification, or functional gene evidence levels.

Expected outputs include:

- `topic_scope.md`
- `plant_functional_gene_inventory.csv`
- `plant_functional_gene_inventory.md`
- `plant_regulatory_edge_table.csv`
- `plant_regulatory_edge_table.md`
- `network_nodes_for_cytoscape.csv`
- `network_edges_for_cytoscape.csv`
- `network_model.md`
- `gene_cards/`
- `need_verification.md`

Core rule: every gene and every network edge must have a source. DEG, WGCNA, GO/KEGG, qPCR, co-expression, homolog inference, database annotation, and review mentions must not be written as functional validation or direct regulation unless primary evidence supports that claim.

## Yuque MCP / API Cloud Document Upload

When publishing literature cards or review outputs to a Yuque knowledge base, follow `references/yuque-cloud-upload.md`.

The workflow requires getting the current `login` with `yuque_get_user`, creating or identifying the knowledge base namespace, testing one document with `yuque_create_doc`, using minimal-log API upload for large batches when MCP returns full document bodies, and checking both `yuque_list_docs` and `yuque_get_toc` before reporting completion.

If documents exist but are missing from the Yuque directory tree, repair the TOC with `yuque_update_toc`. Do not report the upload as complete until the document list and TOC both contain every target document.

Literature discovery example:

```text
Run the Literature Discovery and Prioritization Module for the Plant Trait and Stress Functional Gene Network Curation Workflow.
Topic: cotton fiber development.
Species priority: cotton, Arabidopsis.
Goal: identify candidate papers worth downloading and full-text reading before network curation.
```

Journal metrics enrichment example:

```text
Use scientific-review-skill.

Run Plant Trait and Stress Functional Gene Network Curation Workflow.
Start with Literature Discovery and Prioritization Module.
Enable Journal Metrics Enrichment Module.

Topic:
drought stress functional genes and regulatory networks in plants.

Species priority:
Arabidopsis, rice, maize, wheat, cotton.

Journal metrics:
- Add JCR Impact Factor if available.
- Add JCR quartile and category if available.
- Add CiteScore and SJR as fallback metrics.
- Record metric year and source.
- Do not invent missing journal metrics.
- Do not use journal metrics as evidence strength.

Output:
literature-notes/plant-gene-network-curation/literature_discovery/
```

Example 1:

```text
Run Plant Trait and Stress Functional Gene Network Curation Workflow.
Topic: nitrogen response and NUE.
Species priority: Arabidopsis, rice, maize, wheat, cotton.
Evidence scope: include functional validation, candidate genes, omics associations, homolog-inferred genes, and regulatory network edges.
Input sources: papers/, literature-notes/, user-provided gene list, user-provided DEG/WGCNA/GWAS/QTL table, public database notes, SRA/GEO metadata notes, accession-linked paper notes, manually curated seed papers.
```

Example 2:

```text
Run Plant Trait and Stress Functional Gene Network Curation Workflow.
Topic: drought stress.
Species priority: Arabidopsis, rice, maize, cotton.
Evidence scope: include functional validation, candidate genes, omics associations, homolog-inferred genes, and regulatory network edges.
Input sources: papers/, literature-notes/, and user-provided DEG/WGCNA/GWAS/QTL table.
```

Example 3:

```text
Run Plant Trait and Stress Functional Gene Network Curation Workflow.
Topic: cotton fiber development.
Species priority: cotton, Arabidopsis.
Evidence scope: include functional validation, candidate genes, homolog-inferred genes, and regulatory network edges.
Input sources: papers/, literature-notes/, public database notes, SRA/GEO metadata notes, accession-linked paper notes, and manually curated seed papers.
```

## Important Limitation

This skill improves evidence handling and writing structure. It does not replace expert scientific review, clinical judgment, statistical review, or verification against original full-text sources.



## Install

### User-level install

Clone this repository into Codex's user skills directory:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/zpliu1126/scientific-review-skill.git ~/.agents/skills/scientific-review-skill
```

Then reload skills in Codex or restart the Codex IDE extension.

You can invoke the skill in Codex with:

```text
$scientific-review-skill
```

### Project-level install

For a single project, place the skill under the project's `.agents/skills/` directory:

```bash
mkdir -p .agents/skills
git clone https://github.com/zpliu1126/scientific-review-skill.git .agents/skills/scientific-review-skill
```

Then reload skills in Codex or restart the Codex IDE extension.

You can invoke the skill in Codex with:

```text
$scientific-review-skill
```

### Update

To update the skill later:

```bash
cd ~/.agents/skills/scientific-review-skill
git pull
```

For a project-level installation:

```bash
cd .agents/skills/scientific-review-skill
git pull
```
