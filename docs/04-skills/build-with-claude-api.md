# build-with-claude-api

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: Build with Claude API |
| 分类 | Skills → API 开发 |
| 文件路径 | `system-prompts/skill-build-with-claude-api.md` |
| CC 版本 | 2.1.91 |
| 模板变量 | `{{OPUS_NAME}}`、`{{OPUS_ID}}`、`{{SONNET_ID}}`、`{{PREV_SONNET_ID}}` |

## 原文（摘要）

这是一个大型路由指南（267 行），帮助 Claude 构建基于 Claude API 的 LLM 应用。主要章节：

### Defaults
> "For the Claude model version, please use {{OPUS_NAME}}, which you can access via the exact model string `{{OPUS_ID}}`. Please default to using adaptive thinking (`thinking: {type: "adaptive"}`) for anything remotely complicated."

### Language Detection
根据项目文件自动检测用户语言：`.py` → Python、`.ts` → TypeScript、`.java` → Java、`.go` → Go、`.rb` → Ruby、`.cs` → C#、`.php` → PHP。支持多语言检测和不支持语言的回退方案。

### Which Surface Should I Use?
> "**Start simple.** Default to the simplest tier that meets your needs. Single API calls and workflows handle most use cases — only reach for agents when the task genuinely requires open-ended, model-driven exploration."

决策树分为四层：Single LLM call → Workflow → Agent (Claude API) → Agent (Agent SDK)

### Architecture
> "Everything goes through `POST /v1/messages`. Tools and output constraints are features of this single endpoint — not separate APIs."

### Current Models
列出 Claude Opus 4.6、Sonnet 4.6、Haiku 4.5 的模型 ID、上下文长度和定价。

> "**ALWAYS use `{{OPUS_ID}}` unless the user explicitly names a different model.** This is non-negotiable."

### Thinking & Effort
> "**Opus 4.6 — Adaptive thinking (recommended):** Use `thinking: {type: "adaptive"}`. Claude dynamically decides when and how much to think. No `budget_tokens` needed — `budget_tokens` is deprecated on Opus 4.6 and Sonnet 4.6."

### Compaction / Prompt Caching / Reading Guide / Common Pitfalls
涵盖长对话压缩、缓存优化、按任务类型查阅文档的指引、以及常见错误（不要截断输入、不要低估 `max_tokens`、不要重新实现 SDK 功能等）。

## 中文翻译

### 默认设置

除非用户另行要求：对于 Claude 模型版本，请使用 {{OPUS_NAME}}，可通过精确模型字符串 `{{OPUS_ID}}` 访问。对于任何稍微复杂的任务，请默认使用自适应思考 (`thinking: {type: "adaptive"}`)。对于可能涉及长输入、长输出或高 `max_tokens` 的任何请求，请默认使用流式传输——它可以防止请求超时。

### 语言检测

在阅读代码示例之前，确定用户使用的语言：

1. **查看项目文件** 推断语言（Python、TypeScript、Java、Go、Ruby、C#、PHP）
2. **如果检测到多种语言**：检查用户当前文件或问题相关的语言；仍然不明确时询问用户
3. **如果无法推断语言**：使用 AskUserQuestion 提供选项，不可用时默认使用 Python
4. **如果检测到不支持的语言**：建议 cURL/原始 HTTP 示例

### 应该使用哪个接口？

**从简单开始。** 默认使用满足需求的最简单层级。

| 用例 | 层级 | 推荐接口 | 原因 |
| --- | --- | --- | --- |
| 分类、摘要、提取、问答 | 单次 LLM 调用 | **Claude API** | 一次请求，一次响应 |
| 批处理或嵌入 | 单次 LLM 调用 | **Claude API** | 专用端点 |
| 代码控制逻辑的多步管道 | 工作流 | **Claude API + 工具使用** | 你来编排循环 |
| 自定义工具的 Agent | Agent | **Claude API + 工具使用** | 最大灵活性 |
| 内置文件/Web/终端工具的 AI Agent | Agent | **Agent SDK** | 内置工具、安全和 MCP 支持 |

#### 决策树

1. 单次 LLM 调用 → Claude API
2. Claude 本身是否需要发现和访问文件/Web/Shell？→ 是 → Agent SDK
3. 工作流（多步、代码编排、自有工具）→ Claude API 带工具使用
4. 开放式 Agent（模型决定自身轨迹）→ Claude API Agent 循环

#### 是否应该构建 Agent？

构建前检查四个标准：
- **复杂性** — 任务是否多步且难以完全预先指定？
- **价值** — 结果是否值得更高的成本和延迟？
- **可行性** — Claude 是否擅长此类任务？
- **错误成本** — 错误能否被捕获和恢复？

任何一项为"否"，则留在更简单的层级。

### 架构

一切通过 `POST /v1/messages`。工具和输出约束是该单一端点的功能——不是单独的 API。

