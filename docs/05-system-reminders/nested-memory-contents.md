# nested-memory-contents

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Nested memory contents |
| 分类 | System Reminders → 技能与工具 |
| 文件路径 | `system-prompts/system-reminder-nested-memory-contents.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> Contents of ${ATTACHMENT_OBJECT.content.path}:
>
> ${ATTACHMENT_OBJECT.content.content}

## 中文翻译

> **原文：**
> Contents of ${ATTACHMENT_OBJECT.content.path}:

**翻译：**
${ATTACHMENT_OBJECT.content.path} 的内容：

${ATTACHMENT_OBJECT.content.content}

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 嵌套记忆加载 | "Contents of ${ATTACHMENT_OBJECT.content.path}" | 支持嵌套结构的记忆文件加载，使记忆系统能够以层次化方式组织和注入信息 |
| 2 | 路径透明 | "${ATTACHMENT_OBJECT.content.path}" | 显示记忆文件的完整路径，帮助模型追踪信息来源并在需要时重新访问 |
