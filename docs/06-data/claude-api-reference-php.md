# Data: Claude API reference — PHP

| 属性 | 值 |
|------|-----|
| 原始名称 | Data: Claude API reference — PHP |
| 分类 | Data → API 参考 |
| 文件路径 | `system-prompts/data-claude-api-reference-php.md` |
| CC 版本 | 2.1.83 |
| 模板变量 | 无 |

## 概述

此数据文件是 PHP SDK（官方 Anthropic SDK）的完整 API 参考。涵盖客户端初始化（含 Bedrock、Vertex AI、Foundry 三种云平台）、消息请求、流式传输、工具使用（含 Beta Tool Runner 和手动循环）、扩展思维、提示缓存、结构化输出和 Beta 功能等。

## 原文（摘要）

> - **Installation**: `composer require "anthropic-ai/sdk"` Composer 安装
> - **Client Initialization**: 标准 API 密钥初始化，以及 Bedrock、Vertex AI、Foundry 三种云平台客户端
> - **Basic Message Request**: 多态内容块处理，警告不要直接访问 `->text` 而应检查 `->type`
> - **Streaming**: 需要 SDK v0.5.0+，旧版使用单数组参数会报错
> - **Tool Use — Tool Runner (Beta)**: `BetaRunnableTool` 定义工具及 `run` 闭包
> - **Tool Use — Manual Loop**: SDK 使用 camelCase 键名（`inputSchema`、`toolUseID`、`stopReason`）
> - **Extended Thinking**: 自适应思维（推荐），需保留 `$block->signature` 用于多轮对话
> - **Prompt Caching**: 数组语法设置 `cacheControl`，支持 TTL
> - **Structured Outputs**: `StructuredOutputModel` 接口配合 `#[Constrained]` 属性和原始 schema 两种方式
> - **Beta Features**: `betas:` 参数仅在 `->beta->messages` 命名空间有效

## 内容结构

文件包含 380 行。PHP SDK 的特色是数组语法配置、camelCase 键名自动映射到 API 的 snake_case、`StructuredOutputModel` 接口的属性注解、以及三种云平台客户端的工厂方法。版本兼容性说明（v0.5.0 命名参数变更）是重要的注意事项。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 版本兼容性警告 | `Requires SDK v0.5.0+. v0.4.0 and earlier used a single $params array; calling with named parameters throws Unknown named parameter` | 明确版本断裂点和错误信息，让模型根据用户 SDK 版本生成兼容代码 |
| 2 | 键名约定标注 | `The SDK uses camelCase keys (inputSchema, toolUseID, stopReason) and auto-maps to the API's snake_case` | 标注 SDK 与 API 的键名映射关系，防止模型混用两种命名风格 |
| 3 | 多态块安全访问 | `Accessing ->text on content[0] without checking the block type will throw if the first block is not a TextBlock` | 解释直接访问的风险并提供安全的 foreach+type 检查模式 |
