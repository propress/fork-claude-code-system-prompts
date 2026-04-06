# bash-parallel-commands

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (parallel commands) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-parallel-commands.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${BASH_TOOL_NAME}` |

## 原文

> If the commands are independent and can run in parallel, make multiple ${BASH_TOOL_NAME} tool calls in a single message. Example: if you need to run "git status" and "git diff", send a single message with two ${BASH_TOOL_NAME} tool calls in parallel.

## 中文翻译

> **原文：**
> If the commands are independent and can run in parallel, make multiple ${BASH_TOOL_NAME} tool calls in a single message. Example: if you need to run "git status" and "git diff", send a single message with two ${BASH_TOOL_NAME} tool calls in parallel.

**翻译：**
如果命令之间相互独立且可以并行运行，请在一条消息中发起多个 ${BASH_TOOL_NAME} 工具调用。例如：如果你需要运行"git status"和"git diff"，请在一条消息中发送两个并行的 ${BASH_TOOL_NAME} 工具调用。

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${BASH_TOOL_NAME}` | Bash 工具的名称 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 条件逻辑注入（Conditional Logic Injection） | `If the commands are independent and can run in parallel` | 设定并行执行的前提条件（命令独立且可并行），确保只有满足条件的命令才会被并行调用。 |
| 2 | 示例引导（Example-driven Guidance） | `if you need to run "git status" and "git diff", send a single message with two tool calls` | 用具体的 git 命令示例说明并行调用的使用场景和操作方式，便于模型理解和模仿。 |
| 3 | 动态上下文注入（Dynamic Context Injection） | `${BASH_TOOL_NAME}` | 通过模板变量动态插入实际的工具名称，使指令在不同配置下都能正确引用 Bash 工具。 |
