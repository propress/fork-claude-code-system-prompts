# compact-file-reference

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Compact file reference |
| 分类 | System Reminders → 文件状态 |
| 文件路径 | `system-prompts/system-reminder-compact-file-reference.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}`, `${READ_TOOL_OBJECT}` |

## 原文

> Note: ${ATTACHMENT_OBJECT.filename} was read before the last conversation was summarized, but the contents are too large to include. Use ${READ_TOOL_OBJECT.name} tool if you need to access it.

## 中文翻译

> **原文：**
> Note: ${ATTACHMENT_OBJECT.filename} was read before the last conversation was summarized, but the contents are too large to include. Use ${READ_TOOL_OBJECT.name} tool if you need to access it.

**翻译：**
注意：${ATTACHMENT_OBJECT.filename} 在上次对话摘要生成之前已被读取，但内容过大无法包含在此处。如需访问，请使用 ${READ_TOOL_OBJECT.name} 工具。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 上下文恢复提示 | "was read before the last conversation was summarized" | 解释文件曾经被读取过但现在不在上下文中，帮助模型理解信息缺失的原因而非将其视为从未存在 |
| 2 | 工具引导 | "Use ${READ_TOOL_OBJECT.name} tool if you need to access it" | 提供明确的补救路径，避免模型因缺乏信息而编造文件内容 |
