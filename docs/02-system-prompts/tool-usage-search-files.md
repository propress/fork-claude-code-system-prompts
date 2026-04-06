# tool-usage-search-files

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Tool usage (search files) |
| 分类 | System Prompts → 工具使用策略 |
| 文件路径 | `system-prompts/system-prompt-tool-usage-search-files.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${GLOB_TOOL_NAME}` |
| 首次出现版本 | 2.1.53 |

## 原文

> To search for files use ${GLOB_TOOL_NAME} instead of find or ls

## 中文翻译

**翻译：**
搜索文件时使用 ${GLOB_TOOL_NAME} 而非 find 或 ls。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `GLOB_TOOL_NAME` | 字符串 | 文件搜索工具的实际名称（如 Glob） |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 拆分 | 从工具使用策略大文件中拆分 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
