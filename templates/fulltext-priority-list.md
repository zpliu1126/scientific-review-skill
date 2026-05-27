# Full-Text Priority List Template

Use this template for `fulltext_priority_list.md` and `need_fulltext.md` in:

```text
literature-notes/plant-gene-network-curation/literature_discovery/
```

## Source Basis

- Topic:
- Species priority:
- Candidate paper source:
- Search mode:
- Source basis: metadata-level / abstract-level / mixed
- Full-text access status:
- Journal metric source:

## Priority A: Download and Read First

Use Priority A when metadata or abstract indicates likely high-value primary evidence.

Criteria:
- mutant / overexpression / CRISPR / complementation
- ChIP / EMSA / Y1H / dual-luc / DAP-seq
- clear regulatory relationship
- target species evidence

| Rank | Title | Authors | Year | Species | Gene names | Evidence signal | Why Priority A | DOI/PMID | Access status | Full text needed | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | unknown | unknown | unknown | unknown | unknown | unknown | [需要核实] | unknown | [需要核实] | yes |  |

## Priority B: Download After Priority A

Use Priority B when metadata or abstract indicates strong candidate-gene evidence, but not direct functional or mechanistic validation.

Criteria:
- GWAS / QTL / fine mapping
- physiological phenotype plus expression validation
- candidate gene with strong trait association

| Rank | Title | Authors | Year | Species | Gene names | Evidence signal | Why Priority B | DOI/PMID | Access status | Full text needed | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | unknown | unknown | unknown | unknown | unknown | unknown | [需要核实] | unknown | [需要核实] | yes |  |

## Priority C: Useful but Lower Priority

Use Priority C for background, candidate generation, or citation mining.

Criteria:
- RNA-seq / DEG / WGCNA / GO/KEGG / co-expression
- review papers
- homolog inference only

| Rank | Title | Authors | Year | Species | Gene names | Evidence signal | Why Priority C | DOI/PMID | Access status | Full text needed | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | unknown | unknown | unknown | unknown | unknown | unknown | [需要核实] | unknown | [需要核实] | yes |  |

## Priority Scoring

Use the score only to sort candidate papers for full-text acquisition. It is not an evidence level.

```text
Priority Score = Evidence Score + Topic Relevance Score + Species Priority Score + Recency Score + Journal Metric Score
```

Suggested weights:

- Evidence Score: 40%
- Topic Relevance Score: 25%
- Species Priority Score: 15%
- Recency Score: 5%
- Journal Metric Score: 15%

Rules:

- Evidence Score must remain the largest component.
- Journal Metric Score must not exceed 15% of the total score.
- Journal Metric Score must not upgrade weak evidence to high-confidence functional evidence.
- Low journal metrics must not automatically exclude papers with strong functional or mechanistic evidence.
- High journal metrics must not upgrade omics-only, review-only, or homolog-inferred papers into high-confidence evidence.
- If journal metrics are unavailable or unverified, score the journal metric component as unknown or 0 and mark `[需要核实]`.

| Rank | Title | Evidence Score | Topic Relevance Score | Species Priority Score | Recency Score | Journal Metric Score | Priority Score | Priority Class | Metric Source | Metric Access Status | Score Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | unknown | unknown | unknown | unknown | unknown | unknown | unknown | unknown | unknown | need verification |  |

## need_fulltext.md Section

List papers requiring user or institutional access before full-text evidence curation.

| Title | DOI/PMID | Priority | Access status | Needed for | Notes |
|---|---|---|---|---|---|
| unknown | unknown | unknown | need user/institutional access | [需要核实] | Do not use illegal full-text sources. |

## Boundary Rules

- Candidate-paper priority is not evidence strength.
- Journal metric score is auxiliary and must not exceed 15% of the priority score.
- Without full text, all judgments remain metadata-level or abstract-level.
- Do not build high-confidence regulatory edges from metadata or abstract alone.
- Do not treat review papers as primary experimental evidence.
- Do not treat journal impact metrics as proof of paper quality, experimental reliability, gene function, or regulatory evidence.
- After PDFs or verified full-text notes are supplied, move to full-text evidence curation.
