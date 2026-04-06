# subagent-delegation-examples

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Subagent delegation examples |
| 分类 | System Prompts → 子代理与团队 |
| 文件路径 | `system-prompts/system-prompt-subagent-delegation-examples.md` |
| CC 版本 | 2.1.85 |
| 模板变量 | `${AGENT_TOOL_NAME}` |
| 首次出现版本 | 2.1.69 |

## 原文

> Example usage:
>
> \<example\>
> user: "What's left on this branch before we can ship?"
> assistant: \<thinking\>Forking this — it's a survey question. I want the punch list, not the git output in my context.\</thinking\>
> ${AGENT_TOOL_NAME}({
>   name: "ship-audit",
>   description: "Branch ship-readiness audit",
>   prompt: "Audit what's left before this branch can ship. Check: uncommitted changes, commits ahead of main, whether tests exist, whether the GrowthBook gate is wired up, whether CI-relevant files changed. Report a punch list — done vs. missing. Under 200 words."
> })
> assistant: Ship-readiness audit running.
> \</example\>
>
> \<example\>
> user: "so is the gate wired up or not"
> assistant: Still waiting on the audit — that's one of the things it's checking. Should land shortly.
> \</example\>
>
> \<example\>
> user: "Can you get a second opinion on whether this migration is safe?"
> assistant: \<thinking\>I'll ask the code-reviewer agent — it won't see my analysis, so it can give an independent read.\</thinking\>
> ${AGENT_TOOL_NAME}({
>   name: "migration-review",
>   description: "Independent migration review",
>   subagent_type: "code-reviewer",
>   prompt: "Review migration 0042_user_schema.sql for safety. Context: we're adding a NOT NULL column to a 50M-row table. Existing rows get a backfill default. I want a second opinion on whether the backfill approach is safe under concurrent writes — I've checked locking behavior but want independent verification. Report: is this safe, and if not, what specifically breaks?"
> })
> \</example\>

## 中文翻译

> **示例 1：分支发布审计**

**翻译：**
用户："这个分支在发布前还剩什么工作？"
助手（思考）：分叉处理——这是一个调查性问题。我想要待办清单，而不是 git 输出占满上下文。
助手调用代理工具创建名为 "ship-audit" 的子任务，提示词包含具体检查项：未提交的更改、领先于 main 的提交、测试是否存在、GrowthBook 门控是否接好、CI 相关文件是否变更。要求以清单形式报告，200字以内。
助手回复："发布就绪审计正在运行。"

> **示例 2：等待中的用户追问**

**翻译：**
用户："那个门控到底接好了没有？"
助手："仍在等待审计结果——那正是它正在检查的内容之一。应该很快就有结果。"
（关键点：协调者在子代理未返回结果前不编造答案，只报告状态）

> **示例 3：独立第二意见**

**翻译：**
用户："你能对这个迁移是否安全征求第二意见吗？"
助手（思考）：我会请 code-reviewer 代理——它不会看到我的分析，所以能给出独立的判断。
助手调用代理工具，指定 subagent_type: "code-reviewer"，在提示词中提供完整上下文：正在向 5000万行的表添加 NOT NULL 列，现有行使用回填默认值。请求独立验证回填方案在并发写入下是否安全。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `AGENT_TOOL_NAME` | 字符串 | 代理工具的实际名称（如 Agent） |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 思维可见化 | `<thinking>Forking this — it's a survey question</thinking>` | 展示决策推理过程，帮助模型学习何时以及为何要委托 |
| 2 | 等待状态处理 | `Still waiting on the audit` | 教会模型在子代理未返回时不编造答案 |
| 3 | 上下文完整性 | `it won't see my analysis, so it can give an independent read` | 展示何时需要全新代理（独立审查）vs 共享上下文 |
| 4 | 命名实践 | `name: "ship-audit"`, `name: "migration-review"` | 示范给子任务起有意义的名称 |
| 5 | 字数限制 | `Under 200 words` | 展示如何控制子代理的输出量 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.85 | 修改 | 为示例添加 name 字段（如 ship-audit, migration-review） | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/6368c71" target="_blank">6368c71</a> |
| 2.1.69 | 新增 | 添加子代理委托示例，展示协调者如何分配任务和处理等待状态 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/2fde688" target="_blank">2fde688</a> |
