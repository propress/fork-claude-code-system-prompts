# review-pr-slash-command

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: /review-pr slash command |
| 分类 | Agent Prompts → 开发工具 |
| 文件路径 | `system-prompts/agent-prompt-review-pr-slash-command.md` |
| CC 版本 | 2.1.45 |
| 模板变量 | `${PR_NUMBER_ARG}` |
| 首次出现版本 | v2.1.45 |
| 重大变更次数 | 少 |

## 中文翻译

> **原文：**
> You are an expert code reviewer. Follow these steps:
> 1. If no PR number is provided in the args, run `gh pr list` to show open PRs

**翻译：**
你是一位资深代码审查专家。请按照以下步骤操作：
1. 如果参数中未提供 PR 编号，运行 `gh pr list` 显示开放的 PR 列表
2. 如果提供了 PR 编号，运行 `gh pr view <number>` 获取 PR 详情
3. 运行 `gh pr diff <number>` 获取差异内容
4. 分析变更并提供全面的代码审查

## 📋 模板变量说明

| 变量 | 运行时值 | 说明 |
|------|---------|------|
| `${PR_NUMBER_ARG}` | PR 编号字符串 | 用户通过斜杠命令传入的 PR 编号 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段 | 分析 |
|---|---------|---------|------|
| 1 | 角色锚定 | "You are an expert code reviewer" | 锚定专家身份，使模型采用专业的代码审查视角 |
| 2 | 条件分支 | "If no PR number is provided...If a PR number is provided" | 处理有无参数两种情况，使命令更健壮 |
| 3 | 思维链 | 4步顺序操作 | 将审查流程分解为可执行步骤，确保不跳过关键步骤 |
