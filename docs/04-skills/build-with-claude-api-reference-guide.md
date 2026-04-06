# build-with-claude-api-reference-guide

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: Build with Claude API (reference guide) |
| 分类 | Skills → API 开发 |
| 文件路径 | `system-prompts/skill-build-with-claude-api-reference-guide.md` |
| CC 版本 | 2.1.91 |
| 模板变量 | 无（但使用 `{lang}` 路径占位符） |

## 原文（摘要）

这是一个简短的参考指南模板（43 行），为检测到的编程语言提供快速任务导航。以 `<doc>` 标签形式包含语言特定文档，并提供任务到文档的映射。

> ## Reference Documentation
>
> The relevant documentation for your detected language is included below in `<doc>` tags. Each tag has a `path` attribute showing its original file path. Use this to find the right section:

### Quick Task Reference 完整列表

> **Single text classification/summarization/extraction/Q&A:**
> → Refer to `{lang}/claude-api/README.md`
>
> **Chat UI or real-time response display:**
> → Refer to `{lang}/claude-api/README.md` + `{lang}/claude-api/streaming.md`
>
> **Long-running conversations (may exceed context window):**
> → Refer to `{lang}/claude-api/README.md` — see Compaction section
>
> **Prompt caching / optimize caching / "why is my cache hit rate low":**
> → Refer to `shared/prompt-caching.md` + `{lang}/claude-api/README.md` (Prompt Caching section)
>
> **Function calling / tool use / agents:**
> → Refer to `{lang}/claude-api/README.md` + `shared/tool-use-concepts.md` + `{lang}/claude-api/tool-use.md`
>
> **Batch processing (non-latency-sensitive):**
> → Refer to `{lang}/claude-api/README.md` + `{lang}/claude-api/batches.md`
>
> **File uploads across multiple requests:**
> → Refer to `{lang}/claude-api/README.md` + `{lang}/claude-api/files-api.md`
>
> **Agent design (tool surface, context management, caching strategy):**
> → Refer to `shared/agent-design.md`
>
> **Agent with built-in tools (file/web/terminal) (Python & TypeScript only):**
> → Refer to `{lang}/agent-sdk/README.md` + `{lang}/agent-sdk/patterns.md`
>
> **Error handling:**
> → Refer to `shared/error-codes.md`
>
> **Latest docs via WebFetch:**
> → Refer to `shared/live-sources.md` for URLs

## 中文翻译

## 参考文档

检测到的语言的相关文档包含在下面的 `<doc>` 标签中。每个标签都有一个 `path` 属性显示其原始文件路径。使用它来找到正确的章节：

### 快速任务参考

**单次文本分类/摘要/提取/问答：**
→ 参见 `{lang}/claude-api/README.md`

**聊天 UI 或实时响应显示：**
→ 参见 `{lang}/claude-api/README.md` + `{lang}/claude-api/streaming.md`

**长时间对话（可能超过上下文窗口）：**
→ 参见 `{lang}/claude-api/README.md` — 查看 Compaction 章节

**Prompt 缓存 / 优化缓存 / "为什么我的缓存命中率低"：**
→ 参见 `shared/prompt-caching.md` + `{lang}/claude-api/README.md`（Prompt Caching 章节）

**函数调用 / 工具使用 / Agent：**
→ 参见 `{lang}/claude-api/README.md` + `shared/tool-use-concepts.md` + `{lang}/claude-api/tool-use.md`

**批处理（非延迟敏感型）：**
→ 参见 `{lang}/claude-api/README.md` + `{lang}/claude-api/batches.md`

**跨多个请求的文件上传：**
→ 参见 `{lang}/claude-api/README.md` + `{lang}/claude-api/files-api.md`

**Agent 设计（工具表面、上下文管理、缓存策略）：**
→ 参见 `shared/agent-design.md`

**内置工具的 Agent（文件/Web/终端）（仅 Python 和 TypeScript）：**
→ 参见 `{lang}/agent-sdk/README.md` + `{lang}/agent-sdk/patterns.md`

**错误处理：**
→ 参见 `shared/error-codes.md`

**通过 WebFetch 获取最新文档：**
→ 参见 `shared/live-sources.md` 获取 URL

## 📋 模板变量说明

| 变量 | 说明 |
|------|------|
| `{lang}` | 运行时路径占位符，指代检测到的编程语言目录名（如 `python`、`typescript`、`java` 等） |

注：`{lang}` 不是 `${}` 形式的模板变量，而是文档中的路径占位符，在 Claude 阅读文档时根据语言检测结果替换。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 任务-文档映射表 | 每个任务用 "→ Refer to" 指向精确的文件路径 | 将开放式的"我需要什么文档"问题转化为确定性的查找表，消除 LLM 的猜测 |
| 2 | 问题驱动导航 | 用用户可能提出的问题作为键（"why is my cache hit rate low"） | 使用自然语言问题而非技术分类，让 LLM 更容易匹配用户意图 |
| 3 | 渐进式复杂度 | 从简单（单次调用）到复杂（Agent SDK）的排列顺序 | 引导 LLM 优先推荐简单方案，只在必要时才加载更多文档 |
| 4 | 最小化加载策略 | 每个任务只指向必需的 1-3 个文件 | 避免一次性加载所有文档占满上下文窗口，是 Skill 系统按需加载理念的体现 |
