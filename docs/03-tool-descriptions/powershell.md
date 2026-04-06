# powershell

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: PowerShell |
| 分类 | Tool Descriptions → 通用工具 |
| 文件路径 | `system-prompts/tool-description-powershell.md` |
| CC 版本 | 2.1.88 |
| 模板变量 | `${RENDER_COMMAND_NOTES_FN}`, `${COMMAND_NOTES}`, `${MAX_TIMEOUT_MS_FN}`, `${DEFAULT_TIMEOUT_MS_FN}`, `${MAX_OUTPUT_CHARS_FN}`, `${CUSTOM_USAGE_NOTE}`, `${GLOB_TOOL_NAME}`, `${GREP_TOOL_NAME}`, `${READ_TOOL_NAME}`, `${EDIT_TOOL_NAME}`, `${WRITE_TOOL_NAME}`, `${POWERSHELL_TOOL_NAME}`, `${CUSTOM_GIT_NOTES}` |

## 原文

> Executes a given PowerShell command with optional timeout. Working directory persists between commands; shell state (variables, functions) does not.
>
> IMPORTANT: This tool is for terminal operations via PowerShell: git, npm, docker, and PS cmdlets. DO NOT use it for file operations (reading, writing, editing, searching, finding files) - use the specialized tools for this instead.
>
> ${RENDER_COMMAND_NOTES_FN(COMMAND_NOTES)}
>
> Before executing the command, please follow these steps:
>
> 1. Directory Verification:
>    - If the command will create new directories or files, first use `Get-ChildItem` (or `ls`) to verify the parent directory exists and is the correct location
>
> 2. Command Execution:
>    - Always quote file paths that contain spaces with double quotes
>    - Capture the output of the command.
>
> PowerShell Syntax Notes:
>    - Variables use $ prefix: $myVar = "value"
>    - Escape character is backtick (`), not backslash
>    - Use Verb-Noun cmdlet naming: Get-ChildItem, Set-Location, New-Item, Remove-Item
>    - Common aliases: ls (Get-ChildItem), cd (Set-Location), cat (Get-Content), rm (Remove-Item)
>    - Pipe operator | works similarly to bash but passes objects, not text
>    - Use Select-Object, Where-Object, ForEach-Object for filtering and transformation
>    - String interpolation: "Hello $name" or "Hello $($obj.Property)"
>    - Registry access uses PSDrive prefixes: `HKLM:\SOFTWARE\...`, `HKCU:\...` — NOT raw `HKEY_LOCAL_MACHINE\...`
>    - Environment variables: read with `$env:NAME`, set with `$env:NAME = "value"` (NOT `Set-Variable` or bash `export`)
>    - Call native exe with spaces in path via call operator: `& "C:\Program Files\App\app.exe" arg1 arg2`
>
> Interactive and blocking commands (will hang — this tool runs with -NonInteractive):
>    - NEVER use `Read-Host`, `Get-Credential`, `Out-GridView`, `$Host.UI.PromptForChoice`, or `pause`
>    - Destructive cmdlets (`Remove-Item`, `Stop-Process`, `Clear-Content`, etc.) may prompt for confirmation. Add `-Confirm:$false` when you intend the action to proceed. Use `-Force` for read-only/hidden items.
>    - Never use `git rebase -i`, `git add -i`, or other commands that open an interactive editor
>
> Passing multiline strings (commit messages, file content) to native executables:
>    - Use a single-quoted here-string so PowerShell does not expand `$` or backticks inside. The closing `'@` MUST be at column 0 (no leading whitespace) on its own line — indenting it is a parse error:
> <example>
> git commit -m @'
> Commit message here.
> Second line with $literal dollar signs.
> '@
> </example>
>    - Use `@'...'@` (single-quoted, literal) not `@"..."@` (double-quoted, interpolated) unless you need variable expansion
>    - For arguments containing `-`, `@`, or other characters PowerShell parses as operators, use the stop-parsing token: `git log --% --format=%H`
>
> Usage notes:
>   - The command argument is required.
>   - You can specify an optional timeout in milliseconds (up to ${MAX_TIMEOUT_MS_FN()}ms / ${MAX_TIMEOUT_MS_FN()/60000} minutes). If not specified, commands will timeout after ${DEFAULT_TIMEOUT_MS_FN()}ms (${DEFAULT_TIMEOUT_MS_FN()/60000} minutes).
>   - It is very helpful if you write a clear, concise description of what this command does.
>   - If the output exceeds ${MAX_OUTPUT_CHARS_FN()} characters, output will be truncated before being returned to you.
> ${CUSTOM_USAGE_NOTE?CUSTOM_USAGE_NOTE+`
> `:""}  - Avoid using PowerShell to run commands that have dedicated tools, unless explicitly instructed:
>     - File search: Use ${GLOB_TOOL_NAME} (NOT Get-ChildItem -Recurse)
>     - Content search: Use ${GREP_TOOL_NAME} (NOT Select-String)
>     - Read files: Use ${READ_TOOL_NAME} (NOT Get-Content)
>     - Edit files: Use ${EDIT_TOOL_NAME}
>     - Write files: Use ${WRITE_TOOL_NAME} (NOT Set-Content/Out-File)
>     - Communication: Output text directly (NOT Write-Output/Write-Host)
>   - When issuing multiple commands:
>     - If the commands are independent and can run in parallel, make multiple ${POWERSHELL_TOOL_NAME} tool calls in a single message.
>     - If the commands depend on each other and must run sequentially, chain them in a single ${POWERSHELL_TOOL_NAME} call (see edition-specific chaining syntax above).
>     - Use `;` only when you need to run commands sequentially but don't care if earlier commands fail.
>     - DO NOT use newlines to separate commands (newlines are ok in quoted strings and here-strings)
>   - Do NOT prefix commands with `cd` or `Set-Location` -- the working directory is already set to the correct project directory automatically.
> ${CUSTOM_GIT_NOTES?CUSTOM_GIT_NOTES+`
> `:""}  - For git commands:
>     - Prefer to create a new commit rather than amending an existing commit.
>     - Before running destructive operations (e.g., git reset --hard, git push --force, git checkout --), consider whether there is a safer alternative that achieves the same goal. Only use destructive operations when they are truly the best approach.
>     - Never skip hooks (--no-verify) or bypass signing (--no-gpg-sign, -c commit.gpgsign=false) unless the user has explicitly asked for it. If a hook fails, investigate and fix the underlying issue.

## 中文翻译

> **原文：**
> Executes a given PowerShell command with optional timeout. Working directory persists between commands; shell state (variables, functions) does not.

**翻译：**
执行给定的 PowerShell 命令，支持可选的超时设置。工作目录在命令之间保持不变；Shell 状态（变量、函数）不会保留。

---

> **原文：**
> IMPORTANT: This tool is for terminal operations via PowerShell: git, npm, docker, and PS cmdlets. DO NOT use it for file operations (reading, writing, editing, searching, finding files) - use the specialized tools for this instead.

**翻译：**
重要：此工具用于通过 PowerShell 执行终端操作：git、npm、docker 和 PS cmdlet。不要将其用于文件操作（读取、写入、编辑、搜索、查找文件）——请改用专用工具。

---

> **原文：**
> ${RENDER_COMMAND_NOTES_FN(COMMAND_NOTES)}

**翻译：**
${RENDER_COMMAND_NOTES_FN(COMMAND_NOTES)}（动态渲染的命令注意事项）

---

> **原文：**
> Before executing the command, please follow these steps:
>
> 1. Directory Verification:
>    - If the command will create new directories or files, first use `Get-ChildItem` (or `ls`) to verify the parent directory exists and is the correct location
>
> 2. Command Execution:
>    - Always quote file paths that contain spaces with double quotes
>    - Capture the output of the command.

**翻译：**
在执行命令之前，请遵循以下步骤：

1. 目录验证：
   - 如果命令将创建新目录或文件，先使用 `Get-ChildItem`（或 `ls`）验证父目录存在且是正确的位置

2. 命令执行：
   - 始终用双引号引用包含空格的文件路径
   - 捕获命令的输出。

---

> **原文：**
> PowerShell Syntax Notes:
>    - Variables use $ prefix: $myVar = "value"
>    - Escape character is backtick (`), not backslash
>    - Use Verb-Noun cmdlet naming: Get-ChildItem, Set-Location, New-Item, Remove-Item
>    - Common aliases: ls (Get-ChildItem), cd (Set-Location), cat (Get-Content), rm (Remove-Item)
>    - Pipe operator | works similarly to bash but passes objects, not text
>    - Use Select-Object, Where-Object, ForEach-Object for filtering and transformation
>    - String interpolation: "Hello $name" or "Hello $($obj.Property)"
>    - Registry access uses PSDrive prefixes: `HKLM:\SOFTWARE\...`, `HKCU:\...` — NOT raw `HKEY_LOCAL_MACHINE\...`
>    - Environment variables: read with `$env:NAME`, set with `$env:NAME = "value"` (NOT `Set-Variable` or bash `export`)
>    - Call native exe with spaces in path via call operator: `& "C:\Program Files\App\app.exe" arg1 arg2`

**翻译：**
PowerShell 语法说明：
   - 变量使用 $ 前缀：$myVar = "value"
   - 转义字符是反引号（`），不是反斜杠
   - 使用动词-名词的 cmdlet 命名：Get-ChildItem、Set-Location、New-Item、Remove-Item
   - 常用别名：ls（Get-ChildItem）、cd（Set-Location）、cat（Get-Content）、rm（Remove-Item）
   - 管道操作符 | 与 bash 类似但传递的是对象而非文本
   - 使用 Select-Object、Where-Object、ForEach-Object 进行过滤和转换
   - 字符串插值："Hello $name" 或 "Hello $($obj.Property)"
   - 注册表访问使用 PSDrive 前缀：`HKLM:\SOFTWARE\...`、`HKCU:\...` —— 不要使用原始的 `HKEY_LOCAL_MACHINE\...`
   - 环境变量：用 `$env:NAME` 读取，用 `$env:NAME = "value"` 设置（不要使用 `Set-Variable` 或 bash 的 `export`）
   - 通过调用操作符调用路径中有空格的原生可执行文件：`& "C:\Program Files\App\app.exe" arg1 arg2`

---

> **原文：**
> Interactive and blocking commands (will hang — this tool runs with -NonInteractive):
>    - NEVER use `Read-Host`, `Get-Credential`, `Out-GridView`, `$Host.UI.PromptForChoice`, or `pause`
>    - Destructive cmdlets (`Remove-Item`, `Stop-Process`, `Clear-Content`, etc.) may prompt for confirmation. Add `-Confirm:$false` when you intend the action to proceed. Use `-Force` for read-only/hidden items.
>    - Never use `git rebase -i`, `git add -i`, or other commands that open an interactive editor

**翻译：**
交互式和阻塞命令（会挂起——此工具以 -NonInteractive 模式运行）：
   - 切勿使用 `Read-Host`、`Get-Credential`、`Out-GridView`、`$Host.UI.PromptForChoice` 或 `pause`
   - 破坏性 cmdlet（`Remove-Item`、`Stop-Process`、`Clear-Content` 等）可能会提示确认。当你确定要执行操作时添加 `-Confirm:$false`。对只读/隐藏项使用 `-Force`。
   - 切勿使用 `git rebase -i`、`git add -i` 或其他会打开交互式编辑器的命令

---

> **原文：**
> Passing multiline strings (commit messages, file content) to native executables:
>    - Use a single-quoted here-string so PowerShell does not expand `$` or backticks inside. The closing `'@` MUST be at column 0 (no leading whitespace) on its own line — indenting it is a parse error:
>    - Use `@'...'@` (single-quoted, literal) not `@"..."@` (double-quoted, interpolated) unless you need variable expansion
>    - For arguments containing `-`, `@`, or other characters PowerShell parses as operators, use the stop-parsing token: `git log --% --format=%H`

**翻译：**
向原生可执行文件传递多行字符串（提交消息、文件内容）：
   - 使用单引号 here-string，这样 PowerShell 不会展开其中的 `$` 或反引号。结束标记 `'@` 必须在第 0 列（无前导空白）独占一行——缩进会导致解析错误：
   - 使用 `@'...'@`（单引号，字面量）而非 `@"..."@`（双引号，会插值），除非你需要变量展开
   - 对于包含 `-`、`@` 或其他 PowerShell 解析为操作符的字符的参数，使用停止解析标记：`git log --% --format=%H`

---

> **原文：**
> Usage notes:
>   - The command argument is required.
>   - You can specify an optional timeout in milliseconds (up to ${MAX_TIMEOUT_MS_FN()}ms / ${MAX_TIMEOUT_MS_FN()/60000} minutes). If not specified, commands will timeout after ${DEFAULT_TIMEOUT_MS_FN()}ms (${DEFAULT_TIMEOUT_MS_FN()/60000} minutes).
>   - It is very helpful if you write a clear, concise description of what this command does.
>   - If the output exceeds ${MAX_OUTPUT_CHARS_FN()} characters, output will be truncated before being returned to you.

**翻译：**
使用说明：
   - command 参数是必需的。
   - 你可以指定可选的超时时间（毫秒），最大 ${MAX_TIMEOUT_MS_FN()}ms / ${MAX_TIMEOUT_MS_FN()/60000} 分钟。如果未指定，命令将在 ${DEFAULT_TIMEOUT_MS_FN()}ms（${DEFAULT_TIMEOUT_MS_FN()/60000} 分钟）后超时。
   - 为命令编写清晰简洁的描述会非常有帮助。
   - 如果输出超过 ${MAX_OUTPUT_CHARS_FN()} 个字符，输出将在返回给你之前被截断。

---

> **原文：**
>   - Avoid using PowerShell to run commands that have dedicated tools, unless explicitly instructed:
>     - File search: Use ${GLOB_TOOL_NAME} (NOT Get-ChildItem -Recurse)
>     - Content search: Use ${GREP_TOOL_NAME} (NOT Select-String)
>     - Read files: Use ${READ_TOOL_NAME} (NOT Get-Content)
>     - Edit files: Use ${EDIT_TOOL_NAME}
>     - Write files: Use ${WRITE_TOOL_NAME} (NOT Set-Content/Out-File)
>     - Communication: Output text directly (NOT Write-Output/Write-Host)

**翻译：**
   - 避免使用 PowerShell 运行有专用工具的命令，除非明确指示：
     - 文件搜索：使用 ${GLOB_TOOL_NAME}（而非 Get-ChildItem -Recurse）
     - 内容搜索：使用 ${GREP_TOOL_NAME}（而非 Select-String）
     - 读取文件：使用 ${READ_TOOL_NAME}（而非 Get-Content）
     - 编辑文件：使用 ${EDIT_TOOL_NAME}
     - 写入文件：使用 ${WRITE_TOOL_NAME}（而非 Set-Content/Out-File）
     - 通信：直接输出文本（而非 Write-Output/Write-Host）

---

> **原文：**
>   - When issuing multiple commands:
>     - If the commands are independent and can run in parallel, make multiple ${POWERSHELL_TOOL_NAME} tool calls in a single message.
>     - If the commands depend on each other and must run sequentially, chain them in a single ${POWERSHELL_TOOL_NAME} call (see edition-specific chaining syntax above).
>     - Use `;` only when you need to run commands sequentially but don't care if earlier commands fail.
>     - DO NOT use newlines to separate commands (newlines are ok in quoted strings and here-strings)
>   - Do NOT prefix commands with `cd` or `Set-Location` -- the working directory is already set to the correct project directory automatically.

**翻译：**
   - 发出多个命令时：
     - 如果命令相互独立且可以并行运行，在一条消息中发出多个 ${POWERSHELL_TOOL_NAME} 工具调用。
     - 如果命令相互依赖且必须顺序运行，将它们链接在一个 ${POWERSHELL_TOOL_NAME} 调用中（参见上方版本特定的链接语法）。
     - 仅在需要顺序运行命令但不关心前面命令是否失败时使用 `;`。
     - 不要使用换行符分隔命令（在引号字符串和 here-string 中换行是可以的）
   - 不要在命令前加 `cd` 或 `Set-Location`——工作目录已自动设置为正确的项目目录。

---

> **原文：**
>   - For git commands:
>     - Prefer to create a new commit rather than amending an existing commit.
>     - Before running destructive operations (e.g., git reset --hard, git push --force, git checkout --), consider whether there is a safer alternative that achieves the same goal. Only use destructive operations when they are truly the best approach.
>     - Never skip hooks (--no-verify) or bypass signing (--no-gpg-sign, -c commit.gpgsign=false) unless the user has explicitly asked for it. If a hook fails, investigate and fix the underlying issue.

**翻译：**
   - 对于 git 命令：
     - 优先创建新提交，而非修改现有提交。
     - 在运行破坏性操作（例如 git reset --hard、git push --force、git checkout --）之前，考虑是否有更安全的替代方案可以达到相同目标。仅在确实是最佳方案时才使用破坏性操作。
     - 切勿跳过钩子（--no-verify）或绕过签名（--no-gpg-sign、-c commit.gpgsign=false），除非用户明确要求。如果钩子失败，应调查并修复根本问题。

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${RENDER_COMMAND_NOTES_FN}` | 渲染命令注意事项的函数 |
| `${COMMAND_NOTES}` | 命令注意事项的内容数据 |
| `${MAX_TIMEOUT_MS_FN}` | 返回最大超时时间（毫秒）的函数 |
| `${DEFAULT_TIMEOUT_MS_FN}` | 返回默认超时时间（毫秒）的函数 |
| `${MAX_OUTPUT_CHARS_FN}` | 返回最大输出字符数的函数 |
| `${CUSTOM_USAGE_NOTE}` | 自定义使用说明文本 |
| `${GLOB_TOOL_NAME}` | 文件匹配（glob）工具的名称 |
| `${GREP_TOOL_NAME}` | 搜索（grep）工具的名称 |
| `${READ_TOOL_NAME}` | 文件读取工具的名称 |
| `${EDIT_TOOL_NAME}` | 文件编辑工具的名称 |
| `${WRITE_TOOL_NAME}` | 文件写入工具的名称 |
| `${POWERSHELL_TOOL_NAME}` | PowerShell 工具的名称 |
| `${CUSTOM_GIT_NOTES}` | 自定义的 git 命令注意事项 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | `DO NOT use it for file operations` / `NEVER use Read-Host` / `DO NOT use newlines to separate commands` | 通过多处大写的 DO NOT/NEVER 约束，明确禁止将 PowerShell 用于文件操作和交互式命令，防止工具误用和会话挂起。 |
| 2 | 优先级排序（Priority Ordering） | 专用工具对照表：`File search: Use ${GLOB_TOOL_NAME} (NOT Get-ChildItem -Recurse)` 等 | 通过正反对比的工具映射表，为每种文件操作指明正确工具和错误工具，建立清晰的工具选择优先级。 |
| 3 | 结构化列表（Structured Enumeration） | `Directory Verification` → `Command Execution` → `PowerShell Syntax Notes` → `Interactive commands` → `Usage notes` | 按照命令执行的时间顺序组织内容：先验证→再执行→语法参考→注意事项，形成完整的操作流程。 |
| 4 | 示例引导（Example-driven Guidance） | here-string 示例 `git commit -m @'...'@` 和 stop-parsing 示例 `git log --% --format=%H` | 对于 PowerShell 特有的复杂语法（here-string、stop-parsing），通过具体示例降低出错概率。 |
| 5 | 安全防护指令（Safety Guard） | `Before running destructive operations, consider whether there is a safer alternative` / `Never skip hooks` | 对破坏性 git 操作和钩子绕过设置多层安全防护，引导 LLM 优先选择安全的替代方案。 |
| 6 | 动态上下文注入（Dynamic Context Injection） | `${MAX_TIMEOUT_MS_FN()}`, `${DEFAULT_TIMEOUT_MS_FN()}`, `${MAX_OUTPUT_CHARS_FN()}` 等 | 通过函数调用动态注入运行时的超时和输出限制参数，使提示词自适应不同的部署环境。 |
| 7 | 条件逻辑注入（Conditional Logic Injection） | `${CUSTOM_USAGE_NOTE?CUSTOM_USAGE_NOTE+...:""}`, `${CUSTOM_GIT_NOTES?...:""}` | 通过条件表达式按需注入自定义说明，使工具描述在不同配置下保持灵活性而不显示空内容。 |
