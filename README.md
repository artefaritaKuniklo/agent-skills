# Agent Skills Repository

This repository contains Agent Skills for Claude. Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.

For more information, check out:

- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Agent Skills specification](https://agentskills.io/)

## Repository Structure

<<<<<<< HEAD
\\\
agent-skills/
├── README.md                        # This file
├── .gitignore                       # Git ignore file
├── skills/                          # Custom skill implementations
│   ├── bioinfo-envision/            # R bioinformatics skill (production)
│   │   ├── README.md                # Skill overview and analysis standards
│   │   ├── CORE_PRACTICES.md        # Tidyverse best practices for R
│   │   ├── QUICK_START.md           # Quick setup and basic usage
│   │   ├── scripts/
│   │   │   └── analyze_rna_seq.R    # Example RNA-seq analysis template
│   │   └── references/
│   │       ├── INDEX.md                        # Standards documentation index
│   │       ├── bioinformatics_guides.md        # RNA-seq workflow overview
│   │       ├── tidyverse_best_practices.md     # R coding standards
│   │       ├── ENVISION_STANDARDS.md           # Legacy full standards (archived)
│   │       ├── data-processing.md              # Data download & QC guidelines
│   │       ├── differential-analysis.md        # Differential expression analysis
│   │       ├── network-analysis.md             # WGCNA, PPI, co-expression analysis
│   │       ├── machine-learning.md             # ML, ROC, prognosis models
│   │       ├── enrichment-analysis.md          # GSEA, GSVA, pathway analysis
│   │       ├── single-cell-analysis.md         # Single-cell & advanced methods
│   │       ├── special-cases.md                # Special cases and exceptions
│   │       └── thresholds.yaml                 # Analytical thresholds (machine-readable)
│   │
│   └── clean-code/                  # Code quality & best practices skill
│       ├── README.md                # Skill overview
│       ├── SKILL.md                 # Skill definition and instructions
│       ├── CORE_PRACTICES.md        # Core code quality principles
│       ├── QUICK_START.md           # Quick reference guide
│       ├── INDEX.md                 # Documentation index
│       ├── PROJECT_SUMMARY.md       # Project summary
│       ├── scripts/                 # Code examples and templates
│       └── references/              # Supporting documentation
│
├── template/                        # Skill template for creating new skills
│   └── SKILL.md                     # Template SKILL.md file
│
├── spec/                            # Agent Skills specification
│   └── README.md                    # Skills specification documentation
│
\\\

## Available Skills

### 1. bioinfo-envision

**Type**: Production Skill  
**Purpose**: Comprehensive R-based bioinformatics analysis with focus on reproducibility and departmental standards compliance.

**Core Capabilities**:

- RNA-seq differential expression analysis (DESeq2, limma)
- Quality control and batch effect detection
- Co-expression network analysis (WGCNA)
- Protein-protein interaction networks
- Gene set enrichment and pathway analysis (GSEA, GSVA)
- Machine learning and predictive modeling
- Prognosis and survival analysis
- Single-cell transcriptomics
- Advanced statistical methods

**Quick Access**:

- [Overview & Standards](./skills/bioinfo-envision/README.md)
- [Setup Guide](./skills/bioinfo-envision/QUICK_START.md)
- [R Best Practices](./skills/bioinfo-envision/CORE_PRACTICES.md)

**Standards Documentation**:
Complete analytical standards organized by method:

| Document | Coverage |
| ---------- | ---------- |
| [INDEX.md](./skills/bioinfo-envision/references/INDEX.md) | Navigation index for all standards |
| [data-processing.md](./skills/bioinfo-envision/references/data-processing.md) | Data download, QC, annotation |
| [differential-analysis.md](./skills/bioinfo-envision/references/differential-analysis.md) | DESeq2, limma, thresholds |
| [network-analysis.md](./skills/bioinfo-envision/references/network-analysis.md) | WGCNA, PPI, GeneMANIA |
| [machine-learning.md](./skills/bioinfo-envision/references/machine-learning.md) | ROC, Cox regression, prediction models |
| [enrichment-analysis.md](./skills/bioinfo-envision/references/enrichment-analysis.md) | GSEA, GSVA, pathway analysis |
| [single-cell-analysis.md](./skills/bioinfo-envision/references/single-cell-analysis.md) | Single-cell, clustering, advanced methods |
| [special-cases.md](./skills/bioinfo-envision/references/special-cases.md) | Disease-specific and project exceptions |

**Machine-Readable Resources**:

- [thresholds.yaml](./skills/bioinfo-envision/references/thresholds.yaml) - Complete analytical thresholds in YAML format

### 2. clean-code

**Type**: Development Skill  
**Purpose**: Code quality, best practices, and refactoring guidelines.

**Core Topics**:

- Code organization and structure
- Naming conventions and readability
- Testing and documentation
- Refactoring strategies

**Access**:

- [Skill Overview](./skills/clean-code/README.md)
- [Quick Start](./skills/clean-code/QUICK_START.md)
- [Core Practices](./skills/clean-code/CORE_PRACTICES.md)

---

## Directory Descriptions

### /skills - Skill Implementations

Contains production and development skills. Each skill is a self-contained folder with documentation, examples, and resources.

**Each skill includes**:

- SKILL.md — Skill manifest (name, description, activation conditions)
- README.md — Comprehensive overview and usage guide
-

\references/ — Detailed documentation and specifications

- scripts/ — Example code and templates
- Other supporting files as needed

### /template - Skill Template

Reference template for creating new skills. Use as a starting point when developing new agent skills.

### /spec - Specification Documents

Formal Agent Skills specification and compliance documentation.

---

## Creating a New Skill

### Basic Structure

Create a new folder in \skills/\ with this structure:

\\\
my-skill/
├── SKILL.md                 # Skill manifest (required)
├── README.md                # Comprehensive overview
├── references/              # Documentation (optional)
│   ├── INDEX.md            # Documentation index
│   └── *.md                # Detailed guides
├── scripts/                 # Code examples (optional)
│   └── example.py
└── assets/                  # Templates, media (optional)
    └── template.xlsx
\\\

### SKILL.md Format

Every skill must have a \SKILL.md\ with YAML frontmatter:

\\\markdown

---

name: my-skill-name

description: Clear description of what this skill does and when to use it

---

## My Skill Name

- Detailed instructions that Claude will follow when this skill is active

## Examples

- Example usage 1
- Example usage 2

## Guidelines

- Best practice 1
- Best practice 2
\\\

### Required Fields

- \ame\ — Unique lowercase identifier (use hyphens for spaces)
- \description\ — Complete description of functionality and use cases

### Bundled Resources

#### \scripts/\ - Executable Code

Include reusable or frequently-written code:

- Data processing scripts
- API integration examples
- File conversion utilities
- Analysis templates

**Benefits**: Token-efficient, deterministic execution, reproducible results

#### \references/\ - Documentation

Long-form reference material and guides:

- Database schemas
- API documentation  
- Domain expertise
- Workflow guides
- Detailed specifications

**Best Practice**: For large files (>10k words), include search patterns in SKILL.md

#### \ssets/\ - Output Resources

Templates and files used in generated output:

- Document templates (PPTX, DOCX, XLSX)
- Images and icons
- Boilerplate code
- Fonts and styling

---

## Documentation Standards

All skills follow these documentation principles:

### Structure

- Clear heading hierarchy (## for sections, ### for subsections)
- Logical organization by topic or workflow

### Content

- **Specific**: Include actual thresholds, parameters, and requirements
- **Actionable**: Provide concrete steps, not just theory
- **Examples**: Real code, workflows, or use cases
- **Machine-Readable**: Use YAML/JSON for data and configuration

### Linking

- Cross-reference related documents
- Use INDEX files for navigation
- Link to relevant examples and code

### What NOT to Include

Avoid extraneous files that don't directly support the skill:

- Auxiliary README files (consolidate into SKILL.md or main README)
- INSTALLATION_GUIDE.md (use QUICK_START.md)
- CHANGELOG.md (use version control)
- Extra documentation that isn't referenced

Keep skills focused: only include files that directly enable Claude's work.

---

## Getting Started

### To Use an Existing Skill

1. Review the skill's [README.md](./skills/)
2. Check [QUICK_START.md](./skills/) for setup
3. Read relevant documentation in \references/\
4. Use examples from \scripts/\ as templates

### To Create a New Skill

1. Review the [template SKILL.md](./template/SKILL.md)
2. Create a new folder: \skills/your-skill-name/\
3. Add \SKILL.md\ with proper frontmatter
4. Create \README.md\ with comprehensive overview
5. Add \references/\ directory for documentation
6. Add \scripts/\ directory with code examples
7. Test the skill with Claude

### Best Practices

- Start with clear, concise descriptions
- Include real-world examples
- Document all thresholds and parameters
- Use machine-readable formats (YAML/JSON) for data
- Keep documentation DRY (Don't Repeat Yourself)
- Link between related documents frequently
- Update documentation when changing behavior

---

## Repository Management

### File Organization

- Avoid duplicate content across skills
- Use INDEX files to guide navigation
- Keep machine-readable data in YAML/JSON
- Document all links and cross-references

### Quality Standards

- All documentation must be accessible and clear
- Code examples should be complete and runnable
- Specifications must include concrete thresholds
- Keep skills self-contained

### Updates

When updating skills:

1. Update relevant documentation in \references/\
2. Update thresholds in YAML format
3. Update code examples in \scripts/\
4. Update repository README if structure changes

---

## Additional Resources

- [Claude Skills Documentation](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Agent Skills Specification](https://agentskills.io/)
- [Template SKILL.md](./template/SKILL.md)

---

**Note**: These skills are provided for demonstration and educational purposes. Always test thoroughly before relying on them for critical work.

**Last Updated**: January 17, 2026
=======
- **`./skills`** - Custom skill implementations
- **`./template`** - Skill template for creating new skills
- **`./spec`** - Agent Skills specification documents

## Creating a New Skill

Skills are simple to create - just a folder with a `SKILL.md` file containing YAML frontmatter and instructions. You can use the template in this repository as a starting point:

    ```markdown
    ---
    name: my-skill-name
    description: A clear description of what this skill does and when to use it
    ---

    # My Skill Name

    [Add your instructions here that Claude will follow when this skill is active]

    ## Examples

    - Example usage 1
    - Example usage 2

    ## Guidelines

    - Guideline 1
    - Guideline 2
    ```

### Frontmatter Requirements

The YAML frontmatter requires only two fields:

- `name` - A unique identifier for your skill (lowercase, hyphens for spaces)
- `description` - A complete description of what the skill does and when to use it

### Skill Anatomy

A complete skill directory structure:

```plaintext
skills/
  my-skill/
    SKILL.md
    references/
    scripts/
    assets/
```

## Skill Guidelines

### When to Include Bundled Resources

#### Scripts (`scripts/`)

Executable code for tasks that require deterministic reliability or are repeatedly rewritten.

- **When to include**: When the same code is being rewritten repeatedly or deterministic reliability is needed
- **Examples**: Python/Bash scripts for file conversion, data processing, API calls
- **Benefits**: Token efficient, deterministic, may be executed without loading into context

#### References (`references/`)

Documentation and reference material intended to be loaded into context as needed.

- **When to include**: For documentation that Claude should reference while working
- **Examples**: Database schemas, API documentation, domain knowledge, company policies
- **Use cases**: Detailed workflow guides, specifications, long reference material
- **Best practice**: If files are large (>10k words), include grep search patterns in SKILL.md

#### Assets (`assets/`)

Files not intended to be loaded into context, but used within the output Claude produces.

- **When to include**: When the skill needs files that will be used in the final output
- **Examples**: Templates (PPTX, DOCX), images, icons, fonts, boilerplate code
- **Use cases**: Files that get copied, modified, or served as output

### What NOT to Include

Do NOT create extraneous documentation or auxiliary files:

- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md
- Other auxiliary context not needed for AI agents to perform the skill

A skill should only contain essential files that directly support its functionality.

## Getting Started

1. Read the [template SKILL.md](./template/SKILL.md) to understand the basic structure
2. Create a new folder in `./skills/` with your skill name
3. Add a `SKILL.md` file with proper frontmatter and instructions
4. Add optional bundled resources if needed (`scripts/`, `references/`, `assets/`)
5. Test your skill with Claude

---

**Note**: These skills are provided for demonstration and educational purposes. Always test skills thoroughly before relying on them for critical tasks.
>>>>>>> 3af9f7c7e9a419d3bbea79495a73b202ec0040c8
