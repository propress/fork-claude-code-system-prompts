# Data: Claude API reference — cURL

| 属性 | 值 |
|------|-----|
| 原始名称 | Data: Claude API reference — cURL |
| 分类 | Data → API 参考 |
| 文件路径 | `system-prompts/data-claude-api-reference-curl.md` |
| CC 版本 | 2.1.83 |
| 模板变量 | 无 |

## 概述

此数据文件是使用 cURL/原始 HTTP 请求调用 Claude API 的参考文档。适用于没有官方 SDK 的语言环境或需要直接发送 HTTP 请求的场景，包含基础消息请求、响应解析、流式传输、工具使用、提示缓存和扩展思维等核心功能的原始 API 调用示例。

## 原文（摘要）

> - **Setup**: 设置 `ANTHROPIC_API_KEY` 环境变量
> - **Basic Message Request**: 完整的 cURL 命令示例，包含必需的请求头和 JSON 请求体
> - **Parsing the response**: 使用 `jq` 解析 JSON 响应，明确警告不要使用 `grep`/`sed` 解析 JSON
> - **Streaming (SSE)**: 设置 `stream: true` 启用 Server-Sent Events 流式传输，展示完整的事件格式
> - **Tool Use**: 工具定义和工具结果往返的完整 JSON 结构
> - **Prompt Caching**: 使用 `cache_control` 标记可缓存的内容块，支持 TTL 配置
> - **Extended Thinking**: 自适应思维（推荐用于 Opus 4.6/Sonnet 4.6）和固定预算思维（旧模型）
> - **Required Headers**: 必需的 HTTP 请求头表格（Content-Type、x-api-key、anthropic-version、anthropic-beta）

## 内容结构

文件包含 221 行，是最简洁的 API 参考之一。以原始 cURL 命令为主，直接展示 HTTP 请求的完整结构。特别包含响应解析的最佳实践（使用 `jq`）和 SSE 流式事件的完整格式说明。使用 `{{OPUS_ID}}` 模板变量作为模型 ID 占位符。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 明确工具选择指导 | `Use jq to extract fields... Do not use grep/sed — JSON strings can contain any character and regex parsing will break` | 直接禁止常见的错误做法并解释原因，防止模型生成脆弱的 JSON 解析代码 |
| 2 | 完整 SSE 事件格式 | 展示从 `message_start` 到 `message_stop` 的完整事件序列和数据结构 | 提供可参考的事件流格式让模型准确处理流式响应的每个阶段 |
| 3 | 版本兼容性标注 | `Opus 4.6 and Sonnet 4.6: Use adaptive thinking. budget_tokens is deprecated on both` | 按模型版本区分推荐用法，让模型根据用户使用的模型版本生成正确的配置 |
