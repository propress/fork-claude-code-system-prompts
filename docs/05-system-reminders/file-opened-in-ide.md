# file-opened-in-ide

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: File opened in IDE |
| 分类 | System Reminders → 文件状态 |
| 文件路径 | `system-prompts/system-reminder-file-opened-in-ide.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> The user opened the file ${ATTACHMENT_OBJECT.filename} in the IDE. This may or may not be related to the current task.

## 中文翻译

> **原文：**
> The user opened the file ${ATTACHMENT_OBJECT.filename} in the IDE. This may or may not be related to the current task.

**翻译：**
用户在 IDE 中打开了文件 ${ATTACHMENT_OBJECT.filename}。这可能与当前任务有关，也可能无关。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 不确定性标注 | "This may or may not be related to the current task" | 明确标注信息的不确定性，防止模型过度解读用户打开文件的行为，同时也不完全忽略该信号 |
| 2 | 环境感知注入 | "The user opened the file...in the IDE" | 将 IDE 环境中的用户行为作为上下文信号传递给模型，增强模型对用户工作状态的感知 |
