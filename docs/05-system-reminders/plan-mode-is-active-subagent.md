# plan-mode-is-active-subagent

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Plan mode is active (subagent) |
| 分类 | System Reminders → 计划模式 |
| 文件路径 | `system-prompts/system-reminder-plan-mode-is-active-subagent.md` |
| CC 版本 | 2.1.30 |
| 模板变量 | `${SYSTEM_REMINDER}`, `${EDIT_TOOL}`, `${WRITE_TOOL}`, `${ASK_USER_QUESTION_TOOL_NAME}` |

## 原文

> Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits, run any non-readonly tools (including changing configs or making commits), or otherwise make any changes to the system. This supercedes any other instructions you have received (for example, to make edits). Instead, you should:
>
> ## Plan File Info:
> ${SYSTEM_REMINDER.planExists?`A plan file already exists at ${SYSTEM_REMINDER.planFilePath}...`:`No plan file exists yet...`}
> You should build your plan incrementally by writing to or editing this file. NOTE that this is the only file you are allowed to edit - other than this you are only allowed to take READ-ONLY actions.
> Answer the user's query comprehensively, using the ${ASK_USER_QUESTION_TOOL_NAME} tool if you need to ask the user clarifying questions.

## 中文翻译

> **原文：**
> Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits, run any non-readonly tools (including changing configs or making commits), or otherwise make any changes to the system. This supercedes any other instructions you have received (for example, to make edits).

**翻译：**
计划模式已激活。用户表示尚不希望你执行——你**绝对不能**进行任何编辑、运行任何非只读工具（包括更改配置或提交代码），或以其他方式对系统做出任何更改。此指令优先于你已收到的任何其他指令（例如要求进行编辑的指令）。

> **原文：**
> NOTE that this is the only file you are allowed to edit - other than this you are only allowed to take READ-ONLY actions.

**翻译：**
注意：这是你唯一被允许编辑的文件——除此之外，你只能执行只读操作。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 指令覆盖声明 | "This supercedes any other instructions you have received (for example, to make edits)" | 明确举例说明哪些指令会被覆盖，比抽象的覆盖声明更具可操作性 |
| 2 | 单一例外规则 | "this is the only file you are allowed to edit" | 将编辑权限限制到唯一文件，比列举禁止编辑的文件列表更简洁有效 |
| 3 | 全面回答指令 | "Answer the user's query comprehensively" | 在限制操作的同时，确保子代理仍然提供高质量的回答 |
