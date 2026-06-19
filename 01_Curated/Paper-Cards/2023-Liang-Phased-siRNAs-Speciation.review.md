---
type: curated-paper-card
source: mineru
curation_skill: scientific-review-skill
title: Taxon-specific, phased siRNAs underlie a speciation locus in monkeyflowers
authors: Mei Liang; Wenjie Chen; Amy M. LaFountain; Yuanlong Liu; Foen Peng; Rui Xia; H. D. Bradshaw; Yao-Wu Yuan
year: 2023
journal: Science
doi: 10.1126/science.adf1323
study_type: primary research; functional genetics; evolutionary genomics
field: plant evolutionary genetics; small RNA biology; floral pigmentation
topics: [phased siRNA, speciation, Mimulus, YUP, RCP2, carotenoid pigmentation, pollination syndrome]
source_basis: full.md + content_list.json
evidence_strength: high for YUP-RCP2 functional mechanism; moderate-high for evolutionary/speciation interpretation
curation_status: curated; needs manual PDF check
mineru_dir: mineru-parsed/Liang_2023_Science
created: 2026-06-07
updated: 2026-06-07
---

# Taxon-specific, phased siRNAs underlie a speciation locus in monkeyflowers

## 1. Citation metadata

- Title: Taxon-specific, phased siRNAs underlie a speciation locus in monkeyflowers
- Authors: Mei Liang; Wenjie Chen; Amy M. LaFountain; Yuanlong Liu; Foen Peng; Rui Xia; H. D. Bradshaw; Yao-Wu Yuan
- Year: 2023
- Journal: Science
- DOI: 10.1126/science.adf1323
- Article type: primary research

## 2. Source basis

本凝练基于 MinerU 解析目录 `mineru-parsed/Liang_2023_Science`：

- `full.md`
- `content_list.json`
- `meta.json`
- `full.md` includes figure captions, image links, supplementary-material notes, and some table-like extractions.
- Parser note: standardized output directory does not contain separate `images/` or `tables/` folders; figure/table anchor uncertain; needs manual PDF check.

## 3. One-sentence takeaway

本文证明 Mimulus 的物种分化位点 YUP 是一个产生 phased siRNA 的非编码基因，其中 siR-RCP2 靶向并抑制 RCP2，从而改变花瓣类胡萝卜素沉积并影响传粉者介导的物种分化。

## 4. Research question

本文试图回答：Mimulus 中控制花色、传粉者偏好和生殖隔离的 YUP 位点究竟是什么分子实体，以及 taxon-specific small RNA locus 是否能作为功能性演化创新参与表型分化和物种形成。

## 5. Study design

研究系统为 Mimulus lewisii complex，包括 bumble bee-pollinated `M. lewisii`、self-pollinated `M. parishii`、hummingbird-pollinated `M. cardinalis` 及多个 near-isogenic lines (NILs) 和转基因材料。作者通过 `M. parishii` 与 `M. cardinalis` 遗传背景进行精细定位，将 YUP 缩小到 70-kb interval；随后用 RNA-seq/sRNA-seq、qRT-PCR、转基因过表达、人工 siRNA、5' RLM RACE、RCP2-YFP reporter、siR-RCP2-resistant RCP2、遗传杂交和 synteny/evolutionary analysis 解析分子机制和演化来源。

## 6. Key methods

- Fine-scale genetic mapping and NIL construction: 定位 YUP 到 70-kb candidate interval。
- RNA interference screen: 测试 candidate interval 中蛋白编码基因是否影响 carotenoid pigmentation。
- RNA-seq and transcript inspection: 识别约 1.3-kb noncoding transcript。
- Small RNA sequencing and phasing analysis: 发现 inverted repeat 区域产生 phased 21-nt siRNAs。
- qRT-PCR: 检测 YUP_siR1/siR-RCP2 在发育阶段和组织中的积累。
- Transgenic overexpression: 35S:YUP alleles、35S:amiR-RCP2、35S:RCP2-YFP、35S:mRCP2-YFP。
- 5' RLM RACE: 验证 RCP2 transcript 的 siR-RCP2 预测切割位点。
- Confocal microscopy/YFP reporter: 评估 RCP2 translational repression。
- Mutant/NIL crosses: 验证 RCP1-YUP-RCP2 调控顺序。
- Synteny and genome sequencing: 推断 YUP-SOLAR-PELAN superlocus 的起源和演化时间。

## 7. Main findings with anchors

### Finding 1

- Source-reported content: 通过约 3000 个 BC3S1/BC3S2 个体的 genotyping，作者将 YUP 定位到 70-kb interval，并获得带有 petal lobe carotenoid accumulation 的 refined NIL。
- Figure/table/section anchor if available: Results, "YUP is a noncoding locus that produces siRNAs"; Fig. 1I; fig. S2.
- Evidence type: genetic mapping and NIL phenotype.
- Limitation: exact genotyping markers and supplementary details require manual PDF check.
- Confidence level: high.

### Finding 2

- Source-reported content: 70-kb interval 中 8 个 protein-coding genes 的 RNAi 在 M. lewisii 中未产生 carotenoid pigmentation phenotype；RNA-seq reads 显示该区域有约 1.3-kb transcript，无 conserved ORF，但含可形成约 250 bp arm 的 inverted repeat。
- Figure/table/section anchor if available: Fig. 1I; fig. S3; fig. S4; fig. S5.
- Evidence type: candidate gene test; transcript evidence.
- Limitation: RNAi knockdown efficiency details are in supplementary materials and need manual check.
- Confidence level: high for reported screen result; moderate-high for excluding every protein-coding candidate.

### Finding 3

- Source-reported content: sRNA sequencing showed the inverted repeat region in M. lewisii and M. parishii produced abundant 21-nt siRNAs in a phased pattern; M. cardinalis allele produced a different siRNA profile. YUP_siR1 was higher in M. parishii than M. cardinalis and enriched in corolla/petal lobes.
- Figure/table/section anchor if available: Fig. 2A-C; fig. S5.
- Evidence type: sRNA-seq plus qRT-PCR.
- Limitation: phasing and abundance metrics should be checked against full supplementary methods.
- Confidence level: high.

### Finding 4

- Source-reported content: Overexpression of M. lewisii and M. parishii YUP transcripts in orange-flowered Mpar DPKC/C NIL caused dark pink flowers without carotenoid accumulation in all 30 and 35 independent lines, respectively; M. cardinalis allele caused no phenotypic change among 41 lines.
- Figure/table/section anchor if available: Fig. 2D-G; figs. S7/S8.
- Evidence type: transgenic functional validation.
- Limitation: 35S overexpression may not fully reproduce endogenous regulation, but allele contrast is strong.
- Confidence level: high.

### Finding 5

- Source-reported content: YUP_siR1/siR-RCP2 was predicted to target RCP2, and 5' RLM RACE confirmed cleavage at the predicted target site. Artificial siR-RCP2 overexpression suppressed carotenoid accumulation in 6 of 21 lines.
- Figure/table/section anchor if available: Fig. 3A-D; fig. S9; fig. S8D.
- Evidence type: target prediction, RLM RACE, artificial small RNA overexpression.
- Limitation: not all amiR-RCP2 lines showed phenotype; expression-level differences may matter.
- Confidence level: high for target relationship; high for sufficient suppression in expressing lines.

### Finding 6

- Source-reported content: RCP2-YFP showed weak protein signal in petal lobes despite only moderate transcript differences, whereas siR-RCP2-resistant mRCP2-YFP showed comparable expression in petal lobes and filaments and increased carotenoid accumulation in both organs.
- Figure/table/section anchor if available: Fig. 3E-H; fig. S10.
- Evidence type: reporter assay and target-site mutagenesis.
- Limitation: reporter constructs are transgenic assays; endogenous protein quantification is not fully visible in provided text.
- Confidence level: high for translational-inhibition model.

### Finding 7

- Source-reported content: RCP1 expression is complementary to YUP/siR-RCP2; rcp1 mutant increased siR-RCP2, RCP1 overexpression decreased it; rcp1 yupC/C and rcp2 yupC/C crosses support RCP1 upstream of YUP and YUP upstream of RCP2.
- Figure/table/section anchor if available: Fig. 4.
- Evidence type: qRT-PCR, mutant/overexpression, genetic interaction.
- Limitation: direct binding of RCP1 to YUP regulatory DNA is not reported in provided text.
- Confidence level: moderate-high.

