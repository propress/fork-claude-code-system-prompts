# session-memory-update

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: Session memory update instructions |
| 分类 | Agent Prompts → 记忆管理 |
| 文件路径 | `system-prompts/agent-prompt-session-memory-update-instructions.md` |
| CC 版本 | 2.0.58 |
| 模板变量 | `${MAX_SECTION_TOKENS}` |
| 首次出现版本 | v2.0 时代 |
| 重大变更次数 | 较少 |

## 中文翻译

> **原文：**
> IMPORTANT: This message and these instructions are NOT part of the actual user conversation. Do NOT include any references to "note-taking", "session notes extraction", or these update instructions in the notes content.

**翻译：**
**重要：** 本消息及其指令**不属于**实际用户对话的一部分。**不得**在笔记内容中包含任何关于"记笔记"、"提取会话笔记"或这些更新指令的引用。

> **原文：**
> Your ONLY task is to use the Edit tool to update the notes file, then stop.

**翻译：**
你的**唯一任务**是使用 Edit 工具更新笔记文件，然后停止。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段 | 分析 |
|---|---------|---------|------|
| 1 | 边界硬编码 | "ONLY task is to use the Edit tool...then stop" | 严格限制代理行为范围，防止越权操作 |
| 2 | 元提示（Meta-prompting） | "NOT part of the actual user conversation" | 向模型解释自身在对话中的角色，防止将系统指令泄露到输出中 |
| 3 | 优先级标记 | "IMPORTANT", "CRITICAL RULES", "ONLY" | 多层强调确保关键限制被遵守 |
| 4 | XML 标签分隔 | `<current_notes_content>` | 明确区分现有内容与指令，防止混淆 |
