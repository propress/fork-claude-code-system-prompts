# Data: Agent SDK reference — Python

| 属性 | 值 |
|------|-----|
| 原始名称 | Data: Agent SDK reference — Python |
| 分类 | Data → SDK 参考 |
| 文件路径 | `system-prompts/data-agent-sdk-reference-python.md` |
| CC 版本 | 2.1.83 |
| 模板变量 | 无 |

## 概述

此数据文件是 Python Agent SDK 的完整 API 参考文档。包含安装指南、两种主要接口（`query()` 和 `ClaudeSDKClient`）、内置工具列表、权限系统、MCP 支持、钩子系统、消息类型及会话管理等完整的 SDK 参考信息。

## 原文（摘要）

> - **Installation**: `pip install claude-agent-sdk` 安装命令
> - **Quick Start**: 最简示例，使用 `query()` 配合 `ResultMessage` 获取结果
> - **Built-in Tools**: 10 个内置工具列表（Read、Write、Edit、Bash、Glob、Grep、WebSearch、WebFetch、AskUserQuestion、Agent）
> - **Primary Interfaces**: `query()` 简单一次性用法和 `ClaudeSDKClient` 完整控制两种接口
> - **Permission System**: 四种权限模式（default、plan、acceptEdits、bypassPermissions）
> - **MCP Support**: 通过 `mcp_servers` 配置外部 MCP 服务器
> - **Hooks**: 钩子回调函数，支持 `PreToolUse`、`PostToolUse` 等 10 种事件
> - **Common Options**: `ClaudeAgentOptions` 的完整参数表（cwd、allowed_tools、model、max_turns 等）
> - **Message Types**: `ResultMessage`、`SystemMessage`、`AssistantMessage`、`RateLimitEvent` 等消息类型
> - **Subagents**: 通过 `AgentDefinition` 定义子代理
> - **Error Handling**: `CLINotFoundError`、`CLIConnectionError` 异常处理
> - **Session History**: `list_sessions()` 和 `get_session_messages()` 同步函数
> - **Session Mutations**: `rename_session()` 和 `tag_session()` 会话管理

## 内容结构

文件包含 360 行，结构为标准 API 参考格式。以表格列出内置工具和配置选项，以代码示例展示各 API 的用法。特别区分了 `query()` 简单接口和 `ClaudeSDKClient` 完整控制接口的适用场景。包含消息类型的详细说明，包括 `TaskStartedMessage`、`TaskProgressMessage` 等子代理任务事件。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 双接口分层设计 | `query()` — Simple One-Shot Usage vs `ClaudeSDKClient` — Full Control | 提供两个抽象层次让模型根据用户需求复杂度选择合适的接口，避免简单场景过度复杂化 |
| 2 | 同步/异步标注 | `list_sessions()` 和 `get_session_messages()` 标注为 `sync function — no await` | 明确标注同步函数防止模型错误地添加 `await`，避免常见的异步混用错误 |
| 3 | 完整选项参数表 | 以表格形式列出所有 `ClaudeAgentOptions` 参数及类型和描述 | 结构化的参数表让模型能准确生成配置代码，减少参数名拼写错误和类型不匹配 |
