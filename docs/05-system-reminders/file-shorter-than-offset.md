# file-shorter-than-offset

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: File shorter than offset |
| 分类 | System Reminders → 文件状态 |
| 文件路径 | `system-prompts/system-reminder-file-shorter-than-offset.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${RESULT_OBJECT}` |

## 原文

> Warning: the file exists but is shorter than the provided offset (${RESULT_OBJECT.file.startLine}). The file has ${RESULT_OBJECT.file.totalLines} lines.

## 中文翻译

> **原文：**
> Warning: the file exists but is shorter than the provided offset (${RESULT_OBJECT.file.startLine}). The file has ${RESULT_OBJECT.file.totalLines} lines.

**翻译：**
警告：文件存在但长度不足以到达所提供的偏移量（${RESULT_OBJECT.file.startLine}）。该文件共有 ${RESULT_OBJECT.file.totalLines} 行。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 精确错误报告 | "shorter than the provided offset (${RESULT_OBJECT.file.startLine})" | 提供具体的偏移量数值，帮助模型理解错误的确切原因并做出正确的后续决策 |
| 2 | 补充数据提供 | "The file has ${RESULT_OBJECT.file.totalLines} lines" | 提供文件实际行数作为参考数据，使模型能够自行计算正确的偏移量 |
