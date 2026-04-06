# verify-plan-reminder

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Verify plan reminder |
| 分类 | System Reminders → 计划模式 |
| 文件路径 | `system-prompts/system-reminder-verify-plan-reminder.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${TASK_TOOL_NAME}` |

## 原文

> You have completed implementing the plan. Please call the "" tool directly (NOT the ${TASK_TOOL_NAME} tool or an agent) to verify that all plan items were completed correctly.

## 中文翻译

> **原文：**
> You have completed implementing the plan. Please call the "" tool directly (NOT the ${TASK_TOOL_NAME} tool or an agent) to verify that all plan items were completed correctly.

**翻译：**
你已完成计划的实施。请直接调用 "" 工具（而非 ${TASK_TOOL_NAME} 工具或代理）来验证所有计划项是否已正确完成。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 直接调用约束 | "call the tool directly (NOT the ${TASK_TOOL_NAME} tool or an agent)" | 排除间接调用方式，确保验证工具被直接执行而非委托给子代理，保证验证的可靠性 |
| 2 | 完成后验证 | "You have completed implementing the plan. Please...verify" | 在实施完成后立即触发验证步骤，形成"实施→验证"的闭环工作流 |
