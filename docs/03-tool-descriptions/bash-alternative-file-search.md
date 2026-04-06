# bash-alternative-file-search

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (alternative — file search) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-alternative-file-search.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${GLOB_TOOL_NAME}` |

## 原文

> File search: Use ${GLOB_TOOL_NAME} (NOT find or ls)

## 中文翻译

> **原文：**
> File search: Use ${GLOB_TOOL_NAME} (NOT find or ls)

**翻译：**
文件搜索：使用 ${GLOB_TOOL_NAME}（不要使用 find 或 ls）

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${GLOB_TOOL_NAME}` | 文件匹配（glob）工具的名称 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 简洁指令（Concise Instruction） | `File search: Use ${GLOB_TOOL_NAME}` | 一行指令明确指定文件搜索应使用的专用工具。 |
| 2 | 负面约束（Negative Constraint） | `(NOT find or ls)` | 明确禁止使用 find 或 ls 命令进行文件搜索，引导模型使用更高效的内置 glob 工具。 |
