# parallel-tool-call-note-part-of-tool-usage-policy

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Parallel tool call note (part of "Tool usage policy") |
| 分类 | System Prompts → 工具使用策略 |
| 文件路径 | `system-prompts/system-prompt-parallel-tool-call-note-part-of-tool-usage-policy.md` |
| CC 版本 | 2.1.30 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.30 |

## 原文

> You can call multiple tools in a single response. If you intend to call multiple tools and there are no dependencies between them, make all independent tool calls in parallel. Maximize use of parallel tool calls where possible to increase efficiency. However, if some tool calls depend on previous calls to inform dependent values, do NOT call these tools in parallel and instead call them sequentially. For instance, if one operation must complete before another starts, run these operations sequentially instead.

## 中文翻译

> **原文：**
> You can call multiple tools in a single response. If you intend to call multiple tools and there are no dependencies between them, make all independent tool calls in parallel.

**翻译：**
你可以在单次响应中调用多个工具。如果你打算调用多个工具且它们之间没有依赖关系，就将所有独立的工具调用并行执行。

> **原文：**
> Maximize use of parallel tool calls where possible to increase efficiency. However, if some tool calls depend on previous calls to inform dependent values, do NOT call these tools in parallel and instead call them sequentially. For instance, if one operation must complete before another starts, run these operations sequentially instead.

**翻译：**
尽可能最大化使用并行工具调用以提高效率。但是，如果某些工具调用依赖于前序调用的返回值，则不要并行调用这些工具，而应按顺序调用。例如，如果一个操作必须在另一个操作开始之前完成，就按顺序运行这些操作。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 正反对比 | `make all independent tool calls in parallel` vs `do NOT call these tools in parallel` | 用明确的正反两面规则消除歧义 |
| 2 | 依赖判断准则 | `depend on previous calls to inform dependent values` | 给出具体的判断标准而非模糊的"视情况而定" |
| 3 | 具体实例 | `if one operation must complete before another starts` | 用具体场景帮助模型理解何时应该串行 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 拆分 | 从工具使用策略大文件中拆分为独立子提示词 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
| 2.1.30 | 新增 | 首次添加并行工具调用指令 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/d2ddab8" target="_blank">d2ddab8</a> |
