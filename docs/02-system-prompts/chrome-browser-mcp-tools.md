# chrome-browser-mcp-tools

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Chrome browser MCP tools |
| 分类 | System Prompts → 浏览器工具 |
| 文件路径 | `system-prompts/system-prompt-chrome-browser-mcp-tools.md` |
| CC 版本 | 2.1.20 |
| 模板变量 | 无 |
| 首次出现版本 | 2.0.77 |

## 原文

> **IMPORTANT: Before using any chrome browser tools, you MUST first load them using ToolSearch.**
>
> Chrome browser tools are MCP tools that require loading before use. Before calling any mcp__claude-in-chrome__* tool:
> 1. Use ToolSearch with `select:mcp__claude-in-chrome__<tool_name>` to load the specific tool
> 2. Then call the tool
>
> For example, to get tab context:
> 1. First: ToolSearch with query "select:mcp__claude-in-chrome__tabs_context_mcp"
> 2. Then: Call mcp__claude-in-chrome__tabs_context_mcp

## 中文翻译

> **原文：**
> **IMPORTANT: Before using any chrome browser tools, you MUST first load them using ToolSearch.**

**翻译：**
**重要：在使用任何 Chrome 浏览器工具之前，你必须先使用 ToolSearch 加载它们。**

> **原文：**
> Chrome browser tools are MCP tools that require loading before use. Before calling any mcp__claude-in-chrome__* tool:
> 1. Use ToolSearch with `select:mcp__claude-in-chrome__<tool_name>` to load the specific tool
> 2. Then call the tool

**翻译：**
Chrome 浏览器工具是需要在使用前加载的 MCP 工具。在调用任何 `mcp__claude-in-chrome__*` 工具之前：
1. 使用 ToolSearch 的 `select:mcp__claude-in-chrome__<tool_name>` 来加载特定工具
2. 然后调用该工具

> **原文：**
> For example, to get tab context:
> 1. First: ToolSearch with query "select:mcp__claude-in-chrome__tabs_context_mcp"
> 2. Then: Call mcp__claude-in-chrome__tabs_context_mcp

**翻译：**
例如，要获取标签页上下文：
1. 首先：使用 ToolSearch 查询 "select:mcp__claude-in-chrome__tabs_context_mcp"
2. 然后：调用 mcp__claude-in-chrome__tabs_context_mcp

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 前置强制检查 | "you MUST first load them using ToolSearch" | 用 MUST 大写强调加载是先决条件，防止模型直接调用未加载的 MCP 工具导致错误。 |
| 2 | 两步操作协议 | "1. Use ToolSearch... 2. Then call the tool" | 将操作分解为清晰的两步流程，避免了模型试图在单步中完成加载和调用的错误。 |
| 3 | 具体示例 | "select:mcp__claude-in-chrome__tabs_context_mcp" | 提供了完整的工具名称字符串示例，消除了工具命名格式的歧义。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.0.77 | 新增 | 首次添加 Chrome MCP 工具加载指南（当时引用 MCPSearch） | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/36f34b8" target="_blank">36f34b8</a> |
| 2.1.14 | 修改 | 将 MCPSearch 引用更新为 ToolSearch | — |
