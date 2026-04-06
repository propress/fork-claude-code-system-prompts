# tool-usage-direct-search

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Tool usage (direct search) |
| 分类 | System Prompts → 工具使用策略 |
| 文件路径 | `system-prompts/system-prompt-tool-usage-direct-search.md` |
| CC 版本 | 2.1.72 |
| 模板变量 | `${SEARCH_TOOLS}` |
| 首次出现版本 | 2.1.53 |

## 原文

> For simple, directed codebase searches (e.g. for a specific file/class/function) use ${SEARCH_TOOLS} directly.

## 中文翻译

**翻译：**
对于简单的、有针对性的代码库搜索（例如搜索特定文件/类/函数），直接使用 ${SEARCH_TOOLS}。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `SEARCH_TOOLS` | 字符串 | 搜索工具名称（如 Glob/Grep） |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 场景匹配 | `simple, directed ... (e.g. for a specific file/class/function)` | 用具体示例定义"简单搜索"的范围 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.72 | 修改 | 泛化为统一的搜索工具引用 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/7a45418" target="_blank">7a45418</a> |
| 2.1.53 | 拆分 | 从工具使用策略大文件中拆分 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
