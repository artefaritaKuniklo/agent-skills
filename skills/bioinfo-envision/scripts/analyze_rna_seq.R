#!/usr/bin/env Rscript

# Basic RNA-seq analysis template (tidyverse + DESeq2)

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 3) {
  stop('Usage: Rscript analyze_rna_seq.R counts.tsv metadata.tsv outdir')
}

counts_file <- args[1]
meta_file <- args[2]
outdir <- args[3]

dir.create(outdir, recursive = TRUE, showWarnings = FALSE)

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(tibble)
  library(ggplot2)
  library(DESeq2)
  library(tximport)
})

# Helper: safe read
safe_read_tsv <- function(path) {
  if (!file.exists(path)) stop(sprintf('File not found: %s', path))
  read_tsv(path, col_types = cols())
}

counts <- safe_read_tsv(counts_file)
meta <- safe_read_tsv(meta_file)

# Expect: counts has gene id in first column, samples in remaining columns
if (ncol(counts) < 2) stop('Counts file must have at least two columns (gene + samples)')

gene_ids <- counts[[1]]
count_mat <- counts %>% select(-1) %>% as.matrix()
colnames(count_mat) <- names(counts)[-1]
rownames(count_mat) <- gene_ids

# Metadata: require a `sample` column and a `condition` column
if (!all(c('sample', 'condition') %in% names(meta))) {
  stop('Metadata must contain `sample` and `condition` columns')
}

# Align metadata to columns
if (!all(colnames(count_mat) %in% meta$sample)) {
  stop('Sample names in counts do not match metadata$sample')
}

meta_df <- meta %>% column_to_rownames('sample')

# Build DESeq2 object and run
dds <- DESeqDataSetFromMatrix(
  countData = count_mat,
  colData = as.data.frame(meta_df),
  design = ~ condition
)

dds <- DESeq(dds)
res <- results(dds)

# Write results
res_tbl <- as_tibble(as.data.frame(res), rownames = 'gene')
readr::write_csv(res_tbl, file.path(outdir, 'deseq2_results.csv'))

# Generate variance-stabilized PCA plot
vsd <- vst(dds, blind = FALSE)
pca_plot <- DESeq2::plotPCA(vsd, intgroup = 'condition')
ggsave(filename = file.path(outdir, 'pca.png'), plot = pca_plot, width = 6, height = 4)

message('Analysis complete. Results in: ', normalizePath(outdir))

# Notes on Envision Standards
# - Ensure raw counts are used for differential analysis.
# - Perform PCA and boxplot checks for batch effects.
