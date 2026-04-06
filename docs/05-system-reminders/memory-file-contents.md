# memory-file-contents

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Memory file contents |
| 分类 | System Reminders → 技能与工具 |
| 文件路径 | `system-prompts/system-reminder-memory-file-contents.md` |
| CC 版本 | 2.1.79 |
| 模板变量 | `${MEMORY_ITEM}`, `${MEMORY_TYPE_DESCRIPTION}`, `${MEMORY_CONTENT}` |

## 原文

> Contents of ${MEMORY_ITEM.path}${MEMORY_TYPE_DESCRIPTION}:
>
> ${MEMORY_CONTENT}

## 中文翻译

> **原文：**
> Contents of ${MEMORY_ITEM.path}${MEMORY_TYPE_DESCRIPTION}:

**翻译：**
${MEMORY_ITEM.path}${MEMORY_TYPE_DESCRIPTION} 的内容：

${MEMORY_CONTENT}

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 记忆注入 | "Contents of ${MEMORY_ITEM.path}" | 将持久化记忆文件的内容注入当前上下文，使模型能够访问跨会话的知识和偏好设置 |
| 2 | 类型标注 | "${MEMORY_TYPE_DESCRIPTION}" | 标注记忆文件的类型描述，帮助模型理解内容的用途和优先级 |
