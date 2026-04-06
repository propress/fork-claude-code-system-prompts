# mcp-resource-no-content

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: MCP resource no content |
| 分类 | System Reminders → 技能与工具 |
| 文件路径 | `system-prompts/system-reminder-mcp-resource-no-content.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${ATTACHMENT_OBJECT}` |

## 原文

> `<mcp-resource server="${ATTACHMENT_OBJECT.server}" uri="${ATTACHMENT_OBJECT.uri}">(No content)</mcp-resource>`

## 中文翻译

> **原文：**
> `<mcp-resource server="${ATTACHMENT_OBJECT.server}" uri="${ATTACHMENT_OBJECT.uri}">(No content)</mcp-resource>`

**翻译：**
`<mcp-resource server="${ATTACHMENT_OBJECT.server}" uri="${ATTACHMENT_OBJECT.uri}">`（无内容）`</mcp-resource>`

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 结构化空状态 | `<mcp-resource ...>(No content)</mcp-resource>` | 使用 XML 标签包裹空状态信息，使模型能通过结构化方式识别 MCP 资源的可用性 |
| 2 | 来源追踪 | `server="${ATTACHMENT_OBJECT.server}" uri="${ATTACHMENT_OBJECT.uri}"` | 保留资源的服务器和 URI 信息，即使内容为空也能追踪资源来源 |
