# tool-usage-search-content

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Tool usage (search content) |
| 分类 | System Prompts → 工具使用策略 |
| 文件路径 | `system-prompts/system-prompt-tool-usage-search-content.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${GREP_TOOL_NAME}` |
| 首次出现版本 | 2.1.53 |

## 原文

> To search the content of files, use ${GREP_TOOL_NAME} instead of grep or rg

## 中文翻译

**翻译：**
搜索文件内容时，使用 ${GREP_TOOL_NAME} 而非 grep 或 rg。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `GREP_TOOL_NAME` | 字符串 | 内容搜索工具的实际名称（如 Grep） |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 拆分 | 从工具使用策略大文件中拆分 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
