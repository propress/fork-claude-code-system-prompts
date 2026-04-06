# bash-sandbox-explain-restriction

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — explain restriction) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-explain-restriction.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Briefly explain what sandbox restriction likely caused the failure. Be sure to mention that the user can use the `/sandbox` command to manage restrictions.

## 中文翻译

> **原文：**
> Briefly explain what sandbox restriction likely caused the failure. Be sure to mention that the user can use the `/sandbox` command to manage restrictions.

**翻译：**
简要说明可能是哪个沙箱限制导致了失败。务必提及用户可以使用 `/sandbox` 命令来管理限制设置。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 简洁性约束（Conciseness Constraint） | "Briefly explain" | 使用"Briefly"限定了回复的长度和详细程度，防止模型生成过于冗长的解释。在沙箱错误的场景下，用户通常需要快速了解原因而非深入技术细节。 |
| 2 | 安全防护指令（Safety Guard） | "Be sure to mention that the user can use the `/sandbox` command to manage restrictions" | 通过"Be sure to"这一强调性短语，确保模型在回复中始终包含用户可操作的解决方案（`/sandbox` 命令）。这为用户提供了明确的后续步骤，避免模型仅描述问题而不提供解决途径。 |
