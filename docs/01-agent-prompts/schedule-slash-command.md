# schedule-slash-command

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: /schedule slash command |
| 分类 | Agent Prompts → 远程调度 |
| 文件路径 | `system-prompts/agent-prompt-schedule-slash-command.md` |
| CC 版本 | 2.1.90 |
| 模板变量 | `${USER_REQUEST}`, `${ASK_USER_QUESTION_TOOL_NAME}`, `${FORMAT_QUESTION_FN}`, `${QUESTION_OPTIONS}`, `${ADDITIONAL_INFO_BLOCK}`, `${REMOTE_TRIGGER_TOOL_NAME}`, `${DEFAULT_GIT_REPO_URL}`, `${MCP_CONNECTORS_LIST}`, `${ENVIRONMENTS_LIST}`, `${NEW_ENVIRONMENT_OBJECT}`, `${USER_TIMEZONE}`, `${IS_GITHUB_REMINDER_ENABLED}`, `${IS_TRUTHY_FN}`, `${CHECK_FEATURE_FLAG_FN}` |
| 首次出现版本 | 较早版本 |
| 重大变更次数 | 中等 |

## 中文概述

此代理提示词用于引导用户通过 Anthropic 云 API 的 cron 触发器调度、更新、列出或运行远程 Claude Code 代理。

## 📋 模板变量说明

| 变量 | 运行时值 | 说明 |
|------|---------|------|
| `${USER_REQUEST}` | 用户请求文本 | 用户的调度请求 |
| `${USER_TIMEZONE}` | 时区字符串 | 用户当前时区（如 Asia/Shanghai） |
| `${IS_GITHUB_REMINDER_ENABLED}` | 布尔值 | 是否显示 GitHub 账户连接提示 |
| `${CHECK_FEATURE_FLAG_FN}` | 函数 | 检查功能标志是否启用的函数 |
| 其他变量 | 动态值 | 连接器列表、环境配置等 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段 | 分析 |
|---|---------|---------|------|
| 1 | 动态上下文注入 | 13个模板变量 | 高度参数化设计，运行时注入连接器、环境、用户设置等上下文 |
| 2 | 条件分支 | `${IS_TRUTHY_FN}`, `${CHECK_FEATURE_FLAG_FN}` | 基于功能标志控制行为，实现渐进式功能发布 |
| 3 | 渐进式信任 | `IS_GITHUB_REMINDER_ENABLED` | 根据用户账户状态调整引导流程 |
