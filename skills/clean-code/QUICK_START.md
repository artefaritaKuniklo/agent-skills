# Clean Code Skill Quick Start Guide

快速开始指南

## Get Started in 5 Minutes / 5分钟快速上手

### Step 1: Understand What This Is / 1️⃣ 了解是什么
Read the beginning of `SKILL.md` (2-3 minutes):
首阅 `SKILL.md` 序言部分（2-3分钟）：
- What is Clean Code / 什么是Clean Code
- When to Use This Skill / 何时使用此Skill

### Step 2: Learn the 6 Core Principles / 2️⃣ 学习6大原则
Check the "Core Principles" section in `SKILL.md`:
`SKILL.md` 之"核心原则"部分含：
1. **Meaningful Names** - Spend time choosing good names / **有意义的命名** - 花时间起好名字
2. **Functions** - Keep them small and focused / **函数** - 保持小而专注
3. **Comments** - Explain WHY, not WHAT / **注释** - 解释WHY，不是WHAT
4. **Formatting** - Stay consistent / **格式化** - 保持一致
5. **Error Handling** - Use exceptions / **错误处理** - 使用异常
6. **Code Smells** - Recognize problem signals / **代码气味** - 识别问题信号

### Step 3: Apply in Practice / 3️⃣ 运用到实践
Choose one approach:
择其一而行之：

#### Approach A: Code Review / 方式A：代码审查
Use the "Code Review Workflow" to review code:
采用"代码审查工作流"以系统检视代码
```
1. Check if names are clear / 检查名字是否清晰
2. Evaluate if functions are too large / 评估函数是否太大
3. Review comment quality / 审查注释质量
4. Check formatting consistency / 检查格式一致性
5. Evaluate error handling / 评估错误处理
6. Identify code smells / 识别代码气味
```

#### Approach B: Automated Detection / 方式B：自动化检测
```bash
python scripts/analyze_code_quality.py your_code.py
```

#### Approach C: Learn Specific Standards / 方式C：学习具体规范
- Python/JS developers → See `references/naming-conventions.md` / Python/JS开发者 → 查看 `references/naming-conventions.md`
- Want to refactor code → See `references/code-smells.md` / 要重构代码 → 查看 `references/code-smells.md`

---

## Quick Reference: Core Concepts / 核心概念速查表

### Good Function / 好的函数
```python
# Good: Small, meaningful name / 好：小、有意义
def process_payment(order):
    validate_order(order)
    calculate_total(order)
    charge_card(order)
```

### Bad Function / 坏的函数
```python
# Bad: Too many parameters, unclear names / 坏：太多参数，名字不清楚
def p(o, f1, f2, f3):
    # 100 lines doing multiple things / 100行代码...做很多事
```

### Good Naming / 好的命名
```python
is_active = True              # Clear boolean / 清晰的布尔变量
get_user_count()              # Clear function name / 清晰的函数名
MAX_RETRY_ATTEMPTS = 3        # Clear constant / 清晰的常量
```

### Bad Naming / 坏的命名
```python
a = True                      # Meaningless / 无意义
u = get(1)                    # Too short / 太短
5  # in code directly         # Magic number / 魔法数字
```

### Good Error Handling / 好的错误处理
```python
if not is_valid(data):
    raise ValidationError("Invalid data")
```

### Bad Error Handling / 坏的错误处理
```python
if is_valid(data):
    return True
else:
    return False
```

---

## Code Review Checklist / 代码审查检查清单

When reviewing code, quickly check these 5 points:
代码审查时，速检此五点：

- [ ] **Names** - Are names clear and reveal intent? / **Names** - 名字是否清晰表达意图？
- [ ] **Functions** - Are functions focused on a single task? / **Functions** - 函数是否专注于单一任务？
- [ ] **Comments** - Do comments explain WHY? / **Comments** - 注释是否解释WHY？
- [ ] **Format** - Is the style consistent? / **Format** - 风格是否一致？
- [ ] **Errors** - Are exceptions used for error handling? / **Errors** - 是否使用异常处理？

---

## Common Code Smells Quick Reference / 常见代码气味速查

| Problem / 问题 | Sign / 表现 | Solution / 解决方案 |
|------|------|---------|
| Duplicated Code / 重复代码 | Same code appears multiple times / 相同的代码出现多次 | Extract to shared function / 提取到共享函数 |
| Long Function / 长函数 | Function exceeds 20-30 lines / 函数超过20-30行 | Break into smaller functions / 分解成小函数 |
| Long Parameter List / 长参数列表 | More than 3 parameters / 超过3个参数 | Group parameters into object / 用对象分组参数 |
| Magic Numbers / 魔法数字 | Numbers directly in code / 直接在代码中的数字 | Extract as named constant / 提取为命名常量 |
| Large Class / 大类 | Class has too many responsibilities / 类有太多职责 | Break into focused classes / 分解成多个专注的类 |

---

## Naming Standards by Language / 按语言的命名规范速查

### Python
```python
my_variable = "value"        # Variables: snake_case / 变量: snake_case
def my_function():           # Functions: snake_case / 函数: snake_case
class MyClass:               # Classes: PascalCase / 类: PascalCase
MAX_SIZE = 100              # Constants: UPPER_SNAKE_CASE / 常量: UPPER_SNAKE_CASE
_private_var = 5            # Private: _leading_underscore / 私有: _leading_underscore
```

