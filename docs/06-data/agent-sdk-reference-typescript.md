# Data: Agent SDK reference — TypeScript

| 属性 | 值 |
|------|-----|
| 原始名称 | Data: Agent SDK reference — TypeScript |
| 分类 | Data → SDK 参考 |
| 文件路径 | `system-prompts/data-agent-sdk-reference-typescript.md` |
| CC 版本 | 2.1.83 |
| 模板变量 | 无 |

## 概述

此数据文件是 TypeScript Agent SDK 的完整 API 参考文档。包含安装、内置工具、权限系统、MCP 支持（含进程内自定义工具）、钩子系统、子代理、消息类型、会话管理及 MCP 服务器运行时管理等全面的 SDK 参考信息。

## 原文（摘要）

> - **Installation**: `npm install @anthropic-ai/claude-agent-sdk` 安装命令
> - **Quick Start**: 使用 `for await...of` 消费 `query()` 返回的消息流
> - **Built-in Tools**: 与 Python 版相同的 10 个内置工具列表
> - **Permission System**: 五种权限模式，比 Python 多了 `dontAsk` 模式（拒绝未预批准的操作）
> - **MCP Support**: 外部 MCP 服务器配置
> - **In-Process MCP Tools**: 使用 `tool()` 和 `createSdkMcpServer` 定义进程内自定义工具（含 Zod schema）
> - **Hooks**: 支持 21 种钩子事件，比 Python 版更丰富（含 `Setup`、`TeammateIdle`、`WorktreeCreate` 等）
> - **Common Options**: 完整参数表，含 TypeScript 特有的 `allowDangerouslySkipPermissions`、`agentProgressSummaries` 等
> - **Subagents**: 子代理定义，支持 `skills` 和 `mcpServers` 自定义
> - **Message Types**: 消息类型及任务相关系统消息（`task_started`、`task_progress`、`task_notification`）
> - **Session History**: `listSessions`、`getSessionMessages`、`getSessionInfo` 异步函数（支持分页）
> - **Session Mutations**: `renameSession`、`tagSession`、`forkSession` 会话管理
> - **MCP Server Management**: 运行时管理 MCP 服务器（`reconnectMcpServer`、`toggleMcpServer`、`mcpServerStatus`）
> - **Best Practices**: 五条最佳实践建议

## 内容结构

文件包含 302 行，结构为标准 API 参考格式。与 Python 版对应但包含更多 TypeScript 特有功能：进程内 MCP 工具（使用 Zod schema）、更丰富的钩子事件（21 种 vs Python 的 10 种）、`dontAsk` 权限模式、`systemPrompt` 预设模式、以及运行时 MCP 服务器管理 API。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 联合类型标注 | `systemPrompt: string \| preset` 和 `tools: array \| preset` 类型说明 | 明确标注联合类型让模型正确处理字符串和预设对象两种传参方式 |
| 2 | 安全约束强调 | `"bypassPermissions": Skip all prompts (requires allowDangerouslySkipPermissions: true)` | 通过必需的布尔标志强制开发者明确承认风险，模型不会意外生成不安全配置 |
| 3 | 进程内工具完整示例 | `tool()` + `createSdkMcpServer` + Zod schema 的端到端示例 | 展示从工具定义到服务器创建到传入 query 的完整链路，避免模型遗漏任何步骤 |
