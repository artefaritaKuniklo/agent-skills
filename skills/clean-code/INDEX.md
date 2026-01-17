# Clean Code Skill File Index / 整洁代码索引

## Quick Navigation / 快速导航

### Find Files by Your Needs / 按需快速定位

#### I'm a Beginner and Want to Learn Clean Code / 初学者学习整洁代码
```
1. Start: QUICK_START.md (5-minute quick start / 五分钟快速上手)
2. Deep Dive: README.md (Beginner Path / 初学路径)
3. Detailed: SKILL.md (Core Principles / 核心原则)
4. Core Practices: CORE_PRACTICES.md / 核心实践分析
```

#### I Need to Conduct Code Reviews / 代码审查需求
```
1. Workflow: SKILL.md → "Code Review Workflow / 代码审查流程"
2. Checklist: QUICK_START.md → "Code Review Checklist / 审查清单"
3. Reference: code-smells.md (Identify Problems / 问题识别)
4. Tool: analyze_code_quality.py (Automated Detection / 自动检测)
```

#### I Need to Refactor Legacy Code / 重构遗留代码
```
1. Workflow: SKILL.md → "Refactoring Workflow / 重构流程"
2. Smell Identification: code-smells.md (All Smells and Solutions / 气味与解决方案)
3. Tool Support: analyze_code_quality.py
4. Deep Understanding: CORE_PRACTICES.md → Error Handling & Smells / 错误处理与代码气味
```

#### I Need to Learn Naming Conventions / 学习命名规范
```
1. Python: naming-conventions.md → Python Section / Python部分
2. JavaScript: naming-conventions.md → JavaScript Section / JavaScript部分
3. Java: naming-conventions.md → Java Section / Java部分
4. C#: naming-conventions.md → C# Section / C#部分
5. Bad Patterns: naming-conventions.md → Patterns to Avoid / 避免模式
6. Checklist: naming-conventions.md → End of File / 文件末尾
```

#### I Want to Implement Clean Code in My Team / 团队推行整洁代码
```
1. Understand: CORE_PRACTICES.md (Deep Understanding / 深入理解)
2. Implementation Plan: README.md → "Team Implementation / 团队实施"
3. Standard Documentation: SKILL.md (Team Reference / 团队参考)
4. Automation: analyze_code_quality.py (Integrate CI/CD / 集成CI/CD)
```

---

## Complete File Reference / 完整文件说明

### Getting Started Files / 入门文件

#### QUICK_START.md (Quick Start Guide / 快速开始指南)
- **Length:** ~500 lines / ~500行
- **Reading Time:** 5-15 minutes / 5-15分钟
- **Difficulty:** ⭐ Easy / 简单
- **Content / 内容:**
  - 5-minute quick start / 5分钟快速上手
  - Core concepts quick reference / 核心概念速查表
  - Code review checklist / 代码审查检查清单
  - Common smell quick reference / 常见气味速查
  - Naming convention quick reference / 命名规范速查
  - Action plan for starting today / 从今天开始的行动计划

**When to Read / 何时阅读:** 
- [ ] First time using this skill / 第一次接触此skill
- [ ] Need quick lookup / 需要快速查阅
- [ ] Want to apply immediately / 想立即应用

---

### Core Files / 核心文件

#### SKILL.md (Main Skill Definition / 主要技能定义)
- **Length:** ~3500 lines / ~3500行
- **Reading Time:** 1-2 hours / 1-2小时
- **Difficulty:** ⭐⭐ Intermediate / 中等
- **Content / 内容:**
  - When to use this skill / 何时使用此Skill
  - 6 Core Principles (detailed) / 6大核心原则（详细展开）
  - Code Review Workflow / 代码审查工作流
  - Refactoring Workflow / 重构工作流
  - 2 Real-world Examples / 2个实战案例
  - Resource Guide / 资源指南

**When to Read / 何时阅读:**
- [ ] Want comprehensive understanding of principles / 想全面了解原则
- [ ] Conducting code reviews / 进行代码审查
- [ ] Need concrete examples / 需要具体例子

**Main Sections / 主要部分:**
1. Core Principles (6 sections, each with code examples / 6个，每个含代码例子)
2. Workflow: Code Review (5 steps / 5步)
3. Workflow: Refactoring (4 steps / 4步)
4. Examples (2 complex cases / 2个复杂案例)

