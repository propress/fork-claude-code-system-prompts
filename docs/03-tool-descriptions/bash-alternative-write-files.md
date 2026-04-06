# bash-alternative-write-files

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (alternative — write files) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-alternative-write-files.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${WRITE_TOOL_NAME}` |

## 原文

> Write files: Use ${WRITE_TOOL_NAME} (NOT echo >/cat <<EOF)

## 中文翻译

> **原文：**
> Write files: Use ${WRITE_TOOL_NAME} (NOT echo >/cat <<EOF)

**翻译：**
写入文件：使用 ${WRITE_TOOL_NAME}（不要使用 echo > 或 cat <<EOF）

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${WRITE_TOOL_NAME}` | 文件写入工具的名称 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 简洁指令（Concise Instruction） | `Write files: Use ${WRITE_TOOL_NAME}` | 一行指令明确指定文件写入应使用的专用工具。 |
| 2 | 负面约束（Negative Constraint） | `(NOT echo >/cat <<EOF)` | 明确禁止使用 shell 重定向和 heredoc 方式写入文件，避免潜在的格式问题和安全风险，引导使用专用写入工具。 |
