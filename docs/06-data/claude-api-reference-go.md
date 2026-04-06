# Data: Claude API reference — Go

| 属性 | 值 |
|------|-----|
| 原始名称 | Data: Claude API reference — Go |
| 分类 | Data → API 参考 |
| 文件路径 | `system-prompts/data-claude-api-reference-go.md` |
| CC 版本 | 2.1.83 |
| 模板变量 | 无 |

## 概述

此数据文件是 Go SDK 的完整 API 参考文档。涵盖客户端初始化、消息请求、流式传输、工具使用（含 BetaToolRunner 自动循环和手动循环两种模式）、思维链、提示缓存、服务端工具、PDF 输入、文件 API 和上下文编辑/压缩等功能。

## 原文（摘要）

> - **Installation**: `go get github.com/anthropics/anthropic-sdk-go` 安装
> - **Client Initialization**: 默认读取环境变量或显式传入 API 密钥
> - **Basic Message Request**: 使用 `block.AsAny().(type)` 类型开关提取内容变体
> - **Streaming**: `NewStreaming` 创建流，使用 `Accumulate` 方法累积最终消息（无 `GetFinalMessage()`）
> - **Tool Use — Tool Runner (Beta)**: `BetaToolRunner` 自动工具循环，使用 `jsonschema` 结构体标签自动生成 schema
> - **Tool Use — Manual Loop**: 手动定义 `ToolParam`、检查 `StopReason`、执行工具、回送结果的完整循环
> - **Thinking**: 自适应思维（推荐），使用 `NewThinkingConfigAdaptiveParam()` 构造
> - **Prompt Caching**: 在 `TextBlockParam` 上设置 `CacheControl`，支持 TTL
> - **Server-Side Tools**: 版本后缀命名，通过 `ToolUnionParam` 的 `Of*` 字段包装
> - **PDF/Document Input**: `NewDocumentBlock` 泛型辅助函数自动设置 MediaType
> - **Files API (Beta)**: `Upload` 方法（非 `New`/`Create`），使用 `anthropic.File()` 附加文件名
> - **Context Editing/Compaction (Beta)**: 使用 `Beta.Messages.New` 和 `ContextManagement` 配置

## 内容结构

文件包含 426 行，是最长的 API 参考之一。Go SDK 的特色是类型安全的联合类型处理模式：`AsAny().(type)` 类型开关、`ToolUnionParam{Of*: &t}` 联合包装、`resp.ToParam()` 响应往返转换。手动工具循环部分包含详细的 API 表面说明表格。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | API 表面速查表 | 以表格列出 `resp.ToParam()`、`block.AsAny().(type)` 等核心符号及用途 | 集中展示关键 API 让模型快速查找正确的方法名，避免在冗长代码中遗漏关键模式 |
| 2 | 源码溯源标注 | `Derived from anthropic-sdk-go/examples/tools/main.go` | 标注代码来源增强可信度，也帮助模型理解代码模式的权威性 |
| 3 | 否定式指导 | `There is no GetFinalMessage() on the stream` 和 `Method is Upload (NOT New/Create)` | 明确指出不存在的 API 防止模型凭经验猜测错误的方法名 |
