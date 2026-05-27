# Candidate Paper Inventory Template

Use this template for `candidate_papers.md` and the matching `candidate_papers.csv` in:

```text
literature-notes/plant-gene-network-curation/literature_discovery/
```

## Source Basis

- Topic:
- Species priority:
- Search date:
- Search databases:
- Search mode: live search / user-provided results / generated strategy only / mixed
- Evidence scope:
- Source basis: metadata-level / abstract-level / full-text available / mixed

## Candidate Paper Inventory

| Title | Authors | Year | Journal | ISSN/eISSN | Publisher | JCR Impact Factor | JIF Year | JCR Category | JCR Quartile | CiteScore | CiteScore Year | CiteScore Percentile/Quartile | SJR | SJR Year | SJR Quartile | Metric Source | Metric Access Status | Journal Metric Notes | DOI | PMID | Species | Gene names | Trait / stress | Evidence type | Source basis | Whether full text is needed | Priority | Access status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| unknown | unknown | unknown | unknown | unknown | unknown | [需要核实] | unknown | [需要核实] | [需要核实] | [需要核实] | unknown | [需要核实] | [需要核实] | unknown | [需要核实] | unknown | need verification |  | unknown | unknown | unknown | unknown | unknown | unknown | metadata-level | yes | unknown | [需要核实] |  |

## Journal Metric Fields

- Journal: journal name from paper metadata.
- ISSN/eISSN: use to disambiguate abbreviated or similar journal names.
- Publisher: journal publisher when available.
- JCR Impact Factor: Journal Impact Factor from Journal Citation Reports.
- JIF Year: year of the Journal Impact Factor, such as 2024 JIF.
- JCR Category: JCR subject category.
- JCR Quartile: Q1 / Q2 / Q3 / Q4 in the relevant JCR category.
- CiteScore: Scopus CiteScore.
- CiteScore Year: year of the CiteScore metric.
- CiteScore Percentile/Quartile: Scopus percentile or quartile.
- SJR: SCImago Journal Rank.
- SJR Year: year of the SJR metric.
- SJR Quartile: SCImago quartile.
- Metric Source: JCR / Scopus CiteScore / SCImago / user-provided table / unknown.
- Metric Access Status: verified / user-provided / public-source / unavailable / need verification.
- Journal Metric Notes: journal name changes, abbreviation ambiguity, metric-year mismatch, category differences, or ISSN uncertainty.

## Evidence Type Vocabulary

- mutant / overexpression / CRISPR / complementation
- transgenic validation
- ChIP / EMSA / Y1H / dual-luc / DAP-seq
- clear regulatory relationship
- target species evidence
- GWAS / QTL / fine mapping
- haplotype / allele association
- physiological phenotype plus expression validation
- RNA-seq / DEG
- WGCNA / co-expression
- GO/KEGG enrichment
- review paper
- homolog inference only
- database annotation
- unknown

## Priority Rules

- Priority A: likely highest value for full-text curation because metadata/abstract indicates direct functional, mechanistic, regulatory, or target-species evidence.
- Priority B: likely useful for candidate gene discovery because metadata/abstract indicates mapping, strong trait association, physiological phenotype, or expression validation.
- Priority C: useful for background, candidate generation, or review framing, but not sufficient for high-confidence functional or regulatory claims without primary evidence.

## Boundary Notes

- Candidate paper inventory is not full-text evidence.
- Metadata-level and abstract-level signals must not be used to build high-confidence regulatory edges.
- Journal metrics are auxiliary screening information, not evidence strength.
- Do not upgrade or downgrade functional gene evidence levels based on journal metrics.
- Paywalled papers should be marked `need user/institutional access`.
- Illegal full-text sources must not be used or recommended.
- Do not invent Impact Factor, JCR quartile, CiteScore, SJR, ISSN, publisher, or metric year.
- If metrics cannot be confirmed, write `[需要核实]` or `unknown`.

## Evidence Boundary

- Source-reported content:
- Reasonable inference:
- Model synthesis:
