# Clean Code Skill Guide / 《代码整洁之道》技能指南

整洁代码技能指南

This is a comprehensive code quality improvement skill package based on Robert C. Martin's "Clean Code" principles.

基于《代码整洁之道》原则的完整学习与实践包，旨在提升代码质量。

## Package Contents / 包含内容

### Core Files / 核心文件

- **`SKILL.md`** - Main skill documentation with Clean Code principles, best practices, and examples / 主要技能文档，涵盖整洁代码核心原则、最佳实践与实例

- **`CORE_PRACTICES.md`** - Deep dive into core practices and principles / 核心实践与原则深入分析

### Reference Resources / 参考资源

- **`references/code-smells.md`** - Code smell explanations and refactoring techniques / 代码风格解析与重构技术

- **`references/naming-conventions.md`** - Naming convention guides for various programming languages / 各编程语言命名规范指南

### Practical Tools / 实用工具

- **`scripts/analyze_code_quality.py`** - Python code quality analysis script / Python代码质量分析脚本

## Use Cases / 使用场景

### 1. Learning Clean Code Principles / 学习整洁代码原则

Read the core principles section in `SKILL.md` to understand:

- Meaningful Names / 有意义的命名
- Function Design / 函数设计
- Comments / 注释的正确用法
- Error Handling / 错误处理
- Code Smell Identification / 代码风格识别

### 2. Code Review / 代码审查

Use the "Code Review Workflow" section to systematically review code:

1. Check naming clarity / 检查命名清晰度
2. Evaluate function design / 评估函数设计
3. Review comment quality / 审查注释质量
4. Check code formatting / 检查代码格式
5. Evaluate error handling / 评估错误处理
6. Detect code smells / 检测代码风格

### 3. Legacy Code Refactoring / 重构遗留代码

Refer to the "Refactoring Workflow" section:

1. Identify problems in code / 识别代码问题
2. Write tests to ensure functionality / 编写测试确保功能
3. Incrementally refactor / 逐步重构
4. Verify tests pass / 验证测试通过

### 4. Analyze Code Quality / 分析代码质量

Use the Python analysis script:

```bash
# Analyze single file / 分析单个文件
python scripts/analyze_code_quality.py my_module.py

# Analyze entire directory / 分析整个目录
python scripts/analyze_code_quality.py src/
```

The script detects:

- Line length violations / 行长度超限
- Long functions / 函数过长
- Magic numbers / 魔法数字
- Naming violations / 命名违规
- Too many parameters / 参数过多
- Too many return statements / 返回语句过多

### 5. Learn Naming Conventions / 学习命名规范

Consult `references/naming-conventions.md` to learn:

- Python naming conventions / Python 命名规范
- JavaScript/TypeScript naming conventions / JavaScript/TypeScript 命名规范
- Java naming conventions / Java 命名规范
- C# naming conventions / C# 命名规范
- Common naming mistakes / 常见的命名错误

### 6. Understand Code Smells / 深入理解代码风格

See `references/code-smells.md` to learn about:

- Application-level smells / 应用级气味（重复代码、Shotgun Surgery等）
- Class-level smells / 类级气味（大类、过长参数列表等）
- Method-level smells / 方法级气味（长方法、过多参数等）
- Refactoring techniques / 重构技巧

## Recommended Reading Order / 推荐阅读顺序

### Beginner Path / 初学者路径

1. `SKILL.md` - Core principles section / 核心原则部分
2. `CORE_PRACTICES.md` - Master all 6 core skills / 掌握所有6大核心技能
3. `references/naming-conventions.md` - Learn naming conventions / 学习命名规范
4. `references/code-smells.md` - Identify common issues / 识别常见问题

### Practitioner Path / 实践者路径

1. `SKILL.md` - Quick reference / 快速参考
2. `references/code-smells.md` - Identify and fix problems / 识别和修复问题
3. Run `scripts/analyze_code_quality.py` - Automated detection / 自动化检测
4. Use "Code Review Workflow" for team evaluation / 使用"代码审查工作流"进行团队评审

