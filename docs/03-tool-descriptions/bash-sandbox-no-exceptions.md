# bash-sandbox-no-exceptions

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — no exceptions) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-no-exceptions.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Commands cannot run outside the sandbox under any circumstances.

## 中文翻译

> **原文：**
> Commands cannot run outside the sandbox under any circumstances.

**翻译：**
在任何情况下，命令都不能在沙箱外运行。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | "Commands cannot run outside the sandbox under any circumstances" | 使用"cannot"和"under any circumstances"构成了绝对否定的约束，彻底封堵了任何绕过沙箱的可能性。这种不留余地的措辞确保模型不会寻找例外情况或变通方案。 |
| 2 | 安全防护指令（Safety Guard） | "under any circumstances" | 这个短语作为安全兜底条款，覆盖所有可能的边缘情况。即使在用户请求、任务需要或命令失败等极端场景下，也不允许在沙箱外执行命令。 |
