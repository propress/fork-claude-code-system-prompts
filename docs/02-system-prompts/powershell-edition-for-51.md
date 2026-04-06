# powershell-edition-for-51

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: PowerShell edition for 5.1 |
| 分类 | System Prompts → 平台与环境 |
| 文件路径 | `system-prompts/system-prompt-powershell-edition-for-51.md` |
| CC 版本 | 2.1.88 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.88 |

## 原文

> PowerShell edition: Windows PowerShell 5.1 (powershell.exe)
>    - Pipeline chain operators `&&` and `||` are NOT available — they cause a parser error. To run B only if A succeeds: `A; if ($?) { B }`. To chain unconditionally: `A; B`.
>    - Ternary (`?:`), null-coalescing (`??`), and null-conditional (`?.`) operators are NOT available. Use `if/else` and explicit `$null -eq` checks instead.
>    - Avoid `2>&1` on native executables. In 5.1, redirecting a native command's stderr inside PowerShell wraps each line in an ErrorRecord (NativeCommandError) and sets `$?` to `$false` even when the exe returned exit code 0. stderr is already captured for you — don't redirect it.
>    - Default file encoding is UTF-16 LE (with BOM). When writing files other tools will read, pass `-Encoding utf8` to `Out-File`/`Set-Content`.
>    - `ConvertFrom-Json` returns a PSCustomObject, not a hashtable. `-AsHashtable` is not available.

## 中文翻译

> **原文：**
> PowerShell edition: Windows PowerShell 5.1 (powershell.exe)

**翻译：**
PowerShell 版本：Windows PowerShell 5.1 (powershell.exe)

> **原文：**
> Pipeline chain operators `&&` and `||` are NOT available — they cause a parser error. To run B only if A succeeds: `A; if ($?) { B }`. To chain unconditionally: `A; B`.

**翻译：**
管道链操作符 `&&` 和 `||` 不可用——它们会导致解析器错误。要在 A 成功时才运行 B：`A; if ($?) { B }`。无条件链式执行：`A; B`。

> **原文：**
> Ternary (`?:`), null-coalescing (`??`), and null-conditional (`?.`) operators are NOT available. Use `if/else` and explicit `$null -eq` checks instead.

**翻译：**
三元运算符 (`?:`)、空合并运算符 (`??`) 和空条件运算符 (`?.`) 不可用。请使用 `if/else` 和显式 `$null -eq` 检查代替。

> **原文：**
> Avoid `2>&1` on native executables. In 5.1, redirecting a native command's stderr inside PowerShell wraps each line in an ErrorRecord (NativeCommandError) and sets `$?` to `$false` even when the exe returned exit code 0. stderr is already captured for you — don't redirect it.

**翻译：**
避免在原生可执行文件上使用 `2>&1`。在 5.1 中，在 PowerShell 内重定向原生命令的 stderr 会将每行包装为 ErrorRecord (NativeCommandError)，并将 `$?` 设置为 `$false`，即使 exe 返回了退出码 0。stderr 已经为你捕获了——不要重定向它。

> **原文：**
> Default file encoding is UTF-16 LE (with BOM). When writing files other tools will read, pass `-Encoding utf8` to `Out-File`/`Set-Content`.

**翻译：**
默认文件编码是 UTF-16 LE（带 BOM）。当写入其他工具需要读取的文件时，请向 `Out-File`/`Set-Content` 传递 `-Encoding utf8`。

> **原文：**
> `ConvertFrom-Json` returns a PSCustomObject, not a hashtable. `-AsHashtable` is not available.

**翻译：**
`ConvertFrom-Json` 返回 PSCustomObject 而非 hashtable。`-AsHashtable` 参数不可用。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 平台感知 | `PowerShell edition: Windows PowerShell 5.1` | 精确标注运行时版本，避免使用 PS 7+ 特性 |
| 2 | 替代方案配对 | `are NOT available ... Use if/else ... instead` | 每个"不能用"都配对一个"应该用什么"，直接可操作 |
| 3 | 陷阱预警 | `sets $? to $false even when the exe returned exit code 0` | 解释底层机制帮助模型理解为何要避免 |
| 4 | 编码提醒 | `Default file encoding is UTF-16 LE (with BOM)` | 跨工具兼容性的关键细节 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.88 | 新增 | 添加 Windows PowerShell 5.1 的平台特定信息 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/7d7c728" target="_blank">7d7c728</a> |
