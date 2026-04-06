# bash-sandbox-default-to-sandbox

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — default to sandbox) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-default-to-sandbox.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> You should always default to running commands within the sandbox. Do NOT attempt to set `dangerouslyDisableSandbox: true` unless:

## 中文翻译

> **原文：**
> You should always default to running commands within the sandbox. Do NOT attempt to set `dangerouslyDisableSandbox: true` unless:

**翻译：**
你应该始终默认在沙箱内运行命令。不要尝试设置 `dangerouslyDisableSandbox: true`，除非：

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 安全防护指令（Safety Guard） | `You should always default to running commands within the sandbox` | 建立安全默认行为，确保所有命令默认在沙箱中运行，从根本上降低安全风险。 |
| 2 | 负面约束（Negative Constraint） | `Do NOT attempt to set dangerouslyDisableSandbox: true unless:` | 明确禁止禁用沙箱的操作，并用"unless:"暗示后续有严格的例外条件列表，提高禁用门槛。 |
