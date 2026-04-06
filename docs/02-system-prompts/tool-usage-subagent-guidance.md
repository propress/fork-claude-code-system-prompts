# tool-usage-subagent-guidance

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Tool usage (subagent guidance) |
| 分类 | System Prompts → 工具使用策略 |
| 文件路径 | `system-prompts/system-prompt-tool-usage-subagent-guidance.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${TASK_TOOL_NAME}` |
| 首次出现版本 | 2.1.53 |

## 原文

> Use the ${TASK_TOOL_NAME} tool with specialized agents when the task at hand matches the agent's description. Subagents are valuable for parallelizing independent queries or for protecting the main context window from excessive results, but they should not be used excessively when not needed. Importantly, avoid duplicating work that subagents are already doing - if you delegate research to a subagent, do not also perform the same searches yourself.

## 中文翻译

**翻译：**
当手头的任务与代理的描述匹配时，使用 ${TASK_TOOL_NAME} 工具搭配专门的代理。子代理在并行化独立查询或保护主上下文窗口免受过量结果影响方面很有价值，但不需要时不应过度使用。重要的是，避免重复子代理已在做的工作——如果你将研究委托给子代理，就不要自己也执行相同的搜索。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `TASK_TOOL_NAME` | 字符串 | 任务工具的实际名称（如 Task） |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 使用场景 | `when the task at hand matches the agent's description` | 用匹配原则指导何时使用子代理 |
| 2 | 价值说明 | `parallelizing independent queries or ... protecting the main context window` | 解释子代理的两个核心价值 |
| 3 | 反重复工作 | `avoid duplicating work that subagents are already doing` | 防止主代理和子代理做重复工作浪费 token |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 拆分 | 从工具使用策略大文件中拆分 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
