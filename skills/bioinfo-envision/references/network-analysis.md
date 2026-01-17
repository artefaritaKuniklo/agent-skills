# Network Analysis & Co-expression Methods

## WGCNA (Weighted Gene Co-expression Network Analysis)

### Sample Requirements

- Minimum 15 samples (regardless of group; e.g., 5 vs 10 is acceptable)

### Trait & Phenotype Requirements

If using scores or immune infiltration abundance as traits:
- **Diagnostic projects**: Score/abundance significantly differs between disease and control groups
- **Prognosis projects**: Score/abundance significantly differs in KM analysis among tumor samples
- **Reporting**: Report must specify sample type used (all samples or disease samples only)

### Data Preparation

- Input matrix must be normalized expression matrix
  - For high-throughput: use TPM/FPKM (note if log2-transformed)
  - Remove low-expressing or non-expressing genes
  
### Soft Threshold Selection

- Recommend R² ≥ 0.8 (minimum 0.8, recommended 0.85–0.9)
- Mean connectivity should be < 200
- Select first threshold meeting both criteria

### Module Selection

- **Minimum Requirement**: module-trait correlation |r| > 0.3 and p < 0.05
- **Prioritize**: largest |r| modules (gray module meaningless)
- **Correlation Method**: use Pearson correlation

### MM and GS Thresholds

- **Suggested Values**: GS > 0.2, MM > 0.8 (ref. PMID: 36311726)
- **Other Thresholds**: require literature support

### Gene Expression Matrix Requirements

- Must include all genes (incorrect: using only differentially expressed genes)
- Module count should be moderate; optimize by adjusting clustering parameters

---

## PPI (Protein-Protein Interaction) Networks

### Gene Count Restrictions

- Minimum: 10 genes
- Maximum: 2000 genes

### Analysis Strategy

- Do not use PPI alone to select key genes
- Recommend combining Cytoscape cytoHubba plugin with multiple algorithms
- Save results and visualizations (.pdf) for each algorithm
- Avoid ties (e.g., genes 10 and 11 with same score); adjust algorithm or Top value if necessary
- Save all gene results for audit

### Isolated Nodes

- If showing interactions only: retain
- If used for selection: may remove

### Purpose & Visualization

- Purpose must be clear (show relationships or reduce gene count)
- Use downstream analysis to guide decisions; consult supervisor if uncertain
- Document STRING confidence thresholds in report
- After Cytoscape beautification, save environment (`.cys`)
- For many genes, may show Top 30 by degree ranking

---

## GeneMANIA Networks

### Input Gene Count

- Avoid excessive genes; recommend ≤ 10

### Visualization

- Distinguish input genes from predicted genes in network diagram
- Display biologically relevant processes related to disease

---

## Gene Set Scoring (ssGSEA, GSVA)

### Method Selection

- **Recommended**: `ssGSEA` for scoring
- **Clarify**: sample type (all samples or disease samples only)

### Gene Count Requirements

- When using direction genes: 10–200 genes total
- For `ssGSEA`: minimum 10 genes, 30+ preferred

### Key Metrics

- **Prognosis projects**: focus on survival differences in disease samples
- **Diagnostic projects**: focus on differences between disease and normal groups

---

## References

See [INDEX.md](INDEX.md) and [differential-analysis.md](differential-analysis.md) for related guidelines.
