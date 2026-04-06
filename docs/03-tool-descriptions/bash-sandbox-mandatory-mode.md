# bash-sandbox-mandatory-mode

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — mandatory mode) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-mandatory-mode.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> All commands MUST run in sandbox mode - the `dangerouslyDisableSandbox` parameter is disabled by policy.

## 中文翻译

> **原文：**
> All commands MUST run in sandbox mode - the `dangerouslyDisableSandbox` parameter is disabled by policy.

**翻译：**
所有命令必须在沙箱模式下运行——`dangerouslyDisableSandbox` 参数已被策略禁用。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | "All commands MUST run in sandbox mode" | 使用全大写的"MUST"建立了绝对强制性的约束，不留任何例外空间。这是一条核心安全策略，确保模型在任何情况下都不会尝试绕过沙箱。 |
| 2 | 安全防护指令（Safety Guard） | "the `dangerouslyDisableSandbox` parameter is disabled by policy" | 明确告知模型该参数不可用，并以"by policy"说明这是策略层面的限制而非技术故障。这防止模型尝试使用该参数或建议用户启用它。 |
