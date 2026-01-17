# Agent Skills Specification

This directory contains documentation about the Agent Skills standard and specification.

For the official specification, visit: https://agentskills.io/

## Overview

Agent Skills is an open standard for packaging and sharing AI agent capabilities through structured, self-contained modules. Skills enable AI agents like Claude to perform specialized tasks by providing:

- Procedural knowledge and workflow guidance
- Integration patterns for tools and APIs
- Domain-specific expertise and best practices
- Reusable scripts, references, and resources

## Key Concepts

### Skill Structure
Each skill is a folder containing:
- `SKILL.md` - Main skill definition with YAML frontmatter and instructions
- Optional `scripts/` - Executable code
- Optional `references/` - Reference documentation
- Optional `assets/` - Output resources (templates, images, etc.)

### YAML Frontmatter
Every SKILL.md requires:
- `name` - Unique skill identifier (lowercase, hyphens for spaces)
- `description` - Complete description of what the skill does and when to use it

### When Skills Are Activated
Claude loads a skill based on the `description` field when:
1. A user asks for help with tasks matching the description
2. The description clearly communicates the skill's purpose and triggers
3. The skill provides relevant procedural knowledge for the requested task

## Best Practices

1. **Keep skills focused** - One skill should address a specific domain or set of related tasks
2. **Write clear descriptions** - Descriptions determine when skills are activated, so be specific about triggers
3. **Organize by context** - Use bundled resources to keep SKILL.md lean
4. **Test thoroughly** - Always validate skills with Claude before distribution
5. **Document workflows** - Provide clear step-by-step procedures for complex tasks

## Resources

- [Official Agent Skills Documentation](https://agentskills.io/)
- [Claude Skills Guide](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Creating Custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)

---

For more information about Agent Skills and the open standard, visit the official specification at https://agentskills.io/
