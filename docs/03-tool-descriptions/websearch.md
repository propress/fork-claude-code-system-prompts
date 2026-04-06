# websearch

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: WebSearch |
| 分类 | Tool Descriptions → 通用工具 |
| 文件路径 | `system-prompts/tool-description-websearch.md` |
| CC 版本 | 2.1.42 |
| 模板变量 | `${GET_CURRENT_MONTH_YEAR}` |

## 原文

> - Allows Claude to search the web and use the results to inform responses
> - Provides up-to-date information for current events and recent data
> - Returns search result information formatted as search result blocks, including links as markdown hyperlinks
> - Use this tool for accessing information beyond Claude's knowledge cutoff
> - Searches are performed automatically within a single API call
>
> CRITICAL REQUIREMENT - You MUST follow this:
>   - After answering the user's question, you MUST include a "Sources:" section at the end of your response
>   - In the Sources section, list all relevant URLs from the search results as markdown hyperlinks: [Title](URL)
>   - This is MANDATORY - never skip including sources in your response
>   - Example format:
>
>     [Your answer here]
>
>     Sources:
>     - [Source Title 1](https://example.com/1)
>     - [Source Title 2](https://example.com/2)
>
> Usage notes:
>   - Domain filtering is supported to include or block specific websites
>   - Web search is only available in the US
>
> IMPORTANT - Use the correct year in search queries:
>   - The current month is ${GET_CURRENT_MONTH_YEAR()}. You MUST use this year when searching for recent information, documentation, or current events.
>   - Example: If the user asks for "latest React docs", search for "React documentation" with the current year, NOT last year

## 中文翻译

> **原文：**
> Allows Claude to search the web and use the results to inform responses

**翻译：**
允许 Claude 搜索网络并使用结果来辅助响应：
- 提供当前事件和最新数据的最新信息
- 返回格式化为搜索结果块的信息，包括作为 markdown 超链接的链接
- 当需要访问 Claude 知识截止日期之后的信息时使用此工具
- 搜索在单次 API 调用中自动执行

> **原文：**
> CRITICAL REQUIREMENT - You MUST follow this:

**翻译：**
**关键要求** —— 你必须遵守：
- 回答用户问题后，你**必须**在响应末尾包含 "Sources:" 部分
- 在 Sources 部分，将搜索结果中所有相关 URL 列为 markdown 超链接：`[Title](URL)`
- 这是**强制性的**——永远不要跳过在响应中包含来源

> **原文：**
> IMPORTANT - Use the correct year in search queries:

**翻译：**
**重要** —— 在搜索查询中使用正确的年份：
- 当前月份是 ${GET_CURRENT_MONTH_YEAR()}。搜索最新信息、文档或当前事件时必须使用当前年份
- 示例：如果用户要求"最新 React 文档"，搜索"React documentation"并使用当前年份，而非去年

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `GET_CURRENT_MONTH_YEAR` | 函数 | 运行时返回当前月份和年份字符串 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 强制来源引用 | `CRITICAL REQUIREMENT` + `MANDATORY` | 用最高级别的强调确保搜索结果附带来源链接 |
| 2 | 格式模板 | Sources 部分的具体格式示例 | 提供可复制的输出模板 |
| 3 | 年份校正 | `MUST use this year ... NOT last year` | 防止模型使用过时的年份进行搜索 |
| 4 | 地区限制 | `Web search is only available in the US` | 透明说明功能可用性限制 |
