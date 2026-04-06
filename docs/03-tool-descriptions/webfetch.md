# webfetch

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: WebFetch |
| 分类 | Tool Descriptions → 通用工具 |
| 文件路径 | `system-prompts/tool-description-webfetch.md` |
| CC 版本 | 2.1.14 |
| 模板变量 | 无 |

## 原文

> - Fetches content from a specified URL and processes it using an AI model
> - Takes a URL and a prompt as input
> - Fetches the URL content, converts HTML to markdown
> - Processes the content with the prompt using a small, fast model
> - Returns the model's response about the content
> - Use this tool when you need to retrieve and analyze web content
>
> Usage notes:
>   - IMPORTANT: If an MCP-provided web fetch tool is available, prefer using that tool instead of this one, as it may have fewer restrictions.
>   - The URL must be a fully-formed valid URL
>   - HTTP URLs will be automatically upgraded to HTTPS
>   - The prompt should describe what information you want to extract from the page
>   - This tool is read-only and does not modify any files
>   - Results may be summarized if the content is very large
>   - Includes a self-cleaning 15-minute cache for faster responses when repeatedly accessing the same URL
>   - When a URL redirects to a different host, the tool will inform you and provide the redirect URL in a special format. You should then make a new WebFetch request with the redirect URL to fetch the content.
>   - For GitHub URLs, prefer using the gh CLI via Bash instead (e.g., gh pr view, gh issue view, gh api).

## 中文翻译

> **原文：**
> Fetches content from a specified URL and processes it using an AI model

**翻译：**
从指定 URL 获取内容并使用 AI 模型处理：
- 接受 URL 和提示词作为输入
- 获取 URL 内容，将 HTML 转换为 markdown
- 使用小型快速模型根据提示词处理内容
- 返回模型对内容的响应
- 当你需要检索和分析网页内容时使用此工具

> **原文：**
> Usage notes:

**翻译：**
使用说明：
- **重要**：如果有 MCP 提供的 web fetch 工具可用，优先使用该工具而非此工具，因为它可能限制更少。
- URL 必须是格式完整的有效 URL
- HTTP URL 会自动升级为 HTTPS
- 提示词应描述你想从页面中提取什么信息
- 此工具是只读的，不修改任何文件
- 如果内容非常大，结果可能会被摘要
- 包含 15 分钟自清理缓存，重复访问同一 URL 时响应更快
- 当 URL 重定向到不同主机时，工具会通知你并以特殊格式提供重定向 URL。你应该用重定向 URL 发起新的 WebFetch 请求
- 对于 GitHub URL，优先通过 Bash 使用 gh CLI（如 gh pr view、gh issue view、gh api）

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | MCP 优先 | `If an MCP-provided web fetch tool is available, prefer using that tool` | 建立明确的工具优先级层次 |
| 2 | 协议升级 | `HTTP URLs will be automatically upgraded to HTTPS` | 透明说明自动行为减少困惑 |
| 3 | 重定向处理 | `make a new WebFetch request with the redirect URL` | 教会模型正确处理跨域重定向 |
| 4 | GitHub 例外 | `For GitHub URLs, prefer using the gh CLI` | 针对特定域名提供更优路径 |
