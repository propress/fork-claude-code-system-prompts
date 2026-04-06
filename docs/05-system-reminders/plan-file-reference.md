# plan-file-reference

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Plan file reference |
| 分类 | System Reminders → 计划模式 |
| 文件路径 | `system-prompts/system-reminder-plan-file-reference.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> A plan file exists from plan mode at: ${ATTACHMENT_OBJECT.planFilePath}
>
> Plan contents:
>
> ${ATTACHMENT_OBJECT.planContent}
>
> If this plan is relevant to the current work and not already complete, continue working on it.

## 中文翻译

> **原文：**
> A plan file exists from plan mode at: ${ATTACHMENT_OBJECT.planFilePath}
>
> If this plan is relevant to the current work and not already complete, continue working on it.

**翻译：**
计划模式下的计划文件位于：${ATTACHMENT_OBJECT.planFilePath}

计划内容：

${ATTACHMENT_OBJECT.planContent}

如果此计划与当前工作相关且尚未完成，请继续执行该计划。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 条件执行 | "If this plan is relevant to the current work and not already complete" | 设置两个条件（相关性+未完成），防止模型盲目执行已过时或不相关的计划 |
| 2 | 上下文持久化 | "A plan file exists from plan mode at: ..." | 将计划文件路径和内容注入上下文，确保计划在会话中断后仍能被恢复和继续 |
