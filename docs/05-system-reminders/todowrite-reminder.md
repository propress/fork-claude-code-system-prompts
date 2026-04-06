# todowrite-reminder

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: TodoWrite reminder |
| 分类 | System Reminders → 团队协作 |
| 文件路径 | `system-prompts/system-reminder-todowrite-reminder.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | 无 |

## 原文

> The TodoWrite tool hasn't been used recently. If you're working on tasks that would benefit from tracking progress, consider using the TodoWrite tool to track progress. Also consider cleaning up the todo list if has become stale and no longer matches what you are working on. Only use it if it's relevant to the current work. This is just a gentle reminder - ignore if not applicable. Make sure that you NEVER mention this reminder to the user

## 中文翻译

> **原文：**
> The TodoWrite tool hasn't been used recently. If you're working on tasks that would benefit from tracking progress, consider using the TodoWrite tool to track progress. Also consider cleaning up the todo list if has become stale and no longer matches what you are working on. Only use it if it's relevant to the current work. This is just a gentle reminder - ignore if not applicable. Make sure that you NEVER mention this reminder to the user

**翻译：**
TodoWrite 工具近期未被使用。如果你正在进行需要跟踪进度的工作，考虑使用 TodoWrite 工具来跟踪进度。如果待办事项列表已过时且不再与当前工作匹配，也请考虑清理。仅在与当前工作相关时使用。这只是一个温和的提醒——如不适用请忽略。确保你**绝对不要**将此提醒告知用户。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 定期触发式提醒 | "The TodoWrite tool hasn't been used recently" | 基于工具使用频率触发提醒，而非定时触发，更符合实际工作场景 |
| 2 | 低压力措辞 | "consider using" + "gentle reminder" + "ignore if not applicable" | 多层次的低压力措辞避免模型在不需要时强制使用工具 |
| 3 | 隐式提醒模式 | "NEVER mention this reminder to the user" | 将此设计为系统内部的隐式提醒，保持用户体验的无缝性 |
