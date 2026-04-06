# hook-stopped-continuation

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Hook stopped continuation |
| 分类 | System Reminders → Hook 系统 |
| 文件路径 | `system-prompts/system-reminder-hook-stopped-continuation.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> ${ATTACHMENT_OBJECT.hookName} hook stopped continuation: ${ATTACHMENT_OBJECT.message}

## 中文翻译

> **原文：**
> ${ATTACHMENT_OBJECT.hookName} hook stopped continuation: ${ATTACHMENT_OBJECT.message}

**翻译：**
${ATTACHMENT_OBJECT.hookName} hook 已停止继续执行：${ATTACHMENT_OBJECT.message}

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 流程中断信号 | "stopped continuation" | 明确告知模型当前执行流程已被 hook 中断，模型需根据附带消息决定后续行为 |
| 2 | 消息传递 | "${ATTACHMENT_OBJECT.message}" | 传递 hook 提供的具体中断原因，使模型能够做出基于原因的判断 |
