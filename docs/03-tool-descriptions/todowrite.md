# todowrite

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: TodoWrite |
| 分类 | Tool Descriptions → 通用工具 |
| 文件路径 | `system-prompts/tool-description-todowrite.md` |
| CC 版本 | 2.1.84 |
| 模板变量 | `${EDIT_TOOL_NAME}` |

## 原文

> Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
> It also helps the user understand the progress of the task and overall progress of their requests.
>
> ## When to Use This Tool
> Use this tool proactively in these scenarios:
>
> 1. Complex multi-step tasks - When a task requires 3 or more distinct steps or actions
> 2. Non-trivial and complex tasks - Tasks that require careful planning or multiple operations
> 3. User explicitly requests todo list - When the user directly asks you to use the todo list
> 4. User provides multiple tasks - When users provide a list of things to be done (numbered or comma-separated)
> 5. After receiving new instructions - Immediately capture user requirements as todos
> 6. When you start working on a task - Mark it as in_progress BEFORE beginning work. Ideally you should only have one todo as in_progress at a time
> 7. After completing a task - Mark it as completed and add any new follow-up tasks discovered during implementation
>
> ## When NOT to Use This Tool
>
> Skip using this tool when:
> 1. There is only a single, straightforward task
> 2. The task is trivial and tracking it provides no organizational benefit
> 3. The task can be completed in less than 3 trivial steps
> 4. The task is purely conversational or informational
>
> ## Task States and Management
>
> 1. **Task States**: pending, in_progress (limit to ONE at a time), completed
> 2. **Task descriptions** must have two forms:
>    - content: imperative form (e.g., "Run tests")
>    - activeForm: present continuous form (e.g., "Running tests")
> 3. **Task Management**: Update in real-time, mark complete IMMEDIATELY, exactly ONE task in_progress at any time
> 4. **Task Completion**: ONLY mark completed when FULLY accomplished. Never mark completed if tests fail, implementation is partial, or errors unresolved.

## 中文翻译

> **原文：**
> Use this tool to create and manage a structured task list for your current coding session.

**翻译：**
使用此工具为当前编码会话创建和管理结构化任务列表。这有助于你跟踪进度、组织复杂任务，并向用户展示工作全面性。

> **原文：**
> ## When to Use This Tool (7 scenarios)

**翻译：**
## 何时使用此工具

在以下场景中主动使用：
1. **复杂多步骤任务** —— 当任务需要 3 个或更多不同的步骤或操作
2. **非平凡的复杂任务** —— 需要仔细规划或多步操作的任务
3. **用户明确要求** —— 当用户直接要求使用待办列表
4. **用户提供多个任务** —— 当用户提供一个待办事项列表（编号或逗号分隔）
5. **收到新指令后** —— 立即将用户需求捕获为待办项
6. **开始任务时** —— 在开始工作之前标记为 in_progress。理想情况下同一时间只有一个待办项处于 in_progress
7. **完成任务后** —— 标记为已完成，并添加实现过程中发现的后续任务

> **原文：**
> ## When NOT to Use This Tool

**翻译：**
## 何时不使用此工具

在以下情况跳过：
1. 只有一个简单明了的任务
2. 任务微不足道，跟踪它不会带来组织上的好处
3. 任务可以在少于 3 个简单步骤内完成
4. 任务纯粹是对话性或信息性的

> **原文：**
> ## Task States and Management

**翻译：**
## 任务状态和管理

1. **任务状态**：pending（待办）、in_progress（进行中，限制同时只有一个）、completed（已完成）
2. **任务描述**必须有两种形式：
   - content：祈使句形式（如 "Run tests"）
   - activeForm：现在进行时形式（如 "Running tests"）
3. **任务管理**：实时更新状态，完成后立即标记，任何时候恰好有一个任务处于 in_progress
4. **完成标准**：仅在完全完成时标记为 completed。如果测试失败、实现不完整或有未解决的错误，绝不标记为已完成

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `EDIT_TOOL_NAME` | 字符串 | 编辑工具的实际名称，在示例中引用 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 正反示例教学 | 4个"何时用" + 4个"何时不用"的详细示例 | 用 example+reasoning 格式教会模型判断边界 |
| 2 | 单任务约束 | `limit to ONE task at a time` + `Exactly ONE ... in_progress` | 反复强调同一时间只能有一个进行中任务 |
| 3 | 双形式要求 | content（祈使句）+ activeForm（进行时） | 为 UI 不同上下文准备适当的文本 |
| 4 | 完成禁令 | `Never mark ... if: Tests are failing, Implementation is partial` | 用具体的禁止条件防止虚假完成 |
| 5 | 数量阈值 | `3 or more distinct steps` / `less than 3 trivial steps` | 用对称的数字阈值定义工具的使用/不使用边界 |
