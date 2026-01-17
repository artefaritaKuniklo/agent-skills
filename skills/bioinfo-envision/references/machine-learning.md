# Machine Learning & Prediction Models

## Single-Gene ROC Analysis

- **AUC Threshold**: AUC > 0.7 (cannot equal 1; AUC=1 cannot be used for selection)
- **Sample Size**: minimum 8 vs 8 (insufficient samples require approval)
- **Visualization**: ensure clear line colors, labels, and readable font sizes
- **Training Set**: single-gene AUC must reach 0.7; if too many genes, may increase threshold (0.8, 0.9) to reduce number

## Single-Gene Expression Analysis

### Validation Requirements

- Expression trend must be consistent and statistically significant
- Minimum 2 external validations must pass
- **Key Gene Limits**:
  - Diagnostic projects: maximum 5 genes (require external validation)
  - Prognosis projects: maximum 8 genes
- **Missing Genes in Validation**: maximum 1 gene can be missing; more requires adjustment or new validation set

### Data Normalization

- When count and FPKM trends differ, may apply VST normalization to count and use rank-sum test
- If using VST, must apply consistently across all analyses

---

## Diagnostic Model ROC

- **Model AUC**: must be > 0.7
- **Comparative Performance**: model AUC should exceed single-gene AUC (if not, may remove related single-gene ROC)
- **AUC Constraint**: neither model nor gene AUC can equal 1
  - If AUC = 1: use confusion matrix, PR curve, or C-index instead
- **Sample Size**: recommend minimum 8 vs 8
- **Visualization**: annotate optimal cutoff and 95% confidence interval; use dark line colors, moderate font

---

## Machine Learning

### Sample & Cross-Validation Requirements

- **Sample Size**: minimum 8 vs 8
- **Cross-Validation Folds** (based on sample count):
  - Small samples (dozen examples): 3-fold
  - Other sizes: 5-fold or 10-fold
  - Minimum samples per fold: 3

### Algorithm Strategy

- Prioritize self-limiting methods and take intersection
- Take intersection with non-self-limiting methods to increase robustness
- **Class Coding**: Normal control = 0, Disease = 1

### Analysis Goals

- May be used for: gene selection, feature importance, or classification only (no importance scores)

### Algorithm Notes

**For Gene Selection**:
- SVM-RFE, Lasso (alpha=1), XGBoost, Boruta

**For Feature Importance**:
- RF, GBM, XGBoost

**Model Validation**:
- Model error must not be 0; accuracy must not be 1 (indicates overfitting)
- If input genes equal output genes, change algorithm or adjust workflow

---

## Prognosis Models

### Concept Distinction

- **Risk Model**: uses only genes
- **Independent Prognosis Model**: uses riskScore + clinical features

### Cox Regression Standards

#### Single-Factor Cox
- **PH Assumption**: test before Cox (PH.p > 0.05)
- **Significance Level**: prioritize p < 0.05, may extend to p < 0.2 (if p < 0.2, adjust confidence interval)

#### Multi-Factor Cox
- Perform PH assumption test before analysis
- Gene p-values may exceed 0.05, but PH test must be > 0.05 for all variables
- Use stepwise regression only when model is essentially determined and optimal

### Construction Methods

- Lasso-Cox
- Multi-factor Cox (with PH testing)
- Stepwise regression
- CoxBoost
- randomForestSRC

### Independent Prognosis Model Requirements

- Must include riskScore + at least 1 clinical feature
- If only riskScore available, do not build nomogram

### Nomogram Construction & Evaluation

- **AUC**: must be > 0.6
- **Additional Validation**: need at least one more metric to pass (e.g., calibration curve p > 0.05 or DCA showing model superiority)

### Prognosis ROC Requirements

- **Training & Validation Sets**: both must have AUC > 0.6 (with consistent years)
- **Non-Standard Years**: require literature support if using unusual time points
- **Survival Consistency**: training and validation sets must use same survival type and units (OS/PFS/DFS, years/months/days)

---

## References

See [INDEX.md](INDEX.md) for full documentation overview.
