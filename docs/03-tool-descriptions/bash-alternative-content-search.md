# bash-alternative-content-search

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (alternative — content search) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-alternative-content-search.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${GREP_TOOL_NAME}` |

## 原文

> Content search: Use ${GREP_TOOL_NAME} (NOT grep or rg)

## 中文翻译

> **原文：**
> Content search: Use ${GREP_TOOL_NAME} (NOT grep or rg)

**翻译：**
内容搜索：使用 ${GREP_TOOL_NAME}（不要使用 grep 或 rg）

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${GREP_TOOL_NAME}` | 搜索（grep）工具的名称 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 简洁指令（Concise Instruction） | `Content search: Use ${GREP_TOOL_NAME}` | 一行指令明确指定内容搜索应使用的专用工具，简洁高效。 |
| 2 | 负面约束（Negative Constraint） | `(NOT grep or rg)` | 明确禁止使用命令行的 grep 或 rg，引导模型使用内置的搜索工具以获得更好的用户体验。 |
