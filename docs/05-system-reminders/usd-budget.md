# usd-budget

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: USD budget |
| 分类 | System Reminders → 会话管理 |
| 文件路径 | `system-prompts/system-reminder-usd-budget.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> USD budget: $${ATTACHMENT_OBJECT.used}/$${ATTACHMENT_OBJECT.total}; $${ATTACHMENT_OBJECT.remaining} remaining

## 中文翻译

> **原文：**
> USD budget: $${ATTACHMENT_OBJECT.used}/$${ATTACHMENT_OBJECT.total}; $${ATTACHMENT_OBJECT.remaining} remaining

**翻译：**
美元预算：$${ATTACHMENT_OBJECT.used}/$${ATTACHMENT_OBJECT.total}；剩余 $${ATTACHMENT_OBJECT.remaining}

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 成本感知注入 | "USD budget: used/total; remaining" | 向模型提供实时的费用消耗数据，使其能在接近预算上限时采取节省措施（如减少工具调用） |
| 2 | 货币化呈现 | 使用 `$` 符号和美元计价 | 以用户熟悉的货币单位呈现预算信息，便于模型理解资源消耗的经济影响 |
