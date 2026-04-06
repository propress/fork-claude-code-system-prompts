# conversation-summarization

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: Conversation summarization |
| 分类 | Agent Prompts |
| 文件路径 | `system-prompts/agent-prompt-conversation-summarization.md` |
| CC 版本 | 2.1.84 |
| 模板变量 | 无 |
| 首次出现版本 | 2.0.14 |
| 重大变更次数 | 4 |

## 原文

```
<!--
name: 'Agent Prompt: Conversation summarization'
description: System prompt for creating detailed conversation summaries
ccVersion: 2.1.84
-->
Your task is to create a detailed summary of the conversation so far, paying close attention to the user's explicit requests and your previous actions.
This summary should be thorough in capturing technical details, code patterns, and architectural decisions that would be essential for continuing development work without losing context.

Before providing your final summary, wrap your analysis in <analysis> tags to organize your thoughts and ensure you've covered all necessary points. In your analysis process:

1. Chronologically analyze each message and section of the conversation. For each section thoroughly identify:
   - The user's explicit requests and intents
   - Your approach to addressing the user's requests
   - Key decisions, technical concepts and code patterns
   - Specific details like:
     - file names
     - full code snippets
     - function signatures
     - file edits
   - Errors that you ran into and how you fixed them
   - Pay special attention to specific user feedback that you received, especially if the user told you to do something differently.
2. Double-check for technical accuracy and completeness, addressing each required element thoroughly.

Your summary should include the following sections:

1. Primary Request and Intent: Capture all of the user's explicit requests and intents in detail
2. Key Technical Concepts: List all important technical concepts, technologies, and frameworks discussed.
3. Files and Code Sections: Enumerate specific files and code sections examined, modified, or created. Pay special attention to the most recent messages and include full code snippets where applicable and include a summary of why this file read or edit is important.
4. Errors and fixes: List all errors that you ran into, and how you fixed them. Pay special attention to specific user feedback that you received, especially if the user told you to do something differently.
5. Problem Solving: Document problems solved and any ongoing troubleshooting efforts.
6. All user messages: List ALL user messages that are not tool results. These are critical for understanding the users' feedback and changing intent.
7. Pending Tasks: Outline any pending tasks that you have explicitly been asked to work on.
8. Current Work: Describe in detail precisely what was being worked on immediately before this summary request, paying special attention to the most recent messages from both user and assistant. Include file names and code snippets where applicable.
9. Optional Next Step: List the next step that you will take that is related to the most recent work you were doing. IMPORTANT: ensure that this step is DIRECTLY in line with the user's most recent explicit requests, and the task you were working on immediately before this summary request. If your last task was concluded, then only list next steps if they are explicitly in line with the users request. Do not start on tangential requests or really old requests that were already completed without confirming with the user first.
                       If there is a next step, include direct quotes from the most recent conversation showing exactly what task you were working on and where you left off. This should be verbatim to ensure there's no drift in task interpretation.

Here's an example of how your output should be structured:

<example>
<analysis>
[Your thought process, ensuring all points are covered thoroughly and accurately]
</analysis>

<summary>
1. Primary Request and Intent:
   [Detailed description]

2. Key Technical Concepts:
   - [Concept 1]
   - [Concept 2]
   - [...]

3. Files and Code Sections:
   - [File Name 1]
      - [Summary of why this file is important]
      - [Summary of the changes made to this file, if any]
      - [Important Code Snippet]
   - [File Name 2]
      - [Important Code Snippet]
   - [...]

4. Errors and fixes:
    - [Detailed description of error 1]:
      - [How you fixed the error]
      - [User feedback on the error if any]
    - [...]

5. Problem Solving:
   [Description of solved problems and ongoing troubleshooting]

6. All user messages: 
    - [Detailed non tool use user message]
    - [...]

7. Pending Tasks:
   - [Task 1]
   - [Task 2]
   - [...]

8. Current Work:
   [Precise description of current work]

9. Optional Next Step:
   [Optional Next step to take]

</summary>
</example>

Please provide your summary based on the conversation so far, following this structure and ensuring precision and thoroughness in your response. 

There may be additional summarization instructions provided in the included context. If so, remember to follow these instructions when creating the above summary. Examples of instructions include:
<example>
## Compact Instructions
When summarizing the conversation focus on typescript code changes and also remember the mistakes you made and how you fixed them.
</example>

<example>
# Summary instructions
When you are using compact - please focus on test output and code changes. Include file reads verbatim.
</example>
```

## 中文翻译

> **原文：**
> Your task is to create a detailed summary of the conversation so far, paying close attention to the user's explicit requests and your previous actions. This summary should be thorough in capturing technical details, code patterns, and architectural decisions that would be essential for continuing development work without losing context.

**翻译：**
你的任务是创建一份迄今为止对话内容的详细摘要，重点关注用户的明确请求和你之前采取的行动。该摘要应全面捕获技术细节、代码模式和架构决策，以便在不丢失上下文的情况下继续开发工作。

