# taskcreate

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: TaskCreate |
| 分类 | Tool Descriptions → Agent 工具 |
| 文件路径 | `system-prompts/tool-description-taskcreate.md` |
| CC 版本 | 2.1.84 |
| 模板变量 | `${CONDTIONAL_TEAMMATES_NOTE}`, `${CONDITIONAL_TASK_NOTES}` |

## 原文

> Use this tool to create a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
> It also helps the user understand the progress of the task and overall progress of their requests.
>
> ## When to Use This Tool
>
> Use this tool proactively in these scenarios:
>
> - Complex multi-step tasks - When a task requires 3 or more distinct steps or actions
> - Non-trivial and complex tasks - Tasks that require careful planning or multiple operations${CONDTIONAL_TEAMMATES_NOTE}
> - Plan mode - When using plan mode, create a task list to track the work
> - User explicitly requests todo list - When the user directly asks you to use the todo list
> - User provides multiple tasks - When users provide a list of things to be done (numbered or comma-separated)
> - After receiving new instructions - Immediately capture user requirements as tasks
> - When you start working on a task - Mark it as in_progress BEFORE beginning work
> - After completing a task - Mark it as completed and add any new follow-up tasks discovered during implementation
>
> ## When NOT to Use This Tool
>
> Skip using this tool when:
> - There is only a single, straightforward task
> - The task is trivial and tracking it provides no organizational benefit
> - The task can be completed in less than 3 trivial steps
> - The task is purely conversational or informational
>
> NOTE that you should not use this tool if there is only one trivial task to do. In this case you are better off just doing the task directly.
>
> ## Task Fields
>
> - **subject**: A brief, actionable title in imperative form (e.g., "Fix authentication bug in login flow")
> - **description**: What needs to be done
> - **activeForm** (optional): Present continuous form shown in the spinner when the task is in_progress (e.g., "Fixing authentication bug"). If omitted, the spinner shows the subject instead.
>
> All tasks are created with status `pending`.
>
> ## Tips
>
> - Create tasks with clear, specific subjects that describe the outcome
> - After creating tasks, use TaskUpdate to set up dependencies (blocks/blockedBy) if needed
> ${CONDITIONAL_TASK_NOTES}- Check TaskList first to avoid creating duplicate tasks

## 中文翻译

> **原文：**
> Use this tool to create a structured task list for your current coding session.

**翻译：**
使用此工具为你当前的编码会话创建一个结构化的任务列表。这有助于你跟踪进度、组织复杂任务，并向用户展示工作的全面性。它还帮助用户了解任务进展和请求的整体完成情况。

> **原文：**
> ## When to Use This Tool

**翻译：**
## 何时使用此工具

在以下场景中主动使用此工具：
- **复杂多步骤任务** —— 当任务需要 3 个或更多不同的步骤或操作时
- **非平凡的复杂任务** —— 需要仔细规划或多步操作的任务
- **计划模式** —— 使用计划模式时，创建任务列表来跟踪工作
- **用户明确要求** —— 当用户直接要求使用待办列表时
- **用户提供多个任务** —— 当用户提供一个待办事项列表（编号或逗号分隔）时
- **收到新指令后** —— 立即将用户需求捕获为任务
- **开始任务时** —— 在开始工作之前将其标记为 in_progress
- **完成任务后** —— 标记为已完成，并添加实现过程中发现的后续任务

> **原文：**
> ## When NOT to Use This Tool

**翻译：**
## 何时不使用此工具

在以下情况跳过使用此工具：
- 只有一个简单明了的任务
- 任务微不足道，跟踪它不会带来组织上的好处
- 任务可以在少于 3 个简单步骤内完成
- 任务纯粹是对话性或信息性的

注意：如果只有一个微不足道的任务，不应使用此工具。这种情况下直接做任务更好。

> **原文：**
> ## Task Fields

**翻译：**
## 任务字段

- **subject**：简短的、可操作的祈使句标题（例如 "Fix authentication bug in login flow"）
- **description**：需要做什么
- **activeForm**（可选）：任务为 in_progress 时在加载动画中显示的现在进行时形式（例如 "Fixing authentication bug"）。省略时显示 subject。

所有任务创建时状态为 `pending`。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `CONDTIONAL_TEAMMATES_NOTE` | 字符串 | 条件性注释，在团队模式下追加队友相关说明 |
| `CONDITIONAL_TASK_NOTES` | 字符串 | 条件性注释，追加额外的任务使用提示 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 正反使用场景 | When to Use vs When NOT to Use | 用正反两面清晰定义工具的适用范围 |
| 2 | 数量阈值 | `3 or more distinct steps` | 用具体数字定义"复杂"的门槛 |
| 3 | 状态前置 | `Mark it as in_progress BEFORE beginning work` | 大写 BEFORE 强调状态更新必须先于工作 |
| 4 | 双形式字段 | subject（祈使句） + activeForm（进行时） | 为不同UI上下文准备适当的文本形式 |
