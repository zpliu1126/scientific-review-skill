# PDF Section Heading Rules

Use these rules after PDF parsing to decide whether section boundaries are stable enough for close reading, batch review, cited-reference mining, or functional gene evidence curation.

## Target Sections

Try to identify:

- Title
- Authors
- Abstract
- Keywords
- Introduction
- Materials and Methods / Methods
- Results
- Discussion
- Conclusion
- Figures / Tables captions
- References

## Synonym Headings

### Introduction 同义标题

- Introduction
- INTRODUCTION
- Background
- 1 Introduction
- 1. Introduction
- Background and aims
- Background / Introduction
- Research background
- General introduction

### Methods 同义标题

- Materials and Methods
- Material and methods
- Methods
- Experimental procedures
- Experimental design
- Plant materials and growth conditions
- Sample preparation
- RNA extraction and sequencing
- Statistical analysis

### Results 同义标题

- Results
- Results and analysis
- Findings
- 2 Results
- Results and Discussion, if combined

### Discussion 同义标题

- Discussion
- Results and Discussion
- Conclusions
- Conclusion
- General discussion

### References 同义标题

- References
- Literature cited
- Bibliography

## Required Rules

1. 不能只靠标题字符串。
2. 结合字体大小、加粗、编号、前后空行、页内位置、目录和阅读顺序判断。
3. 如果 Introduction 未稳定识别，但正文开头明显是背景介绍，标记为 `probable_introduction`，不要直接说已确认。
4. 如果 Results and Discussion 合并，标记 `combined_results_discussion`。
5. 如果没有 Methods，例如综述文章，标记 `not_applicable`。
6. 如果章节标题缺失或解析失败，必须写 `[需要人工复核]`。
7. 不要因为未识别 Introduction 就停止精读；应降级为 `section-uncertain full-text reading`。

## Confidence Rules

- `high`: title/abstract and most major sections are stable; References and captions are detectable when present.
- `medium`: enough full text is available, but at least one major section is probable, combined, or parser-dependent.
- `low`: headings are missing, reading order is unstable, the PDF is scanned without usable OCR, or major sections cannot be separated.

## Manual Review Triggers

Mark `need_manual_review=yes` when:

- Introduction is `missing` or only `probable_introduction`.
- Methods, Results, Discussion, or References are missing and not clearly `not_applicable`.
- Results and Discussion are combined and downstream extraction requires separate claims.
- Figure/table captions are absent but the paper clearly relies on figures/tables.
- The parser reports double-column reading order problems, page-header/footer contamination, or broken references.
- OCR was used and text quality may affect gene names, methods, statistics, or citations.

## Downstream Handling

When section detection is uncertain:

- Continue reading if full text is available.
- Label the source basis as `section-uncertain full-text reading`.
- Preserve section uncertainty in `templates/fulltext-paper-card.md`.
- Do not claim a result came from Introduction, Methods, Results, or Discussion unless the section boundary is stable.
- Use page, figure, table, or quoted local context as anchors where section anchors are unreliable.
