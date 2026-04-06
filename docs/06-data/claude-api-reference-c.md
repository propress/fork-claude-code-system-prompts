# Data: Claude API reference — C#

| 属性 | 值 |
|------|-----|
| 原始名称 | Data: Claude API reference — C# |
| 分类 | Data → API 参考 |
| 文件路径 | `system-prompts/data-claude-api-reference-c.md` |
| CC 版本 | 2.1.83 |
| 模板变量 | 无 |

## 概述

此数据文件是 C# SDK（官方 Anthropic SDK）的完整 API 参考。涵盖客户端初始化、消息请求、流式传输、思维链、工具使用（含手动 JSON schema 定义）、上下文编辑/压缩（Beta）、提示缓存、结构化输出、PDF 输入、服务端工具和文件 API 等功能。

## 原文（摘要）

> - **Installation**: `dotnet add package Anthropic` NuGet 包安装
> - **Client Initialization**: 支持环境变量和显式 API 密钥初始化
> - **Basic Message Request**: 使用 `ContentBlock` 联合类型，通过 `.Value` 和 `OfType<T>` 提取文本
> - **Streaming**: 使用 `CreateStreaming` 和 `TryPick*` 方法处理 SSE 事件流
> - **Thinking**: 自适应思维（推荐）和固定预算思维（已弃用），使用 `TryPickThinking` 提取思考块
> - **Tool Use**: 手动定义 `Tool` 和 `InputSchema`，无类注解工具运行器；详细的响应内容往返转换
> - **Context Editing/Compaction (Beta)**: Beta 命名空间前缀不一致问题详解，15 种 `BetaContentBlock.TryPick*` 变体
> - **Effort Parameter**: 嵌套在 `OutputConfig` 下，支持 Low/Medium/High/Max
> - **Prompt Caching**: 使用 `CacheControlEphemeral` 设置缓存，支持 TTL 配置
> - **Token Counting**: `MessageCountTokensParams` 计算 token 数量
> - **Structured Output**: 通过 `JsonOutputFormat` 和 JSON schema 实现结构化输出
> - **PDF/Document Input**: `DocumentBlockParam` 支持 Base64、URL、纯文本和内容块四种来源
> - **Server-Side Tools**: 版本后缀命名的服务端工具（WebSearch、Bash、TextEditor、CodeExecution）
> - **Files API (Beta)**: `client.Beta.Files` 下的文件上传和引用

## 内容结构

文件包含 407 行，是所有 API 参考中最详尽的之一。特别强调了 C# SDK 的类型系统特性：`TryPick*` 联合类型缩窄模式、`ContentBlock` 到 `ContentBlockParam` 的手动转换（无 `.ToParam()` 辅助方法）、Beta 命名空间前缀不一致等 SDK 特有的注意事项。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 反模式警告 | `Do NOT use new ContentBlockParam(block.Json): it compiles and serializes, but .Value stays null` | 明确指出编译通过但运行时失败的陷阱，防止模型生成看似正确但实际有缺陷的代码 |
| 2 | 命名空间冲突指导 | Beta 前缀不一致问题和 `CS0104` 冲突的解决方案 | 提供具体的编译器错误号和 `using` 别名解决方案，让模型生成可编译的代码 |
| 3 | 源码验证标注 | `source-verified against src/Anthropic/Models/Beta/Messages/*.cs @ 12.9.0` | 标注信息来源增强可信度，让模型在生成代码时更有信心使用这些特定的类型名 |
