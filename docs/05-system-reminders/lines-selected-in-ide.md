# lines-selected-in-ide

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Lines selected in IDE |
| 分类 | System Reminders → 技能与工具 |
| 文件路径 | `system-prompts/system-reminder-lines-selected-in-ide.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}`, `${TRUNCATED_CONTENT}` |

## 原文

> The user selected the lines ${ATTACHMENT_OBJECT.lineStart} to ${ATTACHMENT_OBJECT.lineEnd} from ${ATTACHMENT_OBJECT.filename}:
> ${TRUNCATED_CONTENT}
>
> This may or may not be related to the current task.

## 中文翻译

> **原文：**
> The user selected the lines ${ATTACHMENT_OBJECT.lineStart} to ${ATTACHMENT_OBJECT.lineEnd} from ${ATTACHMENT_OBJECT.filename}:

**翻译：**
用户从 ${ATTACHMENT_OBJECT.filename} 中选择了第 ${ATTACHMENT_OBJECT.lineStart} 行到第 ${ATTACHMENT_OBJECT.lineEnd} 行：
${TRUNCATED_CONTENT}

这可能与当前任务有关，也可能无关。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 精确定位 | "lines ${ATTACHMENT_OBJECT.lineStart} to ${ATTACHMENT_OBJECT.lineEnd}" | 提供精确的行号范围，使模型能够准确理解用户关注的代码区域 |
| 2 | 不确定性标注 | "This may or may not be related to the current task" | 防止模型对用户选择行为做出过度解读，保持判断的灵活性 |
