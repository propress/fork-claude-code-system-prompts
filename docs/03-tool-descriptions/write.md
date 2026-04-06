# write

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Write |
| 分类 | Tool Descriptions → 文件操作 |
| 文件路径 | `system-prompts/tool-description-write.md` |
| CC 版本 | 2.1.92 |
| 模板变量 | `${GET_NEW_FILE_NOTE_FN}`, `${PREFER_EDIT_NOTE}` |

## 原文

> Writes a file to the local filesystem.
>
> Usage:
> - This tool will overwrite the existing file if there is one at the provided path.${GET_NEW_FILE_NOTE_FN()}
> - Prefer the Edit tool for modifying existing files — it only sends the diff.${PREFER_EDIT_NOTE} Only use this tool to create new files or for complete rewrites.
> - NEVER create documentation files (*.md) or README files unless explicitly requested by the User.
> - Only use emojis if the user explicitly requests it. Avoid writing emojis to files unless asked.

## 中文翻译

> **原文：**
> Writes a file to the local filesystem.

**翻译：**
将文件写入本地文件系统。

> **原文：**
> This tool will overwrite the existing file if there is one at the provided path.

**翻译：**
如果在提供的路径上存在文件，此工具会覆盖现有文件。

> **原文：**
> Prefer the Edit tool for modifying existing files — it only sends the diff. Only use this tool to create new files or for complete rewrites.

**翻译：**
修改现有文件时优先使用 Edit 工具——它只发送差异部分。仅将此工具用于创建新文件或完全重写。

> **原文：**
> NEVER create documentation files (*.md) or README files unless explicitly requested by the User.

**翻译：**
除非用户明确要求，**永远不要**创建文档文件（*.md）或 README 文件。

> **原文：**
> Only use emojis if the user explicitly requests it. Avoid writing emojis to files unless asked.

**翻译：**
仅在用户明确要求时使用 emoji。除非被要求，避免向文件写入 emoji。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `GET_NEW_FILE_NOTE_FN` | 函数 | 运行时返回关于新文件的附加说明 |
| `PREFER_EDIT_NOTE` | 字符串 | 关于优先使用 Edit 的附加说明 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | Edit 优先 | `Prefer the Edit tool ... it only sends the diff` | 解释性能原因建立工具优先级 |
| 2 | 文档禁令 | `NEVER create documentation files (*.md) or README` | 防止模型主动生成未请求的文档 |
| 3 | Emoji 限制 | `Only use emojis if the user explicitly requests it` | 控制输出的专业性 |
| 4 | 覆盖警告 | `will overwrite the existing file` | 明确说明破坏性行为 |