---

### Reference Files / 参考文件

#### CORE_PRACTICES.md (Core Practices Deep Analysis / 核心实践深入分析)
- **Length:** ~1500 lines / ~1500行
- **Reading Time:** 1-1.5 hours / 1-1.5小时
- **Difficulty:** ⭐⭐ Intermediate / 中等
- **Content / 内容:**
  - Foundation (why clean code matters / 为什么重要) / 基础
  - 6 Core Skills with detailed explanations and examples / 6大核心技能
  - Core Design Principles / 核心设计原则
  - How skills work together / 技能协同方式
  - 5 Code Review Questions / 5大审查问题
  - From Theory to Practice / 从理论到实践

**When to Read / 何时阅读:**
- [ ] Want mastery of core practices / 想掌握核心实践
- [ ] Need understanding for code review / 进行代码审查需要了解
- [ ] Establishing team standards / 为团队建立标准

**Six Core Skills / 六大核心技能:**
- Skill 1: Meaningful Names / 掌握有意义的命名
- Skill 2: Small Focused Functions / 设计精小而专注的函数
- Skill 3: Comment Well / 恰当地编写注释
- Skill 4: Consistent Formatting / 代码格式的一致性
- Skill 5: Master Error Handling / 掌握错误处理
- Skill 6: Recognize Code Smells / 识别和重构代码气味

---

#### code-smells.md (Complete Code Smells Guide / 代码气味完全指南)
- **Length:** ~1000 lines / ~1000行
- **Reading Time:** 45 minutes to 1 hour / 45分钟到1小时
- **Difficulty:** ⭐⭐⭐ Advanced / 进阶
- **Content / 内容:**
  - Application-level Smells (2) / 应用级气味（2个）
  - Class-level Smells (6) / 类级气味（6个）
  - Method-level Smells (3) / 方法级气味（3个）
  - Refactoring Smells (4) / 重构气味（4个）
  - Each smell includes / 每个气味包含:
    - Description and examples / 描述和例子
    - Why it's bad / 为什么不好
    - Refactoring techniques / 重构技术
    - Code comparison / 代码对比

**When to Read / 何时阅读:**
- [ ] Identify problems in code / 识别代码中的问题
- [ ] Learn refactoring techniques / 学习重构技巧
- [ ] Conduct in-depth code reviews / 进行深入的代码审查
- [ ] Reference guide for refactoring / 作为重构的参考

**Quick Lookup / 快速查找:**
- Duplicated Code (Application-level / 应用级)
- Large Class / God Class (Class-level / 类级)
- Long Method (Method-level / 方法级)
- Too Many Parameters (Multiple levels / 多个级别)
- Shotgun Surgery (Refactoring-level / 重构级)

---

#### naming-conventions.md (Multi-language Naming Standards / 多语言命名规范)
- **Length:** ~700 lines / ~700行
- **Reading Time:** 30-45 minutes / 30-45分钟
- **Difficulty:** ⭐ Easy / 简单
- **Content / 内容:**
  - Universal Principles (8) / 通用原则（8个）
  - Python Standards / Python 规范
  - JavaScript Standards / JavaScript 规范
  - Java Standards / Java 规范
  - C# Standards / C# 规范
  - Each language includes / 每种语言包含:
    - Variables, functions, classes, constants / 变量、函数、类、常量
    - Private members, boolean variables / 私有成员、布尔变量
    - Concrete examples / 具体例子

- **5 Bad Patterns to Avoid (with examples / 带示例)** / 5个要避免的坏模式
- **Naming Quality Checklist / 命名质量检查清单**
- **Standards Comparison Table / 规范对比表**

**When to Read / 何时阅读:**
- [ ] Learn specific language standards / 学习特定语言的规范
- [ ] Review variable and function names / 审查变量和函数名
- [ ] Establish team naming standards / 建立团队命名标准
- [ ] Quick lookup for specific concepts / 快速查阅某个概念

---

### Tool Files / 工具文件

