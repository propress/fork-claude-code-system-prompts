# tool-usage-skill-invocation

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Tool usage (skill invocation) |
| 分类 | System Prompts → 工具使用策略 |
| 文件路径 | `system-prompts/system-prompt-tool-usage-skill-invocation.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${SKILL_TOOL_NAME}` |
| 首次出现版本 | 2.1.53 |

## 原文

> /\<skill-name\> (e.g., /commit) is shorthand for users to invoke a user-invocable skill. When executed, the skill gets expanded to a full prompt. Use the ${SKILL_TOOL_NAME} tool to execute them. IMPORTANT: Only use ${SKILL_TOOL_NAME} for skills listed in its user-invocable skills section - do not guess or use built-in CLI commands.

## 中文翻译

**翻译：**
/\<skill-name\>（例如 /commit）是用户调用可调用技能的简写形式。执行时，技能会展开为完整的提示词。使用 ${SKILL_TOOL_NAME} 工具来执行它们。重要：仅对用户可调用技能列表中列出的技能使用 ${SKILL_TOOL_NAME}——不要猜测或使用内置 CLI 命令。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `SKILL_TOOL_NAME` | 字符串 | 技能工具的实际名称（如 Skill） |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 白名单约束 | `Only use ... for skills listed in its user-invocable skills section` | 限制技能调用范围，防止幻觉调用不存在的技能 |
| 2 | 双重禁止 | `do not guess or use built-in CLI commands` | 同时禁止猜测和混淆 CLI 命令 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 拆分 | 从工具使用策略大文件中拆分 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
