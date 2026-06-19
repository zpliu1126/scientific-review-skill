---
type: curated-paper-card
source: mineru
curation_skill: scientific-review-skill
title: Dynamic Roles for Small RNAs and DNA Methylation during Ovule and Fiber Development in Allotetraploid Cotton
authors: Qingxin Song; Xueying Guan; Z. Jeffrey Chen
year: 2015
journal: PLOS Genetics
doi: 10.1371/journal.pgen.1005724
study_type: primary research; multi-omics developmental epigenomics
field: cotton fiber development; plant epigenomics; small RNA biology
topics: [cotton, fiber development, ovule, CHH methylation, RdDM, CMT2, small RNA, homoeolog expression bias]
source_basis: full.md + content_list.json
evidence_strength: moderate-high; genome-wide multi-omics plus methylation inhibitor perturbation
curation_status: curated; needs manual PDF check
mineru_dir: mineru-parsed/Song_2015_PLOS Genetics
created: 2026-06-07
updated: 2026-06-07
---

# Dynamic Roles for Small RNAs and DNA Methylation during Ovule and Fiber Development in Allotetraploid Cotton

## 1. Citation metadata

- Title: Dynamic Roles for Small RNAs and DNA Methylation during Ovule and Fiber Development in Allotetraploid Cotton
- Authors: Qingxin Song; Xueying Guan; Z. Jeffrey Chen
- Year: 2015
- Journal: PLOS Genetics
- DOI: 10.1371/journal.pgen.1005724
- Article type: primary research

## 2. Source basis

本凝练基于 MinerU 解析目录 `mineru-parsed/Song_2015_PLOS Genetics`：

- `full.md`
- `content_list.json`
- `meta.json`
- `full.md` contains figure captions and several extracted chart/table blocks.
- Parser note: standardized output directory does not contain separate `images/` or `tables/` folders; figure/table anchor uncertain; needs manual PDF check.

## 3. One-sentence takeaway

本文在异源四倍体棉花中显示 ovule 和 fiber 具有不同 CHH methylation 模式：ovule 近基因 CHH 与 24-nt siRNA/RdDM 和基因激活相关，fiber 异染色质 CHH 与 TE 抑制、CMT2/H1 状态和纤维发育相关。

## 4. Research question

本文试图回答：DNA methylation、small RNAs 和 homoeolog expression bias 如何参与棉花 ovule epidermal cell 到 rapidly elongating fiber cell 的发育转变。

## 5. Study design

研究材料为 allotetraploid cotton `Gossypium hirsutum L. acc. TM-1`。作者对 leaves、0 DPA ovules、14 DPA fibers，以及 14 DPA ovules 进行 MethylC-seq；对 leaves、0 DPA ovules、14 DPA fibers 进行 small RNA-seq；并结合 RNA-seq 分析 gene/TE expression。功能扰动部分使用 in vitro cultured ovules，加入 DNA methyltransferase inhibitor 5-aza-2'-deoxycytidine (5-aza-dC) 观察 fiber initiation/elongation。

## 6. Key methods

- Whole-genome bisulfite sequencing / MethylC-seq: 测定 CG/CHG/CHH methylation。
- small RNA-seq: 分析 24-nt siRNA abundance and genomic distribution。
- RNA-seq: 测定 gene and TE expression。
- CHH DMR calling: 100-bp sliding windows, CHH cytosine coverage criteria, ANOVA and methylation-difference cutoffs。
- Bisulfite sequencing validation: 对部分 DMRs 进行 cloned-fragment validation。
- Homoeolog identification and expression-bias analysis: blastp + MCScanX。
- qRT-PCR: 验证 DNA methylation-related genes expression。
- In vitro ovule culture and 5-aza-dC treatment: 测试 DNA methylation inhibition 对 fiber cell number/length 的影响。

## 7. Main findings with anchors

### Finding 1

- Source-reported content: CG and CHG methylation levels were similar among fibers, ovules and leaves, but CHH methylation was much higher in fibers (~14%) than ovules (~8.1%) and leaves (~7.8%); 24-nt siRNAs were higher in fibers and ovules than leaves.
- Figure/table/section anchor if available: Results, "DNA methylation dynamics in cotton leaves, ovules, and fibers"; Fig. 1A-B; S1 Table.
- Evidence type: MethylC-seq and small RNA-seq.
- Limitation: 14 DPA ovule had one replicate in provided text.
- Confidence level: high for reported global methylation/sRNA patterns.

### Finding 2

- Source-reported content: OL CHH hypermethylation correlated with gene-rich/euchromatic regions and siRNA distribution, whereas FO CHH hypermethylation was enriched in TE- and repeat-rich heterochromatic regions.
- Figure/table/section anchor if available: Fig. 1C-G; S1D Fig.
- Evidence type: genome-wide methylome and sRNA distribution analysis.
- Limitation: correlation with genomic features does not by itself identify enzyme causality.
- Confidence level: high for distribution pattern; moderate for pathway assignment.

### Finding 3

- Source-reported content: Authors identified 39,668 OL CHH-hyper DMRs and 124,681 FO CHH-hyper DMRs; OL DMRs were overrepresented in intergenic regions, whereas FO DMRs were enriched in TEs. A subset of DMRs was validated by bisulfite sequencing.
- Figure/table/section anchor if available: Fig. 2; S2 Table; S3 Fig.
- Evidence type: DMR analysis plus targeted validation.
- Limitation: DMR validation subset size/details require manual PDF check.
- Confidence level: high.

### Finding 4

