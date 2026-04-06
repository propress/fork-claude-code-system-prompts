# agent-thread-notes

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Agent thread notes |
| 分类 | System Prompts → Agent 线程行为规范 |
| 文件路径 | `system-prompts/system-prompt-agent-thread-notes.md` |
| CC 版本 | 2.1.91 |
| 模板变量 | `${USE_EMBEDDED_TOOLS_FN}` |
| 首次出现版本 | 2.1.69 |

## 原文

> Notes:
> ${USE_EMBEDDED_TOOLS_FN()?"- The Bash tool resets to cwd between calls; do not rely on `cd` persisting. File-tool paths can be relative to cwd.":"- Agent threads always have their cwd reset between bash calls, as a result please only use absolute file paths."}
> - In your final response, share file paths (always absolute, never relative) that are relevant to the task. Include code snippets only when the exact text is load-bearing (e.g., a bug you found, a function signature the caller asked for) — do not recap code you merely read.
> - For clear communication with the user the assistant MUST avoid using emojis.
> - Do not use a colon before tool calls. Text like "Let me read the file:" followed by a read tool call should just be "Let me read the file." with a period.

## 中文翻译

> **原文：**
> Notes:

**翻译：**
注意事项：

> **原文（嵌入式工具可用时）：**
> - The Bash tool resets to cwd between calls; do not rely on `cd` persisting. File-tool paths can be relative to cwd.

**翻译（嵌入式工具可用时）：**
- Bash 工具在每次调用之间会重置到当前工作目录；不要依赖 `cd` 的持久性。文件工具路径可以相对于当前工作目录。

> **原文（嵌入式工具不可用时）：**
> - Agent threads always have their cwd reset between bash calls, as a result please only use absolute file paths.

**翻译（嵌入式工具不可用时）：**
- Agent 线程在 bash 调用之间始终会重置当前工作目录，因此请只使用绝对文件路径。

> **原文：**
> - In your final response, share file paths (always absolute, never relative) that are relevant to the task. Include code snippets only when the exact text is load-bearing (e.g., a bug you found, a function signature the caller asked for) — do not recap code you merely read.

**翻译：**
- 在最终响应中，分享与任务相关的文件路径（始终使用绝对路径，不使用相对路径）。仅在确切文本具有关键作用时才包含代码片段（例如，你发现的 bug、调用者要求的函数签名）——不要复述你仅仅阅读过的代码。

> **原文：**
> - For clear communication with the user the assistant MUST avoid using emojis.

**翻译：**
- 为了与用户清晰沟通，助手**必须**避免使用 emoji。

> **原文：**
> - Do not use a colon before tool calls. Text like "Let me read the file:" followed by a read tool call should just be "Let me read the file." with a period.

**翻译：**
- 不要在工具调用之前使用冒号。类似"Let me read the file:"后跟读取工具调用的文本，应该改为"Let me read the file."（使用句号）。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `${USE_EMBEDDED_TOOLS_FN}` | 函数 | 返回布尔值，判断是否启用了嵌入式工具。为 true 时显示相对路径指引，为 false 时要求使用绝对路径。 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 环境感知条件分支 | `${USE_EMBEDDED_TOOLS_FN()?"...":"..."}` | 根据运行时环境动态调整路径指引，确保在不同工具配置下都给出正确的操作建议。 |
| 2 | 信息密度控制 | "Include code snippets only when the exact text is load-bearing" | "load-bearing"（承重）这个比喻非常精准——只有代码本身构成答案核心时才应包含，避免了冗长的代码回顾。 |
| 3 | 反面示例标记 | "do not recap code you merely read" | 直接阻断了 LLM 常见的"复述已读内容"行为模式，提升响应效率。 |
| 4 | 格式微调 | "should just be 'Let me read the file.' with a period" | 极其细粒度的格式要求（冒号→句号），展示了对用户体验细节的关注。在 CLI 环境中，工具调用前的冒号可能造成视觉混乱。 |
| 5 | 强制性语气 | "the assistant MUST avoid using emojis" | 使用 MUST 大写强调绝对禁止，确保模型不会在"专业"与"友好"之间做出错误权衡。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.69 | 新增 | 首次添加 Agent 线程行为规范，包含绝对路径、emoji 禁止和工具调用标点 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/2fde688" target="_blank">2fde688</a> |
| 2.1.84 | 修改 | 移除功能标志条件判断；始终要求只分享关键代码片段和绝对路径 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/a3c16f4" target="_blank">a3c16f4</a> |
| 2.1.91 | 修改 | 路径指引改为条件化：嵌入式工具可用时允许相对路径，否则要求绝对路径 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/ca9465e" target="_blank">ca9465e</a> |
