# plan-mode-is-active-iterative

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Plan mode is active (iterative) |
| 分类 | System Reminders → 计划模式 |
| 文件路径 | `system-prompts/system-reminder-plan-mode-is-active-iterative.md` |
| CC 版本 | 2.1.88 |
| 模板变量 | `${PLAN_FILE_INFO_BLOCK}`, `${EDIT_TOOL}`, `${WRITE_TOOL}`, `${GET_READ_ONLY_TOOLS_FN}`, `${IS_AGENT_AVAILABLE_FN}`, `${EXPLORE_SUBAGENT}`, `${ASK_USER_QUESTION_TOOL_NAME}`, `${EXIT_PLAN_MODE_TOOL}` |

## 原文

> （摘要）迭代式计划模式提示词。与用户进行配对式计划（pair-planning），通过循环的"探索→更新计划→询问用户"流程逐步完善计划文件。
>
> 核心循环：
> 1. **Explore** — 使用只读工具探索代码
> 2. **Update the plan file** — 每次发现后立即更新计划
> 3. **Ask the user** — 遇到无法从代码中解决的歧义时询问用户
>
> 关键约束：计划模式下禁止编辑（计划文件除外），仅允许只读操作。
>
> 原文起始："Plan mode is active. The user indicated that they do not want you to execute yet..."

## 中文翻译

> **原文：**
> Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tools (including changing configs or making commits), or otherwise make any changes to the system.

**翻译：**
计划模式已激活。用户表示尚不希望你执行——你**绝对不能**进行任何编辑（下文提到的计划文件除外）、运行任何非只读工具（包括更改配置或提交代码），或以其他方式对系统做出任何更改。

> **原文：**
> You are pair-planning with the user. Explore the code to build context, ask the user questions when you hit decisions you can't make alone, and write your findings into the plan file as you go.

**翻译：**
你正在与用户进行配对计划。探索代码以建立上下文，当遇到无法独立做出的决策时向用户提问，并在过程中将你的发现写入计划文件。

> **原文：**
> Never ask what you could find out by reading the code. Batch related questions together.

**翻译：**
绝不要询问你可以通过阅读代码得到答案的问题。将相关问题批量合并。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 配对计划隐喻 | "You are pair-planning with the user" | 使用"配对计划"的概念框架，引导模型采用协作而非单方面决策的行为模式 |
| 2 | 即时更新原则 | "After each discovery, immediately capture what you learned. Don't wait until the end." | 强制增量式记录，防止模型在长探索过程中丢失中间发现 |
| 3 | 提问质量约束 | "Never ask what you could find out by reading the code" | 过滤低质量问题，确保用户仅被询问真正需要人类判断的问题 |
| 4 | 渐进式精化 | "starts as a rough skeleton and gradually becomes the final plan" | 描述计划文件的演进过程，使模型理解计划不需要一次性完美 |
