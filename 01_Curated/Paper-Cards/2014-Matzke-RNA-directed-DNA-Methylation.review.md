---
type: curated-paper-card
source: mineru
curation_skill: scientific-review-skill
title: RNA-directed DNA methylation: an epigenetic pathway of increasing complexity
authors: Marjori A. Matzke; Rebecca A. Mosher
year: 2014
journal: Nature Reviews Genetics
doi: 10.1038/nrg3683
study_type: review
field: plant epigenetics; small RNA biology
topics: [RdDM, RNA-directed DNA methylation, Pol IV, Pol V, siRNA, AGO4, DRM2, Arabidopsis]
source_basis: full.md + content_list.json
evidence_strength: review-level evidence
curation_status: curated; needs manual PDF check
mineru_dir: mineru-parsed/Matzke_2014_Nature Reviews Genetics
created: 2026-06-07
updated: 2026-06-07
---

# RNA-directed DNA methylation: an epigenetic pathway of increasing complexity

## 1. Citation metadata

- Title: RNA-directed DNA methylation: an epigenetic pathway of increasing complexity
- Authors: Marjori A. Matzke; Rebecca A. Mosher
- Year: 2014
- Journal: Nature Reviews Genetics
- DOI: 10.1038/nrg3683
- Article type: review

## 2. Source basis

本凝练基于 MinerU 解析目录 `mineru-parsed/Matzke_2014_Nature Reviews Genetics`：

- `full.md`
- `content_list.json`
- `meta.json`
- Parser note: `full.md` includes review text, glossary boxes, Table 1 and figure captions, but one extracted flowchart appears structurally corrupted; figure/table anchor uncertain; needs manual PDF check.

## 3. One-sentence takeaway

这篇综述系统概括了植物 RdDM 的 canonical pathway、Pol IV/Pol V 专化转录机制、辅助因子、染色质互作以及非 canonical 变体，是构建植物 small RNA-表观遗传知识框架的基础综述。

## 4. Research question

本文综述的问题是：植物 RNA-directed DNA methylation 如何通过 small RNAs、Pol IV/Pol V、AGO proteins 和 DNA methyltransferases 建立转录沉默，以及这一通路在转座子、基因调控、胁迫、防御和繁殖中的作用边界是什么。

## 5. Study design

这是 review article，不是单篇原始实验研究。文章主要基于 Arabidopsis thaliana 文献，同时在适当位置纳入其他植物研究。文中整合了遗传学、生化、ChIP-seq、methylome、small RNA sequencing 和突变体研究，但这些证据来自被综述文献；本卡不把综述观点当作原始实验结果。

## 6. Key methods

本文自身没有新增实验方法。综述中反复讨论的证据类型和方法包括：

- RdDM-defective mutant screens
- genetic and biochemical identification of Pol IV/Pol V components
- small RNA sequencing
- genome-wide DNA methylation profiling
- ChIP-seq for Pol V and chromatin features
- chromatin/protein interaction assays reported in cited studies
- comparative/evolutionary analysis of plant-specific RNA polymerases

## 7. Main findings with anchors

### Finding 1

- Source-reported content: RdDM is described as the major small RNA-mediated epigenetic pathway in plants, requiring plant-specific Pol IV and Pol V plus accessory proteins.
- Figure/table/section anchor if available: Abstract; Box 1; Canonical RdDM pathway mechanisms; Fig. 1; Table 1.
- Evidence type: review-level evidence.
- Limitation: source is a synthesis of prior studies, not a primary experiment.
- Confidence level: high as review consensus circa 2014.

### Finding 2

- Source-reported content: Canonical RdDM model involves Pol IV-derived transcripts, RDR2 copying to dsRNA, DCL3 processing into 24-nt siRNAs, HEN1 stabilization, AGO4 loading, Pol V scaffold transcripts, and DRM2-mediated de novo methylation in CG/CHG/CHH contexts.
- Figure/table/section anchor if available: Introductory canonical model; Canonical RdDM pathway mechanisms; Fig. 1; Table 1.
- Evidence type: review-level mechanistic synthesis.
- Limitation: article notes that some functions and in vivo templates of Pol IV/Pol V remain incompletely understood.
- Confidence level: high for pathway outline; moderate for unresolved mechanistic details.

### Finding 3

- Source-reported content: Pol IV-defective mutant analyses are summarized as showing that Pol IV is responsible for precursors of >90% of 24-nt siRNAs in canonical RdDM; SHH1 helps recruit Pol IV to a subset of targets by binding H3K9me and unmethylated H3K4.
- Figure/table/section anchor if available: "Pol IV-dependent siRNA biogenesis"; Table 1.
- Evidence type: review-level evidence from mutant and chromatin recruitment studies.
- Limitation: Pol IV recruitment is explicitly described as not fully understood.
- Confidence level: high for Pol IV role; moderate for complete recruitment model.

### Finding 4

