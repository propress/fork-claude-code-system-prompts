# tool-usage-edit-files

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Tool usage (edit files) |
| 分类 | System Prompts → 工具使用策略 |
| 文件路径 | `system-prompts/system-prompt-tool-usage-edit-files.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${EDIT_TOOL_NAME}` |
| 首次出现版本 | 2.1.53 |

## 原文

> To edit files use ${EDIT_TOOL_NAME} instead of sed or awk

## 中文翻译

**翻译：**
编辑文件时使用 ${EDIT_TOOL_NAME} 而非 sed 或 awk。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `EDIT_TOOL_NAME` | 字符串 | 编辑文件工具的实际名称（如 Edit） |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 工具替代 | `instead of sed or awk` | 明确列出要替代的 shell 工具 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 拆分 | 从工具使用策略大文件中拆分 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
