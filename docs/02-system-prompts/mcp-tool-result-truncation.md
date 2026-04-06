# mcp-tool-result-truncation

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: MCP Tool Result Truncation |
| 分类 | System Prompts → 工具使用指导 |
| 文件路径 | `system-prompts/system-prompt-mcp-tool-result-truncation.md` |
| CC 版本 | 2.1.92 |
| 模板变量 | `${AGENT_TOOL_NAME}`, `${FILE_PATH}` |
| 首次出现版本 | 2.1.89 |

## 原文

> - For targeted queries (find a row, filter by field): use jq or grep on the file directly.
> - For analysis or summarization that requires reading the full content: use the ${AGENT_TOOL_NAME} tool to process the file in an isolated context so the full output does not enter your main context. Be explicit about what the subagent must return — e.g. "Read ${FILE_PATH} in sequential chunks using offset/limit until you have read 100% of it, then summarize it and quote any key findings, decisions, or action items verbatim" — a vague "summarize this" may lose the detail you actually need. Require it to read the entire file in chunks before answering.

## 中文翻译

> **原文：**
> - For targeted queries (find a row, filter by field): use jq or grep on the file directly.

**翻译：**
- 对于定向查询（查找某行、按字段过滤）：直接在文件上使用 jq 或 grep。

> **原文：**
> - For analysis or summarization that requires reading the full content: use the ${AGENT_TOOL_NAME} tool to process the file in an isolated context so the full output does not enter your main context. Be explicit about what the subagent must return — e.g. "Read ${FILE_PATH} in sequential chunks using offset/limit until you have read 100% of it, then summarize it and quote any key findings, decisions, or action items verbatim" — a vague "summarize this" may lose the detail you actually need. Require it to read the entire file in chunks before answering.

**翻译：**
- 对于需要读取完整内容的分析或总结：使用 ${AGENT_TOOL_NAME} 工具在隔离上下文中处理文件，使完整输出不会进入你的主上下文。明确子代理必须返回什么——例如 "使用 offset/limit 按顺序分块读取 ${FILE_PATH} 直到 100% 读取完毕，然后总结并逐字引用任何关键发现、决策或行动项"——模糊的 "summarize this" 可能会丢失你实际需要的细节。要求子代理在回答前分块读取整个文件。

## 📋 模板变量说明

| 变量 | 说明 |
|------|------|
| `${AGENT_TOOL_NAME}` | 代理工具的名称，运行时解析为实际的子代理工具名（如 Task/Agent）。 |
| `${FILE_PATH}` | 需要处理的文件路径，运行时解析为 MCP 工具输出的实际文件路径。 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 策略分流 | "For targeted queries... For analysis or summarization..." | 根据任务类型提供两条不同的路径，避免对所有情况使用单一方法（如总是用子代理或总是直接处理）。 |
| 2 | 上下文隔离 | "in an isolated context so the full output does not enter your main context" | 明确解释了使用子代理的动机是上下文管理，而非能力限制，使指令更易理解和遵循。 |
| 3 | 反模式示例 | "a vague 'summarize this' may lose the detail you actually need" | 给出具体的错误做法（模糊的 "summarize this"）与正确做法的对比，直接指出失败模式。 |
| 4 | 完整性要求 | "Require it to read the entire file in chunks before answering" | 防止子代理仅读取部分文件就生成总结，确保分析的全面性。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.89 | 新增 | 首次引入 MCP 工具结果截断处理指南 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/0e24543" target="_blank">0e24543</a> |
| 2.1.92 | 更新 | 将子代理文件读取指导从 "Read ALL of [file]" 改为按顺序分块读取 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/0b6cc0c" target="_blank">0b6cc0c</a> |