### Mentor/Architect Path / 导师/架构师路径

1. `CORE_PRACTICES.md` - Complete understanding / 完整理解
2. `SKILL.md` - Determine team standards / 确定团队标准
3. All references - Establish coding guidelines / 所有参考资源 - 建立编码指南
4. Customize script - Automate standards enforcement / 定制分析脚本 - 自动化执行标准

## Customizing the Analysis Script / 自定义分析脚本

`analyze_code_quality.py` can be customized as needed. For example:

```python
# Modify line length limit / 修改行长度限制
# Change 120 to your standard in _check_line_length()

# Modify function length limit / 修改函数长度限制
# Change 30 to your standard in _check_function_length()

# Add more checks / 添加更多检查
# Add new _check_* methods to CodeQualityAnalyzer class
```

## Practical Recommendations / 实践建议

### Phases of Applying Clean Code / 应用整洁代码原则的阶段

#### Phase 1: Awareness (Week 1-2) / 第1阶段：意识（Week 1-2）

- [ ] Read `SKILL.md` core principles / 阅读 `SKILL.md` 核心原则
- [ ] Understand code smells / 了解代码风格
- [ ] Start applying principles in code review / 在代码审查中开始应用原则

#### Phase 2: Practice (Week 3-4) / 第2阶段：实践（Week 3-4）

- [ ] Refactor an existing module / 重构一个现有模块
- [ ] Apply principles in new code / 在新代码中应用原则
- [ ] Write tests to support refactoring / 编写测试来支持重构

#### Phase 3: Habit (Month 2+) / 第3阶段：习惯（Month 2+）

- [ ] Integrate principles into daily coding / 将原则融入日常编码
- [ ] Guide others in applying principles / 指导他人应用这些原则
- [ ] Continuously refine and optimize / 不断精进和优化

### Team Implementation / 团队推行

1. **Share Resources** / **共享资源** - Share this skill with your team / 将此skill分享给团队
2. **Regular Discussions** / **定期讨论** - Discuss code smells in team meetings / 在团队会议上讨论代码风格
3. **Code Review** / **代码审查** - Use workflows for systematic review / 使用工作流进行系统化审查
4. **Tool Integration** / **工具集成** - Integrate analysis script in CI/CD / 在CI/CD流程中集成分析脚本
5. **Continuous Improvement** / **持续改进** - Adjust standards based on feedback / 根据实践反馈调整标准

## Code Quality Metrics / 代码质量指标

A codebase following Clean Code principles should have:

| Metric / 指标 | Target / 目标 |
|------|------|
| Average function length / 平均函数长度 | < 20 lines / 行 |
| Function parameters / 函数参数数量 | < 3 |
| Class methods / 类方法数量 | < 15 |
| Code duplication rate / 代码重复率 | < 5% |
| Test coverage / 测试覆盖率 | > 80% |
| Code smell count / 代码风格数量 | Minimize / 最少化 |

## Further Learning / 进一步学习

### Related Books / 相关书籍

1. **Clean Code** - Robert C. Martin (Uncle Bob)
2. **Clean Coder** - Robert C. Martin
3. **Clean Architecture** - Robert C. Martin
4. **Refactoring** - Martin Fowler
5. **Design Patterns** - Gang of Four

### Online Resources / 在线资源

- [Uncle Bob's Blog](https://blog.cleancoder.com/)
- [Code Smell Definition](https://martinfowler.com/bliki/CodeSmell.html)
- [Clean Code Online Course](https://cleancoders.com/)

## Contribution and Feedback / 贡献和反馈

This skill is active and welcomes:

- Improvement suggestions / 提出改进建议
- Successful refactoring case studies / 分享成功的重构案例
- Language-specific best practices / 添加特定语言的最佳实践
- Script improvements / 改进分析脚本
