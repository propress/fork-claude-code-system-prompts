# readfile

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: ReadFile |
| 分类 | Tool Descriptions → 文件操作 |
| 文件路径 | `system-prompts/tool-description-readfile.md` |
| CC 版本 | 2.1.91 |
| 模板变量 | `${SUPPORTS_RELATIVE_PATHS_FN}`, `${DEFAULT_READ_LINES_LIMIT}`, `${CONDITIONAL_LENGTH_NOTE}`, `${CAT_DASH_N_NOTE}`, `${READ_FULL_FILE_NOTE}`, `${CAN_READ_PDF_FILES_FN}`, `${BASH_TOOL_NAME}`, `${HAS_ADDITIONAL_READ_NOTE_FN}`, `${ADDITIONAL_READ_NOTE}` |

## 原文

> Reads a file from the local filesystem. You can access any file directly by using this tool.
> Assume this tool is able to read all files on the machine. If the User provides a path to a file assume that path is valid. It is okay to read a file that does not exist; an error will be returned.
>
> Usage:
> - ${SUPPORTS_RELATIVE_PATHS_FN()?"The file_path parameter can be relative to cwd (preferred for brevity) or absolute":"The file_path parameter must be an absolute path, not a relative path"}
> - By default, it reads up to ${DEFAULT_READ_LINES_LIMIT} lines starting from the beginning of the file${CONDITIONAL_LENGTH_NOTE}
> ${CAT_DASH_N_NOTE}
> ${READ_FULL_FILE_NOTE}
> - This tool allows Claude Code to read images (eg PNG, JPG, etc). When reading an image file the contents are presented visually as Claude Code is a multimodal LLM.${CAN_READ_PDF_FILES_FN()?`
> - This tool can read PDF files (.pdf). For large PDFs (more than 10 pages), you MUST provide the pages parameter to read specific page ranges (e.g., pages: "1-5"). Reading a large PDF without the pages parameter will fail. Maximum 20 pages per request.`:""}
> - This tool can read Jupyter notebooks (.ipynb files) and returns all cells with their outputs, combining code, text, and visualizations.
> - This tool can only read files, not directories. To read a directory, use an ls command via the ${BASH_TOOL_NAME} tool.
> - You will regularly be asked to read screenshots. If the user provides a path to a screenshot, ALWAYS use this tool to view the file at the path. This tool will work with all temporary file paths.
> - If you read a file that exists but has empty contents you will receive a system reminder warning in place of file contents.${HAS_ADDITIONAL_READ_NOTE_FN()?ADDITIONAL_READ_NOTE:""}

## 中文翻译

> **原文：**
> Reads a file from the local filesystem. You can access any file directly by using this tool.
> Assume this tool is able to read all files on the machine. If the User provides a path to a file assume that path is valid. It is okay to read a file that does not exist; an error will be returned.

**翻译：**
从本地文件系统读取文件。你可以使用此工具直接访问任何文件。
假定此工具能够读取机器上的所有文件。如果用户提供了文件路径，假定该路径有效。读取不存在的文件是可以的；会返回一个错误。

---

> **原文：**
> Usage:
> - ${SUPPORTS_RELATIVE_PATHS_FN()?"The file_path parameter can be relative to cwd (preferred for brevity) or absolute":"The file_path parameter must be an absolute path, not a relative path"}
> - By default, it reads up to ${DEFAULT_READ_LINES_LIMIT} lines starting from the beginning of the file${CONDITIONAL_LENGTH_NOTE}
> ${CAT_DASH_N_NOTE}
> ${READ_FULL_FILE_NOTE}

**翻译：**
用法：
- （当支持相对路径时）file_path 参数可以是相对于当前工作目录的路径（简洁起见推荐使用）或绝对路径（不支持时）file_path 参数必须是绝对路径，不能是相对路径
- 默认情况下，从文件开头读取最多 ${DEFAULT_READ_LINES_LIMIT} 行${CONDITIONAL_LENGTH_NOTE}
${CAT_DASH_N_NOTE}
${READ_FULL_FILE_NOTE}

---

> **原文：**
> - This tool allows Claude Code to read images (eg PNG, JPG, etc). When reading an image file the contents are presented visually as Claude Code is a multimodal LLM.${CAN_READ_PDF_FILES_FN()?`
> - This tool can read PDF files (.pdf). For large PDFs (more than 10 pages), you MUST provide the pages parameter to read specific page ranges (e.g., pages: "1-5"). Reading a large PDF without the pages parameter will fail. Maximum 20 pages per request.`:""}

