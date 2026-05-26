# Single-Paper Close Reading Prompt

Use this prompt when the user provides one paper, title, abstract, PDF text, or extracted sections. Default to a readable "文献速读卡片 + 证据审计附录" rather than a mechanical field-by-field audit.

```text
Read the provided life science paper using scientific-review-skill. Apply the general evidence rules. If it is a plant, crop, population genomics, evolutionary genomics, comparative genomics, transcriptomics, animal, human, or biomedical paper, apply the relevant domain-specific reference.

Default output:

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

Rules:
- Do not invent missing citation metadata.
- Mark missing information as [需要核实] or [source needed], matching the user's requested language.
- Preserve the distinction between source-reported content, reasonable inference, and model synthesis, but do not repeat those labels on every line when readability would suffer.
- Use cautious language for extrapolation.
- Do not overstate RNA-seq, DEG, GO/KEGG, WGCNA, qRT-PCR/qPCR, population/comparative genomics, cell-line, animal-model, or clinical association evidence as stronger than it is.
- For title + abstract input, explicitly write "abstract-level judgment" or the user's language equivalent.
```
