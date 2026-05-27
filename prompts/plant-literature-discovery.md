# Plant Literature Discovery Prompt

```text
Use scientific-review-skill to run the Literature Discovery and Prioritization Module for the Plant Trait and Stress Functional Gene Network Curation Workflow.

Goal:
Start from a plant trait, stress response, hormone pathway, developmental process, crop topic, or molecular-breeding topic and generate a candidate paper inventory plus full-text acquisition priorities. This module is for discovery and prioritization only; it is not full-text evidence curation.

Use when:
- The user only provides a topic, such as drought stress, nitrogen response, cotton fiber development, root architecture, ABA response, disease resistance, or yield traits.
- The user has not collected PDFs yet.
- The user wants to know which papers are worth downloading and reading first.

Required inputs:
- Topic:
- Species priority:
- Optional gene names:
- Optional trait/stress keywords:
- Optional evidence scope:
- Optional date range:
- Optional database preference:
- Optional journal metrics mode: disabled / enabled / user-provided metrics table

Default output directory:
literature-notes/plant-gene-network-curation/literature_discovery/

Required outputs:
- search_strategy.md
- candidate_papers.csv
- candidate_papers.md
- fulltext_priority_list.md
- need_fulltext.md
- journal_metrics_summary.md
- need_journal_metric_verification.md

Workflow:
1. Generate topic keywords.
   - Start from the user topic.
   - Add synonyms, trait terms, stress terms, gene-function terms, and crop/plant terms.
   - Keep separate keyword groups for topic, species, evidence type, gene/regulatory terms, and omics/database terms.

2. Expand by species, trait, and evidence type.
   - Species examples: Arabidopsis, rice, maize, wheat, cotton, soybean, tomato, or user-specified species.
   - Trait/stress examples: nitrogen response, nitrogen use efficiency, drought, salt, cold, heat, phosphate starvation, ABA response, disease resistance, root architecture, flowering time, fiber development, yield, seed development, hormone signaling.
   - Evidence keywords:
     - Functional validation: mutant, overexpression, CRISPR, complementation, transgenic.
     - Mechanistic regulation: ChIP, EMSA, Y1H, dual-luc, DAP-seq, promoter, transcription factor, regulatory relationship.
     - Genetic mapping: GWAS, QTL, fine mapping, haplotype, allele.
     - Omics association: RNA-seq, DEG, WGCNA, GO, KEGG, co-expression.
     - Secondary or weak evidence: review, homolog, annotation.

3. Generate database search strategies.
   - Provide query strings suitable for PubMed, Google Scholar, Web of Science, Scopus, Crossref, Semantic Scholar, Europe PMC, bioRxiv, and plant/crop databases when relevant.
   - If live search is available and requested, use reliable scholarly sources and record the source database for each result.
   - If live search is not available, generate reproducible query strings and mark candidate entries as user-search-needed.

4. Collect candidate paper metadata.
   - Title
   - Authors
   - Year
   - Journal
   - ISSN/eISSN
   - Publisher
   - DOI
   - PMID
   - Species
   - Gene names
   - Trait / stress
   - Evidence type
   - Whether full text is needed
   - Priority

5. Enrich journal metrics when requested.
   - Follow references/journal-metrics-rules.md.
   - Add JCR Impact Factor, JIF Year, JCR Category, JCR Quartile, CiteScore, CiteScore Year, CiteScore Percentile/Quartile, SJR, SJR Year, SJR Quartile, Metric Source, Metric Access Status, and Journal Metric Notes when available.
   - Use ISSN/eISSN to disambiguate journal names when possible.
   - Prefer user-provided JCR exports or journal metrics tables.
   - If JCR is unavailable, use publicly checkable CiteScore or SJR as auxiliary fallback metrics.
   - Put unresolved metrics in need_journal_metric_verification.md.

6. Assign full-text priority.
   - Priority A:
     - mutant / overexpression / CRISPR / complementation
     - ChIP / EMSA / Y1H / dual-luc / DAP-seq
     - clear regulatory relationship
     - target species evidence
   - Priority B:
     - GWAS / QTL / fine mapping
     - physiological phenotype plus expression validation
     - candidate gene with strong trait association
   - Priority C:
     - RNA-seq / DEG / WGCNA / GO/KEGG / co-expression
     - review papers
     - homolog inference only
   - If scoring is requested, use:
     - Evidence Score: 40%
     - Topic Relevance Score: 25%
     - Species Priority Score: 15%
     - Recency Score: 5%
     - Journal Metric Score: 15%
   - Journal Metric Score is auxiliary and must not exceed 15% of the priority score.

7. Generate need_fulltext.md.
   - List papers whose metadata or abstract suggests useful evidence but whose full text is required before curation.
   - Mark paywalled papers as need user/institutional access.
   - Do not suggest illegal full-text sources.

8. Generate journal_metrics_summary.md when journal metrics are enabled.
   - Confirmed journals with JCR Impact Factor.
   - Journals with only CiteScore/SJR.
   - Journals with inconsistent metric years.
   - Journals requiring manual verification.
   - Papers with ambiguous journal name or ISSN.

Rules:
- Do not treat a candidate paper list as full-text evidence.
- Without full text, label judgments as metadata-level or abstract-level only.
- Without original figures, tables, methods, and full-text evidence, do not create high-confidence regulatory edges.
- Enter full-text evidence curation only after the user provides PDFs, extracted text, or verified full-text notes.
- Do not use illegal full-text sources.
- For paywalled papers, write need user/institutional access.
- Do not invent Impact Factor, JCR category, JCR quartile, CiteScore, SJR, ISSN/eISSN, publisher, or metric year.
- Journal metrics can guide reading priority but cannot replace evidence type, experimental design, or source-traced functional validation.
- Low journal metrics must not automatically exclude papers with strong functional or mechanistic evidence.
- High journal metrics must not upgrade weak evidence into high-confidence functional gene or regulatory network evidence.
- Do not invent authors, years, journals, DOI, PMID, gene IDs, species, experiments, regulatory relationships, figures, or conclusions.
- Use unknown, [需要核实], or [source needed] for missing information.
- Separate Source-reported content, Reasonable inference, and Model synthesis when discussing why a paper is prioritized.

Final quality check:
1. Are all candidate-paper judgments marked as metadata-level, abstract-level, or full-text available?
2. Are missing DOI, PMID, authors, year, journal, species, and gene names marked as unknown or [需要核实]?
3. Are Priority A papers justified by evidence-type signals rather than assumed full-text conclusions?
4. Are review papers and omics-only papers prevented from becoming high-confidence regulatory evidence?
5. Are paywalled papers marked need user/institutional access?
6. Are journal metrics sourced, year-labeled, and kept separate from evidence strength?
7. Are missing or ambiguous journal metrics listed in need_journal_metric_verification.md?
8. Is the next step clearly stated: user should provide PDFs/full text for full-text evidence curation.
```