**翻译：**
- 此工具允许 Claude Code 读取图片（如 PNG、JPG 等）。读取图片文件时，内容以视觉方式呈现，因为 Claude Code 是一个多模态 LLM。（当支持 PDF 时）
- 此工具可以读取 PDF 文件（.pdf）。对于大型 PDF（超过 10 页），你必须提供 pages 参数来读取特定页面范围（例如，pages: "1-5"）。不带 pages 参数读取大型 PDF 将会失败。每次请求最多 20 页。

---

> **原文：**
> - This tool can read Jupyter notebooks (.ipynb files) and returns all cells with their outputs, combining code, text, and visualizations.
> - This tool can only read files, not directories. To read a directory, use an ls command via the ${BASH_TOOL_NAME} tool.
> - You will regularly be asked to read screenshots. If the user provides a path to a screenshot, ALWAYS use this tool to view the file at the path. This tool will work with all temporary file paths.
> - If you read a file that exists but has empty contents you will receive a system reminder warning in place of file contents.${HAS_ADDITIONAL_READ_NOTE_FN()?ADDITIONAL_READ_NOTE:""}

**翻译：**
- 此工具可以读取 Jupyter notebook（.ipynb 文件）并返回所有单元格及其输出，结合代码、文本和可视化内容。
- 此工具只能读取文件，不能读取目录。要读取目录，请通过 ${BASH_TOOL_NAME} 工具使用 ls 命令。
- 你会经常被要求读取截图。如果用户提供了截图的路径，始终使用此工具查看该路径下的文件。此工具适用于所有临时文件路径。
- 如果你读取的文件存在但内容为空，你将收到一条系统提醒警告来代替文件内容。${HAS_ADDITIONAL_READ_NOTE_FN()?ADDITIONAL_READ_NOTE:""}

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${SUPPORTS_RELATIVE_PATHS_FN}` | 返回是否支持相对路径的函数 |
| `${DEFAULT_READ_LINES_LIMIT}` | 默认读取的最大行数限制 |
| `${CONDITIONAL_LENGTH_NOTE}` | 条件性的文件长度相关说明 |
| `${CAT_DASH_N_NOTE}` | 关于 cat -n 命令的说明 |
| `${READ_FULL_FILE_NOTE}` | 关于读取完整文件的说明 |
| `${CAN_READ_PDF_FILES_FN}` | 返回是否支持读取 PDF 文件的函数 |
| `${BASH_TOOL_NAME}` | Bash 工具的名称 |
| `${HAS_ADDITIONAL_READ_NOTE_FN}` | 返回是否有附加读取说明的函数 |
| `${ADDITIONAL_READ_NOTE}` | 附加的读取说明文本 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 角色/行为锚定（Role/Behavior Anchoring） | `Assume this tool is able to read all files on the machine` | 赋予工具"全能读取"的能力定义，让 LLM 不会因为怀疑权限而拒绝尝试读取文件，消除不必要的犹豫。 |
| 2 | 安全防护指令（Safety Guard） | `For large PDFs (more than 10 pages), you MUST provide the pages parameter` | 对大文件读取设置强制性参数要求，防止因一次性读取过大文件导致资源耗尽或超时。 |
| 3 | 条件逻辑注入（Conditional Logic Injection） | `${SUPPORTS_RELATIVE_PATHS_FN()?...}`, `${CAN_READ_PDF_FILES_FN()?...}` | 根据运行时能力动态调整路径格式要求和 PDF 支持说明，使同一提示词适应不同的功能配置。 |
| 4 | 范围限定（Scope Limitation） | `This tool can only read files, not directories. To read a directory, use an ls command via the ${BASH_TOOL_NAME} tool` | 明确工具的能力边界，并提供替代方案，防止 LLM 用此工具做它不擅长的事情。 |
| 5 | 负面约束（Negative Constraint） | `Reading a large PDF without the pages parameter will fail` | 预先警告失败场景，帮助 LLM 在首次调用时就使用正确的参数，避免浪费一次工具调用。 |
| 6 | 结构化列表（Structured Enumeration） | 使用 `-` 列表枚举所有支持的文件类型和用法 | 系统地列出支持的文件类型（图片、PDF、notebook）和使用注意事项，形成完整的功能参考。 |
| 7 | 动态上下文注入（Dynamic Context Injection） | `${DEFAULT_READ_LINES_LIMIT}`, `${BASH_TOOL_NAME}` 等 | 通过变量注入运行时的行数限制和工具名称，确保提示词与实际环境保持一致。 |
