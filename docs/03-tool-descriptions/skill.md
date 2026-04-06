# skill

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Skill |
| 分类 | Tool Descriptions → Agent 工具 |
| 文件路径 | `system-prompts/tool-description-skill.md` |
| CC 版本 | 2.1.23 |
| 模板变量 | `${SKILL_TAG_NAME}` |

## 原文

> Execute a skill within the main conversation
>
> When users ask you to perform tasks, check if any of the available skills match. Skills provide specialized capabilities and domain knowledge.
>
> When users reference a "slash command" or "/\<something\>" (e.g., "/commit", "/review-pr"), they are referring to a skill. Use this tool to invoke it.
>
> How to invoke:
> - Use this tool with the skill name and optional arguments
> - Examples:
>   - `skill: "pdf"` - invoke the pdf skill
>   - `skill: "commit", args: "-m 'Fix bug'"` - invoke with arguments
>   - `skill: "review-pr", args: "123"` - invoke with arguments
>   - `skill: "ms-office-suite:pdf"` - invoke using fully qualified name
>
> Important:
> - Available skills are listed in system-reminder messages in the conversation
> - When a skill matches the user's request, this is a BLOCKING REQUIREMENT: invoke the relevant Skill tool BEFORE generating any other response about the task
> - NEVER mention a skill without actually calling this tool
> - Do not invoke a skill that is already running
> - Do not use this tool for built-in CLI commands (like /help, /clear, etc.)
> - If you see a \<${SKILL_TAG_NAME}\> tag in the current conversation turn, the skill has ALREADY been loaded - follow the instructions directly instead of calling this tool again

## 中文翻译

> **原文：**
> Execute a skill within the main conversation

**翻译：**
在主对话中执行一个技能。

> **原文：**
> When users reference a "slash command" or "/\<something\>", they are referring to a skill.

**翻译：**
当用户引用"斜杠命令"或"/\<something\>"（如 "/commit"、"/review-pr"）时，他们指的是一个技能。使用此工具来调用它。

> **原文：**
> When a skill matches the user's request, this is a BLOCKING REQUIREMENT: invoke the relevant Skill tool BEFORE generating any other response about the task

**翻译：**
当技能匹配用户请求时，这是一个阻塞性要求：在生成关于该任务的任何其他响应之前，先调用相关的 Skill 工具。

> **原文：**
> If you see a \<${SKILL_TAG_NAME}\> tag in the current conversation turn, the skill has ALREADY been loaded

**翻译：**
如果你在当前对话轮次中看到 `<${SKILL_TAG_NAME}>` 标签，说明技能已经加载——直接遵循指令而非再次调用此工具。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `SKILL_TAG_NAME` | 字符串 | 技能标签名称，用于检测技能是否已加载 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 阻塞性要求 | `BLOCKING REQUIREMENT: invoke ... BEFORE` | 确保技能调用优先于任何文本生成 |
| 2 | 重复调用防护 | `skill has ALREADY been loaded` | 通过标签检测防止重复调用 |
| 3 | 边界划定 | `Do not use ... for built-in CLI commands` | 区分技能与内置命令 |
