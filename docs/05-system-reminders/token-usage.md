# token-usage

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Token usage |
| 分类 | System Reminders → 会话管理 |
| 文件路径 | `system-prompts/system-reminder-token-usage.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> Token usage: ${ATTACHMENT_OBJECT.used}/${ATTACHMENT_OBJECT.total}; ${ATTACHMENT_OBJECT.remaining} remaining

## 中文翻译

> **原文：**
> Token usage: ${ATTACHMENT_OBJECT.used}/${ATTACHMENT_OBJECT.total}; ${ATTACHMENT_OBJECT.remaining} remaining

**翻译：**
Token 使用量：${ATTACHMENT_OBJECT.used}/${ATTACHMENT_OBJECT.total}；剩余 ${ATTACHMENT_OBJECT.remaining}

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 资源感知注入 | "Token usage: used/total; remaining" | 向模型提供 token 消耗的实时数据，使其能够在接近上限时调整行为（如简化输出） |
| 2 | 三维度呈现 | "used / total / remaining" | 同时提供已用、总量和剩余三个维度，使模型无需计算即可评估资源状态 |
