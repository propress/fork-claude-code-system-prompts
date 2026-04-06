# tool-usage-read-files

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Tool usage (read files) |
| 分类 | System Prompts → 工具使用策略 |
| 文件路径 | `system-prompts/system-prompt-tool-usage-read-files.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${READ_TOOL_NAME}` |
| 首次出现版本 | 2.1.53 |

## 原文

> To read files use ${READ_TOOL_NAME} instead of cat, head, tail, or sed

## 中文翻译

**翻译：**
读取文件时使用 ${READ_TOOL_NAME} 而非 cat、head、tail 或 sed。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `READ_TOOL_NAME` | 字符串 | 读文件工具的实际名称（如 Read） |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 完整替代清单 | `instead of cat, head, tail, or sed` | 列出所有需要替代的 shell 读文件命令 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 拆分 | 从工具使用策略大文件中拆分 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
