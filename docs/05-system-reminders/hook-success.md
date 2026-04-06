# hook-success

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Hook success |
| 分类 | System Reminders → Hook 系统 |
| 文件路径 | `system-prompts/system-reminder-hook-success.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> ${ATTACHMENT_OBJECT.hookName} hook success: ${ATTACHMENT_OBJECT.content}

## 中文翻译

> **原文：**
> ${ATTACHMENT_OBJECT.hookName} hook success: ${ATTACHMENT_OBJECT.content}

**翻译：**
${ATTACHMENT_OBJECT.hookName} hook 执行成功：${ATTACHMENT_OBJECT.content}

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 状态反馈 | "hook success" | 向模型反馈 hook 执行的成功状态，使模型了解操作流程中的进展 |
| 2 | 结果传递 | "${ATTACHMENT_OBJECT.content}" | 传递 hook 执行成功后的输出内容，模型可利用此信息进行后续决策 |