#### analyze_code_quality.py (Code Quality Analysis Script / 代码质量分析脚本)
- **Length:** ~500 lines / ~500行
- **Language:** Python 3
- **Dependencies:** None (Standard Library only / 无依赖，仅标准库)
- **Detection Items / 检测项:**
  - Line length (Recommended ≤ 120 / 推荐 ≤ 120)
  - Function length (Recommended ≤ 30 lines / 推荐 ≤ 30行)
  - Magic numbers / 魔法数字
  - Naming violations / 命名违规
  - Too many parameters (Recommended ≤ 3 / 推荐 ≤ 3个)
  - Too many return statements / 返回语句过多
  - Duplicate code patterns / 重复代码模式

**Usage / 使用方法:**
```bash
# Analyze single file / 分析单个文件
python analyze_code_quality.py my_module.py

# Analyze entire directory / 分析整个目录
python analyze_code_quality.py src/
```

**Output / 输出:**
- Issues list (Organized by file / 按文件组织)
- Line numbers and severity levels / 行号和严重级别
- Specific suggestions / 具体建议

---

### Documentation Files / 文档文件

#### README.md (Usage Guide / 使用指南)
- **Length:** ~400 lines / ~400行
- **Reading Time:** 15-20 minutes / 15-20分钟
- **Difficulty:** ⭐ Easy / 简单
- **Content / 内容:**
  - Contents Checklist / 包含内容清单
  - 5 Use Cases / 5种使用场景
  - 3 Recommended Paths (Beginner/Practitioner/Mentor / 初学者/实践者/导师) / 3条推荐路径
  - Script Customization / 脚本自定义
  - Phased Practice / 分阶段实践
  - Code Quality Metrics / 代码质量指标
  - Further Learning Resources / 进一步学习资源

**When to Read / 何时阅读:**
- [ ] First time using this skill / 第一次使用此skill
- [ ] Unsure how to start / 不确定如何开始
- [ ] Want to understand the big picture / 想了解全局

---

#### PROJECT_SUMMARY.md (Project Completion Summary / 项目完成总结)
- **Length:** ~600 lines / ~600行
- **Reading Time:** 20-30 minutes / 20-30分钟
- **Difficulty:** ⭐⭐ Intermediate / 中等
- **Content / 内容:**
  - Complete directory structure / 完整的目录结构
  - Detailed file descriptions / 每个文件的详细说明
  - Content creation statistics / 创建的内容统计
  - Clean Code 6 Core Principles Summary / Clean Code 6大原则总结
  - Document statistics table / 文档统计表
  - Project highlights / 项目亮点
  - Usage recommendations / 使用建议

**When to Read / 何时阅读:**
- [ ] Understand the entire project / 了解整个项目构成
- [ ] Review project completeness / 审视项目完整性
- [ ] Plan your learning path / 规划学习路径

---

## File Statistics Overview / 文件统计总览

| File / 文件 | Type / 类型 | Lines / 行数 | Purpose / 用途 | Difficulty / 难度 |
|------|------|------|------|------|
| QUICK_START.md | Getting Started / 入门 | 500 | Quick Start / 快速开始 | ⭐ |
| README.md | Guide / 指南 | 400 | Usage Instructions / 使用说明 | ⭐ |
| SKILL.md | Core / 核心 | 3500 | Principles and Workflows / 原则和工作流 | ⭐⭐ |
| CORE_PRACTICES.md | Reference / 参考 | 1500 | Core Practices Analysis / 核心实践分析 | ⭐⭐ |
| code-smells.md | Reference / 参考 | 1000 | Smell Identification and Refactoring / 气味识别和重构 | ⭐⭐⭐ |
| naming-conventions.md | Reference / 参考 | 700 | Multi-language Naming / 多语言命名 | ⭐ |
| analyze_code_quality.py | Tool / 工具 | 500 | Automated Detection / 自动检测 | ⭐⭐ |
| PROJECT_SUMMARY.md | Documentation / 文档 | 600 | Project Summary / 项目总结 | ⭐⭐ |
| **Total / 总计** | - | **8700+** | **Complete Package / 完整包** | - |

---

## Recommended Reading Order / 推荐阅读顺序

### Scenario 1: I Only Have 15 Minutes / 我只有15分钟
```
QUICK_START.md → Code Review Checklist / 代码审查检查清单
↓
Apply to your next code review / 应用到下一个代码审查
```