- **用户定义工具** — 通过装饰器、Zod schema 或原始 JSON 定义工具，SDK 的 tool runner 处理 API 调用、函数执行和循环。
- **服务端工具** — Anthropic 托管的工具，在 Anthropic 基础设施上运行。
- **结构化输出** — 约束 Messages API 响应格式 (`output_config.format`) 和/或工具参数验证 (`strict: true`)。
- **支持端点** — Batches、Files、Token Counting 和 Models API。

### 当前模型（缓存日期：2026-02-17）

| 模型 | 模型 ID | 上下文 | 输入 $/1M | 输出 $/1M |
| --- | --- | --- | --- | --- |
| Claude Opus 4.6 | `claude-opus-4-6` | 200K (1M beta) | $5.00 | $25.00 |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | 200K (1M beta) | $3.00 | $15.00 |
| Claude Haiku 4.5 | `claude-haiku-4-5` | 200K | $1.00 | $5.00 |

**始终使用 `{{OPUS_ID}}`，除非用户明确指定其他模型。** 这是不可协商的。不要为了成本而降级——那是用户的决定，不是你的。

**关键：仅使用上表中的精确模型 ID 字符串——它们本身就是完整的。不要附加日期后缀。**

### 思考与努力程度

- **Opus 4.6 — 自适应思考（推荐）**：使用 `thinking: {type: "adaptive"}`。`budget_tokens` 在 Opus 4.6 和 Sonnet 4.6 上已弃用。
- **Effort 参数（GA）**：通过 `output_config: {effort: "low"|"medium"|"high"|"max"}` 控制思考深度。默认为 `high`。`max` 仅 Opus 4.6。
- **Sonnet 4.6**：支持自适应思考。
- **旧模型**：仅在用户明确要求时，使用 `thinking: {type: "enabled", budget_tokens: N}`。

### 压缩

**Beta，Opus 4.6 和 Sonnet 4.6。** 对于可能超过 200K 上下文窗口的长对话，启用服务端压缩。**关键：** 在每个轮次将 `response.content`（不仅仅是文本）追加回消息中。

### Prompt 缓存

**前缀匹配。** 前缀中任何位置的任何字节变化都会使其后的所有内容失效。渲染顺序是 `tools` → `system` → `messages`。保持稳定内容在前，将易变内容放在最后一个 `cache_control` 断点之后。

### 常见陷阱

- 不要在传递文件或内容给 API 时截断输入
- Opus 4.6 / Sonnet 4.6 思考：使用 `thinking: {type: "adaptive"}`——不要使用 `budget_tokens`
- Opus 4.6 已移除 prefill：Assistant 消息预填充在 Opus 4.6 上返回 400 错误
- 不要低估 `max_tokens`——非流式默认 ~16000，流式默认 ~64000
- 128K 输出 token：需要流式传输
- 不要重新实现 SDK 功能
- 不要为 SDK 数据结构定义自定义类型

## 📋 模板变量说明

| 变量 | 说明 |
|------|------|
| `{{OPUS_NAME}}` | 默认推荐模型的显示名称（如 "Claude Opus 4.6"） |
| `{{OPUS_ID}}` | 默认推荐模型的精确 API ID（如 "claude-opus-4-6"） |
| `{{SONNET_ID}}` | Sonnet 模型的 API ID，提示词中作为"不要使用"的警告出现 |
| `{{PREV_SONNET_ID}}` | 上一代 Sonnet 模型的 API ID，同样作为"不要使用"的警告 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 不可协商的硬规则 | "**ALWAYS use `{{OPUS_ID}}` unless the user explicitly names a different model.** This is non-negotiable." | 使用绝对化语言（"non-negotiable"）防止 LLM 自行"优化"成本而降级模型，这是 API 集成中常见的错误倾向 |
| 2 | 渐进式决策树 | 从 "Single LLM call" 到 "Agent" 的四层决策结构 | 让 LLM 从最简单方案开始评估，避免过度工程化的默认倾向 |
| 3 | 四标准检查清单 | Complexity、Value、Viability、Cost of error | 提供结构化的 Agent 必要性评估，防止 LLM 不加思考地推荐 Agent 方案 |
| 4 | 弃用警告强调 | "`budget_tokens` is deprecated... do NOT use `budget_tokens`" | 反复强调弃用信息，因为 LLM 的训练数据中充满了旧版用法，需要强烈的信号来覆盖 |
| 5 | 精确的数字默认值 | "non-streaming: ~16000, streaming: ~64000" | 提供具体数字而非模糊指导，消除 LLM 的猜测空间 |
| 6 | 防幻觉校准 | "if any of the model strings above look unfamiliar to you, that's to be expected — that just means they were released after your training data cutoff" | 预防 LLM 因不认识新模型名而拒绝使用或自行"修正"为旧模型 |
| 7 | 负面示例模式 | Common Pitfalls 章节列出"不要做X"并解释后果 | 明确列出反模式比仅列正确做法更有效，因为 LLM 倾向于复现训练数据中的常见模式 |
