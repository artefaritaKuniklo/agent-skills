# Data Processing Guidelines

Data quality is fundamental to all downstream analyses. These standards ensure consistent, reproducible data handling across projects.

## 1. Data Download

- **GEO Data**: Avoid using NCBI-quantified data from GEO unless sample information is verified. Mismatched samples require re-analysis.
- **Gene Annotation**: If annotation file already provides gene symbols, do not use `bitr` or similar methods for conversion.
- **Symbol Conversion**: Allowed when necessary, but cannot use probe IDs for differential analysis. Use correct annotation versions (e.g., TCGA uses Gencode v36).
- **Sample Replication**: In prognosis projects, avoid duplicate patient samples (e.g., TCGA-DD-A114-01A and TCGA-DD-A114-01B are replicates).
- **Dataset Consistency**: Training, validation, and single-cell datasets should maintain consistent disease definitions, sampling populations, and tissue types.
- **Direction Genes**: Confirm carefully; note that sometimes direction genes consist of two genes combined.

## 2. Quality Control Workflow

Before any statistical analysis:

1. **Inspect Sample Metadata**
   - Verify sample information matches provided documentation
   - Check for missing or misaligned samples
   - Confirm tissue types and disease status

2. **Annotation File Validation**
   - Confirm gene symbols are current and correct
   - Check version consistency (e.g., Gencode versions)
   - Document any manual annotations

3. **Data Integration**
   - Do not arbitrarily combine data from different platforms for batch correction
   - If merging required, clarify in proposal and ensure same platform
   - Document all merge decisions

## References

See parent [INDEX.md](INDEX.md) for full documentation overview.
