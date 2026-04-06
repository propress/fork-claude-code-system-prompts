# hook-additional-context

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Hook additional context |
| 分类 | System Reminders → Hook 系统 |
| 文件路径 | `system-prompts/system-reminder-hook-additional-context.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> ${ATTACHMENT_OBJECT.hookName} hook additional context: ${ATTACHMENT_OBJECT.content.join(\`\n\`)}

## 中文翻译

> **原文：**
> ${ATTACHMENT_OBJECT.hookName} hook additional context: ${ATTACHMENT_OBJECT.content.join(\`\n\`)}

**翻译：**
${ATTACHMENT_OBJECT.hookName} hook 附加上下文：${ATTACHMENT_OBJECT.content.join(\`\n\`)}

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 动态上下文注入 | "hook additional context" | 通过 hook 机制向模型注入运行时动态生成的附加上下文，扩展模型的决策信息源 |
| 2 | 来源标注 | "${ATTACHMENT_OBJECT.hookName} hook" | 明确标注上下文来源于哪个 hook，帮助模型区分不同来源的信息权重 |
