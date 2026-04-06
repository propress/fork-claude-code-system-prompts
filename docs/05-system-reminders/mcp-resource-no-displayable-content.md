# mcp-resource-no-displayable-content

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: MCP resource no displayable content |
| 分类 | System Reminders → 技能与工具 |
| 文件路径 | `system-prompts/system-reminder-mcp-resource-no-displayable-content.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> `<mcp-resource server="${ATTACHMENT_OBJECT.server}" uri="${ATTACHMENT_OBJECT.uri}">(No displayable content)</mcp-resource>`

## 中文翻译

> **原文：**
> `<mcp-resource server="${ATTACHMENT_OBJECT.server}" uri="${ATTACHMENT_OBJECT.uri}">(No displayable content)</mcp-resource>`

**翻译：**
`<mcp-resource server="${ATTACHMENT_OBJECT.server}" uri="${ATTACHMENT_OBJECT.uri}">`（无可显示内容）`</mcp-resource>`

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 状态区分 | "No displayable content" vs "No content" | 区分"无内容"和"有内容但无法显示"两种不同的资源状态，帮助模型做出更准确的判断 |
| 2 | 一致的 XML 结构 | `<mcp-resource ...>...</mcp-resource>` | 保持与 mcp-resource-no-content 一致的标签结构，使模型能以统一的方式处理 MCP 资源状态 |
