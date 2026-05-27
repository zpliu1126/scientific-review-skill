# Preliminary Plant Functional Gene Regulatory Network

## 1. Network Scope

- Topic:
- Species scope:
- Treatment / condition:
- Tissue / stage:
- Evidence scope:
- Input sources:
- Source basis:
- Evidence boundary:

## 2. Core Modules

Select modules that fit the topic; do not force every module into every network.

- signal perception:
- transcriptional regulation:
- transport:
- metabolism:
- hormone crosstalk:
- ROS / stress signaling:
- root / shoot development:
- yield or agronomic traits:
- species-specific modules:

## 3. High-Confidence Edges

Include only Level 1-2 edges with explicit sources.

| Source | Target | Relationship | Directness | Evidence level | Source paper | Figure/Table/Page |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 4. Medium-Confidence Edges

Include Level 3 edges with genetic mapping plus expression, allele, or physiological support.

| Source | Target | Relationship | Directness | Evidence level | Source paper | Figure/Table/Page |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 5. Candidate Edges

Include Level 4-5 edges only when clearly marked as candidate, inferred, co-expression only, homolog-inferred, or literature-inferred.

| Source | Target | Relationship | Directness | Evidence level | Source paper | Figure/Table/Page |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 6. Text Network Model

用中文描述初步调控模型。必须区分文献直接报告的内容、合理推断和模型综合；不得加入无出处的基因或边。

### Source-reported content

### Reasonable inference

### Model synthesis

## 7. Mermaid Network Diagram

Only include sourced edges. Label each edge with evidence level and directness.

```mermaid
graph LR
  A[Gene A] -->|Level 1 direct; source: [需要核实]| B[Gene B]
```

## 8. Cytoscape Export

- `network_nodes_for_cytoscape.csv`
- `network_edges_for_cytoscape.csv`

### Node Fields

```csv
id,gene_symbol,gene_id,species,functional_category,evidence_level,topic,description
```

### Edge Fields

```csv
source,target,interaction,directness,evidence_level,evidence_type,species,topic,condition,source_paper,doi_pmid,figure_table_page,confidence
```

## 9. Evidence Gaps

- Missing ChIP/EMSA/Y1H/dual-luc:
- Missing mutant / CRISPR:
- Missing cross-species validation:
- Missing direct evidence in the target species:
- Missing field phenotype:
- Missing time-series or tissue-specific evidence:

## 10. Review-Ready Claims

Every claim must include supporting genes, supporting edges, and source papers.

| Claim | Supporting genes | Supporting edges | Source papers | Evidence level | Boundary wording |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
