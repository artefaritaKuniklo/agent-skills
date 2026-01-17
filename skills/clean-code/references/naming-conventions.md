# Naming Conventions Reference

Clear names reveal intent and reduce need for comments.

## Universal Principles

1. Pronounceable - Avoid cryptic abbreviations
2. Reveal intent - Answer why something exists
3. Avoid disinformation - Don't use misleading names
4. Make distinctions meaningful - Different names = different things
5. Searchable names - No single-letter variables
6. Avoid type encoding - Let type systems handle types
7. Domain language - Use business domain terms
8. One word per concept - Be consistent

## Language Conventions

**Python**
- Variables/Functions: snake_case
- Classes: PascalCase  
- Constants: UPPER_CASE
- Private: _leading_underscore
- Boolean: is_*, has_*, can_*

**JavaScript/TypeScript**
- Variables/Functions: camelCase
- Classes: PascalCase
- Constants: UPPER_CASE
- Private: _leading_underscore
- Boolean: isActive, hasPermission

**Java**
- Variables/Methods: camelCase
- Classes: PascalCase
- Constants: UPPER_CASE
- Interfaces: I prefix
- Boolean: isValid, hasPermission

**C#**
- Variables: camelCase
- Classes/Properties: PascalCase
- Constants: PascalCase
- Private: _underscore_prefix
- Interfaces: I prefix
