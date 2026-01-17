# Single-Cell & Advanced Methods

## Clustering (Consensus Clustering / NMF)

### Sample Requirements

- Minimum recommended: 30 samples

### Consensus Clustering Evaluation

- CDF curve assessment
- Platform period K value
- Heatmap visualization

### NMF Evaluation

- Identify steepest slope decline point in heatmap and line plot

### Key Metrics

- **Prognosis Projects**: require survival differences between clusters
- **Non-Prognosis Projects**: clusters must show clinical or functional meaning (e.g., pathway scores or GSVA differences)

---

## Molecular Docking

### Compound Selection & Binding

- Document compound selection rationale
- Report binding energy (reference threshold: -1.2 kcal/mol or -5 kJ/mol)

### Visualization Standards

- Include one overview figure and one zoomed detail figure
- Specify protein source or PDB ID
- Structure display format based on completeness (e.g., ribbon chains for helical structures, stick models for complete structures)

---

## ceRNA / TF-miRNA-mRNA Networks

### Data Integration

- Use intersection of relationship pairs from multiple databases (not just target gene intersection)
- Cannot rely on single database predictions

### Reporting Requirements

- Describe node and edge counts in main text
- Document database sources and filtering criteria

---

## Immune Therapy & Immune Infiltration

### Immune Therapy Analysis

- Can use TIDE, IPS, and similar tools
- Document method selection and rationale

### Immune Infiltration Methods

- Multiple algorithms available: CIBERSORT, ssGSEA, xCell, TIMER, etc.
- For mouse data: CIBERSORT, ssGSEA
- Can use \immunedeconv\ package
- **Important**: Note cell type name updates and use latest version annotations

---

## Correlation & Relationship Analysis

### Correlation Coefficient Thresholds

- Minimum recommended: 0.3
- Selection of Pearson vs Spearman depends on data distribution
- When uncertain, avoid Pearson; Spearman is generally safer

### Mendelian Randomization (MR)

- OR direction need not match gene up/downregulation
- However: MR OR should match single-factor Cox HR (if gene is exposure factor)
- Leave-one-out test results must not cross zero line

---

## Single-Cell Analysis Standards

### Quality Control

- Must satisfy three requirements: cell count, gene count, mitochondrial proportion
- Thresholds must have literature support

### Marker Gene Selection

- Cannot use only top features from \indAllMarkers\
- Each cell type should have > 1 marker gene
- Report cell type—marker gene—cluster relationships
- Include marker gene bubble plot before annotation

### Key Gene Requirements

- Key genes must show high expression in key cell types
- Must display temporal differences

### Ligand-Receptor Analysis

- Complex proteins must be separated
- Clarify analysis sample scope (disease or all samples) and target (all cells or key cells only)
- Use default communication probability threshold p < 0.05
- If insufficient, requires literature support and supervisor approval

### Direction Gene Extension

- Cannot use drug or disease target genes for extension
- For drug/disease targets: prioritize intersection across multiple databases

---

## Special hdWGCNA Considerations

- Traits can use cell types or direction gene set scores
- Key cells can be selected using AUCell scoring

---

## Single-Gene Projects

- Genes must show expression differences between disease and control groups
- Trend must match mainstream literature findings

---

## Other Important Considerations

### Outlier Handling

- Extreme OR, HR, or CI values can be judged anomalous and removed
- Likely source: low-expression genes
- Recommend filtering low-expression genes at raw data stage

### Drug Sensitivity Prediction

- For large drug sets: can plot boxplots for drugs with high riskScore correlation

### Quality Standards Across Methods

- Seed setting for reproducibility
- Version tracking for packages
- Proper documentation of thresholds and parameters
- Literature support for non-standard choices

---

## References

See [INDEX.md](INDEX.md) for full documentation overview.
