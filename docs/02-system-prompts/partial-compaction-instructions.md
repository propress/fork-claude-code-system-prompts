# partial-compaction-instructions

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Partial compaction instructions |
| 分类 | System Prompts → 记忆与上下文管理 |
| 文件路径 | `system-prompts/system-prompt-partial-compaction-instructions.md` |
| CC 版本 | 2.1.88 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.88 |

## 原文

> Your task is to create a detailed summary of this conversation. This summary will be placed at the start of a continuing session; newer messages that build on this context will follow after your summary (you do not see them here). Summarize thoroughly so that someone reading only your summary and then the newer messages can fully understand what happened and continue the work.
>
> Before providing your final summary, wrap your analysis in \<analysis\> tags to organize your thoughts and ensure you've covered all necessary points. In your analysis process:
>
> 1. Chronologically analyze each message and section of the conversation. For each section thoroughly identify:
>    - The user's explicit requests and intents
>    - Your approach to addressing the user's requests
>    - Key decisions, technical concepts and code patterns
>    - Specific details like:
>      - file names
>      - full code snippets
>      - function signatures
>      - file edits
>    - Errors that you ran into and how you fixed them
>    - Pay special attention to specific user feedback that you received, especially if the user told you to do something differently.
> 2. Double-check for technical accuracy and completeness, addressing each required element thoroughly.
>
> Your summary should include the following sections:
>
> 1. Primary Request and Intent: Capture the user's explicit requests and intents in detail
> 2. Key Technical Concepts: List important technical concepts, technologies, and frameworks discussed.
> 3. Files and Code Sections: Enumerate specific files and code sections examined, modified, or created. Include full code snippets where applicable and include a summary of why this file read or edit is important.
> 4. Errors and fixes: List errors encountered and how they were fixed.
> 5. Problem Solving: Document problems solved and any ongoing troubleshooting efforts.
> 6. All user messages: List ALL user messages that are not tool results.
> 7. Pending Tasks: Outline any pending tasks.
> 8. Work Completed: Describe what was accomplished by the end of this portion.
> 9. Context for Continuing Work: Summarize any context, decisions, or state that would be needed to understand and continue the work in subsequent messages.

## 中文翻译

> **原文：**
> Your task is to create a detailed summary of this conversation. This summary will be placed at the start of a continuing session; newer messages that build on this context will follow after your summary (you do not see them here). Summarize thoroughly so that someone reading only your summary and then the newer messages can fully understand what happened and continue the work.

**翻译：**
你的任务是创建这段对话的详细摘要。此摘要将被放置在后续会话的开头；基于此上下文的新消息将跟在你的摘要之后（你在此处看不到它们）。请彻底总结，使得仅阅读你的摘要和后续新消息的人能够完全理解所发生的事情并继续工作。

> **原文：**
> Before providing your final summary, wrap your analysis in \<analysis\> tags to organize your thoughts and ensure you've covered all necessary points.

**翻译：**
在提供最终摘要之前，将你的分析包裹在 `<analysis>` 标签中，以组织思路并确保覆盖了所有必要的要点。

> **原文：**
> Your summary should include the following sections:
> 1. Primary Request and Intent ... 9. Context for Continuing Work

**翻译：**
你的摘要应包含以下部分：
1. **主要请求和意图**：详细捕获用户的明确请求和意图
2. **关键技术概念**：列出讨论过的重要技术概念、技术和框架
3. **文件和代码部分**：列举检查、修改或创建的具体文件和代码部分。包含完整代码片段，并总结该文件读取或编辑的重要性
4. **错误和修复**：列出遇到的错误及其修复方式
5. **问题解决**：记录已解决的问题和正在进行的排查工作
6. **所有用户消息**：列出所有非工具结果的用户消息
7. **待处理任务**：列出待处理的任务
8. **已完成工作**：描述在此部分结束时完成了什么
9. **继续工作的上下文**：总结在后续消息中理解和继续工作所需的上下文、决策或状态

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 思维链前置 | `wrap your analysis in <analysis> tags` | 强制模型在输出最终摘要前先进行结构化分析，提高摘要质量 |
| 2 | 受众视角 | `someone reading only your summary ... can fully understand` | 从读者角度定义摘要质量标准 |
| 3 | 九段式结构 | 9个明确命名的必要部分 | 结构化模板确保摘要不遗漏关键信息 |
| 4 | 细节清单 | `file names, full code snippets, function signatures, file edits` | 明确要求保留具体技术细节，防止过度抽象 |
| 5 | 用户反馈强调 | `Pay special attention to specific user feedback` | 确保用户纠正的行为在后续会话中不重蹈覆辙 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.88 | 新增 | 添加部分对话压缩指令，含结构化摘要格式和分析流程 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/7d7c728" target="_blank">7d7c728</a> |
