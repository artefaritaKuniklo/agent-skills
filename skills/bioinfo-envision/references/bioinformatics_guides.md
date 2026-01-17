# Bioinformatics Guidance — Basic RNA-seq Workflow

Typical pipeline steps (concise):

1. **Raw Data QC** — FastQC or astp; inspect per-base quality and adapters.
2. **Trimming (optional)** — remove adapters with astp or 	rim_galore.
3. **Alignment / Quantification** — STAR, hisat2, or pseudo-aligners (salmon, kallisto).
4. **Import Counts** — 	ximport for transcript-level to gene-level summarization.
5. **QC & Normalization** — PCA, library size checks; use DESeq2 or dgeR normalization.
6. **Differential Expression** — design matrix, model fitting, shrinkage for log-fold changes.
7. **Downstream Analysis** — gene set enrichment (clusterProfiler), visualization (ggplot2), pathway plots.

## References

For detailed department-level analysis standards, see:
- [ENVISION_STANDARDS.md](ENVISION_STANDARDS.md) — comprehensive analysis guidelines
- [../README.md](../README.md) — quick overview and best practices
