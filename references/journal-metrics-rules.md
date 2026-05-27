# Journal Metrics Rules

Use this reference when enriching candidate paper inventories or full-text priority lists with journal-level metrics. Journal metrics are auxiliary screening metadata. They do not measure the evidence strength of a specific paper and must not override experimental design, evidence type, source traceability, or full-text evidence curation.

## 1. Scope

This reference applies to the Literature Discovery and Prioritization Module and to candidate paper lists generated for plant functional gene and regulatory network curation.

Supported metrics:

- Journal Citation Reports Journal Impact Factor.
- JIF Year.
- JCR Category.
- JCR Quartile.
- Scopus CiteScore.
- CiteScore Year.
- CiteScore Percentile/Quartile.
- SCImago Journal Rank.
- SJR Year.
- SJR Quartile.
- ISSN/eISSN and publisher metadata used for journal disambiguation.

## 2. Core Rules

1. Do not invent Impact Factor, JCR quartile, CiteScore, SJR, ISSN/eISSN, publisher, metric source, or metric year.
2. If a metric cannot be confirmed, write `[需要核实]`, `unknown`, or `unavailable`.
3. Always record the metric year; do not report a metric as a bare number.
4. Use ISSN/eISSN when possible to avoid confusion between journal abbreviations, renamed journals, and similarly named journals.
5. If the user provides a JCR export or journal metrics table, use it as the preferred source and mark `Metric Access Status = user-provided`.
6. If JCR access is unavailable, CiteScore or SJR may be used as public auxiliary indicators.
7. If JCR, CiteScore, and SJR quartiles differ, record them separately and do not collapse them into one generic `Q1`.
8. Do not treat journal metrics as direct proof of paper quality, experimental reliability, gene function, or regulatory mechanism.
9. Do not exclude a paper solely because its journal metric is low when it contains strong functional validation or mechanistic evidence.
10. Do not upgrade a weak-evidence paper to high-confidence functional gene or regulatory network evidence because its journal metric is high.

## 3. Required Candidate-Paper Fields

Use these fields when journal metrics are enabled:

| Field | Meaning |
|---|---|
| Journal | Journal name from paper metadata. |
| ISSN/eISSN | Identifier used to disambiguate journal titles. |
| Publisher | Journal publisher when available. |
| JCR Impact Factor | Journal Impact Factor from Journal Citation Reports. |
| JIF Year | Year corresponding to the JIF. |
| JCR Category | JCR subject category. |
| JCR Quartile | Q1 / Q2 / Q3 / Q4 in a JCR category. |
| CiteScore | Scopus CiteScore. |
| CiteScore Year | Year corresponding to CiteScore. |
| CiteScore Percentile/Quartile | Scopus percentile or quartile. |
| SJR | SCImago Journal Rank. |
| SJR Year | Year corresponding to SJR. |
| SJR Quartile | SCImago quartile. |
| Metric Source | JCR / Scopus CiteScore / SCImago / user-provided table / unknown. |
| Metric Access Status | verified / user-provided / public-source / unavailable / need verification. |
| Journal Metric Notes | Name changes, abbreviation ambiguity, metric-year mismatch, category differences, or ISSN uncertainty. |

## 4. Priority Score Rule

When a priority score is used for full-text acquisition, use:

```text
Priority Score = Evidence Score + Topic Relevance Score + Species Priority Score + Recency Score + Journal Metric Score
```

Suggested weights:

- Evidence Score: 40%.
- Topic Relevance Score: 25%.
- Species Priority Score: 15%.
- Recency Score: 5%.
- Journal Metric Score: 15%.

Journal Metric Score must not exceed 15% of the total priority score. Evidence Score remains the dominant component.

## 5. Interpretation Boundaries

- Journal metrics can help decide which papers to inspect first when many candidates are available.
- Journal metrics cannot replace full-text reading, figure/table verification, methods assessment, or evidence-level assignment.
- A Priority A paper is prioritized because of functional, mechanistic, regulatory, or target-species evidence signals, not because of a journal metric.
- A Priority C paper remains candidate/background evidence even if the journal metric is high.
- A low-metric journal can still publish a high-value functional validation paper.

## 6. Output Files

When journal metrics are enabled, generate:

- `journal_metrics_summary.md`
- `need_journal_metric_verification.md`

`journal_metrics_summary.md` should include:

1. Journals with confirmed JCR Impact Factor.
2. Journals with only CiteScore/SJR.
3. Journals with inconsistent metric years.
4. Journals requiring manual verification.
5. Papers with ambiguous journal name or ISSN.

`need_journal_metric_verification.md` should list unresolved journal title, ISSN/eISSN, publisher, metric source, metric year, category, quartile, and access issues.

## 7. Quality Check

Before finalizing:

- No journal metric is fabricated.
- Every numeric metric has a metric year.
- Every metric has a source and access status.
- JCR, CiteScore, and SJR values are kept separate.
- Journal name ambiguity is recorded.
- Missing metrics are marked `[需要核实]`, `unknown`, or `unavailable`.
- Journal metrics are not used as evidence strength.
- Functional gene and regulatory network evidence levels still follow experimental evidence rules.
