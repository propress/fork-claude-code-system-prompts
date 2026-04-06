# security-review-slash-command

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: /security-review slash command |
| 分类 | Agent Prompts → 安全审查 |
| 文件路径 | `system-prompts/agent-prompt-security-review-slash-command.md` |
| CC 版本 | 2.1.70 |
| 模板变量 | 无（使用内联 bash 命令） |
| 首次出现版本 | v2.1.70 |
| 重大变更次数 | 较少 |

## 中文翻译

> **原文：**
> You are a senior security engineer conducting a focused security review of the changes on this branch.

**翻译：**
你是一位高级安全工程师，正在对当前分支上的变更进行专项安全审查。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段 | 分析 |
|---|---------|---------|------|
| 1 | 角色锚定 | "senior security engineer" | 锚定安全工程师角色，使模型以安全视角而非功能视角审查代码 |
| 2 | 动态上下文注入 | 内联的 `git status`、`git diff` | 将实时代码状态注入提示词，确保审查基于真实变更 |
| 3 | YAML 前置配置 | `allowed-tools` 字段 | 限制可用工具范围，防止安全审查代理执行写操作 |
| 4 | 边界硬编码 | `allowed-tools: Bash(git diff:*)` | 仅允许只读 git 操作，确保审查不会意外修改代码 |
