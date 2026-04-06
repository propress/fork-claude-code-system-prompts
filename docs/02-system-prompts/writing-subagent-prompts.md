# writing-subagent-prompts

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Writing subagent prompts |
| 分类 | System Prompts → 子代理与团队 |
| 文件路径 | `system-prompts/system-prompt-writing-subagent-prompts.md` |
| CC 版本 | 2.1.88 |
| 模板变量 | `${HAS_SUBAGENT_TYPE}` |
| 首次出现版本 | 2.1.69 |

## 原文

> ## Writing the prompt
>
> ${HAS_SUBAGENT_TYPE?"When spawning a fresh agent (with a `subagent_type`), it starts with zero context. ":""}Brief the agent like a smart colleague who just walked into the room — it hasn't seen this conversation, doesn't know what you've tried, doesn't understand why this task matters.
> - Explain what you're trying to accomplish and why.
> - Describe what you've already learned or ruled out.
> - Give enough context about the surrounding problem that the agent can make judgment calls rather than just following a narrow instruction.
> - If you need a short response, say so ("report in under 200 words").
> - Lookups: hand over the exact command. Investigations: hand over the question — prescribed steps become dead weight when the premise is wrong.
>
> ${HAS_SUBAGENT_TYPE?"For fresh agents, terse":"Terse"} command-style prompts produce shallow, generic work.
>
> **Never delegate understanding.** Don't write "based on your findings, fix the bug" or "based on the research, implement it." Those phrases push synthesis onto the agent instead of doing it yourself. Write prompts that prove you understood: include file paths, line numbers, what specifically to change.

## 中文翻译

> **原文：**
> Brief the agent like a smart colleague who just walked into the room — it hasn't seen this conversation, doesn't know what you've tried, doesn't understand why this task matters.

**翻译：**
像向刚走进房间的聪明同事一样向代理做简报——它没有看过这段对话，不知道你尝试过什么，不理解这个任务为何重要。

> **原文：**
> - Explain what you're trying to accomplish and why.
> - Describe what you've already learned or ruled out.
> - Give enough context about the surrounding problem that the agent can make judgment calls rather than just following a narrow instruction.

**翻译：**
- 解释你要完成什么以及为什么。
- 描述你已经了解到或排除的内容。
- 提供足够的问题上下文，使代理能够做出判断而非仅遵循狭隘的指令。

> **原文：**
> - Lookups: hand over the exact command. Investigations: hand over the question — prescribed steps become dead weight when the premise is wrong.

**翻译：**
- 查找类任务：交出精确的命令。调查类任务：交出问题——当前提错误时，预设步骤就成了累赘。

> **原文：**
> Terse command-style prompts produce shallow, generic work.

**翻译：**
简短的命令式提示词会产出肤浅、通用的工作。

> **原文：**
> **Never delegate understanding.** Don't write "based on your findings, fix the bug" or "based on the research, implement it." Those phrases push synthesis onto the agent instead of doing it yourself. Write prompts that prove you understood: include file paths, line numbers, what specifically to change.

**翻译：**
**永远不要委托理解。** 不要写"根据你的发现，修复这个 bug"或"根据研究，实现它。"这些短语将综合分析推给了代理而非你自己完成。写出证明你已理解的提示词：包含文件路径、行号、具体要改什么。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `HAS_SUBAGENT_TYPE` | 布尔值 | 是否指定了子代理类型。为真时添加全新代理上下文的说明 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 同事比喻 | `like a smart colleague who just walked into the room` | 用具象比喻定义提示词应提供的上下文深度 |
| 2 | 查找vs调查 | `Lookups: hand over the exact command. Investigations: hand over the question` | 根据任务类型区分不同的委托策略 |
| 3 | 反委托理解 | `Never delegate understanding` | 最核心原则——综合分析是主代理的责任 |
| 4 | 反面短语 | `"based on your findings, fix the bug"` | 用具体反面示例展示什么是"委托理解" |
| 5 | 条件文本 | `${HAS_SUBAGENT_TYPE?"...":""}` | 三元运算符根据是否有子代理类型调整措辞 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.88 | 修改 | 将上下文继承/全新代理两节合并为统一流程 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/7d7c728" target="_blank">7d7c728</a> |
| 2.1.69 | 新增 | 添加子代理提示词编写指南 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/2fde688" target="_blank">2fde688</a> |
