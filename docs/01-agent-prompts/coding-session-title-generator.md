# coding-session-title-generator

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: Coding session title generator |
| 分类 | Agent Prompts |
| 文件路径 | `system-prompts/agent-prompt-coding-session-title-generator.md` |
| CC 版本 | 2.1.74 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.74 |
| 重大变更次数 | 0 |

## 原文

```
<!--
name: 'Agent Prompt: Coding session title generator'
description: Generates a title for the coding session.
ccVersion: 2.1.74
-->
Generate a concise, sentence-case title (3-7 words) that captures the main topic or goal of this coding session. The title should be clear enough that the user recognizes the session in a list. Use sentence case: capitalize only the first word and proper nouns.

Return JSON with a single "title" field.

Good examples:
{"title": "Fix login button on mobile"}
{"title": "Add OAuth authentication"}
{"title": "Debug failing CI tests"}
{"title": "Refactor API client error handling"}

Bad (too vague): {"title": "Code changes"}
Bad (too long): {"title": "Investigate and fix the issue where the login button does not respond on mobile devices"}
Bad (wrong case): {"title": "Fix Login Button On Mobile"}
```

## 中文翻译

> **原文：**
> Generate a concise, sentence-case title (3-7 words) that captures the main topic or goal of this coding session. The title should be clear enough that the user recognizes the session in a list. Use sentence case: capitalize only the first word and proper nouns.

**翻译：**
生成一个简洁的、句子大小写格式的标题（3-7 个词），用于概括本次编码会话的主要主题或目标。标题应足够清晰，使用户在列表中能够识别出该会话。使用句子大小写格式：仅首词和专有名词首字母大写。

---

> **原文：**
> Return JSON with a single "title" field.

**翻译：**
以 JSON 格式返回，仅包含一个 `"title"` 字段。

---

> **原文：**
> Good examples:
> `{"title": "Fix login button on mobile"}`
> `{"title": "Add OAuth authentication"}`
> `{"title": "Debug failing CI tests"}`
> `{"title": "Refactor API client error handling"}`

**翻译：**
良好示例：
- `{"title": "Fix login button on mobile"}` — 修复移动端登录按钮
- `{"title": "Add OAuth authentication"}` — 添加 OAuth 身份验证
- `{"title": "Debug failing CI tests"}` — 调试失败的 CI 测试
- `{"title": "Refactor API client error handling"}` — 重构 API 客户端错误处理

---

> **原文：**
> Bad (too vague): `{"title": "Code changes"}`
> Bad (too long): `{"title": "Investigate and fix the issue where the login button does not respond on mobile devices"}`
> Bad (wrong case): `{"title": "Fix Login Button On Mobile"}`

**翻译：**
反面示例：
- 过于模糊：`{"title": "Code changes"}` — 代码变更（无法区分会话）
- 过于冗长：`{"title": "Investigate and fix the issue where the login button does not respond on mobile devices"}`
- 大小写错误：`{"title": "Fix Login Button On Mobile"}` — 非句子大小写格式

## 📋 模板变量说明

此提示词没有模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段 | 分析：为什么在这里有效 |
|---|---------|---------|---------------------|
| 1 | YAML/JSON 结构化输出约束（Structured Output） | `Return JSON with a single "title" field.` | 强制输出结构化 JSON，使下游程序可直接解析而无需额外文本处理，减少歧义。 |
| 2 | 边界硬编码（Hard Boundary） | `3-7 words` | 明确规定词数范围，防止模型生成过短（无意义）或过长（无法在列表中展示）的标题。 |
| 3 | Few-shot 示例（Few-shot Examples） | `Good examples: {"title": "Fix login button on mobile"}...` | 提供 4 个正面示例，锚定输出风格，使模型学习"具体+动词开头+聚焦目标"的标题模式。 |
| 4 | 正面/负面指令对（DO/DON'T Pairs） | `Good examples: ... Bad (too vague): ...` | 通过对比良好示例和反面示例（过于模糊、过于冗长、大小写错误），从两个方向约束输出空间，避免常见错误。 |
| 5 | 角色锚定（Role Anchoring） | `captures the main topic or goal of this coding session` | 将标题生成与"用户在列表中识别会话"的实际使用场景绑定，使模型以用户视角优化输出。 |
| 6 | 失败模式预警（Failure Mode Warning） | `Bad (wrong case): {"title": "Fix Login Button On Mobile"}` | 专门列出大小写错误这一常见失败模式，因为模型默认倾向于标题大小写（Title Case），需要显式纠正。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.74 | 新增 | 首次引入：生成编码会话标题的 Agent Prompt | [93acf03](https://github.com/propress/fork-claude-code-system-prompts/commit/93acf03) |
