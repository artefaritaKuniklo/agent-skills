# Bioinformatics Guidance — Basic RNA-seq Workflow

Typical pipeline steps (concise):

1. Raw data QC — `FastQC` or `fastp`; inspect per-base quality and adapters.
2. Trimming (optional) — remove adapters with `fastp` or `trim_galore`.
3. Alignment / Quantification — `STAR`, `hisat2`, or pseudo-aligners (`salmon`, `kallisto`).
4. Import counts — `tximport` for transcript-level to gene-level summarization.
5. QC & normalization — PCA, library size checks; use `DESeq2` or `edgeR` normalization.
6. Differential expression — design matrix, model fitting, shrinkage for log-fold changes.
7. Downstream analysis — gene set enrichment (clusterProfiler), visualization (ggplot2), pathway plots.

## Notes on Envision Standards
> 详尽的部门级分析规范已整合到 `README.md`（节 “数据分析部门项目分析标准 v5.0”）和 `references/ENVISION_STANDARDS.md`，请在需要时引用完整规范。
