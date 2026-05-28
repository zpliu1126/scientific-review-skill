# PDF Structure Report

## Source

- File path:
- Paper slug:
- Output root:
- Has text layer: yes / no / unknown
- Page count:
- Parser used: grobid / docling / marker / pymupdf4llm / pymupdf_plain / existing
- Parser status: success / failed / skipped_existing
- Fallback used: no / yes: [failed backend chain]
- Confidence: high / medium / low
- Need manual review: yes / no

## Parsed Outputs

- Markdown:
- JSON:
- TEI/XML:

## Metadata

- Detected title:
- Authors:
- Abstract detected: yes / no
- Keywords detected: yes / no / not parsed

## Section Detection

| Section | Status | Evidence or Notes |
|---|---|---|
| Introduction | confirmed / probable_introduction / missing |  |
| Methods | confirmed / not_applicable / missing |  |
| Results | confirmed / combined_results_discussion / missing |  |
| Discussion | confirmed / combined_results_discussion / missing |  |
| Conclusion | confirmed / included_in_discussion / missing / not_applicable |  |
| References | confirmed / missing |  |

## Captions

- Figure captions detected: yes / no
- Table captions detected: yes / no
- Caption extraction notes:

## Detected Headings

- 

## Section Uncertainty Notes

- 

If Introduction is not stable, include:

```text
[Introduction 标题未稳定识别，正文结构需人工复核]
```

If full text is still available, continue downstream reading as:

```text
section-uncertain full-text reading
```
