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

## 数据分析部门项目分析标准 v5.0（已整合）

> 下文为原始 v5.0 文档的结构化整理，保留原文要点（未翻译）。如需引用原始文件见 `references/ENVISION_STANDARDS.md`。

# 数据分析部门项目分析标准 v5.0

> 数据分析部 2025年11月

## 分析人员须知
- 项目责任制：项目分配后，由分析人员全权负责直到项目结题，确保结果专业准确、周期正常、结果可复现。
- 在责任制落实过程中遇到问题，分析人员应主动解决（例如：检索资料、寻求同事帮助、修改分析方案等）。

---

## 一、各个分析点的标准要求

### 1. 数据下载
- 不建议使用 GEO 中经 NCBI 官网定量后的数据；若使用需核对样本信息（样本信息不符视为需重分析）。
- 注释文件若已给出基因 symbol（列名可能不同），禁止再用 `bitr` 或类似方法自行转换基因 symbol。
- 必要时可做基因 symbol 转换，但不能用探针 ID 做差异分析。使用正确的注释版本（例如 TCGA 使用 Gencode v36）。
- 预后项目中避免重复的患者样本（例如 TCGA-DD-A114-01A 与 TCGA-DD-A114-01B 为重复样本）。
- 训练集、验证集与单细胞数据集的疾病定义、取样人群与组织类型应尽量保持一致。
- 对方向基因进行确认，注意有时方向基因由两个基因连在一起。

### 2. 差异分析
- 软件推荐：Count 数据使用 `DESeq2`；芯片数据使用 `limma`。
- 阈值筛选：优先使用 `padj`；最低标准为 `pvalue < 0.05` 且 `|logFC| > 0.5`。
  - 若采用更宽松的阈值（仅 pvalue、仅 padj 或降低 logFC）需申请，提供参考文献并与客户确认。
  - 差异基因数量过少（<100）需反馈主管；若差异基因过多且无法做 PPI，可适当提高 logFC（需有参考文献）。
- 注意事项：
  - 提前绘制 PCA 与箱线图检查看是否存在批次或离群样本；后续也需观察热图表现；
  - 禁止把不同平台的数据随意合并再去去批次（若需合并须在方案中明确并且同平台）；
  - 分组文件与表达矩阵的样本排序必须一致。
- 分组顺序：
  - 在 `DESeq2` 中可通过 `results` 的首行查看分组顺序；
  - 在 `limma` 中 `make.contrasts` 的 +1 为 Case、-1 为 Control（Case vs Control）。
- 数据使用说明：
  - FPKM、TPM、标准化后的 count 不可用于差异分析；`log2(count+1)` 不得用于任何分析；
  - `log2(fpkm+1)` 或 `log2(tpm+1)` 可用于差异分析以外的其他分析；
  - 同一高通量数据集同时存在 raw counts 与 FPKM/TPM 时，差异分析必须使用 raw counts，其他分析统一使用 FPKM/TPM（不可混用）；
  - 如果没有提供 count 数据，该数据集不能用作训练集或差异分析；
  - 检查 FPKM/TPM 是否已经标准化（可用 `range` 判断，标准化数据通常不超过 50）。

### 3. WGCNA
- 样本數至少 15（不区分组别，例如 5 vs 10 也可）。
- 若用评分或免疫浸润丰度作为性状：
  - 诊断类项目：评分/丰度在疾病 vs 对照组间差异显著；
  - 预后类项目：评分/丰度在肿瘤样本中 KM 显著。
- 报告须注明使用的样本类型（全部样本或仅疾病样本）。
- 输入矩阵需为标准化表达矩阵（高通量使用 TPM/FPKM，注意是否经过 log2 处理）；
- 剔除低表达或不表达基因；
- 软阈值筛选建议使 R^2 >= 0.8（最低 0.8，推荐 0.85–0.9），同时平均连接度应低于 200，选择第一个满足两项的软阈值；
- 模块筛选最低要求：模块与特征的相关系数 |r| > 0.3 且 p < 0.05。优先选择 |r| 最大的模块（灰色模块无意义）；相关性使用 Pearson。
- MM 与 GS 阈值建议：GS > 0.2、MM > 0.8（参考 PMID: 36311726），其他阈值需提供文献支持；
- 基因表达矩阵应包含所有基因（错误示例：仅使用差异基因）；
- 模块数量应适中，可通过调整聚类参数优化。

### 4. 第三方基因集评分（如 ssGSEA）
- 明确样本类型（全部样本或仅疾病样本）。
- 推荐方法优先选择 `ssGSEA`。
- 方向基因用于评分时，基因数应在 10–200 之间；`ssGSEA` 最低 10 个基因，30 个以上较好。
- 关键指标：预后项目关注评分在疾病样本中的生存差异；诊断项目关注评分在疾病与正常组间的差异。

### 5. 基因/蛋白网络构建
（详见 `references/ENVISION_STANDARDS.md`）

---

完整文档已放在 `references/ENVISION_STANDARDS.md`（保留原文、已去分页与重复）。

