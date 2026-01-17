# Differential Analysis & Expression

## Differential Expression Analysis

### Software Recommendations

- **Count Data**: use \DESeq2\
- **Microarray Data**: use \limma\

### Threshold Selection

#### Primary Criterion
- **Priority**: use \padj\
- **Minimum Standard**: \pvalue < 0.05\ AND \|logFC| > 0.5\

#### Relaxed Thresholds
- Using relaxed thresholds (p-value only, padj only, or lower logFC) requires approval
- Must provide supporting literature and customer confirmation

#### Gene Count Considerations
- If differentially expressed genes < 100: report to supervisor
- If too many genes and PPI cannot be performed: may increase logFC with literature support

### Quality Control Checklist

Before differential analysis:
1. Draw PCA and boxplots to check for batch effects or outlier samples
2. Observe heatmap performance in subsequent analysis
3. Do not arbitrarily combine data from different platforms for batch correction
4. If merging required: clarify in proposal and ensure same platform
5. **Critical**: Sample order in grouping file and expression matrix must be consistent

### Group Order Documentation

- **DESeq2**: check group order via first row of \
esults()\
- **limma**: in \make.contrasts\, +1 = Case, -1 = Control (Case vs Control)

### Data Usage Guidelines

#### Cannot Be Used for Differential Analysis
- FPKM (raw)
- TPM (raw)
- Normalized count
- \log2(count+1)\ (cannot use for ANY analysis)

#### Can Be Used for Other Analyses
- \log2(fpkm+1)\ or \log2(tpm+1)\ (but only for non-differential analyses)

#### Mixed Count & FPKM/TPM Datasets
- **Differential Analysis**: use raw counts exclusively
- **Other Analyses**: use FPKM/TPM uniformly (no mixing)

#### Validation Checks
- If count data not provided: dataset cannot be training set or used for differential analysis
- Check if FPKM/TPM is normalized (use \
ange()\ to judge; normalized data usually ≤ 50)

---

## References

See [INDEX.md](INDEX.md) and [machine-learning.md](machine-learning.md) for related analyses.
