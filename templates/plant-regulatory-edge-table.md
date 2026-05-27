# Plant Regulatory Edge Table Template

Use this template for `plant_regulatory_edge_table.md` and the matching `plant_regulatory_edge_table.csv`.

## Edge Inclusion Rule

Every edge in the formal edge table must have a source. Unsourced edges, vague pathway statements, unsupported database links, or review-only statements without primary-source verification must be moved to `need_verification.md`.

## Regulatory Edge Table

| Edge ID | Source gene | Source gene ID | Target gene | Target gene ID | Species | Topic | Relationship | Direction | Directness | Condition | Tissue/stage | Evidence level | Evidence type | Experimental support | Source paper | PMID/DOI | Figure/Table/Page | Exact evidence snippet | Confidence | Need verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EDGE-001 | unknown | unknown | unknown | unknown | unknown | unknown | regulates | unknown | literature-inferred | unknown | unknown | Level 5 | unknown | unknown | [source needed] | unknown | [需要核实] | [需要核实] | low | yes |

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

## Direction Vocabulary

- positive
- negative
- unknown

## Directness Vocabulary

- direct
- indirect
- genetic interaction
- pathway association
- co-expression only
- homolog-inferred
- literature-inferred

## Confidence Vocabulary

- high
- medium
- low

## Cytoscape Edge Export

`network_edges_for_cytoscape.csv` must use:

```csv
source,target,interaction,directness,evidence_level,evidence_type,species,topic,condition,source_paper,doi_pmid,figure_table_page,confidence
```

## Evidence Boundary Notes

- Source-reported content:
- Reasonable inference:
- Model synthesis:
