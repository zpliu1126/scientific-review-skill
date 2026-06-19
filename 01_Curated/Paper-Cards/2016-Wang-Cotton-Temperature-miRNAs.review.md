---
type: curated-paper-card
source: mineru
curation_skill: scientific-review-skill
title: Small RNA-mediated responses to low- and high-temperature stresses in cotton
authors: Qiongshan Wang; Nian Liu; Xiyan Yang; Lili Tu; Xianlong Zhang
year: 2016
journal: Scientific Reports
doi: 10.1038/srep35558
study_type: primary research; stress small RNA profiling
field: cotton stress biology; miRNA regulation
topics: [cotton, temperature stress, miRNA, degradome, small RNA, stress response]
source_basis: full.md + content_list.json
evidence_strength: moderate; profiling plus degradome target evidence
curation_status: curated; needs manual PDF check
mineru_dir: mineru-parsed/Wang_2016_Scientific Reports
created: 2026-06-07
updated: 2026-06-07
---

# Small RNA-mediated responses to low- and high-temperature stresses in cotton

## 1. Citation metadata

- Title: Small RNA-mediated responses to low- and high-temperature stresses in cotton
- Authors: Qiongshan Wang; Nian Liu; Xiyan Yang; Lili Tu; Xianlong Zhang
- Year: 2016
- Journal: Scientific Reports
- DOI: 10.1038/srep35558
- Article type: primary research

## 2. Source basis

Based on `mineru-parsed/Wang_2016_Scientific Reports/full.md`, `content_list.json`, and `meta.json`. figure/table anchor uncertain; needs manual PDF check.

## 3. One-sentence takeaway

本文在 cotton seedlings 的低温和高温处理中构建 small RNA/degradome 图谱，识别温度胁迫响应 miRNAs 及其可能靶基因网络。

## 4. Research question

本文要回答：Gossypium hirsutum 在 4/12/35/42 deg C 温度胁迫下有哪些 known/novel miRNAs 发生表达变化，以及这些 miRNAs 的 degradome-supported targets 涉及哪些 stress-response pathways。

## 5. Study design

二叶期 `G. hirsutum cv. YZ1` seedlings 分别处理 4 deg C、12 deg C、25 deg C、35 deg C、42 deg C for 8 h。作者测定 H2O2、proline、MDA、soluble sugar 等生理指标；构建五个 sRNA libraries 和五个 degradome libraries，并进行 miRNA identification、differential expression、target prediction/validation、GO/KEGG enrichment 和 qRT-PCR。

## 6. Key methods

- Temperature stress treatment of cotton seedlings.
- Physiological assays for H2O2, proline, MDA and soluble sugar.
- small RNA library construction and Illumina sequencing.
- Known miRNA identification against miRBase 21.0.
- Novel miRNA prediction by hairpin precursor structure using Mireap.
- Differential expression with log2 ratio thresholds.
- Degradome sequencing and PAREsnip target analysis.
- qRT-PCR validation of selected miRNAs/targets.
- GO and KEGG enrichment.

## 7. Main findings with anchors

### Finding 1

- Source-reported content: 4 deg C, 12 deg C and 42 deg C seedlings showed strong wilting, while 25 deg C and 35 deg C seedlings did not; stress treatments increased several physiological parameters, especially at 4 deg C.
- Figure/table/section anchor if available: Fig. 1; Results "Performance of seedlings under temperature stress conditions".
- Evidence type: physiological stress phenotype.
- Limitation: 8 h treatment only.
- Confidence level: high.

### Finding 2

- Source-reported content: Five sRNA libraries generated about 11.8 million clean reads each; 24-nt reads were most abundant (41.6-46.6%), followed by 21-nt reads.
- Figure/table/section anchor if available: Table 1; Fig. 2; "High-throughput sequencing of small RNAs in cotton".
- Evidence type: sRNA-seq profiling.
- Limitation: leaf seedling tissue only.
- Confidence level: high.

### Finding 3

- Source-reported content: 319 known miRNAs from 144 families and 800 novel miRNAs were identified.
- Figure/table/section anchor if available: known/novel miRNA sections; Table S1-S3.
- Evidence type: computational miRNA identification.
- Limitation: novel miRNAs have lower expression and require further validation.
- Confidence level: moderate-high for known miRNAs; moderate for novel miRNAs.

### Finding 4

- Source-reported content: 168 miRNAs were differentially expressed among treatments; 63 known and 105 novel miRNAs passed expression thresholds; more miRNAs were differentially expressed in high-temperature stress, and most known/novel miRNAs were downregulated under high temperature.
- Figure/table/section anchor if available: Fig. 4; Fig. S4-S6; Table S4.
- Evidence type: differential expression analysis.
- Limitation: log2 ratio threshold without full statistical model in provided text.
- Confidence level: moderate.

### Finding 5

- Source-reported content: Degradome sequencing was used to analyze miRNA targets; GO/KEGG analyses linked many targets to hormone stimulus, oxidation-reduction, photosynthesis, plant-pathogen interaction and plant hormone signal transduction.
- Figure/table/section anchor if available: Abstract; Methods degradome and enrichment sections.
- Evidence type: degradome-supported target and enrichment analysis.
- Limitation: target functions are pathway-level associations, not direct stress-tolerance validation.
- Confidence level: moderate.

## 8. Author conclusions

作者认为 cotton low/high temperature stresses trigger miRNA expression changes, and the identified miRNA-target network provides insight into molecular mechanisms of cotton temperature-stress responses.

## 9. Reasonable inference

- Temperature-responsive miRNAs may coordinate hormone, redox and photosynthesis-related responses.
- High-temperature stress appears to cause stronger miRNA expression reprogramming than mild/normal high temperature in this dataset.

## 10. Model synthesis

该研究是 cotton temperature stress miRNA atlas：先确认温度处理造成生理胁迫，再用 sRNA-seq 识别 known/novel miRNAs，并用 degradome 给出靶基因切割证据，最后通过富集分析把 miRNA changes 连接到 stress-response pathways。

## 11. Limitations and missing controls

- 未见 miRNA overexpression/knockdown 功能验证。
- novel miRNAs 和 targets 需要独立实验验证。
- 仅 8 h seedling leaf treatments，不能直接外推到 fiber yield。
- figure/table anchor uncertain; needs manual PDF check.

## 12. Reusable knowledge

- Concepts: temperature-responsive miRNA; degradome-supported target; cotton stress physiology.
- Methods: sRNA-seq; degradome/PARE analysis; qRT-PCR; GO/KEGG enrichment.
- Experimental designs: compare extreme/normal low/high temperatures with 25 deg C control.

## 13. Open questions

- 哪些 temperature-responsive miRNAs 具有直接提升 cold/heat tolerance 的功能？
- degradome-supported targets 中哪些是关键调控节点？
- seedling leaf miRNA response 是否与 cotton fiber quality/yield under temperature stress 相关？
