# Review Paragraph Prompt

```text
Draft review paragraphs using scientific-review-skill.

Chinese output modes:
- Default mode is 中文速读/中文写作模式. Write natural Chinese review prose first, then provide a brief evidence-boundary note or claim-to-source map as needed.
- Use 证据审计模式 only when the user asks for audit mode, strict evidence table, evidence matrix, claim-to-source audit, or detailed evidence tracing. In that mode, use labels such as Source-reported content, Reasonable inference, and Model synthesis.
- In both modes, every factual claim must trace to an available source or be marked [source needed].

Save-output mode:
If the user asks to "save to file", "保存到文件", "写入 notes", "生成文献卡片文件", or equivalent, save the draft paragraph and evidence audit as a Markdown file. Use literature-notes/ as the recommended default directory. Use a concise descriptive Markdown filename and use unknown for missing metadata rather than inventing it. After saving, respond in chat only with the saved path, a brief summary, and Evidence Check status.

Input:
- Review section:
- Intended claim:
- Available sources:
- Preferred citation style:
- Target audience:

Default output:
1. Draft paragraph in natural Chinese.
2. Brief evidence-boundary note.
3. Unsupported statements that need sources.

Audit-mode output:
1. Draft paragraph.
2. Claim-to-source map.
3. Source-reported content used.
4. Reasonable inference used, if any.
5. Model synthesis used, if any.
6. Unsupported statements that need sources.

Rules:
- Every factual claim must trace to an available source or be marked [source needed].
- Do not invent citations.
- Use cautious language for mechanism, causality, or translational implications unless directly supported.
- For review articles, cite them mainly for background, framework, consensus, controversy, or gaps; trace specific experimental claims to primary studies when possible.
- Do not turn DEG, GO/KEGG, WGCNA, qRT-PCR/qPCR, population/comparative genomics, cell-line perturbation, animal model, or clinical association evidence into causal claims without appropriate validation.
- Save-output mode does not weaken citation integrity, source tracing, evidence tiering, or missing-information labels.
```
