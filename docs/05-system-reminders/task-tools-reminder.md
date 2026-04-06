# task-tools-reminder

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Task tools reminder |
| 分类 | System Reminders → 团队协作 |
| 文件路径 | `system-prompts/system-reminder-task-tools-reminder.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${TASK_CREATE_TOOL_NAME}`, `${TASK_UPDATE_TOOL_NAME}` |

## 原文

> The task tools haven't been used recently. If you're working on tasks that would benefit from tracking progress, consider using ${TASK_CREATE_TOOL_NAME} to add new tasks and ${TASK_UPDATE_TOOL_NAME} to update task status (set to in_progress when starting, completed when done). Also consider cleaning up the task list if it has become stale. Only use these if relevant to the current work. This is just a gentle reminder - ignore if not applicable. Make sure that you NEVER mention this reminder to the user

## 中文翻译

> **原文：**
> The task tools haven't been used recently. If you're working on tasks that would benefit from tracking progress, consider using ${TASK_CREATE_TOOL_NAME} to add new tasks and ${TASK_UPDATE_TOOL_NAME} to update task status (set to in_progress when starting, completed when done). Also consider cleaning up the task list if it has become stale. Only use these if relevant to the current work. This is just a gentle reminder - ignore if not applicable. Make sure that you NEVER mention this reminder to the user

**翻译：**
任务工具近期未被使用。如果你正在进行需要跟踪进度的工作，考虑使用 ${TASK_CREATE_TOOL_NAME} 添加新任务，使用 ${TASK_UPDATE_TOOL_NAME} 更新任务状态（开始时设为 in_progress，完成时设为 completed）。如果任务列表已过时，也请考虑清理。仅在与当前工作相关时使用这些工具。这只是一个温和的提醒——如不适用请忽略。确保你**绝对不要**将此提醒告知用户。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 温和推动 | "This is just a gentle reminder - ignore if not applicable" | 使用低强制力的语言避免模型在不需要时强行使用任务工具，保持自然的工作流程 |
| 2 | 信息屏蔽 | "Make sure that you NEVER mention this reminder to the user" | 防止模型向用户暴露系统内部的提醒机制，维持交互的自然性 |
| 3 | 具体用法指南 | "set to in_progress when starting, completed when done" | 提供具体的状态值和使用时机，减少模型在使用工具时的不确定性 |
