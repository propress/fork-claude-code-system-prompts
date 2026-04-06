# grep

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Grep |
| 分类 | Tool Descriptions → 搜索工具 |
| 文件路径 | `system-prompts/tool-description-grep.md` |
| CC 版本 | 2.0.14 |
| 模板变量 | `${GREP_TOOL_NAME}`, `${BASH_TOOL_NAME}`, `${TASK_TOOL_NAME}` |

## 原文

> A powerful search tool built on ripgrep
>
>   Usage:
>   - ALWAYS use ${GREP_TOOL_NAME} for search tasks. NEVER invoke `grep` or `rg` as a ${BASH_TOOL_NAME} command. The ${GREP_TOOL_NAME} tool has been optimized for correct permissions and access.
>   - Supports full regex syntax (e.g., "log.*Error", "function\s+\w+")
>   - Filter files with glob parameter (e.g., "*.js", "**/*.tsx") or type parameter (e.g., "js", "py", "rust")
>   - Output modes: "content" shows matching lines, "files_with_matches" shows only file paths (default), "count" shows match counts
>   - Use ${TASK_TOOL_NAME} tool for open-ended searches requiring multiple rounds
>   - Pattern syntax: Uses ripgrep (not grep) - literal braces need escaping (use `interface\{\}` to find `interface{}` in Go code)
>   - Multiline matching: By default patterns match within single lines only. For cross-line patterns like `struct \{[\s\S]*?field`, use `multiline: true`

## 中文翻译

> **原文：**
> A powerful search tool built on ripgrep

**翻译：**
基于 ripgrep 构建的强大搜索工具

---

> **原文：**
>   Usage:
>   - ALWAYS use ${GREP_TOOL_NAME} for search tasks. NEVER invoke `grep` or `rg` as a ${BASH_TOOL_NAME} command. The ${GREP_TOOL_NAME} tool has been optimized for correct permissions and access.
>   - Supports full regex syntax (e.g., "log.*Error", "function\s+\w+")
>   - Filter files with glob parameter (e.g., "*.js", "**/*.tsx") or type parameter (e.g., "js", "py", "rust")
>   - Output modes: "content" shows matching lines, "files_with_matches" shows only file paths (default), "count" shows match counts
>   - Use ${TASK_TOOL_NAME} tool for open-ended searches requiring multiple rounds
>   - Pattern syntax: Uses ripgrep (not grep) - literal braces need escaping (use `interface\{\}` to find `interface{}` in Go code)
>   - Multiline matching: By default patterns match within single lines only. For cross-line patterns like `struct \{[\s\S]*?field`, use `multiline: true`

**翻译：**
用法：
- 搜索任务始终使用 ${GREP_TOOL_NAME}。切勿将 `grep` 或 `rg` 作为 ${BASH_TOOL_NAME} 命令调用。${GREP_TOOL_NAME} 工具已针对正确的权限和访问进行了优化。
- 支持完整的正则表达式语法（例如，"log.*Error"、"function\s+\w+"）
- 使用 glob 参数过滤文件（例如，"*.js"、"**/*.tsx"）或使用 type 参数过滤（例如，"js"、"py"、"rust"）
- 输出模式："content" 显示匹配行，"files_with_matches" 仅显示文件路径（默认），"count" 显示匹配计数
- 对于需要多轮搜索的开放式搜索，使用 ${TASK_TOOL_NAME} 工具
- 模式语法：使用 ripgrep（不是 grep）——字面花括号需要转义（使用 `interface\{\}` 来查找 Go 代码中的 `interface{}`）
- 多行匹配：默认情况下模式仅在单行内匹配。对于跨行模式如 `struct \{[\s\S]*?field`，使用 `multiline: true`

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${GREP_TOOL_NAME}` | 搜索（grep）工具的名称 |
| `${BASH_TOOL_NAME}` | Bash 工具的名称 |
| `${TASK_TOOL_NAME}` | 任务/智能体工具的名称 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | `ALWAYS use ${GREP_TOOL_NAME}... NEVER invoke grep or rg as a ${BASH_TOOL_NAME} command` | 使用大写的 ALWAYS/NEVER 配对，强制 LLM 使用专用搜索工具而非通过 Bash 调用 grep/rg，确保权限和访问控制的正确性。 |
| 2 | 示例引导（Example-driven Guidance） | `"log.*Error"`, `"function\s+\w+"`, `"*.js"`, `"**/*.tsx"` | 提供多种正则和 glob 模式示例，帮助 LLM 构造正确的搜索模式，降低语法错误率。 |
| 3 | 结构化列表（Structured Enumeration） | 使用 `-` 列表枚举六条使用规则 | 将所有功能和注意事项以列表形式组织，每条独立且具体，便于 LLM 按需查阅。 |
| 4 | 范围限定（Scope Limitation） | `Use ${TASK_TOOL_NAME} tool for open-ended searches requiring multiple rounds` | 明确划分简单搜索和复杂搜索的工具边界，引导 LLM 在多轮搜索场景中选择更合适的工具。 |
| 5 | 动态上下文注入（Dynamic Context Injection） | `${GREP_TOOL_NAME}`, `${BASH_TOOL_NAME}`, `${TASK_TOOL_NAME}` | 通过变量动态注入实际工具名称，使提示词在不同配置下都能正确引用工具。 |
