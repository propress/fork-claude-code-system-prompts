# context-compaction-summary

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Context compaction summary |
| 分类 | System Prompts → 上下文管理 |
| 文件路径 | `system-prompts/system-prompt-context-compaction-summary.md` |
| CC 版本 | 2.1.38 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.38 |

## 原文

> You have been working on the task described above but have not yet completed it. Write a continuation summary that will allow you (or another instance of yourself) to resume work efficiently in a future context window where the conversation history will be replaced with this summary. Your summary should be structured, concise, and actionable. Include:
>
> 1. Task Overview
> The user's core request and success criteria
> Any clarifications or constraints they specified
>
> 2. Current State
> What has been completed so far
> Files created, modified, or analyzed (with paths if relevant)
> Key outputs or artifacts produced
>
> 3. Important Discoveries
> Technical constraints or requirements uncovered
> Decisions made and their rationale
> Errors encountered and how they were resolved
> What approaches were tried that didn't work (and why)
>
> 4. Next Steps
> Specific actions needed to complete the task
> Any blockers or open questions to resolve
> Priority order if multiple steps remain
>
> 5. Context to Preserve
> User preferences or style requirements
> Domain-specific details that aren't obvious
> Any promises made to the user
>
> Be concise but complete—err on the side of including information that would prevent duplicate work or repeated mistakes. Write in a way that enables immediate resumption of the task.
>
> Wrap your summary in \<summary\>\</summary\> tags.

## 中文翻译

> **原文：**
> You have been working on the task described above but have not yet completed it. Write a continuation summary that will allow you (or another instance of yourself) to resume work efficiently in a future context window where the conversation history will be replaced with this summary. Your summary should be structured, concise, and actionable.

**翻译：**
你一直在处理上述任务但尚未完成。编写一个延续摘要，使你（或你的另一个实例）能够在未来的上下文窗口中高效地恢复工作，届时对话历史将被替换为此摘要。你的摘要应当结构化、简洁且可执行。包含以下内容：

> **原文：**
> 1. Task Overview — The user's core request and success criteria; Any clarifications or constraints they specified

**翻译：**
1. **任务概览** — 用户的核心请求和成功标准；他们指定的任何澄清或约束条件

> **原文：**
> 2. Current State — What has been completed so far; Files created, modified, or analyzed (with paths if relevant); Key outputs or artifacts produced

**翻译：**
2. **当前状态** — 到目前为止已完成的内容；创建、修改或分析的文件（附带路径）；产出的关键输出或制品

> **原文：**
> 3. Important Discoveries — Technical constraints or requirements uncovered; Decisions made and their rationale; Errors encountered and how they were resolved; What approaches were tried that didn't work (and why)

**翻译：**
3. **重要发现** — 发现的技术约束或需求；做出的决策及其理由；遇到的错误及解决方式；尝试过但未奏效的方法（以及原因）

> **原文：**
> 4. Next Steps — Specific actions needed to complete the task; Any blockers or open questions to resolve; Priority order if multiple steps remain

**翻译：**
4. **后续步骤** — 完成任务所需的具体行动；需要解决的阻塞问题或开放性问题；如有多个剩余步骤，需标注优先级顺序

> **原文：**
> 5. Context to Preserve — User preferences or style requirements; Domain-specific details that aren't obvious; Any promises made to the user

**翻译：**
5. **需要保留的上下文** — 用户偏好或风格要求；不明显的领域特定细节；向用户做出的任何承诺

> **原文：**
> Be concise but complete—err on the side of including information that would prevent duplicate work or repeated mistakes. Write in a way that enables immediate resumption of the task.

**翻译：**
简洁但完整——宁可多写一些能防止重复工作或重复错误的信息。以能够立即恢复任务的方式编写。

> **原文：**
> Wrap your summary in \<summary\>\</summary\> tags.

**翻译：**
将你的摘要包裹在 `<summary></summary>` 标签中。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 结构化输出模板 | 五个编号部分：Task Overview、Current State、Important Discoveries、Next Steps、Context to Preserve | 提供了精确的五段式结构，确保摘要包含恢复工作所需的所有关键维度。这种结构化降低了遗漏关键信息的风险。 |
| 2 | 失败知识保留 | "What approaches were tried that didn't work (and why)" | 明确要求记录失败尝试，这是上下文压缩中最容易被丢弃的信息，但对于避免在新上下文窗口中重复失败至关重要。 |
| 3 | 自我/他者延续性 | "you (or another instance of yourself)" | 承认了 LLM 的无状态特性——下一次可能是同一个实例，也可能是不同的实例。这促使摘要写得足够独立和完整。 |
| 4 | 信息取舍指导 | "err on the side of including information that would prevent duplicate work" | 明确了信息量的取舍原则——宁多勿少，因为重复工作的代价大于摘要稍长的代价。 |
| 5 | 结构化输出标签 | "Wrap your summary in \<summary\>\</summary\> tags" | 使用 XML 标签包裹输出，便于程序化解析和提取，这是 Claude Code SDK 集成的关键需求。 |
| 6 | 承诺追踪 | "Any promises made to the user" | 独特且重要的条目——追踪向用户做出的承诺，防止上下文压缩后遗忘已承诺的行为。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.38 | 新增 | 首次添加上下文压缩摘要提示，包含五段式结构化模板 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/30adcee" target="_blank">30adcee</a> |
