#!/usr/bin/env Rscript
#
# RNA-seq Differential Expression Analysis
# Template for basic RNA-seq workflow using tidyverse and DESeq2
#
# Usage:
#   Rscript analyze_rna_seq.R counts.tsv metadata.tsv output_dir
#
# Requirements:
#   - counts.tsv: gene_id in first column, sample counts in remaining columns
#   - metadata.tsv: must contain 'sample' and 'condition' columns
#

# ==============================================================================
# Command-line Arguments
# ==============================================================================

args <- commandArgs(trailingOnly = TRUE)

if (length(args) < 3) {
  stop(
    "\nUsage: Rscript analyze_rna_seq.R counts.tsv metadata.tsv outdir\n",
    "  counts.tsv    - Expression counts (gene_id, samples)\n",
    "  metadata.tsv  - Sample metadata (must include 'sample' and 'condition')\n",
    "  outdir        - Output directory for results\n"
  )
}

counts_file <- args[[1]]
meta_file <- args[[2]]
outdir <- args[[3]]

# Create output directory
dir.create(outdir, recursive = TRUE, showWarnings = FALSE)

# ==============================================================================
# Load Libraries
# ==============================================================================

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(tibble)
  library(ggplot2)
  library(DESeq2)
  library(tximport)
})

# ==============================================================================
# Helper Functions
# ==============================================================================

# Safe file reading with error checking
safe_read_tsv <- function(path) {
  if (!file.exists(path)) {
    stop(sprintf("File not found: %s", path))
  }
  read_tsv(path, col_types = cols())
}

# ==============================================================================
# Load Data
# ==============================================================================

message("Loading counts matrix from: ", counts_file)
counts <- safe_read_tsv(counts_file)

message("Loading sample metadata from: ", meta_file)
meta <- safe_read_tsv(meta_file)

# ==============================================================================
# Validate Count Matrix
# ==============================================================================

if (ncol(counts) < 2) {
  stop("Counts file must have at least two columns (gene_id + at least one sample)")
}

# Extract gene IDs and count matrix
gene_ids <- counts[[1]]
count_mat <- counts %>%
  select(-1) %>%
  as.matrix()

colnames(count_mat) <- names(counts)[-1]
rownames(count_mat) <- gene_ids

message("Loaded ", nrow(count_mat), " genes and ", ncol(count_mat), " samples")

# ==============================================================================
# Validate Metadata
# ==============================================================================

required_cols <- c("sample", "condition")
if (!all(required_cols %in% names(meta))) {
  stop(
    "Metadata must contain columns: ",
    paste(required_cols, collapse = ", ")
  )
}

# Check sample name alignment
missing_samples <- setdiff(colnames(count_mat), meta\)
if (length(missing_samples) > 0) {
  stop(
    "Samples in counts not found in metadata: ",
    paste(missing_samples, collapse = ", ")
  )
}

meta_df <- meta %>%
  column_to_rownames("sample")

# ==============================================================================
# DESeq2 Differential Expression Analysis
# ==============================================================================

message("Building DESeq2 object...")

dds <- DESeqDataSetFromMatrix(
  countData = count_mat,
  colData = as.data.frame(meta_df),
  design = ~ condition
)

message("Running DESeq2 analysis...")
dds <- DESeq(dds)
res <- results(dds)

# ==============================================================================
# Output Results
# ==============================================================================

# Convert results to tibble and write
res_tbl <- as_tibble(as.data.frame(res), rownames = "gene")
results_file <- file.path(outdir, "deseq2_results.csv")

message("Writing differential expression results to: ", results_file)
write_csv(res_tbl, results_file)

# ==============================================================================
# Quality Control Visualizations
# ==============================================================================

message("Generating QC plots...")

# Variance-stabilized transformation for visualization
vsd <- vst(dds, blind = FALSE)

# PCA plot
pca_plot <- DESeq2::plotPCA(vsd, intgroup = "condition")
pca_file <- file.path(outdir, "pca_plot.png")
ggsave(
  filename = pca_file,
  plot = pca_plot,
  width = 7,
  height = 5,
  dpi = 300
)
message("PCA plot saved to: ", pca_file)

# ==============================================================================
# Summary
# ==============================================================================

message("\n", strrep("=", 70))
message("Analysis Complete!")
message(strrep("=", 70))
message("\nOutput directory: ", normalizePath(outdir))
message("Results file: deseq2_results.csv")
message("QC plots: pca_plot.png")
message("\nNote: Review QC plots for batch effects and outliers.")
message("Ref: See ENVISION_STANDARDS.md for analysis guidelines.")
message(strrep("=", 70), "\n")
