# edit

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Edit |
| 分类 | Tool Descriptions → 文件操作 |
| 文件路径 | `system-prompts/tool-description-edit.md` |
| CC 版本 | 2.1.91 |
| 模板变量 | `${MUST_READ_FIRST_FN}`, `${LINE_NUMBER_PREFIX_FORMAT}`, `${ADDITIONAL_EDIT_GUIDELINES_NOTE}` |

## 原文

> Performs exact string replacements in files.
>
> Usage:${MUST_READ_FIRST_FN()}
> - When editing text from Read tool output, ensure you preserve the exact indentation (tabs/spaces) as it appears AFTER the line number prefix. The line number prefix format is: ${LINE_NUMBER_PREFIX_FORMAT}. Everything after that is the actual file content to match. Never include any part of the line number prefix in the old_string or new_string.
> - ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required.
> - Only use emojis if the user explicitly requests it. Avoid adding emojis to files unless asked.${ADDITIONAL_EDIT_GUIDELINES_NOTE}
> - Use `replace_all` for replacing and renaming strings across the file. This parameter is useful if you want to rename a variable for instance.

## 中文翻译

> **原文：**
> Performs exact string replacements in files.

**翻译：**
在文件中执行精确的字符串替换。

---

> **原文：**
> Usage:${MUST_READ_FIRST_FN()}
> - When editing text from Read tool output, ensure you preserve the exact indentation (tabs/spaces) as it appears AFTER the line number prefix. The line number prefix format is: ${LINE_NUMBER_PREFIX_FORMAT}. Everything after that is the actual file content to match. Never include any part of the line number prefix in the old_string or new_string.
> - ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required.
> - Only use emojis if the user explicitly requests it. Avoid adding emojis to files unless asked.${ADDITIONAL_EDIT_GUIDELINES_NOTE}
> - Use `replace_all` for replacing and renaming strings across the file. This parameter is useful if you want to rename a variable for instance.

**翻译：**
用法：${MUST_READ_FIRST_FN()}
- 当编辑来自 Read 工具输出的文本时，确保保留行号前缀之后的精确缩进（制表符/空格）。行号前缀格式为：${LINE_NUMBER_PREFIX_FORMAT}。前缀之后的内容才是需要匹配的实际文件内容。切勿在 old_string 或 new_string 中包含行号前缀的任何部分。
- 始终优先编辑代码库中已有的文件。除非明确要求，否则切勿创建新文件。
- 仅在用户明确请求时才使用表情符号。除非被要求，否则避免向文件中添加表情符号。${ADDITIONAL_EDIT_GUIDELINES_NOTE}
- 使用 `replace_all` 在整个文件中替换和重命名字符串。此参数在你想要重命名变量等场景中非常有用。

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${MUST_READ_FIRST_FN}` | 动态生成的提醒文本，要求在编辑前先读取文件 |
| `${LINE_NUMBER_PREFIX_FORMAT}` | 行号前缀的格式说明 |
| `${ADDITIONAL_EDIT_GUIDELINES_NOTE}` | 附加的编辑指导说明 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | `NEVER write new files unless explicitly required` / `Never include any part of the line number prefix` | 使用大写 NEVER 强调禁止行为，防止 LLM 在编辑时创建不必要的新文件或错误地包含行号前缀，这是常见的错误模式。 |
| 2 | 优先级排序（Priority Ordering） | `ALWAYS prefer editing existing files in the codebase` | 建立明确的行为优先级——编辑优先于创建，引导 LLM 采取最小侵入性的修改方式。 |
| 3 | 结构化列表（Structured Enumeration） | 使用 `-` 列表枚举所有使用规则 | 将多条规则以列表形式呈现，每条规则独立且具体，便于 LLM 逐条遵循。 |
| 4 | 动态上下文注入（Dynamic Context Injection） | `${MUST_READ_FIRST_FN()}`, `${LINE_NUMBER_PREFIX_FORMAT}` | 通过函数调用动态注入"先读后编辑"的前置条件和行号格式，确保工具说明与实际运行时行为一致。 |
| 5 | 安全防护指令（Safety Guard） | `Only use emojis if the user explicitly requests it` | 防止 LLM 自作主张地在代码中添加表情符号，保护代码的专业性和可读性。 |
