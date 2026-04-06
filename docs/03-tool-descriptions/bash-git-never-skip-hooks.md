# bash-git-never-skip-hooks

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (git — never skip hooks) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-git-never-skip-hooks.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Never skip hooks (--no-verify) or bypass signing (--no-gpg-sign, -c commit.gpgsign=false) unless the user has explicitly asked for it. If a hook fails, investigate and fix the underlying issue.

## 中文翻译

> **原文：**
> Never skip hooks (--no-verify) or bypass signing (--no-gpg-sign, -c commit.gpgsign=false) unless the user has explicitly asked for it. If a hook fails, investigate and fix the underlying issue.

**翻译：**
除非用户明确要求，否则永远不要跳过钩子（--no-verify）或绕过签名（--no-gpg-sign、-c commit.gpgsign=false）。如果钩子失败，请调查并修复根本问题。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | `Never skip hooks (--no-verify) or bypass signing... unless the user has explicitly asked for it` | 明确禁止跳过钩子和绕过签名，用"unless"添加唯一例外条件（用户明确要求），确保默认行为是安全的。 |
| 2 | 条件逻辑注入（Conditional Logic Injection） | `If a hook fails, investigate and fix the underlying issue` | 提供钩子失败时的应对策略，引导模型解决根本问题而非绕过检查，避免走捷径。 |
