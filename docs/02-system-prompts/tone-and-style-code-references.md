# tone-and-style-code-references

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Tone and style (code references) |
| 分类 | System Prompts → 输出风格 |
| 文件路径 | `system-prompts/system-prompt-tone-and-style-code-references.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.53 |

## 原文

> When referencing specific functions or pieces of code include the pattern file_path:line_number to allow the user to easily navigate to the source code location.

## 中文翻译

> **原文：**
> When referencing specific functions or pieces of code include the pattern file_path:line_number to allow the user to easily navigate to the source code location.

**翻译：**
当引用特定函数或代码片段时，包含 file_path:line_number 模式，以便用户轻松导航到源代码位置。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 格式规范 | `file_path:line_number` | 定义具体的引用格式而非模糊要求"标注位置" |
| 2 | 用户价值导向 | `to allow the user to easily navigate` | 解释格式要求的目的（用户导航），增加遵守动机 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 拆分 | 从"Tone and style"大文件中拆分为独立子提示词 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
