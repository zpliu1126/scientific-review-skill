# Literature Search Strategy Template

Use this template for `search_strategy.md` in:

```text
literature-notes/plant-gene-network-curation/literature_discovery/
```

## 1. Topic Scope

- Topic:
- Species priority:
- Trait / stress scope:
- Evidence scope:
- Date range:
- Exclusion boundaries:

## 2. Keyword Groups

### Topic Keywords

- 

### Species Keywords

- 

### Trait / Stress Keywords

- 

### Functional Evidence Keywords

- mutant
- overexpression
- CRISPR
- complementation
- transgenic

### Mechanistic / Regulatory Evidence Keywords

- ChIP
- EMSA
- Y1H
- dual-luc
- DAP-seq
- promoter
- transcription factor
- regulatory relationship

### Genetic Mapping Keywords

- GWAS
- QTL
- fine mapping
- haplotype
- allele

### Omics Association Keywords

- RNA-seq
- DEG
- WGCNA
- GO
- KEGG
- co-expression

### Secondary / Weak Evidence Keywords

- review
- homolog
- annotation

## 3. Database Query Strategies

Keep query strings reproducible. Adjust syntax for each database.

### PubMed

```text
({topic terms}) AND ({species terms}) AND ({evidence terms})
```

### Google Scholar

```text
"{topic}" "{species}" "{evidence keyword}"
```

### Web of Science / Scopus

```text
TS=(({topic terms}) AND ({species terms}) AND ({evidence terms}))
```

### Crossref / Semantic Scholar / Europe PMC

```text
{topic terms} {species terms} {evidence terms}
```

### Preprint Servers

```text
{topic terms} {species terms} {gene or evidence terms}
```

### Plant / Crop Databases

```text
{gene or trait terms} {species} {annotation or ortholog terms}
```

### Journal Metrics Sources

Use journal metrics only when the user requests Journal Metrics Enrichment or provides a journal metrics table.

Preferred order:
1. User-provided JCR export or journal metrics table.
2. JCR, when access is available.
3. Scopus CiteScore, when available.
4. SCImago/SJR, when public data are available.
5. unknown / [需要核实] when no reliable source is available.

Lookup keys:

- Full journal title from paper metadata.
- ISSN/eISSN.
- Publisher.
- Metric year.

Do not merge JCR quartile, CiteScore quartile, and SJR quartile into a single generic quartile. Record each source separately.

## 4. Search Expansion Plan

1. Start with broad topic plus plant/crop terms.
2. Add species-specific names and common names.
3. Add functional validation keywords.
4. Add mechanistic regulatory keywords.
5. Add GWAS/QTL/fine-mapping keywords.
6. Add omics association keywords.
7. Add known gene names if supplied by the user.
8. If Journal Metrics Enrichment is enabled, match journals by ISSN/eISSN before adding metrics.

## 5. Journal Metrics Enrichment Plan

1. Extract journal names from candidate paper metadata.
2. Normalize journal names and record ISSN/eISSN when available.
3. Match metrics using user-provided tables first.
4. If JCR is available, add JCR Impact Factor, JIF Year, JCR Category, and JCR Quartile.
5. If JCR is unavailable, use CiteScore and/or SJR as fallback auxiliary metrics.
6. Record Metric Source and Metric Access Status for every metric.
7. Put unresolved, ambiguous, or year-mismatched journal metrics in `need_journal_metric_verification.md`.

## 6. Screening Criteria

Include papers that mention:
- The specified topic or closely related trait/stress.
- Priority species or a clearly relevant model species.
- Plant genes, alleles, loci, or regulatory relationships.
- Evidence types useful for functional gene or network curation.

Exclude or deprioritize:
- Papers with no plant gene, locus, pathway, or regulatory relevance.
- Purely agronomic papers without gene-level evidence unless the user requests them.
- Review-only sources when primary studies are available, except for background and citation mining.

## 7. Search Log

| Database | Query | Date | Result count | Notes |
|---|---|---|---|---|
|  |  |  | unknown |  |

## 8. Journal Metric Lookup Log

| Metric Source | Lookup key | Date | Metric year | Access status | Notes |
|---|---|---|---|---|---|
| unknown | unknown |  | unknown | need verification |  |

## 9. Evidence Boundary

- Search strategy does not establish evidence.
- Candidate metadata is metadata-level unless abstracts or full text were checked.
- Journal metrics are auxiliary literature-screening metadata, not evidence strength.
- Full-text evidence curation starts only after PDFs, extracted text, or verified full-text notes are available.