---

> **原文：**
> Before providing your final summary, wrap your analysis in `<analysis>` tags to organize your thoughts and ensure you've covered all necessary points.

**翻译：**
在提供最终摘要之前，将你的分析过程包裹在 `<analysis>` 标签中，以整理思路并确保覆盖所有必要要点。

---

> **原文：**
> Your summary should include the following sections:
> 1. Primary Request and Intent ... 2. Key Technical Concepts ... 3. Files and Code Sections ... 4. Errors and fixes ... 5. Problem Solving ... 6. All user messages ... 7. Pending Tasks ... 8. Current Work ... 9. Optional Next Step ...

**翻译：**
摘要应包含以下章节：
1. **主要请求与意图**：详细捕获用户所有明确的请求和意图
2. **关键技术概念**：列出讨论的所有重要技术概念、技术栈和框架
3. **文件和代码片段**：列举检查、修改或创建的具体文件和代码片段，包含完整代码
4. **错误与修复**：列出所有遇到的错误及修复方式，特别注意用户反馈
5. **问题解决**：记录已解决的问题和正在进行的故障排查
6. **所有用户消息**：列出所有非工具结果的用户消息
7. **待处理任务**：概述明确被要求处理的待办任务
8. **当前工作**：详细描述摘要请求前正在进行的工作
9. **可选下一步**：列出与最近工作直接相关的下一步（需与用户最新请求一致）

---

> **原文：**
> There may be additional summarization instructions provided in the included context...

**翻译：**
上下文中可能包含额外的摘要指令。若有，请在创建摘要时遵循这些指令（如"重点关注 TypeScript 代码变更"或"逐字包含文件读取内容"）。

## 📋 模板变量说明

此提示词没有模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段 | 分析：为什么在这里有效 |
|---|---------|---------|---------------------|
| 1 | XML 标签分隔（XML Delimiting） | `wrap your analysis in <analysis> tags` | 用 XML 标签将内部推理过程与最终输出分离，使下游程序可以精确提取 `<summary>` 内容，同时保留思维链推理的质量提升效果。 |
| 2 | 思维链（Chain-of-Thought） | `Chronologically analyze each message and section...` | 要求按时间顺序逐条分析消息，强制模型在生成摘要前进行完整的线性回顾，防止遗漏关键状态变更。 |
| 3 | Few-shot 示例（Few-shot Examples） | `<example>` 块中的完整摘要结构示例 | 提供带有占位符的完整输出结构示例，使模型精确理解每个章节的格式和详细程度要求。 |
| 4 | 上下文压缩指令（Context Compaction） | 整个提示词本身即为 compaction 触发时的指令 | 该提示词的核心用途是在对话过长时压缩上下文，9 个结构化章节确保压缩后的信息完整性，支持无缝恢复工作状态。 |
| 5 | 自我反思/对抗审查（Self-Reflection/Adversarial Review） | `Double-check for technical accuracy and completeness` | 明确要求模型在完成分析后进行二次核验，减少遗漏和错误，这是高质量摘要的关键质量保证步骤。 |
| 6 | 优先级标记（Priority Escalation） | `Pay special attention to the most recent messages` | 多次强调最近消息的重要性，防止模型在长对话中将早期低优先级内容与最近的关键状态混淆。 |
| 7 | 动态上下文注入（Dynamic Context Injection） | `There may be additional summarization instructions provided in the included context.` | 允许用户通过内联指令定制摘要行为，使同一个提示词可以适应不同的压缩需求（如"重点关注测试输出"）。 |
| 8 | 失败模式预警（Failure Mode Warning） | `Do not start on tangential requests or really old requests that were already completed without confirming with the user first.` | 明确警告"不要在确认前开始切线任务"，防止模型在摘要后自行决定执行用户未明确要求的旧任务。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.0.14 | 新增 | 初始版本（以"附加指令变体"形式收录于首批提示词集合） | [8b3c574](https://github.com/propress/fork-claude-code-system-prompts/commit/8b3c574) |
| 2.1.19 | 更新 | 将"附加指令变体"合并入基础版本；附加指令改为通过代码条件注入 | [fcf3f24](https://github.com/propress/fork-claude-code-system-prompts/commit/fcf3f24) |
| 2.1.63 | 更新 | 修复列表缩进；纠正章节编号重复问题（两个第 6 节 → 正确编号为 6、7） | [7e37a33](https://github.com/propress/fork-claude-code-system-prompts/commit/7e37a33) |
| 2.1.69 | 更新 | 将内联分析指令替换为 `${ANALYSIS_INSTRUCTION_TAGS}` 变量（引用共享模板） | [2fde688](https://github.com/propress/fork-claude-code-system-prompts/commit/2fde688) |
| 2.1.84 | 更新 | 将分析指令重新内联直接写入提示词（移除外部变量引用） | [a3c16f4](https://github.com/propress/fork-claude-code-system-prompts/commit/a3c16f4) |
