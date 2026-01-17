# Enrichment & Pathway Analysis

## GSEA (Gene Set Enrichment Analysis)

### Method Setup

- If using \clusterProfiler\, note randomness; can set \seed\ parameter for reproducibility
- **Background Gene Set**: prioritize KEGG

### Ranking Criteria

- Can use LogFC or gene correlation as ranking basis
- Recommend comparing single-gene GSEA results with GSVA results

### Significance Thresholds

- **|NES| > 1 AND p < 0.05 (adjusted)**
- Always use adjusted p-values

---

## GSVA (Gene Set Variation Analysis)

### Analysis Standards

- **Threshold**: |t| > 1 (minimum 0) AND p < 0.05 (adjusted)
- **Differential Analysis**: use \limma\ for group comparisons
- **P-value**: prioritize adjusted p-values

---

## GSEA vs GSVA Comparison

- Single-gene GSEA and GSVA results should be compared
- Use results alignment to validate findings

---

## Enrichment Analysis (Functional Enrichment)

### Background Gene Sets

- Prioritize KEGG for background
- Use adjusted p-values where available

### Gene Count Requirements

- Minimum 10 genes for enrichment
- If < 10 genes, convert to single-gene GSEA instead

### Pathway Interpretation

- Focus on biologically relevant pathways
- Document pathway selection rationale
- Cross-reference with disease literature

---

## References

See [INDEX.md](INDEX.md) for documentation overview.
