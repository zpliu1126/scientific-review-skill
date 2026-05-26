# Single-Paper Close Reading Prompt

Use this prompt when the user provides one paper, review article, title, abstract, PDF text, or extracted sections. Default to Chinese quick-reading mode: a readable "中文文献速读卡片" with a concise evidence-boundary section rather than a mechanical field-by-field audit.

```text
Read the provided life science paper using scientific-review-skill. Apply the general evidence rules. If it is a plant, crop, population genomics, evolutionary genomics, comparative genomics, transcriptomics, animal, human, or biomedical paper, apply the relevant domain-specific reference.

Chinese output modes:
- Default mode is 中文速读模式. Use natural Chinese, follow references/chinese-academic-style.md, and avoid repeated English audit labels in the main prose.
- Use 证据审计模式 only when the user asks for audit mode, strict evidence table, evidence matrix, claim-to-source audit, or detailed evidence tracing. In that mode, use labels such as Source-reported content, Reasonable inference, and Model synthesis.
- In both modes, do not weaken citation integrity, source tracing, evidence tiering, or missing-information labels.

Save-output mode:
If the user asks to "save to file", "保存到文件", "写入 notes", "生成文献卡片文件", or equivalent, save the full output as a Markdown file. Use literature-notes/ as the recommended default directory. For a single paper, use the filename pattern:
年份_第一作者_短标题_期刊.md
Use unknown for missing year, first author, short title, or journal. Do not invent metadata to complete the filename. After saving, respond in chat only with the saved path, a brief summary, and Evidence Check status.

Default output for primary research articles:

# 文献速读卡片

## 1. 一句话结论
Summarize the central finding, evidence strength, and use boundary in 1-2 sentences.

## 2. 这篇文章想解决什么问题
Explain the background and scientific question in natural language.

## 3. 作者主要做了什么
Group methods by type, such as genomics, transcriptomics, perturbation, molecular assays, population analysis, animal/human models, or clinical data.

## 4. 作者主要发现了什么
Use 3-5 concise bullets. Do not over-interpret beyond the provided text.

## 5. 证据强度怎么判断
State this as an abstract-level judgment when the input is title + abstract. Distinguish association evidence, likely functional validation, evidence needing full-text verification, and why the result should not be written as complete mechanistic proof unless the source supports it.

## 6. 对综述写作有什么用
Explain where the paper could fit in a review and what kind of claim it can support.

## 7. 不能直接支持什么
List 2-4 overstatements or unsupported claims that should not be written without more evidence.

## 8. 需要回全文核实什么
List key details that require checking in the full text.

## 9. Evidence Check
Briefly state whether there is invented metadata, unsupported evidence, over-causal wording, missing source support, and whether source-reported content, reasonable inference, and model synthesis were separated.

Default output for review articles:

# 综述论文速读卡片

## 1. 这篇综述一句话讲什么
State the review type if available; if not, write [需要核实]. Make clear that a review article is a secondary source.

## 2. 综述范围和核心主线
Summarize the topic boundary, organisms/systems, methods, and conceptual framework reported in the abstract or text.

## 3. 作者主要归纳了什么
Summarize the author's synthesis naturally. Treat classifications, models, and mechanism diagrams as review synthesis, not primary evidence.

## 4. 对我写综述有什么用
Explain what can be used as background, conceptual framing, terminology, field structure, controversy, gap, or primary-study lead.

## 5. 必须回溯原始论文核实什么
List concrete experimental results, gene functions, phenotypes, mechanisms, QTL/GWAS candidates, clinical or breeding claims, and any primary evidence claims that require primary sources.

## 6. 证据边界说明
State that review synthesis is not primary evidence. For outdated or abstract-only reviews, mark claims needing [primary source needed] or [需要原始文献核实].

Rules:
- Do not invent missing citation metadata.
- Mark missing information as [需要核实] or [source needed], matching the user's requested language.
- Preserve the distinction between source-reported content, reasonable inference, and model synthesis, but do not repeat those labels on every line when readability would suffer.
- Use cautious language for extrapolation.
- For review articles, follow references/review-article-synthesis.md and do not treat secondary-source summaries as original experimental results.
- Do not overstate RNA-seq, DEG, GO/KEGG, WGCNA, qRT-PCR/qPCR, population/comparative genomics, cell-line, animal-model, or clinical association evidence as stronger than it is.
- For title + abstract input, explicitly write "abstract-level judgment" or the user's language equivalent.
- Save-output mode does not weaken citation integrity, source tracing, evidence tiering, or missing-information labels.
```
