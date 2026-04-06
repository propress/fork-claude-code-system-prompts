# bash-alternative-edit-files

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (alternative — edit files) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-alternative-edit-files.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${EDIT_TOOL_NAME}` |

## 原文

> Edit files: Use ${EDIT_TOOL_NAME} (NOT sed/awk)

## 中文翻译

> **原文：**
> Edit files: Use ${EDIT_TOOL_NAME} (NOT sed/awk)

**翻译：**
编辑文件：使用 ${EDIT_TOOL_NAME}（不要使用 sed/awk）

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${EDIT_TOOL_NAME}` | 文件编辑工具的名称 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 简洁指令（Concise Instruction） | `Edit files: Use ${EDIT_TOOL_NAME}` | 一行指令明确指定文件编辑应使用的专用工具。 |
| 2 | 负面约束（Negative Constraint） | `(NOT sed/awk)` | 明确禁止使用 sed/awk 等命令行文本处理工具进行文件编辑，因为专用编辑工具提供更好的审查和权限控制体验。 |
