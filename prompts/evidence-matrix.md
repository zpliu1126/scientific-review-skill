# Evidence Matrix Prompt

```text
Compare the provided life science papers using scientific-review-skill. Apply the general review evidence rules. For plant, crop, population genomics, evolutionary genomics, comparative genomics, transcriptomics, animal, human, or biomedical papers, apply the relevant domain-specific reference.

Output mode:
Evidence matrix requests are 证据审计模式 by default. Use explicit columns and labels such as Source-reported content, Reasonable inference, and Model synthesis. If the user asks for a non-tabular Chinese summary instead, use 中文速读模式 and keep the labels only in a concise evidence-boundary section.

Save-output mode:
If the user asks to "save to file", "保存到文件", "写入 notes", "生成文献卡片文件", or equivalent, save the full matrix and synthesis as a Markdown file. Use literature-notes/ as the recommended default directory. If the output is not a single-paper note, use a concise descriptive Markdown filename and use unknown for missing metadata rather than inventing it. After saving, respond in chat only with the saved path, a brief summary, and Evidence Check status.

Create an evidence matrix with columns:
- Citation
- Source basis
- Study type
- Biological system
- Intervention/exposure/condition
- Data type
- Analysis method
- Key methods
- Main findings
- Source-reported content
- Reasonable inference
- Model synthesis
- Validation evidence
- Causality level
- Strengths
- Limitations
- Relevance to the review question
- Confidence level

After the matrix, summarize:
1. Areas of convergence.
2. Areas of disagreement.
3. Methodological differences that may explain disagreement.
4. Evidence gaps.
5. Claims that still need citations.

Rules:
- Do not force a consensus.
- Do not add papers that were not provided or verified.
- Mark unsupported claims as [source needed].
- Do not treat DEG, GO/KEGG enrichment, WGCNA, qRT-PCR/qPCR expression validation, selection scans, synteny, cell-line perturbation, animal models, or clinical association as stronger evidence than they are.
- For review articles in the matrix, mark them as secondary sources and do not treat review synthesis as primary experimental evidence.
- Save-output mode does not weaken citation integrity, source tracing, evidence tiering, or missing-information labels.
```
