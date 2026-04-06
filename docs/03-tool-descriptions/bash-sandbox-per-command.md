# bash-sandbox-per-command

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — per-command) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-per-command.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Treat each command you execute with `dangerouslyDisableSandbox: true` individually. Even if you have recently run a command with this setting, you should default to running future commands within the sandbox.

## 中文翻译

> **原文：**
> Treat each command you execute with `dangerouslyDisableSandbox: true` individually. Even if you have recently run a command with this setting, you should default to running future commands within the sandbox.

**翻译：**
将每个使用 `dangerouslyDisableSandbox: true` 执行的命令视为独立个体。即使你最近刚使用此设置运行过命令，后续命令仍应默认在沙箱内运行。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 范围限定（Scope Limitation） | "Treat each command ... individually" | 将禁用沙箱的权限严格限定在单个命令的粒度上，防止模型将一次的沙箱豁免扩展为全局设置。这种逐命令的范围限定是最小权限原则的体现。 |
| 2 | 安全防护指令（Safety Guard） | "Even if you have recently run a command with this setting, you should default to running future commands within the sandbox" | 预见并阻止了模型可能出现的"惯性行为"——因为刚刚禁用过沙箱就继续保持禁用状态。通过"default to"强调默认行为应该是使用沙箱，确保安全措施的持续性。 |
| 3 | 负面约束（Negative Constraint） | "Even if you have recently run a command with this setting" | 用"Even if"明确否定了"因为之前禁用过所以可以继续禁用"这一潜在推理路径，堵住了模型可能利用的逻辑漏洞。 |
