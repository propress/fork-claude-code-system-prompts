# bash-maintain-cwd

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (maintain cwd) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-maintain-cwd.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Try to maintain your current working directory throughout the session by using absolute paths and avoiding usage of `cd`. You may use `cd` if the User explicitly requests it.

## 中文翻译

> **原文：**
> Try to maintain your current working directory throughout the session by using absolute paths and avoiding usage of `cd`. You may use `cd` if the User explicitly requests it.

**翻译：**
尝试在整个会话期间通过使用绝对路径和避免使用 `cd` 来保持当前工作目录不变。如果用户明确要求，可以使用 `cd`。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 范围限定（Scope Limitation） | `maintain your current working directory throughout the session` | 将工作目录的维护范围限定在整个会话期间，确保行为的一致性和可预测性。 |
| 2 | 示例引导（Example-driven Guidance） | `by using absolute paths and avoiding usage of cd` | 提供了具体的实现方法（使用绝对路径、避免 cd），使抽象指令变得可操作。 |
| 3 | 条件逻辑注入（Conditional Logic Injection） | `You may use cd if the User explicitly requests it` | 添加例外条件，允许在用户明确要求时使用 `cd`，平衡了严格性和灵活性。 |
