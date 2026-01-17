# Special Cases & Exceptions

Some projects have unique characteristics that require modified standards.

## Hematologic Malignancies

### Acute Myeloid Leukemia (AML)

- TCGA samples are from peripheral blood; most GEO samples are from bone marrow
- **Validation Approach**: can use GEO bone marrow datasets for external validation
- **Rationale**: tissue source difference is well-documented

---

## Cancer-Specific Prognosis Analysis

### Cancers with Modified Validation Requirements

The following cancer types may request exemption from external validation set requirement:

- Cervical cancer
- Thyroid cancer
- Endometrial cancer

**Approved Alternative**: 7:3 split + overall validation (with supervisor approval)

**Other Cancer Types**: still require external validation set

---

## Survival Analysis Standards

### ROC Time Point Selection

- Must ensure sufficient survival samples for chosen time points
- Example: cannot create 7-year ROC if insufficient 7-year samples available
- Unusual time points require literature support

### Survival Type Consistency

- Training and validation sets must use same survival type (OS, PFS, or DFS)
- Must use same time units (years, months, or days)

---

## Dataset Homology Restrictions

### Duplicate & Homologous Datasets

- Certain datasets are known to have high homology
- **Prohibition**: cannot use homologous datasets separately as training and validation sets within same study
- **Examples**:
  - GSE108113 and GSE200828 (and similar pairs)
  
**Reason**: prevents overfitting due to sample overlap or batch effect

---

## Approval & Exceptions

For any non-standard approaches, projects must:
1. Provide literature support
2. Get supervisor/manager approval
3. Document rationale in project plan
4. Include justification in final report

---

## References

See [INDEX.md](INDEX.md) for full documentation overview.
