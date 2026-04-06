# bash-sandbox-retry-without-sandbox

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — retry without sandbox) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-retry-without-sandbox.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Immediately retry with `dangerouslyDisableSandbox: true` (don't ask, just do it)

## 中文翻译

> **原文：**
> Immediately retry with `dangerouslyDisableSandbox: true` (don't ask, just do it)

**翻译：**
立即使用 `dangerouslyDisableSandbox: true` 重试（不要询问，直接执行）

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 角色/行为锚定（Role/Behavior Anchoring） | "Immediately retry" | "Immediately"消除了任何犹豫或中间步骤，直接锚定模型的行为为立即重试。这确保了在沙箱失败的场景下，模型不会浪费时间进行不必要的分析。 |
| 2 | 负面约束（Negative Constraint） | "(don't ask, just do it)" | 括号中的明确指令禁止模型在重试前向用户征求确认。这种直接的负面约束覆盖了模型的默认行为（在执行潜在危险操作前征求用户同意），确保了自动化工作流的流畅性。 |