### Finding 8

- Source-reported content: Synteny analysis indicates YUP-SOLAR-PELAN superlocus originated in the common ancestor of sections Erythranthe and Monimanthe about 5 million years ago; overexpressing YUPL in additional Mimulus species reduced flower carotenoid accumulation.
- Figure/table/section anchor if available: Fig. 5.
- Evidence type: comparative genomics and cross-species transgenic assay.
- Limitation: pollinator-mediated selection maintaining the superlocus is partly interpretive.
- Confidence level: moderate-high for origin timing; moderate for selection interpretation.

## 8. Author conclusions

作者明确结论是：YUP 是一个 taxon-restricted noncoding gene，可产生 phased siRNAs；其中 siR-RCP2 通过 transcript cleavage 和 translational inhibition 抑制 RCP2；YUP-SOLAR-PELAN superlocus 自约 5 million years ago 起源后，参与后代 Mimulus 物种的花色多样化、传粉模式适应和物种形成。

## 9. Reasonable inference

- The YUP case may suggest that taxon-restricted regulatory small RNA loci can be major-effect loci in adaptive floral traits.
- The presence of YUP, SOLAR, and PELAN in a linked superlocus is consistent with coordinated selection on flower-color traits, but direct historical selection is not experimentally demonstrated.
- The disrupted phased pattern in M. cardinalis could indicate that loss or alteration of specific phased siRNA output contributed to red-flower evolution.

## 10. Model synthesis

本文把 small RNA 从“调控层背景因素”提升为“物种分化位点本体”：YUP 不是编码色素酶或转录因子的经典基因，而是由基因片段倒置重复形成的非编码 phased siRNA 产生位点。它通过 siR-RCP2 抑制 RCP2，从而控制类胡萝卜素在花瓣中的空间沉积；RCP1 又在 nectar guide 区域压制 YUP，使局部黄色信号保留。这个 RCP1-YUP-RCP2 轴把发育调控、small RNA 靶向和传粉者选择连接成一个可验证的演化机制。

## 11. Limitations and missing controls

- Supplementary Materials and Methods are referenced but not fully present in MinerU `full.md`; needs manual PDF check.
- Figure/table anchor uncertain because separate MinerU `images/`/`tables/` directories are absent.
- Pollinator-mediated speciation background partly依赖 prior studies cited in the paper；本凝练没有把被引文献当作已独立验证证据。
- YUP overexpression in distant Mimulus species说明系统对 YUP action 有 predisposition，但不能单独证明祖先状态下自然表达模式。
- RCP1 对 YUP 的调控在 provided text 中由表达互补、突变体和过表达支持；直接 DNA binding 或顺式元件证据未见报告。

## 12. Reusable knowledge

- Concepts: taxon-restricted regulatory sRNA; phased siRNA; noncoding speciation locus; floral carotenoid patterning; pollinator-mediated reproductive isolation; superlocus.
- Methods: NIL fine mapping; sRNA-seq phasing analysis; 5' RLM RACE; artificial siRNA overexpression; siRNA-resistant target design; YFP translational reporter; synteny analysis.
- Datasets: sRNA sequencing and whole-genome sequencing deposited under BioProject PRJNA882815 and PRJNA882787, according to provided text.
- Experimental designs: allele-specific transgenic rescue/overexpression; target-site mutation to separate transcript abundance from translation repression.
- Analytical frameworks: infer evolutionary origin of a regulatory locus by combining synteny, phylogeny, functional transgenics, and phenotype history.

## 13. Open questions

- YUP 的 phased siRNA biogenesis 是否确由 DCL4 或其他 Dicer-like protein 介导？
- RCP1 是否直接结合 YUP regulatory region，还是通过间接调控降低 YUP/siR-RCP2？
- YUP-SOLAR-PELAN superlocus 的形成过程涉及哪些结构变异机制？
- 在自然群体中，YUP phased pattern 的变异是否与传粉者偏好和适合度直接关联？
- 其他植物类群中是否也存在类似“非编码 small RNA speciation locus”？
