# Review Article Synthesis Prompt

Use this prompt when the input is a narrative review, systematic review, meta-analysis, perspective, mini-review, or field overview. Treat review articles as secondary sources.

```text
Read the provided review article using scientific-review-skill. Follow references/review-article-synthesis.md and, for Chinese output, references/chinese-academic-style.md.

Chinese output modes:
- Default mode is 中文速读模式. Use a natural Chinese "综述论文速读卡片" and avoid repeated English audit labels in the main prose.
- Use 证据审计模式 only when the user asks for audit mode, strict evidence table, evidence matrix, claim-to-source audit, or detailed evidence tracing. In that mode, use labels such as Source-reported content, Reasonable inference, and Model synthesis.
- In both modes, review synthesis is secondary-source evidence and must not be treated as primary experimental evidence.

Default output:

# 综述论文速读卡片

## 1. 这篇综述一句话讲什么
State the review type if available; if not, write [需要核实]. State that the paper is a secondary source.

## 2. 综述范围和核心主线
Summarize the topic boundary, organisms/systems, concepts, technologies, and organizing framework.

## 3. 作者主要归纳了什么
Summarize the author's synthesis naturally. Treat classifications, mechanism models, and field frameworks as review synthesis, not primary evidence.

## 4. 对我写综述有什么用
Explain what can support background, terminology, field structure, consensus, controversy, research gaps, or leads to primary studies.

## 5. 必须回溯原始论文核实什么
List specific experimental results, gene functions, phenotype data, treatment conditions, mechanisms, protein interactions, regulatory claims, QTL/GWAS candidates, clinical claims, breeding claims, or other primary-evidence claims.

## 6. 证据边界说明
Explain what the review can and cannot support. Mark missing primary evidence as [primary source needed] or [需要原始文献核实].

Audit-mode output:
- Review type
- Source basis
- Source-reported content
- Reasonable inference
- Model synthesis
- Claims usable from the review
- Claims requiring primary sources
- Limitations and currency check

Rules:
- Do not invent citation metadata, primary studies, authors, years, DOI, PMID, methods, or results.
- Do not use a review article alone to support specific experimental claims unless the user explicitly accepts secondary-source support.
- If the review is old or abstract-only, state that recent primary studies may be missing.
- Do not weaken citation integrity, source tracing, evidence tiering, or missing-information labels in either output mode.
```
