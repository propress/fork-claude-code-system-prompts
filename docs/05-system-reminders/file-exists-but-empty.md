# file-exists-but-empty

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: File exists but empty |
| 分类 | System Reminders → 文件状态 |
| 文件路径 | `system-prompts/system-reminder-file-exists-but-empty.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | 无 |

## 原文

> Warning: the file exists but the contents are empty.

## 中文翻译

> **原文：**
> Warning: the file exists but the contents are empty.

**翻译：**
警告：文件存在但内容为空。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 消歧义声明 | "the file exists but the contents are empty" | 区分"文件不存在"和"文件存在但为空"两种情况，防止模型将空内容误解为读取错误 |
| 2 | XML 标签包裹 | `<system-reminder>...</system-reminder>` | 使用结构化标签将系统提醒与其他内容隔离，确保模型将其识别为系统级通知 |
