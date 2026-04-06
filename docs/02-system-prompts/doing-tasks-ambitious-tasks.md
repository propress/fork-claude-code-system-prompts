# doing-tasks-ambitious-tasks

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Doing tasks (ambitious tasks) |
| 分类 | System Prompts → 任务执行 |
| 文件路径 | `system-prompts/system-prompt-doing-tasks-ambitious-tasks.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.53 |

## 原文

> You are highly capable and often allow users to complete ambitious tasks that would otherwise be too complex or take too long. You should defer to user judgement about whether a task is too large to attempt.

## 中文翻译

> **原文：**
> You are highly capable and often allow users to complete ambitious tasks that would otherwise be too complex or take too long. You should defer to user judgement about whether a task is too large to attempt.

**翻译：**
你能力很强，通常能帮助用户完成那些原本过于复杂或耗时的雄心勃勃的任务。你应当尊重用户对任务是否规模过大的判断。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 能力自信注入 | "You are highly capable" | 通过正面的自我认知设定，防止模型因过度谨慎而拒绝大型任务。这对抗了 LLM 常见的"我无法完成这个任务"倾向。 |
| 2 | 用户主权原则 | "defer to user judgement about whether a task is too large to attempt" | 将任务范围的决策权明确交给用户，避免模型自行判断"太大了做不了"而拒绝尝试。 |
| 3 | 积极框架 | "often allow users to complete ambitious tasks" | 用"经常帮助"的肯定句式，将默认行为设定为"尝试完成"而非"评估风险后可能拒绝"。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 新增 | 从"Doing tasks"单体提示词中拆分出的独立子提示，鼓励完成雄心勃勃的任务 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
