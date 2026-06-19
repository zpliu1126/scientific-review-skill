---
type: curated-paper-card
source: mineru
curation_skill: scientific-review-skill
title: Plant Small RNAs: Their Biogenesis, Regulatory Roles, and Functions
authors: Junpeng Zhan; Blake C. Meyers
year: 2023
journal: Annual Review of Plant Biology
doi: 10.1146/annurev-arplant-070122-035226
study_type: review
field: plant small RNA biology
topics: [plant small RNAs, miRNA, siRNA, phasiRNA, RdDM, AGO, sRNA mobility]
source_basis: full.md + content_list.json
evidence_strength: review-level evidence
curation_status: curated; needs manual PDF check; figure/table anchor uncertain
mineru_dir: mineru-parsed/Zhan_2023_Annual Review of Plant Biology
created: 2026-06-07
updated: 2026-06-07
---

# Plant Small RNAs: Their Biogenesis, Regulatory Roles, and Functions

## 1. Citation metadata
- Title: Plant Small RNAs: Their Biogenesis, Regulatory Roles, and Functions
- Authors: Junpeng Zhan; Blake C. Meyers
- Year: 2023
- Journal: Annual Review of Plant Biology
- DOI: 10.1146/annurev-arplant-070122-035226
- Study type: review

## 2. Source basis
本凝练基于 MinerU 解析目录 `mineru-parsed/Zhan_2023_Annual Review of Plant Biology`：
- `full.md`
- `content_list.json`
- figures/tables if available

> [!warning]
> MinerU 对 Figure 1 的流程图结构解析含有明显噪声，图文关系应标注为 `figure/table anchor uncertain`，后续需要人工核对 PDF。

## 3. One-sentence takeaway
这篇综述系统整理了植物小 RNA 的主要类别、生物发生、AGO 装载、调控方式、移动性与农业应用潜力，并强调 miRNA、异染色质 siRNA 和次级 siRNA 构成植物小 RNA 调控网络的核心框架。

## 4. Research question
本文想回答的科学问题是：植物小 RNA 如何生成、如何被分选到效应复合体、如何调控靶标，以及这些调控机制如何参与植物发育、基因组稳定性、环境响应和潜在作物改良。

## 5. Study design
本文为综述文章，不是原始实验研究。

- Research object: plant small RNAs
- Materials/samples: not reported in provided text as a new experimental sample set
- Data type: review synthesis of prior plant small RNA literature
- Analysis workflow: 分类整理 miRNA、heterochromatic siRNA、secondary siRNA/phasiRNA 及其他小 RNA 类别；总结生物发生、AGO 装载、作用模式、移动性和应用
- Statistical analysis: not reported in provided text

## 6. Key methods
本文未报告新的实验方法；核心为文献综述。文中整理的方法和机制包括：
- miRNA biogenesis framework
- heterochromatic siRNA/RNA-directed DNA methylation framework
- secondary siRNA/phasiRNA biogenesis framework
- AGO sorting/loading framework
- small RNA mobility and delivery framework

## 7. Main findings with anchors

### Finding 1
- Source-reported content: 文章将植物小 RNA 的主要类别概括为 microRNAs、heterochromatic siRNAs 和 secondary siRNAs，同时指出一些其他类别仍较少被理解或存在争议。
- Figure/table/section anchor if available: Abstract; Introduction
- Evidence type: review-level evidence
- Limitation: 这是综述性分类，不是本文产生的原始实验结果。
- Confidence level: high

### Finding 2
- Source-reported content: miRNA 通常由 Pol II 转录的 MIR 基因产生，DCL1、HYL1、SE 等参与前体加工，HEN1 甲基化保护成熟 miRNA，AGO1 装载后可介导靶标切割、翻译抑制或触发 phasiRNA 产生。
- Figure/table/section anchor if available: Section 2.1; Figure 1 caption
- Evidence type: review-level evidence
- Limitation: Figure 1 的 MinerU 图形解析有噪声，需人工核对图中连接关系。
- Confidence level: high

### Finding 3
- Source-reported content: heterochromatic siRNA 主要与 Pol IV、CLSY、RDR2、DCL3、AGO4/AGO6、Pol V 和 DRM2 相关，并通过 RdDM 参与 DNA 甲基化和转座子/异染色质调控。
- Figure/table/section anchor if available: Section 2.2; Figure 1 caption
- Evidence type: review-level evidence
- Limitation: 该表述来自综述整合，不能作为本文原始实验验证。
- Confidence level: high

### Finding 4
- Source-reported content: secondary siRNA/phasiRNA 可由 miRNA 或 siRNA 触发靶 RNA 切割后生成，RDR6 和 DCL4/DCL5 等参与产生 phased siRNA；草本植物生殖组织中的 21-nt 和 24-nt phasiRNA 被作为重要类别讨论。
- Figure/table/section anchor if available: Section 2.3; Figure 1 caption
- Evidence type: review-level evidence
- Limitation: 不同物种和生殖阶段的功能证据强度需回到原始研究核查。
- Confidence level: medium-high

### Finding 5
- Source-reported content: 文章单独讨论 small RNA sorting/loading onto Argonaute proteins，并把 AGO 装载视为小 RNA 靶向调控活性的关键步骤。
- Figure/table/section anchor if available: Section 3.1
- Evidence type: review-level evidence
- Limitation: Provided text 中没有给出所有 AGO 成员的完整实验比较。
- Confidence level: medium

## 8. Author conclusions
作者明确综述了植物小 RNA 的生物发生机制、靶标调控方式、移动性以及在模式植物和作物中的功能，并在结论与展望中将这些机制与未来研究和应用潜力联系起来。

## 9. Reasonable inference
The review may suggest that plant small RNA biology is best interpreted as a network of pathway-specific biogenesis modules coupled to AGO-dependent effector mechanisms. It is consistent with the idea that agricultural applications require both pathway knowledge and delivery/target-specificity validation.

## 10. Model synthesis
本文可被整理为一个三层框架：第一层是 DCL/RDR/Pol 等生物发生模块，第二层是 AGO 装载和靶标识别模块，第三层是发育、表观遗传、胁迫响应和跨细胞/跨个体移动等功能输出。这个总结属于 model synthesis，不应冒充作者原文结论。

## 11. Limitations and missing controls
- 本文为综述，claim 属于 review-level evidence。
- 不提供新的实验样本、统计检验或原始数据。
- MinerU 对 Figure 1 的结构化解析不完整，标注 `figure/table anchor uncertain`。
- 部分功能性结论来自被综述的一手文献，需要人工回溯原始论文。
- needs manual PDF check。

## 12. Reusable knowledge
- Concepts: miRNA, heterochromatic siRNA, secondary siRNA, phasiRNA, RdDM, AGO loading, sRNA mobility
- Methods: literature synthesis of sRNA biogenesis and effector pathways
- Datasets: not reported in provided text
- Experimental designs: not applicable as a new experimental study
- Analytical frameworks: classify sRNAs by biogenesis route, effector AGO, target class and regulatory output

## 13. Open questions
- 不同植物谱系中 hc-siRNA、phasiRNA 和其他小 RNA 类别的保守性如何？
- sRNA 移动性在发育和胁迫适应中有多大范围的功能意义？
- 如何区分小 RNA 途径中的直接靶标调控与下游网络效应？
- 外源或人工小 RNA 应用如何提升递送效率、特异性和田间稳定性？
