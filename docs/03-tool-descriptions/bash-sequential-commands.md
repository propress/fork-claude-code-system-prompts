# bash-sequential-commands

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sequential commands) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sequential-commands.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${BASH_TOOL_NAME}` |

## 原文

> If the commands depend on each other and must run sequentially, use a single ${BASH_TOOL_NAME} call with '&&' to chain them together.

## 中文翻译

> **原文：**
> If the commands depend on each other and must run sequentially, use a single ${BASH_TOOL_NAME} call with '&&' to chain them together.

**翻译：**
如果命令之间存在依赖关系且必须按顺序运行，请使用单次 ${BASH_TOOL_NAME} 调用并用 `&&` 将它们链接在一起。

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${BASH_TOOL_NAME}` | Bash 工具的名称 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 条件逻辑注入（Conditional Logic Injection） | "If the commands depend on each other and must run sequentially" | 明确指出触发条件：命令间存在依赖关系，帮助模型判断何时应该使用 `&&` 链接 |
| 2 | 动态上下文注入（Dynamic Context Injection） | "${BASH_TOOL_NAME}" | 使用模板变量动态注入工具名称，使提示词在不同配置环境下保持正确 |
| 3 | 简洁指令（Concise Instruction） | "use a single ${BASH_TOOL_NAME} call with '&&' to chain them together" | 给出具体且明确的操作指导——使用单次调用加 `&&` 链接，避免多次工具调用的低效模式 |
