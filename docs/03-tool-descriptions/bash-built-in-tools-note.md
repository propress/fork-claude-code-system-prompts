# bash-built-in-tools-note

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (built-in tools note) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-built-in-tools-note.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${BASH_TOOL_NAME}` |

## 原文

> While the ${BASH_TOOL_NAME} tool can do similar things, it's better to use the built-in tools as they provide a better user experience and make it easier to review tool calls and give permission.

## 中文翻译

> **原文：**
> While the ${BASH_TOOL_NAME} tool can do similar things, it's better to use the built-in tools as they provide a better user experience and make it easier to review tool calls and give permission.

**翻译：**
虽然 ${BASH_TOOL_NAME} 工具可以完成类似的操作，但最好使用内置工具，因为它们提供更好的用户体验，并且更便于审查工具调用和授予权限。

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${BASH_TOOL_NAME}` | Bash 工具的名称 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 优先级排序（Priority Ordering） | `it's better to use the built-in tools` | 虽然承认 Bash 工具具备相同能力，但明确表示内置工具优先，建立了工具选择的优先级层次。 |
| 2 | 简洁指令（Concise Instruction） | `provide a better user experience and make it easier to review tool calls and give permission` | 简洁地给出两个具体理由（更好的用户体验、更容易审查和授权），使优先级建议具有说服力。 |
