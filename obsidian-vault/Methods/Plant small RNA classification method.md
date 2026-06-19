---
title: "Plant small RNA classification method"
aliases:
  - "Hierarchical plant small RNA classification"
source_note: "[[Axtell 2013 - Classification and Comparison of Small RNAs from Plants]]"
method_type: "review-derived classification"
status: "sample"
tags:
  - method/classification
  - topic/plant-small-rna
---

# Plant Small RNA Classification Method

> [!note] Source
> This method note is derived from [[Axtell 2013 - Classification and Comparison of Small RNAs from Plants]]. It is a review-derived classification aid, not a formal ontology standard.

## Minimal Classification Logic

1. Determine precursor type.
2. If the precursor is a single-stranded self-complementary hairpin, classify as [[Hairpin RNA]].
3. If the precursor is double-stranded RNA from two complementary strands or RDR-derived dsRNA, classify as [[Small interfering RNA]].
4. Subclassify by biogenesis factors, size distribution, pathway components, and function.

## Secondary Classes

- [[Hairpin RNA]]
  - microRNA
  - non-miRNA hpRNA
- [[Small interfering RNA]]
  - heterochromatic siRNA
  - [[Phased secondary siRNA|secondary siRNA]]
  - NAT-siRNA

## Practical Annotation Cautions

> [!warning]
> Axtell explicitly notes that classification systems are intellectual constructs. Treat ambiguous categories, especially non-miRNA hpRNAs and NAT-siRNAs, as provisional unless the paper provides direct biogenesis evidence.

## Useful Properties for Future Notes

- `rna_class`
- `precursor_type`
- `size_nt`
- `core_factors`
- `evidence_type`
- `source_paper`
- `primary_or_review`
