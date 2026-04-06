# file-truncated

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: File truncated |
| 分类 | System Reminders → 文件状态 |
| 文件路径 | `system-prompts/system-reminder-file-truncated.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}`, `${MAX_LINES_CONSTANT}`, `${READ_TOOL_OBJECT}` |

## 原文

> Note: The file ${ATTACHMENT_OBJECT.filename} was too large and has been truncated to the first ${MAX_LINES_CONSTANT} lines. Don't tell the user about this truncation. Use ${READ_TOOL_OBJECT.name} to read more of the file if you need.

## 中文翻译

> **原文：**
> Note: The file ${ATTACHMENT_OBJECT.filename} was too large and has been truncated to the first ${MAX_LINES_CONSTANT} lines. Don't tell the user about this truncation. Use ${READ_TOOL_OBJECT.name} to read more of the file if you need.

**翻译：**
注意：文件 ${ATTACHMENT_OBJECT.filename} 过大，已被截断至前 ${MAX_LINES_CONSTANT} 行。不要将截断信息告知用户。如需查看更多内容，请使用 ${READ_TOOL_OBJECT.name} 工具。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 信息屏蔽 | "Don't tell the user about this truncation" | 防止模型向用户暴露系统内部的截断机制，保持用户体验的流畅性 |
| 2 | 补救路径 | "Use ${READ_TOOL_OBJECT.name} to read more of the file if you need" | 提供工具使用指引作为应对截断的解决方案，确保模型不会在信息不完整时做出错误判断 |
| 3 | 量化边界 | "truncated to the first ${MAX_LINES_CONSTANT} lines" | 精确说明截断范围，帮助模型理解当前拥有的信息边界 |
