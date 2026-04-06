# output-style-active

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Output style active |
| 分类 | System Reminders → 会话管理 |
| 文件路径 | `system-prompts/system-reminder-output-style-active.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${OUTPUT_STYLE_CONFIG}` |

## 原文

> ${OUTPUT_STYLE_CONFIG.name} output style is active. Remember to follow the specific guidelines for this style.

## 中文翻译

> **原文：**
> ${OUTPUT_STYLE_CONFIG.name} output style is active. Remember to follow the specific guidelines for this style.

**翻译：**
${OUTPUT_STYLE_CONFIG.name} 输出风格已激活。请记得遵循该风格的具体指导方针。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 状态提醒 | "output style is active" | 作为持续性提醒，确保模型在整个会话过程中保持特定的输出风格 |
| 2 | 规范引用 | "Remember to follow the specific guidelines for this style" | 使用"Remember"触发模型对已加载风格规则的回忆，而非重复列出所有规则 |
