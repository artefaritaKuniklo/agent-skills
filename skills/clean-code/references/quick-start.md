# Clean Code Skill: Quick Start Guide

## Get Started in 5 Minutes

### Step 1: Understand What This Is
Read the beginning of this document (2-3 minutes) and the overview section in SKILL.md.

### Step 2: Learn the 6 Core Principles
Check the "Core Principles" section in SKILL.md:
1. Meaningful Names - Spend time choosing good names
2. Functions - Keep them small and focused
3. Comments - Explain WHY, not WHAT
4. Formatting - Stay consistent
5. Error Handling - Use exceptions
6. Code Smells - Recognize problem signals

### Step 3: Apply in Practice
Choose one approach:

#### Approach A: Code Review
Use the "Code Review Workflow" to review code systematically:

- Check if names are clear
- Evaluate if functions are too large
- Review comment quality
- Check formatting consistency
- Evaluate error handling
- Identify code smells

#### Approach B: Automated Detection
```bash
python scripts/analyze_code_quality.py your_code.py
```

#### Approach C: Learn Specific Standards
- Python/JavaScript developers -> See naming-conventions.md
- Want to refactor code -> See code-smells.md

---

## Quick Reference: Core Concepts

### Good Function
```python
# Good: Small, meaningful name
def process_payment(order):
    validate_order(order)
    calculate_total(order)
    charge_card(order)
```

### Bad Function
```python
# Bad: Too many parameters, unclear names
def p(o, f1, f2, f3):
    # 100 lines doing multiple things
```

### Good Naming
```python
is_active = True              # Clear boolean
get_user_count()              # Clear function name
MAX_RETRY_ATTEMPTS = 3        # Clear constant
```

### Bad Naming
```python
a = True                      # Meaningless
u = get(1)                    # Too short
5                             # Magic number in code
```

### Good Error Handling
```python
if not is_valid(data):
    raise ValidationError("Invalid data")
```

### Bad Error Handling
```python
if is_valid(data):
    return True
else:
    return False
```

---

## Code Review Checklist

When reviewing code, quickly check these 5 points:

- Names - Are names clear and reveal intent?
- Functions - Are functions focused on a single task?
- Comments - Do comments explain WHY?
- Format - Is the style consistent?
- Errors - Are exceptions used for error handling?

---

## Common Code Smells Quick Reference

| Problem | Sign | Solution |
|---------|------|----------|
| Duplicated Code | Same code appears multiple times | Extract to shared function |
| Long Function | Function exceeds 20-30 lines | Break into smaller functions |
| Long Parameter List | More than 3 parameters | Group parameters into object |
| Magic Numbers | Numbers directly in code | Extract as named constant |
| Large Class | Class has too many responsibilities | Break into focused classes |

---

## Naming Standards by Language

### Python
```python
my_variable = "value"        # Variables: snake_case
def my_function():           # Functions: snake_case
class MyClass:               # Classes: PascalCase
MAX_SIZE = 100              # Constants: UPPER_SNAKE_CASE
_private_var = 5            # Private: _leading_underscore
```

### JavaScript
```javascript
const myVariable = "value"   // Variables: camelCase
function myFunction() {}     // Functions: camelCase
class MyClass {}             // Classes: PascalCase
const MAX_SIZE = 100         // Constants: UPPER_SNAKE_CASE
const _privateVar = 5        // Private: _leading_underscore
```

### Java
```java
String myVariable = "value"  // Variables: camelCase
void myMethod() {}           // Methods: camelCase
class MyClass {}             // Classes: PascalCase
static final int MAX_SIZE    // Constants: UPPER_SNAKE_CASE
private String value;        // Private: private keyword
```

### C#
```csharp
string myVariable = "value"  // Variables: camelCase
void MyMethod() {}           // Methods: PascalCase
class MyClass {}             // Classes: PascalCase
const int MaxSize = 100      // Constants: PascalCase
private string value;        // Private: private keyword
```

---

## Command Reference

### Analyze Code Quality
```bash
# Analyze single file
python scripts/analyze_code_quality.py my_file.py

# Analyze entire directory
python scripts/analyze_code_quality.py src/

# Output: Problems and suggestions by line number
```

### Find Specific Content
```
Need multi-language naming standards?
-> See naming-conventions.md

Need to understand code smells and refactoring?
-> See code-smells.md

Need Clean Code core practices analysis?
-> See CORE_PRACTICES.md
```

---

## Start Your Journey

### Day 1: Learn
- Spend 15 minutes reading the first two principles in SKILL.md
- Look at examples showing before/after improvements

### Day 2: Apply
- Use the 5-point checklist in a code review
- Identify 1-2 code smells in existing code

### Day 3: Practice
- Refactor a small function
- Improve its naming and length

### Week 1: Master
- Read through SKILL.md completely
- Collect code smells from your own code
- Conduct a systematic code review

### Month 1+: Habit
- Apply principles in daily coding
- Guide teammates in improving their code
- Integrate automation tools into your workflow

---

## Deep Learning Resources

| Goal | Resource |
|------|----------|
| Learn about Core Practices | Read CORE_PRACTICES.md introduction |
| Master refactoring techniques | See examples in code-smells.md |
| Language-specific standards | See naming-conventions.md |
| Automated detection | Study scripts/analyze_code_quality.py |
| Deeper understanding | Read the Clean Code book |

---

## Five Golden Rules

1. Names are important - Spend time choosing good names
2. Functions should be small - One function, one task
3. Comments explain WHY - Code explains WHAT
4. Style should be consistent - Small things, big impact
5. Use exceptions - Clear and cannot be ignored

---

## FAQ

Q: What should I read first?
A: Start with the overview in SKILL.md, then read "Core Principles"

Q: How do I apply this in my project?
A: Follow the code review and refactoring workflows in SKILL.md

Q: What languages does this skill support?
A: Principles apply to all languages. See naming-conventions.md for specific standards

Q: How do I automatically detect code issues?
A: Run: python scripts/analyze_code_quality.py

Q: How long does it take to learn?
A: Quick start = 5 minutes, Full learning = 1-2 hours, Mastery = ongoing practice