- Source-reported content: Up-regulated genes in ovules were enriched among genes overlapping OL CHH-hyper DMRs in upstream 1-kb sequences, and siRNA levels in promoter regions of ovule-preferred genes were higher in ovules than leaves.
- Figure/table/section anchor if available: "Effects of OL CHH-hyper DMRs on gene expression"; Fig. 3.
- Evidence type: methylome/RNA-seq/sRNA integration.
- Limitation: promoter CHH and expression are correlated; directionality remains unresolved.
- Confidence level: moderate-high.

### Finding 5

- Source-reported content: FO CHH-hyper DMRs were not significantly correlated with fiber gene expression changes, were enriched in TEs, and FO CHH hypermethylation correlated positively with TE density. More TEs were expressed in fibers than in ovules or leaves.
- Figure/table/section anchor if available: "Function of FO CHH hypermethylation"; Fig. 4C-E; S1D Fig.
- Evidence type: methylome/RNA-seq/TE annotation integration.
- Limitation: TE activation and methylation feedback order is interpretive.
- Confidence level: moderate-high for association; moderate for feedback model.

### Finding 6

- Source-reported content: GhCMT2, GhCMT3 and GhMET1 were upregulated in ovules and fibers; multiple RdDM genes were upregulated in ovules but not fibers; HISTONE H1 was repressed in fibers but not ovules. Authors suggest GhCMT2 upregulation plus H1 repression may induce heterochromatic CHH hypermethylation in fibers.
- Figure/table/section anchor if available: Fig. 4F.
- Evidence type: qRT-PCR expression of methylation pathway genes.
- Limitation: expression of pathway genes is indirect evidence, not enzyme-specific loss-of-function proof.
- Confidence level: moderate.

### Finding 7

- Source-reported content: 5-aza-dC treatment in cultured ovules suppressed fiber length and ovule size in initiation and elongation stages; authors state this suggests DNA methylation might be important for normal fiber and ovule development, while noting possible growth-inhibition side effects.
- Figure/table/section anchor if available: Fig. 4G-I; Methods, "Cotton ovule in vitro culture and 5-aza-dC treatment".
- Evidence type: chemical perturbation.
- Limitation: 5-aza-dC side effects cannot be ruled out; pathway specificity is low.
- Confidence level: moderate.

### Finding 8

- Source-reported content: In fibers, 539 A/D homoeolog pairs were differentially methylated at CHG and CHH sites in gene bodies; CHG/CHH gene-body methylation was significantly anti-correlated with homoeolog expression.
- Figure/table/section anchor if available: "Role of DNA methylation in the expression of homoeologous genes"; Fig. 5; S5 Table.
- Evidence type: homoeolog methylation-expression association.
- Limitation: does not establish direct causality for expression bias.
- Confidence level: moderate-high.

## 8. Author conclusions

作者明确提出：ovule 中 promoter/flanking CHH hypermethylation 与 siRNAs/RdDM 和 ovule-preferred gene activation 相关；fiber 中额外 heterochromatic CHH hypermethylation 可能通过 CMT2/DDM1/H1 相关机制抑制 TEs 和 nearby genes；DNA methylation 还影响 homoeolog expression bias 和 fiber development。作者将这些过程概括为调控 gene and TE expression 的 double-lock feedback mechanism。

## 9. Reasonable inference

- The contrast between OL and FO CHH DMRs may suggest that the same methylation context can serve different developmental roles depending on genomic location.
- The 5-aza-dC phenotype is consistent with DNA methylation being required for normal cotton fiber initiation/elongation, but it does not identify which methylation pathway is causal.
- The anti-correlation between CHG/CHH gene-body methylation and homoeolog expression could indicate an epigenetic layer contributing to subgenome expression bias.

## 10. Model synthesis

本文可被整合为“发育阶段分区 CHH methylation 模型”：在 ovule 阶段，近基因短 TE/启动子区域的 24-nt siRNA 和 CHH methylation 与活跃基因表达相伴；进入 fiber elongation 后，异染色质/TE 区域出现额外 CHH methylation，可能作为 TE 活化后的反馈沉默机制，同时影响附近基因和部分 homoeolog expression bias。

## 11. Limitations and missing controls

- 5-aza-dC 是广谱 DNA methylation inhibitor，作者也说明不能排除 growth inhibition side effects。
- GhCMT2/H1 机制主要由表达模式和已知通路推断，缺少 cotton CMT2/H1 loss-of-function 或 rescue 证据。
- DMR 与 gene/TE expression 多为相关性，不能全部解释为直接因果。
- Figure/table anchor uncertain；MinerU 输出没有独立 `images/`/`tables/` 目录。
- 14 DPA ovule replicate 信息在 provided text 中显示为 one replicate，需要 manual PDF check。

## 12. Reusable knowledge

- Concepts: CHH methylation; RdDM-dependent promoter methylation; CMT2/DDM1-related heterochromatic methylation; CHH methylation island; homoeolog expression bias; TE feedback silencing.
- Methods: MethylC-seq; sRNA-seq; RNA-seq; CHH DMR calling; bisulfite validation; qRT-PCR of methylation pathway genes; in vitro cotton ovule culture; 5-aza-dC perturbation.
- Datasets: GEO accession GSE61774.
- Experimental designs: compare leaf -> ovule and ovule -> fiber transitions separately to distinguish organogenesis and cell elongation effects.
- Analytical frameworks: integrate methylation context, genomic compartment, siRNA density, TE proximity and gene expression.

## 13. Open questions

- GhCMT2、GhDDM1 或 HISTONE H1 的遗传扰动是否能直接重现或解除 fiber CHH hypermethylation？
- ovule promoter CHH methylation 是由 gene expression 引发，还是促进 gene activation？
- fiber 中 TE transcription 和 CHH hypermethylation 的时间先后关系是什么？
- 哪些具体 fiber-related genes 受邻近 DMRs 直接调控？
- homoeolog gene-body CHG/CHH methylation 是否可被选择并稳定影响 cotton fiber traits？
