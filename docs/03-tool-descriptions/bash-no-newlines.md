# bash-no-newlines

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (no newlines) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-no-newlines.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> DO NOT use newlines to separate commands (newlines are ok in quoted strings).

## 中文翻译

> **原文：**
> DO NOT use newlines to separate commands (newlines are ok in quoted strings).

**翻译：**
不要使用换行符来分隔命令（在引号字符串中换行是可以的）。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | `DO NOT use newlines to separate commands` | 使用大写"DO NOT"强调禁止行为，明确不允许用换行符分隔命令，防止命令解析错误。 |
| 2 | 范围限定（Scope Limitation） | `(newlines are ok in quoted strings)` | 用括号补充说明例外情况，限定禁令的适用范围，避免过度限制导致引号内字符串的格式问题。 |
