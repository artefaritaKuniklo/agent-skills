# Agent Skills Repository

This repository contains Agent Skills for Claude. Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.

For more information, check out:

- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Agent Skills specification](https://agentskills.io/)

## Repository Structure

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
