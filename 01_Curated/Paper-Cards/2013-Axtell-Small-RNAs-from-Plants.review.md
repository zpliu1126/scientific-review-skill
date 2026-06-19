---
type: curated-paper-card
source: mineru
curation_skill: scientific-review-skill
title: "Classification and Comparison of Small RNAs from Plants"
authors:
  - "Michael J. Axtell"
year: 2013
journal: "Annual Review of Plant Biology"
doi: "10.1146/annurev-arplant-050312-120043"
study_type: review
field: plant small RNA biology
topics:
  - plant small RNAs
  - microRNA
  - siRNA
  - heterochromatic siRNA
  - secondary siRNA
  - NAT-siRNA
source_basis: full.md + content_list.json
evidence_strength: review-level evidence
curation_status: sample_curated_needs_manual_pdf_check
mineru_dir: "mineru-parsed/Axtell_2013_Annual Review of Plant Biology"
created: 2026-06-07
updated: 2026-06-07
---

# Classification and Comparison of Small RNAs from Plants

## 1. Citation metadata

- Title: Classification and Comparison of Small RNAs from Plants
- Authors: Michael J. Axtell
- Year: 2013
- Journal: Annual Review of Plant Biology
- DOI: 10.1146/annurev-arplant-050312-120043
- Article type: review
- PMID: unknown
- Confirmed source: MinerU `full.md` and `meta.json`
- Parsing note: MinerU 文本存在少量编码问题；页码区间显示为 `64:5.1–?.23`，needs manual PDF check。当前目录未保留 `images/` 和 `tables/` 子目录，因此 figure/table anchor uncertain。

## 2. Source basis

本凝练基于以下文件：

- `mineru-parsed/Axtell_2013_Annual Review of Plant Biology/full.md`
- `mineru-parsed/Axtell_2013_Annual Review of Plant Biology/content_list.json`
- `mineru-parsed/Axtell_2013_Annual Review of Plant Biology/meta.json`
- figures/tables: `full.md` 中包含 Figure 1、Figure 3、Figure 4 等图注和图像引用，但当前样本目录没有可直接核对的 `images/` 或 `tables/` 子目录；图表锚点需人工 PDF 核对。

## 3. One-sentence takeaway

这篇综述提出了一个以生物发生来源为核心的植物内源小 RNA 分层分类框架，将植物小 RNA 首先区分为发夹来源的 hpRNA 与双链 RNA 来源的 siRNA，并进一步比较 miRNA、异染色质 siRNA、secondary siRNA 与 NAT-siRNA 的机制、保守性和未解问题。

## 4. Research question

本文真正想回答的科学问题是：如何基于前体来源、生物发生路径、核心因子、作用机制和保守性，对植物内源 DCL/AGO 小 RNA 进行可解释、可比较、可用于注释的分类。

## 5. Study design

- 研究对象: 植物内源 DCL/AGO 小 RNA。
- 材料/样本: not reported in provided text；本文为综述，不报告新的实验样本。
- 实验设计: not reported in provided text；本文未呈现新的实验设计。
- 数据类型: 文献综合、分类框架、机制比较、跨物种保守性讨论。
- 分析流程: 作者基于小 RNA 前体类型、生物发生因子、长度分布、AGO/DCL/RDR 依赖性、作用机制和保守性，提出分层分类体系。
- 证据边界: review-level evidence；不能把综述观点直接写成原始实验结果。

## 6. Key methods

- 文献综合: 整理植物内源小 RNA 的生物发生、功能和保守性研究。
- 分类框架构建: 以 hpRNA 与 siRNA 为一级分类，再细分 miRNA、非 miRNA hpRNA、异染色质 siRNA、secondary siRNA 和 NAT-siRNA。
- 机制比较: 比较 RDR、DCL、AGO 等核心因子在不同小 RNA 类群中的作用。
- 证据评估: 对分类是否稳健进行判断，并指出非 miRNA hpRNA 和 NAT-siRNA 的分类凝聚性较弱。
- 开放问题提炼: 从 miRNA 靶标互补性、Pol IV/Pol V、AGO slicing、NAT-siRNA 触发机制等方面提出 future issues。

## 7. Main findings with anchors

### Finding 1: 植物小 RNA 可按前体来源建立一级分类

- Source-reported content: 作者提出植物小 RNA 的一级分类可区分为单链自互补发夹前体产生的 hpRNA，以及双链 RNA 前体产生的 siRNA。
- Figure/table/section anchor if available: Abstract；`A HIERARCHICAL CLASSIFICATION SYSTEM FOR PLANT SMALL RNAs`；Figure 1。
- Evidence type: review-level evidence / classification framework。
- Limitation: Figure 1 的图像内容在 MinerU 中有识别噪声，figure/table anchor uncertain。
- Confidence level: high for author-reported classification proposal；moderate for downstream reuse without checking original PDF figure。

### Finding 2: miRNA、异染色质 siRNA 和 secondary siRNA 是较稳健的小 RNA 类别

- Source-reported content: 作者指出 miRNAs、heterochromatic siRNAs 和 secondary siRNAs 具有相对一致的 RDR/DCL/AGO 因子、生物发生机制、长度分布和已验证机制，因此分类较稳健。
- Figure/table/section anchor if available: `A HIERARCHICAL CLASSIFICATION SYSTEM FOR PLANT SMALL RNAs`；`SUMMARY POINTS`。
- Evidence type: review-level evidence。
- Limitation: 这是作者基于文献的综合判断，不是本文新增实验。
- Confidence level: medium-high as review synthesis。

