# R Bioinformatics Skill

Overview

This skill provides a tidyverse-style foundation for R-based bioinformatics analyses (RNA-seq, basic QC, differential expression, visualization). It focuses on reproducibility, readable code, and practical workflows.

Key files

- `SKILL.md` — skill manifest and overview
- `CORE_PRACTICES.md` — tidyverse best practices
- `QUICK_START.md` — minimal steps to run an analysis
- `references/` — detailed guides and checklists
- `scripts/analyze_rna_seq.R` — example analysis template

Required R packages (examples)

- tidyverse
- DESeq2 (Bioconductor)
- edgeR (Bioconductor)
- tximport (Bioconductor)
- BiocParallel (optional)
- broom, janitor, here, rlang

Usage

Follow `QUICK_START.md` to set up the environment and run the example script.

---

# Envision Standards — Data Analysis Guidelines v5.0

> Detailed analytical standards and requirements for bioinformatics projects.
> Full documentation available in [references/ENVISION_STANDARDS.md](references/ENVISION_STANDARDS.md).

## Overview

### Analyst Responsibilities

- **Project Ownership**: Analysts are fully responsible for project outcomes from assignment to completion, ensuring professional accuracy, timely delivery, and reproducible results.
- **Proactive Problem Solving**: When issues arise, analysts should actively resolve them (e.g., researching literature, consulting colleagues, adjusting analysis plans).

---

## Analysis Standards by Category

### 1. Data Download

- Avoid using NCBI-quantified data from GEO unless sample information is verified (mismatched samples require re-analysis).
- If annotation file already provides gene symbols, do not use `bitr` or similar methods to convert gene symbols.
- Gene symbol conversion is allowed when necessary, but cannot use probe IDs for differential analysis. Use correct annotation versions (e.g., TCGA uses Gencode v36).
- In prognosis projects, avoid duplicate patient samples (e.g., TCGA-DD-A114-01A and TCGA-DD-A114-01B are replicates).
- Training, validation, and single-cell datasets should maintain consistent disease definitions, sampling populations, and tissue types.
- Confirm direction genes; note that sometimes direction genes consist of two genes combined.

### 2. Differential Analysis

- **Recommended Tools**: Use `DESeq2` for count data; use `limma` for microarray data.
- **Threshold Selection**: Prioritize `padj`; minimum standard is `pvalue < 0.05` and `|logFC| > 0.5`.
  - Using relaxed thresholds (p-value only, padj only, or lower logFC) requires approval with supporting literature and client confirmation.
  - Report to supervisor if differentially expressed genes < 100; if too many genes and PPI cannot be performed, may increase logFC with literature support.
- **Important Considerations**:
  - Draw PCA and boxplots in advance to check for batch effects or outlier samples; observe heatmap performance in subsequent analysis.
  - Do not arbitrarily combine data from different platforms for batch correction (if merging required, clarify in proposal and ensure same platform).
  - Sample order in grouping file and expression matrix must be consistent.
- **Group Order**:
  - In `DESeq2`, check group order via first row of `results`.
  - In `limma`, `make.contrasts` uses +1 for Case, -1 for Control (Case vs Control).
- **Data Usage Guidelines**:
  - FPKM, TPM, and normalized count cannot be used for differential analysis; `log2(count+1)` cannot be used for any analysis.
  - `log2(fpkm+1)` or `log2(tpm+1)` can be used for analyses other than differential analysis.
  - When raw counts and FPKM/TPM coexist in a dataset, differential analysis must use raw counts; other analyses use FPKM/TPM uniformly (no mixing).
  - If count data not provided, dataset cannot be used as training set or for differential analysis.
  - Check if FPKM/TPM is normalized (use `range` to judge; normalized data usually ≤ 50).

### 3. WGCNA

- Minimum 15 samples (regardless of group, e.g., 5 vs 10 is acceptable).
- If using scores or immune infiltration abundance as traits:
  - Diagnostic projects: Score/abundance significantly differs between disease and control groups.
  - Prognosis projects: Score/abundance significantly differs in KM analysis among tumor samples.
- Report must specify sample type used (all samples or disease samples only).
- Input matrix must be normalized expression matrix (for high-throughput use TPM/FPKM; note if log2-transformed).
- Remove low-expressing or non-expressing genes.
- Soft threshold selection: recommend R² ≥ 0.8 (minimum 0.8, recommended 0.85–0.9); mean connectivity < 200. Select first threshold meeting both criteria.
- Module selection minimum requirement: module-trait correlation |r| > 0.3 and p < 0.05. Prioritize largest |r| (gray module meaningless); use Pearson correlation.
- MM and GS threshold suggestions: GS > 0.2, MM > 0.8 (ref. PMID: 36311726); other thresholds require literature support.
- Gene expression matrix must include all genes (incorrect example: using only differentially expressed genes).
- Module count should be moderate; optimize by adjusting clustering parameters.

### 4. Gene Set Scoring (e.g., ssGSEA)

- Clarify sample type (all samples or disease samples only).
- Recommended method: prioritize `ssGSEA`.
- When using direction genes for scoring, gene count should be 10–200; `ssGSEA` minimum 10 genes, 30+ preferred.
- Key Metrics: Prognosis projects focus on survival differences in disease samples; diagnostic projects focus on differences between disease and normal groups.

### 5. Gene/Protein Network Analysis

See [references/ENVISION_STANDARDS.md](references/ENVISION_STANDARDS.md) for complete details.

---

For additional standards and best practices, refer to the complete documentation in [references/ENVISION_STANDARDS.md](references/ENVISION_STANDARDS.md).

