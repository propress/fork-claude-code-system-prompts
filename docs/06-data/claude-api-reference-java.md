# Data: Claude API reference — Java

| 属性 | 值 |
|------|-----|
| 原始名称 | Data: Claude API reference — Java |
| 分类 | Data → API 参考 |
| 文件路径 | `system-prompts/data-claude-api-reference-java.md` |
| CC 版本 | 2.1.83 |
| 模板变量 | 无 |

## 概述

此数据文件是 Java SDK 的完整 API 参考文档。涵盖客户端初始化、消息请求、流式传输、思维链、工具使用（含注解类 BetaToolRunner 和手动 JSON schema）、Effort 参数、提示缓存、Token 计数、结构化输出、PDF 输入、服务端工具和文件 API 等功能。

## 原文（摘要）

> - **Installation**: Maven/Gradle 依赖配置（`com.anthropic:anthropic-java:2.17.0`）
> - **Client Initialization**: `AnthropicOkHttpClient.fromEnv()` 或 builder 模式
> - **Basic Message Request**: 使用 builder 模式和 `.addUserMessage()` 快捷方法
> - **Streaming**: `StreamResponse<RawMessageStreamEvent>` 配合 Java Stream API 和 `flatMap`
> - **Thinking**: 自适应思维（推荐），`ContentBlock` 使用 `.thinking()/.text()` 返回 `Optional<T>`
> - **Tool Use (Beta)**: `@JsonClassDescription` 注解类实现 `Supplier<String>`，`BetaToolRunner` 自动循环
> - **Memory Tool**: `BetaMemoryToolHandler` 实现内存工具后端
> - **Effort Parameter**: 嵌套在 `OutputConfig` 下（非顶级属性）
> - **Prompt Caching**: `.systemOfTextBlockParams()` 方法（非 `.system(String)`）
> - **Token Counting**: `MessageCountTokensParams` 计算输入 token
> - **Structured Output**: 基于类的 `StructuredMessageCreateParams<T>` 自动推导 JSON schema
> - **PDF/Document Input**: `DocumentBlockParam.builder()` 的 `.base64Source()`/`.urlSource()` 快捷方法
> - **Server-Side Tools**: 版本后缀类型，直接 `.addTool()` 重载无需手动包装
> - **Files API (Beta)**: `client.beta().files()` 下的文件上传和引用

## 内容结构

文件包含 437 行，是最长的 API 参考。Java SDK 的特色是 builder 模式、Jackson 注解工具定义、`Optional<T>` 类型缩窄、以及 Beta/非 Beta 命名空间的严格分离。结构化输出部分展示了基于 POJO 的自动 schema 生成。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | Builder 方法精确指导 | `Use .systemOfTextBlockParams(...) — the plain .system(String) overload can't carry cache control` | 指出两个重载方法的功能差异，防止模型选择不支持缓存的简单重载 |
| 2 | 类型安全的结构化输出 | `StructuredMessageCreateParams<BookList>` + `.outputConfig(BookList.class)` | 展示泛型参数化的类型安全输出，模型能生成编译期检查的代码而非运行时解析 |
| 3 | Beta 命名空间隔离警告 | `BetaTool* types are NOT interchangeable with non-beta Tool* — pick one namespace per request` | 明确禁止混用两个命名空间，防止模型生成编译通过但运行时失败的代码 |
