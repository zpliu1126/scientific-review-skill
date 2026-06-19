# Methods extracted from Paper

Source paper: `2013-Axtell-Small-RNAs-from-Plants`

> 注意：本文是综述，以下为文中使用或提炼出的“综述/分类/分析框架方法”，不是作者在本文中新做的实验方法。

## Method list

### Method 1: Literature-based hierarchical classification

- Method name: 文献驱动的植物小 RNA 分层分类
- Purpose: 按生物发生和功能差异组织植物内源小 RNA 类别。
- Input material/data: 已发表的植物小 RNA 研究文献；MinerU 文本中未报告新的原始数据集。
- Output: hpRNA/siRNA 一级分类，以及 miRNA、non-miRNA hpRNA、heterochromatic siRNA、secondary siRNA、NAT-siRNA 等二级/三级类别。
- Key parameters: precursor type, biogenesis pathway, RDR/DCL/AGO dependency, small RNA size distribution, target mechanism, conservation pattern。
- Strengths: 便于跨类别比较；可用于知识库概念组织和文献注释。
- Limitations: 分类体系是 intellectual construct；类别边界可能随新证据改变。
- Used in which result: Finding 1, Finding 2, Finding 3。

### Method 2: Precursor-type annotation

- Method name: 基于前体来源的小 RNA 注释
- Purpose: 区分发夹来源 hpRNA 与双链 RNA 来源 siRNA。
- Input material/data: 小 RNA 前体结构或生物发生证据。
- Output: hpRNA 或 siRNA 一级标签。
- Key parameters: single-stranded self-complementary hairpin precursor; intermolecular or RDR-derived dsRNA precursor。
- Strengths: 逻辑清晰，是本文分类体系的核心。
- Limitations: 对前体来源不清的小 RNA，需要更多实验或计算证据；MinerU 中 Figure 1 锚点需人工核对。
- Used in which result: Finding 1。

### Method 3: Core-factor comparison

- Method name: RDR/DCL/AGO 依赖性比较
- Purpose: 判断小 RNA 类别是否具有稳定的生物发生和作用机制。
- Input material/data: 文献报道的 RDR、DCL、AGO 依赖性。
- Output: 类别稳健性判断，例如 miRNA、heterochromatic siRNA、secondary siRNA 较稳健。
- Key parameters: required RDR clade, DCL clade, AGO clade, size distribution。
- Strengths: 能把分类与可验证机制连接起来。
- Limitations: 本文不提供新实验；特定因子的证据需回读原始文献。
- Used in which result: Finding 2, Finding 3。

### Method 4: Phasing-pattern recognition for secondary siRNAs

- Method name: phased small-RNA pattern identification
- Purpose: 识别 phased secondary siRNA 的候选位点。
- Input material/data: 小 RNA 积累模式或小 RNA sequencing 数据；本文未报告新数据。
- Output: secondary siRNA 候选，尤其是 phased secondary siRNA。
- Key parameters: DCL 从一致 dsRNA terminus 连续加工形成的相位性；upstream small-RNA-directed cleavage。
- Strengths: 作者称 computational identification of phased patterns is powerful。
- Limitations: phasing 不是 secondary siRNA 的必要条件；不应把“未见 phasing”直接等同于“不是 secondary siRNA”。
- Used in which result: Finding 4。

### Method 5: Open-question synthesis

- Method name: 研究空白提炼
- Purpose: 从综述内容中提炼 future issues。
- Input material/data: 作者 Future Issues 与 Concluding remarks。
- Output: 待研究问题清单。
- Key parameters: unresolved mechanism, insufficient sampling, unclear complementarity requirements, pathway-specific uncertainty。
- Strengths: 适合指导下一轮文献检索和知识库主题地图。
- Limitations: 开放问题不是 source-reported experimental finding。
- Used in which result: Finding 5。
