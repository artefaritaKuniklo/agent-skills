# Tidyverse Best Practices (R)

Concise best-practices for writing tidy, reproducible R code following the tidyverse philosophy.

Principles

- Use tidy data: one observation per row, one variable per column.
- Prefer `tibble` over base `data.frame` for predictable printing and subsetting.
- Use pipes (`%>%` or `|>`) to express clear data transformations.
- Write small pure functions with descriptive names and single responsibility.
- Favor vectorized operations and avoid loops when possible; use `purrr` for iteration.
- Use consistent naming: `snake_case` for variables, `camelCase` for functions is acceptable but pick one convention.
- Keep scripts reproducible: set seed, record package versions (use `renv`).
- Document inputs/outputs at the top of scripts and use `here::here()` for paths.
- Use `styler` and `lintr` in CI to enforce style and catch common issues.

Project structure suggestions

- `data/` — raw and processed data (keep raw immutable)
- `scripts/` — R scripts for each pipeline step
- `R/` — reusable functions as package-style modules
- `results/` — outputs and figures
- `docs/` — analysis notes and reports

Testing & QA

- Add small unit tests with `testthat` for core functions
- Use sample datasets to verify pipeline steps

## Notes on Envision Standards
> 详尽的部门级分析规范已整合到 `README.md`（节 “数据分析部门项目分析标准 v5.0”）和 `references/ENVISION_STANDARDS.md`，请在需要时引用完整规范。