- Source-reported content: Pol V transcripts are described as scaffold RNAs that interact with siRNAs and recruit silencing factors; Pol V is localized mostly at transposons and repeats associated with 24-nt siRNAs and cytosine methylation, but some Pol V sites lack these features.
- Figure/table/section anchor if available: "Pol V-mediated de novo methylation"; Fig. 1.
- Evidence type: review-level evidence including ChIP-seq summaries.
- Limitation: Pol V occupancy alone is noted as insufficient for RdDM at some sites.
- Confidence level: moderate-high.

### Finding 5

- Source-reported content: RdDM targets are often euchromatic, especially small or young intergenic transposons and genes containing transposons/repeats in promoters, introns or coding regions; pericentromeric heterochromatin relies more on DDM1/MET1/CMT2/CMT3 pathways.
- Figure/table/section anchor if available: "Pol V-mediated de novo methylation"; "Interplay with chromatin features".
- Evidence type: review-level genome-wide methylation/chromatin synthesis.
- Limitation: locus-specific exceptions likely exist.
- Confidence level: moderate-high.

### Finding 6

- Source-reported content: The article lists expanding biological roles of RdDM, including pathogen defence, stress responses, reproduction, interallelic communication and intercellular communication.
- Figure/table/section anchor if available: Abstract; biological roles sections; references and notes.
- Evidence type: review-level evidence.
- Limitation: each biological role comes from separate underlying studies with different evidence strengths; not all are equally established.
- Confidence level: moderate.

## 8. Author conclusions

作者认为 RdDM 是植物中主要的 small RNA-mediated epigenetic pathway，且其复杂度不断增加：除了 canonical Pol IV/Pol V-dependent pathway，还存在 recruitment factors、chromatin feedback、non-canonical variations 和多个生物学过程中的功能联系。作者同时强调，Pol IV/Pol V 的体内模板、辅助因子功能和靶向机制仍有许多未解问题。

## 9. Reasonable inference

- This review may suggest that plant small RNA biology cannot be separated from chromatin state, because siRNA biogenesis and DNA methylation targeting are coupled to histone marks, polymerase recruitment and repeat architecture.
- The emphasis on Pol IV/Pol V specialization is consistent with a plant-specific expansion of transcriptional machinery for epigenetic regulation.
- Because many examples are Arabidopsis-centered, extrapolation to all crops should be made cautiously.

## 10. Model synthesis

可以把本文的核心模型概括为“双转录系统 RdDM”：Pol IV 侧负责生成 24-nt siRNA 信息，Pol V 侧在目标位点提供 scaffold transcript 和染色质平台，两者通过 AGO4-bound siRNA 的序列互补连接，最终招募 DRM2 建立 de novo DNA methylation。染色质标记、DNA methylation、转座子状态和辅助蛋白共同决定 RdDM 的靶向和稳定性。

## 11. Limitations and missing controls

- 这是综述文章，所有事实性机制陈述属于 review-level evidence，不能等同于本文作者新做的实验结果。
- MinerU 对 Fig. 1 flowchart 的结构化抽取明显失真，需 manual PDF check。
- 文章发表于 2014，后续 RdDM 领域可能已有更新；本凝练只代表 provided text。
- 对许多通路成员的功能，作者本身也标注为 only partially understood 或 recruitment not fully understood。
- 不同 biological roles 的证据强弱不一，需要回读原始研究才能进入正式证据矩阵。

## 12. Reusable knowledge

- Concepts: RdDM; transcriptional gene silencing; de novo methylation; scaffold RNA; siRNA effector complex; chromatin feedback loop.
- Core components: Pol IV/NRPD1; Pol V/NRPE1; RDR2; DCL3; HEN1; AGO4/AGO6/AGO9; DRM2; SHH1; DRD1-DMS3-RDM1; KTF1; IDN2-IDP complex; SUVH2/9; CMT2/CMT3/MET1/DDM1.
- Methods: RdDM mutant screens; sRNA-seq; methylome profiling; ChIP-seq; protein interaction assays; chromatin-state analysis.
- Analytical frameworks: distinguish canonical RdDM, non-canonical RdDM, and siRNA-independent heterochromatic methylation pathways.
- Review utility: 可作为后续阅读 small RNA、DNA methylation、heterosis、transposon silencing 文献时的机制背景卡。

## 13. Open questions

- Pol IV 和 Pol V 的真实 in vivo templates 是什么？
- 不同 genomic targets 如何选择 Pol IV/Pol V-dependent RdDM、RDR6-dependent non-canonical RdDM 或 DDM1/CMT/MET1 体系？
- RdDM 在 pathogen defence、stress response 和 reproduction 中哪些作用是直接因果，哪些只是伴随性甲基化变化？
- 作物和非 Arabidopsis 植物中的 RdDM component 是否有同样功能和靶向偏好？
- RdDM 产生的甲基化变化在自然群体和杂交后代中如何遗传和选择？
