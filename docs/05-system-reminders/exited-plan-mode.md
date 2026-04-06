# exited-plan-mode

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Exited plan mode |
| 分类 | System Reminders → 计划模式 |
| 文件路径 | `system-prompts/system-reminder-exited-plan-mode.md` |
| CC 版本 | 2.1.30 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> ## Exited Plan Mode
>
> You have exited plan mode. You can now make edits, run tools, and take actions.${ATTACHMENT_OBJECT.planExists?` The plan file is located at ${ATTACHMENT_OBJECT.planFilePath} if you need to reference it.`:""}

## 中文翻译

> **原文：**
> You have exited plan mode. You can now make edits, run tools, and take actions.

**翻译：**
你已退出计划模式。你现在可以进行编辑、运行工具和执行操作。如果计划文件存在，其路径为 ${ATTACHMENT_OBJECT.planFilePath}，可供参考。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 状态切换声明 | "You have exited plan mode. You can now make edits, run tools, and take actions." | 明确地告知模型状态已变更，解除之前计划模式中"不允许编辑"的约束 |
| 2 | 条件性信息注入 | `${ATTACHMENT_OBJECT.planExists?...:""}` | 使用条件模板，仅在计划文件存在时才提供路径引用，避免输出无效信息 |
