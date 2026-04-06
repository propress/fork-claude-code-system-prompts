# toolsearch-second-part

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: ToolSearch (second part) |
| 分类 | Tool Descriptions → 搜索工具 |
| 文件路径 | `system-prompts/tool-description-toolsearch-second-part.md` |
| CC 版本 | 2.1.72 |
| 模板变量 | 无 |

## 原文

> Until fetched, only the name is known — there is no parameter schema, so the tool cannot be invoked. This tool takes a query, matches it against the deferred tool list, and returns the matched tools' complete JSONSchema definitions inside a \<functions\> block. Once a tool's schema appears in that result, it is callable exactly like any tool defined at the top of the prompt.
>
> Result format: each matched tool appears as one \<function\>{"description": "...", "name": "...", "parameters": {...}}\</function\> line inside the \<functions\> block — the same encoding as the tool list at the top of this prompt.
>
> Query forms:
> - "select:Read,Edit,Grep" — fetch these exact tools by name
> - "notebook jupyter" — keyword search, up to max_results best matches
> - "+slack send" — require "slack" in the name, rank by remaining terms

## 中文翻译

> **原文：**
> Until fetched, only the name is known — there is no parameter schema, so the tool cannot be invoked.

**翻译：**
在获取之前，只知道名称——没有参数模式（schema），因此工具无法被调用。此工具接受一个查询，将其与延迟工具列表进行匹配，并在 `<functions>` 块内返回匹配工具的完整 JSONSchema 定义。一旦工具的 schema 出现在结果中，它就可以像提示词顶部定义的任何工具一样被调用。

> **原文：**
> Result format: each matched tool appears as one \<function\> line ...

**翻译：**
结果格式：每个匹配的工具在 `<functions>` 块内显示为一行 `<function>{"description": "...", "name": "...", "parameters": {...}}</function>`——与此提示词顶部的工具列表相同的编码格式。

> **原文：**
> Query forms:

**翻译：**
查询形式：
- `"select:Read,Edit,Grep"` —— 按名称获取这些精确的工具
- `"notebook jupyter"` —— 关键词搜索，返回最多 max_results 个最佳匹配
- `"+slack send"` —— 要求名称中包含 "slack"，按其余词项排序

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 延迟加载 | `Until fetched, only the name is known` | 解释工具延迟加载机制，防止模型在未加载时尝试调用 |
| 2 | 查询语法 | 三种查询形式（精确选择/关键词/必须包含） | 用具体示例展示不同的查询语法 |
| 3 | 等价性声明 | `callable exactly like any tool defined at the top` | 消除延迟加载工具与预定义工具之间的行为差异顾虑 |