### JavaScript
```javascript
const myVariable = "value"   // Variables: camelCase / 变量: camelCase
function myFunction() {}     // Functions: camelCase / 函数: camelCase
class MyClass {}             // Classes: PascalCase / 类: PascalCase
const MAX_SIZE = 100         // Constants: UPPER_SNAKE_CASE / 常量: UPPER_SNAKE_CASE
const _privateVar = 5        // Private: _leading_underscore / 私有: _leading_underscore
```

### Java
```java
String myVariable = "value"  // Variables: camelCase / 变量: camelCase
void myMethod() {}           // Methods: camelCase / 方法: camelCase
class MyClass {}             // Classes: PascalCase / 类: PascalCase
static final int MAX_SIZE    // Constants: UPPER_SNAKE_CASE / 常量: UPPER_SNAKE_CASE
private String value;        // Private: private keyword / 私有: private keyword
```

### C#
```csharp
string myVariable = "value"  // Variables: camelCase / 变量: camelCase
void MyMethod() {}           // Methods: PascalCase / 方法: PascalCase
class MyClass {}             // Classes: PascalCase / 类: PascalCase
const int MaxSize = 100      // Constants: PascalCase / 常量: PascalCase
private string value;        // Private: private keyword / 私有: private keyword
```

---

## Command Reference / 命令速查

### Analyze Code Quality / 分析代码质量
```bash
# Analyze single file / 单个文件
python scripts/analyze_code_quality.py my_file.py

# Analyze entire directory / 整个目录
python scripts/analyze_code_quality.py src/

# Output: Issues and suggestions by line number / 输出: 按行号显示问题和建议
```

### Find Specific Content / 查看特定内容
```
Need multi-language naming standards? / 需要学习多语言命名规范?
→ Open references/naming-conventions.md / → 打开 references/naming-conventions.md

Need code smells and refactoring? / 需要了解代码气味和重构?
→ Open references/code-smells.md / → 打开 references/code-smells.md

Need quick principle reference? / 需要快速参考原则?
→ Check "Core Principles" in SKILL.md / → 查看 SKILL.md 的"核心原则"部分

Need deep understanding? / 需要深入理解核心实践?
→ Read CORE_PRACTICES.md / → 阅读 CORE_PRACTICES.md
```

---

## Start Your Journey / 从今天开始

### Day 1: Learn / 第1天：学习
- Spend 15 minutes reading the first two principles in `SKILL.md` / 花15分钟读 `SKILL.md` 的前两个原则
- Look at examples showing before/after improvements / 看一个例子，了解改进前后的差异

### Day 2: Apply / 第2天：应用
- Use the 5-point checklist in a code review / 在代码审查中应用"5点检查清单"
- Identify 1-2 code smells in existing code / 识别代码中的1-2个气味

### Day 3: Practice / 第3天：实践
- Refactor a small function / 重构一个小函数
- Improve its naming and length / 改进其命名和长度

### Week 1: Master / 第1周：掌握
- Read through `SKILL.md` completely / 完整读一遍 `SKILL.md`
- Collect code smells from your own code / 收集自己写的代码中的气味
- Conduct a systematic code review / 系统地进行一次代码审查

### Month 1+: Habit / 第1月：习惯化
- Apply principles in daily coding / 在日常编码中应用这些原则
- Guide teammates in improving their code / 指导同事改进他们的代码
- Integrate automation tools into your workflow / 自动化工具集成到工作流

---

## Deep Learning Resources / 如果你想深入学习

| Goal / 目标 | Resource / 资源 |
|------|------|
| Understand Core Practices | Read CORE_PRACTICES.md / 阅读 CORE_PRACTICES.md |
| Master refactoring techniques | See examples in references/code-smells.md / 查看 references/code-smells.md 中的例子 |
| Language-specific standards | See references/naming-conventions.md / 查看 references/naming-conventions.md |
| Automated detection | Study scripts/analyze_code_quality.py / 学习 scripts/analyze_code_quality.py |
| Deeper understanding | Purchase and read the Clean Code book / 购买《Clean Code》原书 |

---

## Five Golden Rules / 记住这5个金律

1. Names are important / **名字很重要** - Spend time choosing good names / 花时间起好名字
2. Functions should be small / **函数越小越好** - One function, one task / 一个函数做一件事
3. Comments explain WHY / **注释解释WHY** - Code explains WHAT / 代码说WHAT
4. Style should be consistent / **风格要一致** - Small things, big impact / 小事情，大影响
5. Use exceptions / **错误用异常** - Clear and cannot be ignored / 明确且不可忽视

---

## FAQ / 常见问题

**Q: What should I read first? / Q: 我应该先读哪个文件?**
A: Start with `README.md` and choose the path that suits you / A: 从 `README.md` 开始，选择适合你的路径

**Q: How do I apply this in my project? / Q: 如何在我的项目中使用这个skill?**
A: See the "Use Cases" section in `README.md` / A: 参考 `README.md` 的"使用场景"部分

**Q: What languages does this skill support? / Q: 这个skill支持哪些语言?**
A: All languages. See `references/naming-conventions.md` for specific standards / A: 主要用Python示例，但原则适用所有语言。查看 `references/naming-conventions.md` 了解更多

**Q: How do I automatically detect code issues? / Q: 如何自动检测代码问题?**
A: Run: python scripts/analyze_code_quality.py / A: 运行 `python scripts/analyze_code_quality.py`

**Q: How detailed is this skill? / Q: 这个skill有多详细?**
A: 7600+ lines of documentation and code, from beginner to mastery / A: 7600+行文档和代码，适合从入门到精通
