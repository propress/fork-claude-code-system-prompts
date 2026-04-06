# doing-tasks-help-and-feedback

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Doing tasks (help and feedback) |
| 分类 | System Prompts → 任务执行 |
| 文件路径 | `system-prompts/system-prompt-doing-tasks-help-and-feedback.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.53 |

## 原文

> If the user asks for help or wants to give feedback inform them of the following:

## 中文翻译

> **原文：**
> If the user asks for help or wants to give feedback inform them of the following:

**翻译：**
如果用户请求帮助或想要提供反馈，告知他们以下信息：

## 📋 模板变量说明

无模板变量。

> **注意：** 此提示词看起来是一个不完整的片段，实际运行时后面会跟随具体的帮助和反馈渠道信息（如文档链接、反馈地址等），这些内容可能通过模板变量或运行时拼接动态注入。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 触发条件路由 | "If the user asks for help or wants to give feedback" | 定义了两个明确的触发条件（帮助请求 / 反馈意愿），使模型能够在正确的时机提供相应信息，而不是主动推送。 |
| 2 | 信息注入模式 | "inform them of the following:" | 这是一个"信息注入点"的设计模式——提示词本身作为开头，运行时动态拼接实际的帮助/反馈渠道信息。这种模块化设计便于维护。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 新增 | 从"Doing tasks"单体提示词中拆分出的帮助和反馈路由子提示 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
