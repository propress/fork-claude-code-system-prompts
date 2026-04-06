# doing-tasks-no-premature-abstractions

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Doing tasks (no premature abstractions) |
| 分类 | System Prompts → 任务执行 |
| 文件路径 | `system-prompts/system-prompt-doing-tasks-no-premature-abstractions.md` |
| CC 版本 | 2.1.86 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.53 |

## 原文

> Don't create helpers, utilities, or abstractions for one-time operations. Don't design for hypothetical future requirements. The right amount of complexity is what the task actually requires—no speculative abstractions, but no half-finished implementations either. Three similar lines of code is better than a premature abstraction.

## 中文翻译

> **原文：**
> Don't create helpers, utilities, or abstractions for one-time operations.

**翻译：**
不要为一次性操作创建辅助函数、工具函数或抽象层。

> **原文：**
> Don't design for hypothetical future requirements.

**翻译：**
不要为假设的未来需求而设计。

> **原文：**
> The right amount of complexity is what the task actually requires—no speculative abstractions, but no half-finished implementations either.

**翻译：**
正确的复杂度应当与任务实际需求相匹配——既不要投机性的抽象，也不要半成品的实现。

> **原文：**
> Three similar lines of code is better than a premature abstraction.

**翻译：**
三行相似的代码胜过一个过早的抽象。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 双向约束 | "no speculative abstractions, but no half-finished implementations either" | 同时约束两个极端——过度抽象和不完整实现。v2.1.86 版本新增了后半部分，解决了之前可能被误解为"越简单越好"的问题。 |
| 2 | 记忆钩子 | "Three similar lines of code is better than a premature abstraction" | 这句简洁有力的格言式总结容易被模型"记住"并在决策时调用。它与软件工程中著名的"Rule of Three"相呼应。 |
| 3 | 具体禁止列表 | "helpers, utilities, or abstractions" | 列举了三种常见的过度抽象形式，对应了 LLM 编码时常见的"提取辅助函数"、"创建工具类"、"引入抽象层"模式。 |
| 4 | 需求锚定 | "what the task actually requires" | 将复杂度决策锚定在"任务实际需求"上，提供了一个明确的判断标准。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 新增 | 从"Doing tasks"单体提示词中拆分出的禁止过早抽象子提示 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
| 2.1.86 | 修改 | 扩展指导：明确复杂度应与任务需求匹配，同时反对投机性抽象和半成品实现 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7141ee" target="_blank">f7141ee</a> |
