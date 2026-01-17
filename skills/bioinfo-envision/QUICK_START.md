# Quick Start — Bioinfo-Envision Skill

1. Create a project directory and initialize env for reproducibility:

`ash
R -e "install.packages('renv'); renv::init()"
`

2. Install core packages inside R:

`
install.packages('tidyverse')
if (!requireNamespace('BiocManager', quietly=TRUE)) install.packages('BiocManager')
BiocManager::install(c('DESeq2','edgeR','tximport'))
`

3. Run the example analysis (adjust paths):

`ash
Rscript skills/bioinfo-envision/scripts/analyze_rna_seq.R data/counts.tsv metadata/sample_table.tsv results/
`

4. Inspect esults/ for QC reports, differential expression tables, and plots.

## Key Checkpoints

- Verify sample information and annotation files.
- Use DESeq2 for count data and limma for microarray data.
- Perform PCA and boxplot checks for batch effects.
- Ensure consistent gene annotations and sample ordering.

## References

See [references/ENVISION_STANDARDS.md](references/ENVISION_STANDARDS.md) for complete analysis standards and guidelines.
