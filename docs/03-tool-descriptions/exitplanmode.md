# exitplanmode

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: ExitPlanMode |
| 分类 | Tool Descriptions → 计划模式 |
| 文件路径 | `system-prompts/tool-description-exitplanmode.md` |
| CC 版本 | 2.1.14 |
| 模板变量 | 无 |

## 原文

> Use this tool when you are in plan mode and have finished writing your plan to the plan file and are ready for user approval.
>
> ## How This Tool Works
> - You should have already written your plan to the plan file specified in the plan mode system message
> - This tool does NOT take the plan content as a parameter - it will read the plan from the file you wrote
> - This tool simply signals that you're done planning and ready for the user to review and approve
> - The user will see the contents of your plan file when they review it
>
> ## When to Use This Tool
> IMPORTANT: Only use this tool when the task requires planning the implementation steps of a task that requires writing code. For research tasks where you're gathering information, searching files, reading files or in general trying to understand the codebase - do NOT use this tool.
>
> ## Before Using This Tool
> Ensure your plan is complete and unambiguous:
> - If you have unresolved questions about requirements or approach, use AskUserQuestion first (in earlier phases)
> - Once your plan is finalized, use THIS tool to request approval
>
> **Important:** Do NOT use AskUserQuestion to ask "Is this plan okay?" or "Should I proceed?" - that's exactly what THIS tool does. ExitPlanMode inherently requests user approval of your plan.
>
> ## Examples
>
> 1. Initial task: "Search for and understand the implementation of vim mode in the codebase" - Do not use the exit plan mode tool because you are not planning the implementation steps of a task.
> 2. Initial task: "Help me implement yank mode for vim" - Use the exit plan mode tool after you have finished planning the implementation steps of the task.
> 3. Initial task: "Add a new feature to handle user authentication" - If unsure about auth method (OAuth, JWT, etc.), use AskUserQuestion first, then use exit plan mode tool after clarifying the approach.

## 中文翻译

> **原文：**
> Use this tool when you are in plan mode and have finished writing your plan to the plan file and are ready for user approval.

**翻译：**
当你处于计划模式且已将计划写入计划文件，准备好让用户审批时，使用此工具。

---

> **原文：**
> ## How This Tool Works
> - You should have already written your plan to the plan file specified in the plan mode system message
> - This tool does NOT take the plan content as a parameter - it will read the plan from the file you wrote
> - This tool simply signals that you're done planning and ready for the user to review and approve
> - The user will see the contents of your plan file when they review it

**翻译：**
## 此工具如何工作
- 你应该已经将计划写入计划模式系统消息中指定的计划文件
- 此工具不接受计划内容作为参数——它会从你写入的文件中读取计划
- 此工具只是发出信号，表示你已完成计划并准备好让用户审查和批准
- 用户在审查时将看到你计划文件的内容

---

> **原文：**
> ## When to Use This Tool
> IMPORTANT: Only use this tool when the task requires planning the implementation steps of a task that requires writing code. For research tasks where you're gathering information, searching files, reading files or in general trying to understand the codebase - do NOT use this tool.

**翻译：**
## 何时使用此工具
重要：仅在任务需要规划编写代码的实现步骤时使用此工具。对于收集信息、搜索文件、读取文件或总体上试图理解代码库的研究任务——不要使用此工具。

---

> **原文：**
> ## Before Using This Tool
> Ensure your plan is complete and unambiguous:
> - If you have unresolved questions about requirements or approach, use AskUserQuestion first (in earlier phases)
> - Once your plan is finalized, use THIS tool to request approval

**翻译：**
## 使用此工具之前
确保你的计划完整且无歧义：
- 如果你对需求或方案有未解决的问题，先使用 AskUserQuestion（在早期阶段）
- 一旦计划最终确定，使用此工具来请求审批

---

> **原文：**
> **Important:** Do NOT use AskUserQuestion to ask "Is this plan okay?" or "Should I proceed?" - that's exactly what THIS tool does. ExitPlanMode inherently requests user approval of your plan.

**翻译：**
**重要：** 不要使用 AskUserQuestion 来问"这个计划可以吗？"或"我应该继续吗？"——这正是此工具的功能。ExitPlanMode 本质上就是请求用户对你的计划进行审批。

---

> **原文：**
> ## Examples
>
> 1. Initial task: "Search for and understand the implementation of vim mode in the codebase" - Do not use the exit plan mode tool because you are not planning the implementation steps of a task.
> 2. Initial task: "Help me implement yank mode for vim" - Use the exit plan mode tool after you have finished planning the implementation steps of the task.
> 3. Initial task: "Add a new feature to handle user authentication" - If unsure about auth method (OAuth, JWT, etc.), use AskUserQuestion first, then use exit plan mode tool after clarifying the approach.

**翻译：**
## 示例

1. 初始任务："搜索并理解代码库中 vim 模式的实现"——不要使用退出计划模式工具，因为你并非在规划任务的实现步骤。
2. 初始任务："帮我实现 vim 的 yank 模式"——在完成任务实现步骤的计划后使用退出计划模式工具。
3. 初始任务："添加处理用户认证的新功能"——如果不确定认证方式（OAuth、JWT 等），先使用 AskUserQuestion，然后在明确方案后使用退出计划模式工具。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 范围限定（Scope Limitation） | `Only use this tool when the task requires planning the implementation steps of a task that requires writing code` | 精确限定工具的适用范围为"需要写代码的实现规划"，排除了研究类任务，避免 LLM 在探索性任务中误触发审批流程。 |
| 2 | 负面约束（Negative Constraint） | `Do NOT use AskUserQuestion to ask "Is this plan okay?" or "Should I proceed?"` | 明确禁止使用其他工具来实现本工具的功能，防止 LLM 在工具选择上产生混淆，确保工作流的正确性。 |
| 3 | 示例引导（Example-driven Guidance） | 三个不同场景的示例（研究任务、实现任务、需要先澄清的任务） | 通过覆盖三种常见场景的示例，帮助 LLM 准确判断何时使用、何时不使用、何时需要先做其他操作。 |
| 4 | 结构化列表（Structured Enumeration） | `How This Tool Works` / `When to Use` / `Before Using` / `Examples` | 按工具理解的逻辑顺序组织信息：先理解机制，再了解时机，再看前置条件，最后通过示例验证理解。 |
| 5 | 安全防护指令（Safety Guard） | `Ensure your plan is complete and unambiguous` | 在触发工具前设置质量检查点，确保计划完整后才请求审批，避免向用户展示不完整的方案。 |