### Finding 3: 非 miRNA hpRNA 与 NAT-siRNA 的分类凝聚性更弱

- Source-reported content: 作者指出 non-miRNA hpRNAs 与 NAT-siRNAs 的 RDR/DCL 需求、长度分布和保守性证据较不一致，可能不是生物学上高度凝聚的类别。
- Figure/table/section anchor if available: 分类体系讨论段；`NAT-sIRNAs`；`SUMMARY POINTS`。
- Evidence type: review-level evidence。
- Limitation: 该判断依赖当时已有文献；新文献可能改变分类边界。
- Confidence level: medium。

### Finding 4: secondary siRNAs 可参与基因家族级联式协同调控

- Source-reported content: 作者总结 secondary siRNAs 可由上游小 RNA 触发，并可通过 silencing cascades 协同下调大型相似 mRNA 家族，例如 NBS-LRR disease-resistance mRNAs。
- Figure/table/section anchor if available: `SECONDARY siRNAs`；`Phased and Trans-Acting siRNAs`；`Functions of Secondary siRNAs`；Figure 4；`SUMMARY POINTS`。
- Evidence type: review-level evidence summarizing primary studies。
- Limitation: 具体 NBS-LRR 调控证据来自被引原始文献，本文不能替代原始证据。
- Confidence level: medium as review-level claim；primary-evidence confidence requires reading cited papers。

### Finding 5: 植物小 RNA 研究仍存在多个机制和发现层面的开放问题

- Source-reported content: 作者在 Future Issues 中列出 miRNA/target 互补模式、non-miRNA hpRNA 功能、Pol IV/Pol V 启动子、AGO slicing、heterochromatic siRNA scaffold pairing、cis-NAT-siRNA 触发因素以及新类别发现等问题。
- Figure/table/section anchor if available: `FUTURE ISSUES`。
- Evidence type: author-stated open questions。
- Limitation: 开放问题不是结果证明，只能作为研究空白。
- Confidence level: high for representing author-stated future issues。

## 8. Author conclusions

作者明确表达的结论包括：

- 植物内源小 RNA 可按生物发生和功能特征进行分层分类。
- hpRNA 与 siRNA 的一级区分是该分类体系的重要基础。
- miRNA、异染色质 siRNA 和 secondary siRNA 是相对稳健的类别。
- 非 miRNA hpRNA 和 NAT-siRNA 的分类边界与生物学凝聚性仍需要更多证据。
- 未来需要关注未充分采样组织和细胞类型中可能存在的新小 RNA 类别。

## 9. Reasonable inference

- The review may suggest that 后续植物小 RNA 注释工作应优先记录前体类型、RDR/DCL/AGO 依赖性、长度分布和作用对象，而不是只凭小 RNA 长度命名类别。
- The discussion is consistent with 将 secondary siRNA 作为一个适合连接小 RNA 生物发生与基因家族调控的概念节点。
- The author’s cautions could indicate that NAT-siRNA 相关结论在证据矩阵中需要更严格地区分“来源于反义转录本重叠区的相关性证据”和“真正由 NAT 触发的小 RNA 生物发生证据”。

## 10. Model synthesis

模型综合: 本文可被抽象为一个“前体来源 -> 加工因子 -> AGO 装载 -> 靶标作用 -> 保守性/功能”的植物小 RNA 知识框架。该框架适合用作后续文献库的概念骨架：先区分 hpRNA 与 siRNA，再根据 miRNA、heterochromatic siRNA、secondary siRNA、NAT-siRNA 等类别组织证据，并对每个类别标注其证据强弱与开放问题。该综合是基于全文跨段落整合得到的概念性总结，不应写作作者原文结论。

## 11. Limitations and missing controls

- 本文是综述，不提供新的原始实验、样本量、统计检验或验证实验。
- 大量具体机制和功能证据来自被引文献，正式证据矩阵中应回读原始论文。
- MinerU 解析中存在编码错误，页码、部分图注和表格 needs manual PDF check。
- 当前标准化解析目录没有 `images/` 和 `tables/` 子目录，图文关系不清处标注为 figure/table anchor uncertain。
- Arabidopsis 相关证据被大量使用，但作者也提醒 Arabidopsis 具有小基因组、功能性转座元件少和低杂合度等非典型特征，外推到其他植物时需谨慎。

## 12. Reusable knowledge

- Concepts: plant small RNAs, hpRNA, miRNA, siRNA, heterochromatic siRNA, secondary siRNA, phased siRNA, trans-acting siRNA, NAT-siRNA。
- Methods: 小 RNA 分类框架；基于前体来源和核心因子的小 RNA 注释；phasing pattern 用于识别 phased secondary siRNA。
- Datasets: not reported in provided text；本文为综述，不报告新数据集。
- Experimental designs: not reported in provided text；本文总结他人实验。
- Analytical frameworks: 以 precursor type、DCL/RDR/AGO dependency、size distribution、target mechanism、conservation pattern 组织植物小 RNA 证据。

## 13. Open questions

- 植物中是否存在更多功能性 miRNA/target 互补模式？
- 非 miRNA hpRNA 的功能是什么？
- Pol IV 和 Pol V 启动子如何被识别和调控？
- AGO-catalyzed slicing 是否参与异染色质 siRNA 路径中的 target recognition？
- 异染色质 siRNA 与 scaffold transcript 的互补性要求是什么？
- 哪些额外触发因素允许部分 cis-NAT gene pairs 产生 cis-NAT-siRNAs？
- 是否还有更多植物内源小 RNA 类别等待发现？
