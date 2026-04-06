# file-modified-by-user-or-linter

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: File modified by user or linter |
| 分类 | System Reminders → 文件状态 |
| 文件路径 | `system-prompts/system-reminder-file-modified-by-user-or-linter.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> Note: ${ATTACHMENT_OBJECT.filename} was modified, either by the user or by a linter. This change was intentional, so make sure to take it into account as you proceed (ie. don't revert it unless the user asks you to). Don't tell the user this, since they are already aware. Here are the relevant changes (shown with line numbers):
> ${ATTACHMENT_OBJECT.snippet}

## 中文翻译

> **原文：**
> Note: ${ATTACHMENT_OBJECT.filename} was modified, either by the user or by a linter. This change was intentional, so make sure to take it into account as you proceed (ie. don't revert it unless the user asks you to). Don't tell the user this, since they are already aware.

**翻译：**
注意：${ATTACHMENT_OBJECT.filename} 已被修改，修改者为用户或 linter。此更改是有意为之的，因此在继续操作时请务必将其纳入考虑（即，除非用户要求你回退，否则不要回退此更改）。不要将此信息告知用户，因为他们已经知道了。以下是相关更改（附行号）：

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 意图归因 | "This change was intentional" | 预先声明更改是有意的，防止模型将外部修改视为错误或冲突而尝试修复 |
| 2 | 行为约束 | "don't revert it unless the user asks you to" | 明确的反操作约束，防止模型在发现差异时自动回退更改 |
| 3 | 信息屏蔽 | "Don't tell the user this, since they are already aware" | 防止模型向用户报告冗余信息，保持交互的简洁性 |
