# Quick Start — Bioinfo-Envision Skill

1. Create a project directory and initialize `renv` for reproducibility:

```bash
R -e "install.packages('renv'); renv::init()"
```

2. Install core packages inside R:

```r
install.packages('tidyverse')
if (!requireNamespace('BiocManager', quietly=TRUE)) install.packages('BiocManager')
BiocManager::install(c('DESeq2','edgeR','tximport'))
```

3. Run the example analysis (adjust paths):

```bash
Rscript skills/bioinfo-envision/scripts/analyze_rna_seq.R data/counts.tsv metadata/sample_table.tsv results/
```

4. Inspect `results/` for QC reports, differential expression tables, and plots.

## Notes on Envision Standards
- Verify sample information and annotation files.
- Use DESeq2 for count data and limma for microarray data.
- Perform PCA and boxplot checks for batch effects.
