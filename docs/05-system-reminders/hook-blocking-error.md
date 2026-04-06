# hook-blocking-error

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Hook blocking error |
| 分类 | System Reminders → Hook 系统 |
| 文件路径 | `system-prompts/system-reminder-hook-blocking-error.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> ${ATTACHMENT_OBJECT.hookName} hook blocking error from command: "${ATTACHMENT_OBJECT.blockingError.command}": ${ATTACHMENT_OBJECT.blockingError.blockingError}

## 中文翻译

> **原文：**
> ${ATTACHMENT_OBJECT.hookName} hook blocking error from command: "${ATTACHMENT_OBJECT.blockingError.command}": ${ATTACHMENT_OBJECT.blockingError.blockingError}

**翻译：**
${ATTACHMENT_OBJECT.hookName} hook 阻塞性错误，来自命令："${ATTACHMENT_OBJECT.blockingError.command}"：${ATTACHMENT_OBJECT.blockingError.blockingError}

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 错误链追踪 | "hook blocking error from command: ... : ..." | 提供完整的错误链（hook 名称 → 命令 → 错误详情），帮助模型理解错误的根本原因 |
| 2 | 阻塞性语义 | "blocking error" | 使用"blocking"一词暗示此错误阻止了后续操作，引导模型将其视为需要处理的严重错误 |
