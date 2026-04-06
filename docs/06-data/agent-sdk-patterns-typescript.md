# Data: Agent SDK patterns — TypeScript

| 属性 | 值 |
|------|-----|
| 原始名称 | Data: Agent SDK patterns — TypeScript |
| 分类 | Data → 概念指南 |
| 文件路径 | `system-prompts/data-agent-sdk-patterns-typescript.md` |
| CC 版本 | 2.1.78 |
| 模板变量 | 无 |

## 概述

此数据文件包含 TypeScript Agent SDK 的常见使用模式和代码示例。涵盖基础 Agent、钩子、子代理、MCP 服务器集成、会话恢复、会话历史管理和自定义系统提示等场景，是 TypeScript 开发者使用 Claude Agent SDK 的实用参考。

## 原文（摘要）

> - **Basic Agent**: 使用 `query()` 异步迭代器创建基础 Agent，通过 `for await...of` 消费消息流
> - **Hooks**: 定义 `HookCallback` 实现工具使用后的审计日志记录，使用正则匹配器过滤工具
> - **Subagents**: 通过 `agents` 配置定义专门的子代理，如代码审查专家
> - **MCP Server Integration**: 集成 Playwright 等外部 MCP 服务器进行浏览器自动化
> - **Session Resumption**: 捕获 `session_id` 并通过 `resume` 选项恢复会话上下文
> - **Session History**: 使用 `listSessions`、`getSessionMessages`、`getSessionInfo` 查询历史
> - **Session Mutations**: 使用 `renameSession`、`tagSession`、`forkSession` 管理会话
> - **Custom System Prompt**: 通过 `systemPrompt` 自定义 Agent 的角色和行为指南

## 内容结构

文件包含 214 行代码，以 TypeScript 代码示例为主。结构与 Python 版本对应但更简洁，利用 TypeScript 的 `for await...of` 语法和类型检查 `"result" in message` 模式。额外包含 `forkSession` 会话分叉和自定义系统提示章节。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 惯用语法展示 | `if ("result" in message)` 替代 `instanceof` 检查 | 展示 TypeScript 惯用的类型缩窄方式，引导模型生成地道的 TS 代码而非 Python 风格翻译 |
| 2 | 角色定义模板 | `systemPrompt: "You are a senior code reviewer focused on: 1. Security vulnerabilities 2. Performance issues 3. Code maintainability"` | 提供具体的角色定义示例，展示如何通过编号列表结构化 Agent 的关注点 |
| 3 | 会话分叉模式 | `const { sessionId: forkedId } = await forkSession(sessionId)` | 展示 TypeScript 独有的 `forkSession` 能力，使用解构重命名避免变量冲突 |
