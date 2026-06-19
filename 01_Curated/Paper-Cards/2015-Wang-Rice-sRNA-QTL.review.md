---
type: curated-paper-card
source: mineru
curation_skill: scientific-review-skill
title: Genetic basis of sRNA quantitative variation analyzed using an experimental population derived from an elite rice hybrid
authors: Jia Wang; Wen Yao; Dan Zhu; Weibo Xie; Qifa Zhang
year: 2015
journal: eLife
doi: 10.7554/eLife.03913
study_type: primary research; sRNA quantitative genetics
field: rice genomics; small RNA genetics
topics: [rice, sRNA, sQTL, scQTL, IMF2, small RNA biogenesis]
source_basis: full.md + content_list.json
evidence_strength: high for population sRNA-QTL mapping; moderate for candidate biogenesis-gene interpretation
curation_status: curated; needs manual PDF check
mineru_dir: mineru-parsed/Wang_2015_eLife
created: 2026-06-07
updated: 2026-06-07
---

# Genetic basis of sRNA quantitative variation analyzed using an experimental population derived from an elite rice hybrid

## 1. Citation metadata

- Title: Genetic basis of sRNA quantitative variation analyzed using an experimental population derived from an elite rice hybrid
- Authors: Jia Wang; Wen Yao; Dan Zhu; Weibo Xie; Qifa Zhang
- Year: 2015
- Journal: eLife
- DOI: 10.7554/eLife.03913
- Article type: primary research

## 2. Source basis

Based on `mineru-parsed/Wang_2015_eLife/full.md`, `content_list.json`, and `meta.json`. figure/table anchor uncertain; needs manual PDF check.

## 3. One-sentence takeaway

本文用 elite rice hybrid 来源的 immortalized F2 群体把 sRNA abundance 当作数量性状，系统定位了 sQTL/scQTL，显示植物 sRNA 水平具有广泛遗传控制且常与 mother gene expression 不同步。

## 4. Research question

本文要回答：rice 个体间 sRNA abundance 的定量差异由哪些遗传位点控制，sRNA 与其来源基因/cluster 是否共同调控，以及 sRNA biogenesis genes 是否解释特定长度类别的 sRNA variation。

## 5. Study design

材料为 Zhenshan 97 x Minghui 63 RILs 构建的 98 个 IMF2 hybrids、亲本和 F1。作者从 flag leaf full expansion day 取样，构建 104 个 sRNA libraries，并结合 mRNA-seq、WGBS 和 ultrahigh-density bin map 进行 QTL 分析。

## 6. Key methods

- sRNA-seq of 18-26 nt reads.
- SNP-replaced parental reference genomes for mapping.
- RPM quantification of s-traits and DESeq quantification of sRNA cluster traits.
- QTL mapping with R/qtl and ultrahigh-density bin map.
- Local/distant sQTL and scQTL classification.
- mRNA-seq and WGBS for mother gene and methylation context.

## 7. Main findings with anchors

### Finding 1

- Source-reported content: 104 libraries produced 53,613,739 unique sRNAs; 165,797 sRNA expression traits were recovered; 24-nt sRNAs/s-traits were dominant.
- Figure/table/section anchor if available: Abstract; Results "Patterns and distributions of sRNAs"; Table 1; Fig. 1.
- Evidence type: sRNA-seq profiling.
- Limitation: flag leaf only.
- Confidence level: high.

### Finding 2

- Source-reported content: 66,649 s-traits mapped to 40,049 local-sQTLs and 30,809 distant-sQTLs; 22,263 scQTLs were recovered for 20,249 sc-traits.
- Figure/table/section anchor if available: Abstract; QTL sections.
- Evidence type: quantitative genetics.
- Limitation: QTL resolution depends on bin map and IMF2 design.
- Confidence level: high.

### Finding 3

- Source-reported content: sRNAs from the same genes or clusters were usually slightly positively correlated, but most sRNAs and their mother genes showed little co-regulation.
- Figure/table/section anchor if available: Abstract; Fig. 2 and related sections.
- Evidence type: expression correlation and QTL comparison.
- Limitation: correlation does not identify molecular mechanism.
- Confidence level: moderate-high.

### Finding 4

- Source-reported content: Some sRNA biogenesis genes were located in distant-sQTL hotspots and corresponded with specific length classes of sRNAs.
- Figure/table/section anchor if available: Abstract; discussion of distant-sQTL hotspots.
- Evidence type: QTL hotspot/candidate gene association.
- Limitation: candidate-gene causality not functionally tested in provided text.
- Confidence level: moderate.

### Finding 5

- Source-reported content: The paper reports widespread negative dominance of sRNA levels in IMF2, with heterozygotes often below parental means or lower homozygotes; many such sQTLs were distant-sQTLs.
- Figure/table/section anchor if available: Discussion.
- Evidence type: genetic effect analysis.
- Limitation: relationship to hybrid performance is presented as an open challenge.
- Confidence level: moderate.

## 8. Author conclusions

作者认为 rice sRNA abundance 具有大规模遗传控制；sRNAs 与 mother genes 的调控常可分离；部分 distant-sQTL hotspots 可能反映 sRNA biogenesis/function machinery 对特定 sRNA 长度类别的调节。

## 9. Reasonable inference

- The sQTL framework may suggest that small RNA abundance can be treated as a molecular quantitative trait, similar to mRNA eQTL.
- Distant-sQTL hotspots could indicate trans-acting regulators, but specific causal variants need validation.

## 10. Model synthesis

本文提供了“sRNA quantitative genetics”框架：从单条 sRNA、sRNA cluster、mother gene expression 和 genetic bin effects 四个层面，把 sRNA variation 拆成 local genetic control、distant/trans control 和 cluster-level co-regulation。

## 11. Limitations and missing controls

- 主要组织是 flag leaf，不能代表所有 rice tissues。
- QTL/candidate gene associations mostly lack functional perturbation.
- Relationship between negative dominance of sRNA levels and hybrid performance remains unresolved.
- figure/table anchor uncertain; needs manual PDF check.

## 12. Reusable knowledge

- Concepts: s-trait; sQTL; sc-trait; scQTL; local/distant QTL; negative dominance.
- Methods: sRNA population profiling; SNP-replaced reference mapping; R/qtl CIM; sRNA cluster quantification.
- Dataset: Dryad dataset `10.5061/dryad.9d030`.
- Framework: molecular trait QTL mapping for small RNA abundance.

## 13. Open questions

- 哪些 distant-sQTL hotspots 的 candidate genes 真正控制 sRNA biogenesis？
- sRNA negative dominance 与 rice hybrid vigor 是否有关？
- 不同 tissue 和 stress 条件下 sQTL landscape 是否稳定？
