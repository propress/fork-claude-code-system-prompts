# agent-mention

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Agent mention |
| 分类 | System Reminders → 团队协作 |
| 文件路径 | `system-prompts/system-reminder-agent-mention.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> The user has expressed a desire to invoke the agent "${ATTACHMENT_OBJECT.agentType}". Please invoke the agent appropriately, passing in the required context to it.

## 中文翻译

> **原文：**
> The user has expressed a desire to invoke the agent "${ATTACHMENT_OBJECT.agentType}". Please invoke the agent appropriately, passing in the required context to it.

**翻译：**
用户表达了调用代理 "${ATTACHMENT_OBJECT.agentType}" 的意愿。请适当地调用该代理，并将所需的上下文传递给它。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 意图传递 | "The user has expressed a desire to invoke the agent" | 明确告知模型这是用户的意图，而非系统的自动行为，促使模型将其视为高优先级操作 |
| 2 | 上下文注入 | "passing in the required context to it" | 强调必须传递上下文，防止模型在调用代理时遗漏关键信息 |
