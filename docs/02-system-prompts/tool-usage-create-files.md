# tool-usage-create-files

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Tool usage (create files) |
| 分类 | System Prompts → 工具使用策略 |
| 文件路径 | `system-prompts/system-prompt-tool-usage-create-files.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${WRITE_TOOL_NAME}` |
| 首次出现版本 | 2.1.53 |

## 原文

> To create files use ${WRITE_TOOL_NAME} instead of cat with heredoc or echo redirection

## 中文翻译

**翻译：**
创建文件时使用 ${WRITE_TOOL_NAME} 而非 cat heredoc 或 echo 重定向。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `WRITE_TOOL_NAME` | 字符串 | 写文件工具的实际名称（如 Write） |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 工具重定向 | `instead of cat with heredoc or echo redirection` | 明确列出要替代的具体 shell 模式 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 拆分 | 从工具使用策略大文件中拆分 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
