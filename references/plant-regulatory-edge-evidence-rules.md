# Plant Regulatory Edge Evidence Rules

Use this reference when curating regulatory, genetic, pathway, co-expression, homolog-inferred, or literature-inferred relationships for plant functional gene networks.

## Core Rule

Every formal network edge must have a source. If a relationship has no traceable source, place it in `need_verification.md` and do not include it in `plant_regulatory_edge_table.csv` or `network_edges_for_cytoscape.csv`.

## Directness Classes

### direct

Use when there is direct regulatory or mechanistic evidence, such as ChIP-qPCR, ChIP-seq, DAP-seq, EMSA, Y1H, dual-luciferase assay, promoter activity assay, or another source-supported protein-DNA/protein-target assay.

Can support:
- Direct binding, promoter regulation, transcriptional activation/repression, or direct physical interaction when the assay supports it.

Cannot support:
- Whole-pathway causality, field value, or conservation in other species without additional evidence.

### indirect

Use when perturbing one gene changes the target gene, pathway marker, metabolite, or phenotype, but direct binding or direct molecular interaction is not shown.

Can support:
- Upstream regulatory influence or pathway involvement.

Cannot support:
- Direct regulation, promoter binding, or physical interaction.

### genetic interaction

Use for double mutants, epistasis analysis, allele combinations, suppressor/enhancer relationships, or other explicit genetic interaction evidence.

Can support:
- Genetic ordering or pathway relationship when the experimental design supports it.

Cannot support:
- Direct molecular interaction unless biochemical evidence is also present.

### pathway association

Use for genes placed in the same pathway, process, or mechanism chain without direct pairwise regulation.

Can support:
- Shared pathway or functional module membership.

Cannot support:
- Direct activation, repression, binding, or genetic interaction.

### co-expression only

Use for WGCNA, correlation, RNA-seq co-expression, or time-series network inference without perturbation or direct assays.

Can support:
- Coordinated expression or candidate network relationship.

Cannot support:
- Direct regulation or causality.

### homolog-inferred

Use for a relationship inferred from an ortholog or homolog in another species.

Can support:
- A cross-species hypothesis or candidate relation.

Cannot support:
- Validation in the target species.

### literature-inferred

Use when a review, database summary, or secondary source states a relationship but the primary source has not been checked.

Can support:
- A lead for follow-up verification.

Cannot support:
- Primary evidence claims or high-confidence network edges.

## Relationship Vocabulary

- activates
- represses
- regulates
- binds promoter of
- trans-activates
- interacts with
- genetically interacts with
- upstream of
- downstream of
- co-expressed with
- associated with
- homolog-inferred relation

## Direction and Confidence

Direction:
- positive
- negative
- unknown

Confidence:
- high: usually Level 1-2 with clear source support and appropriate experimental context.
- medium: usually Level 3, or Level 2 with important missing details.
- low: usually Level 4-5, review-only, homolog-inferred, or missing key details.

## Review-Article Handling

- Review synthesis is secondary evidence.
- Do not treat a mechanism diagram in a review as a primary edge.
- If the review cites an original paper but the original paper has not been checked, mark the edge as literature-inferred and `Need verification = yes`.
- Upgrade the edge only after the primary source is verified.

## Quality Check

Before finalizing edge tables, verify:

- Every edge has a source paper or source note.
- Every high-confidence edge has experimental support.
- Co-expression is not labeled as direct regulation.
- Homolog-inferred edges are not labeled as target-species validation.
- Review-derived edges are not labeled as primary evidence.
- Missing DOI/PMID/figure/table/page values are marked as unknown or `[需要核实]`.
- Exact evidence snippets are short, source-grounded, and do not exceed copyright-safe quoting limits.
