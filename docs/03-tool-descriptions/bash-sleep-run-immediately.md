# bash-sleep-run-immediately

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sleep — run immediately) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sleep-run-immediately.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Do not sleep between commands that can run immediately — just run them.

## 中文翻译

> **原文：**
> Do not sleep between commands that can run immediately — just run them.

**翻译：**
不要在可以立即运行的命令之间使用 sleep——直接运行即可。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | "Do not sleep between commands that can run immediately" | 直接禁止在无需等待的命令间插入 sleep，消除不必要的延迟 |
| 2 | 简洁指令（Concise Instruction） | "just run them" | 用最简短的语言给出替代方案——直接执行，使指令清晰无歧义 |
