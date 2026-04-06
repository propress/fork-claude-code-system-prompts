# bash-alternative-communication

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (alternative — communication) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-alternative-communication.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Communication: Output text directly (NOT echo/printf)

## 中文翻译

> **原文：**
> Communication: Output text directly (NOT echo/printf)

**翻译：**
通信：直接输出文本（不要使用 echo/printf）

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 简洁指令（Concise Instruction） | `Communication: Output text directly` | 极简的一行指令，明确指定通信方式应直接输出文本，不留歧义。 |
| 2 | 负面约束（Negative Constraint） | `(NOT echo/printf)` | 括号中的大写 NOT 强调禁止使用 echo/printf 命令，防止模型使用 Bash 命令来输出文本。 |
