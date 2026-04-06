# Data: Agent SDK patterns — Python

| 属性 | 值 |
|------|-----|
| 原始名称 | Data: Agent SDK patterns — Python |
| 分类 | Data → 概念指南 |
| 文件路径 | `system-prompts/data-agent-sdk-patterns-python.md` |
| CC 版本 | 2.1.78 |
| 模板变量 | 无 |

## 概述

此数据文件包含 Python Agent SDK 的常见使用模式和代码示例。涵盖从基础 Agent 创建到自定义工具、钩子、子代理、MCP 服务器集成、权限模式、错误恢复和会话管理等完整的开发场景，为开发者提供实用的参考代码。

## 原文（摘要）

> - **Basic Agent**: 使用 `query()` 函数创建最简单的 Agent，配置工作目录和允许的工具
> - **Custom Tools**: 通过 `@tool` 装饰器和 `create_sdk_mcp_server` 创建自定义工具，需要使用 `ClaudeSDKClient`
> - **Hooks**: 使用 `PostToolUse` 钩子在工具执行后记录文件变更审计日志
> - **Subagents**: 定义 `AgentDefinition` 创建专门的子代理（如代码审查员）
> - **MCP Server Integration**: 集成 Playwright 浏览器自动化和 PostgreSQL 数据库访问等外部 MCP 服务器
> - **Permission Modes**: 展示 default、plan、acceptEdits、bypassPermissions 四种权限模式
> - **Error Recovery**: 处理 `CLINotFoundError`、`CLIConnectionError`、`ProcessError` 等异常
> - **Session Resumption**: 通过捕获 `session_id` 实现会话恢复，保持上下文连续性
> - **Session History**: 使用 `list_sessions()` 和 `get_session_messages()` 查询历史会话
> - **Session Mutations**: 使用 `rename_session()` 和 `tag_session()` 管理会话元数据

## 内容结构

文件包含 364 行代码，以完整的 Python 代码示例为主。每个章节展示一个独立的使用模式，从简单到复杂递进。代码示例使用 `anyio` 异步框架，展示了 `query()` 简单接口和 `ClaudeSDKClient` 完整控制两种使用方式。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 渐进式复杂度展示 | 从 Basic Agent 到 Custom Tools 再到 Subagents 的递进结构 | 按复杂度排列示例让模型能根据用户需求匹配最合适的模式，避免过度工程化 |
| 2 | 内联注释标注关键约束 | `Custom SDK MCP tools require ClaudeSDKClient — query() only supports external stdio/http MCP servers` | 在代码旁直接标注 API 限制，防止模型生成不兼容的代码组合 |
| 3 | 完整错误处理模式 | 展示 `CLINotFoundError`、`CLIConnectionError`、`ProcessError` 三种异常的分别捕获 | 提供具体的异常类型而非泛化的 try/except，引导模型生成健壮的错误处理代码 |