### Scenario 2: I Have 1 Hour / 我有1小时
```
QUICK_START.md (15 minutes / 分钟)
↓
SKILL.md Core Principles Section (30 minutes / 分钟)
↓
Choose 1 reference file (15 minutes / 分钟)
```

### Scenario 3: I Have Half a Day / 我有半天时间
```
README.md Recommended Path (Choose one / 选择一条)
↓
SKILL.md (Complete / 完整) (2 hours / 小时)
↓
1-2 Reference Files (1 hour / 小时)
↓
Run analysis script on your own code / 在自己的代码上运行分析脚本
```

### Scenario 4: I Want to Establish Team Standards / 我要建立团队标准
```
CORE_PRACTICES.md (Deep Understanding / 深入理解)
↓
SKILL.md (Complete Learning / 完整学习)
↓
All Reference Files (As Standards / 作为标准)
↓
Integrate analyze_code_quality.py
↓
Share with team and discuss / 与团队分享并讨论
```

---

## Find Answers by Question / 按问题查找答案

| Question / 问题 | Answer Located In / 答案在这里 |
|------|-----------|
| How should I name variables? / 我应该如何命名变量？ | naming-conventions.md |
| How many lines should a function have? / 函数应该有多少行？ | SKILL.md + QUICK_START.md |
| When should I write comments? / 什么时候写注释？ | SKILL.md or CORE_PRACTICES.md / 或 |
| What problems does my code have? / 代码有什么问题？ | code-smells.md or analyze_code_quality.py / 或 |
| How do I conduct code reviews? / 如何进行代码审查？ | SKILL.md Workflow Section + QUICK_START.md Checklist / 工作流部分 + 检查清单 |
| How do I refactor code? / 如何重构代码？ | SKILL.md Refactoring Workflow + code-smells.md / 重构工作流 + |
| Why is clean code important? / 整洁代码为什么重要？ | CORE_PRACTICES.md Foundation Section / 基础部分 |
| How do I automatically detect issues? / 如何自动检测问题？ | analyze_code_quality.py Usage Instructions / 使用说明 |
| Which language standards should I follow? / 我选择哪种语言的规范？ | naming-conventions.md Select Your Language / 中选择你的语言 |
| Where should I start? / 我该从哪里开始？ | README.md Recommended Paths / 推荐路径 |

---

## Usage Tips / 使用技巧

### Tip 1: Common Queries / 常见查询
Save these links for quick reference / 保存以下链接以便快速查询：
- Quick Start / 快速开始: QUICK_START.md
- Checklist / 检查清单: QUICK_START.md → Checklist / 检查清单
- My Language Standards / 我的语言规范: naming-conventions.md

### Tip 2: Share with Team / 团队分享
- Beginners / 初学者: Share QUICK_START.md / 分享
- Reviewers / 审查人员: Share SKILL.md + code-smells.md / 分享
- Architects / 架构师: Share CORE_PRACTICES.md / 分享
- Automation / 自动化: Share analyze_code_quality.py / 分享

### Tip 3: Integrate into Workflow / 集成工作流
```bash
# Run before commit / 在提交前运行
python scripts/analyze_code_quality.py .

# Use in CI/CD / 在CI/CD中使用
# See README.md Integration Suggestions / 参考集成建议
```

### Tip 4: Regular Review / 定期回顾
- Week 1 / 第1周: Read QUICK_START.md / 读
- Week 2 / 第2周: Read SKILL.md Core Principles / 读核心原则
- Week 3 / 第3周: Practice Code Review Workflow / 实践工作流
- Week 4+ / 第4周以后: Deep dive into reference files / 深入学习参考文件

---

## Need Help? / 需要帮助？

| Situation / 情况 | See File / 查看文件 |
|------|---------|
| Complete Beginner / 完全新手 | README.md Beginner Path + QUICK_START.md / 初学者路径 + |
| Want Quick Application / 想快速应用 | QUICK_START.md Checklist / 检查清单 |
| Need Detailed Examples / 需要详细例子 | SKILL.md Examples + code-smells.md / 例子 + |
| Need Automation Tool / 需要自动化工具 | analyze_code_quality.py |
| Need Team Standards / 需要建立团队标准 | README.md Team Implementation + CORE_PRACTICES.md / 团队推行 + |

---

**This index helps you quickly find what you need.** / 这个索引帮助你快速找到所需的内容。
