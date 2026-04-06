# bash-alternative-read-files

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (alternative — read files) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-alternative-read-files.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${READ_TOOL_NAME}` |

## 原文

> Read files: Use ${READ_TOOL_NAME} (NOT cat/head/tail)

## 中文翻译

> **原文：**
> Read files: Use ${READ_TOOL_NAME} (NOT cat/head/tail)

**翻译：**
读取文件：使用 ${READ_TOOL_NAME}（不要使用 cat/head/tail）

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${READ_TOOL_NAME}` | 文件读取工具的名称 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 简洁指令（Concise Instruction） | `Read files: Use ${READ_TOOL_NAME}` | 一行指令明确指定文件读取应使用的专用工具。 |
| 2 | 负面约束（Negative Constraint） | `(NOT cat/head/tail)` | 明确禁止使用 cat、head、tail 等命令行工具读取文件，确保模型使用可以提供更好审查体验的内置工具。 |
