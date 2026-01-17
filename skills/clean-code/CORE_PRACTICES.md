# Clean Code: Core Practices

## Why Clean Code Matters

Code is read far more than written. Prioritize readability and maintainability.

- Reduces maintenance costs
- Enables team productivity  
- Technical debt from poor code accumulates and compounds

## 6 Core Skills

### Skill 1: Meaningful Names

Most important skill for readable code.

**8 Core Principles:**
1. Reveal intent - names should answer WHY it exists
2. Avoid disinformation - don't use confusing names like `l` or `O`
3. Make meaningful distinctions - avoid `a1, a2, a3` or meaningless suffixes
4. Use pronounceable names - enables team discussion
5. Use searchable names - avoid single-letter variables
6. Avoid encoding - don't include type info in names
7. Class names use nouns: `Customer`, `Account`
8. Method names use verbs: `postPayment()`, `getData()`

### Skill 2: Small, Focused Functions

**Golden Rules:**
- Keep functions small (10-20 lines, fit on screen)
- Single responsibility - do one thing well
- Minimize parameters: 0 ideal, 1 good, 2 acceptable, 3+ refactor
- Avoid side effects - name should describe behavior
- Use exceptions, not error codes
- Don't repeat yourself (DRY principle)

### Skill 3: Comments

Good code needs few comments. Comments explain WHY, not WHAT.

**Avoid:** What-code-does, redundant text, commented-out code, change history
**Include:** Why decisions made, non-obvious consequences, warnings, legal info

### Skill 4: Formatting

Formatting shows respect for code. Choose conventions and follow consistently.

**Key principles:** Keep lines 80-120 chars, use consistent indentation, separate logical groups with blank lines, organize imports logically, place variables near usage

### Skill 5: Error Handling

Handle errors explicitly and clearly.

**Key principles:** Use exceptions not codes, provide context in exceptions, avoid null (use exceptions or special objects), define clear error types, don't silently ignore errors

### Skill 6: Recognize & Refactor Code Smells / 第六技能：识别和重构代码气味

A code smell is a surface-level indicator of deeper design problems.

代码气味乃设计缺陷之先兆。

### Skill 6: Code Smells

Recognize patterns that indicate refactoring needs:

- **Duplicated Code** - Extract to shared functions
- **Long Methods** - Split into focused functions (10-20 lines max)
- **Long Parameter Lists** - Group into objects
- **Magic Numbers** - Use named constants
- **Large Classes** - Split into focused classes
- **Shotgun Surgery** - One change affects many files (bad cohesion)
