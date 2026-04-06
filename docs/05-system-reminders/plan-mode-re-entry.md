# plan-mode-re-entry

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Plan mode re-entry |
| 分类 | System Reminders → 计划模式 |
| 文件路径 | `system-prompts/system-reminder-plan-mode-re-entry.md` |
| CC 版本 | 2.0.52 |
| 模板变量 | `${SYSTEM_REMINDER}`, `${EXIT_PLAN_MODE_TOOL_OBJECT}` |

## 原文

> ## Re-entering Plan Mode
>
> You are returning to plan mode after having previously exited it. A plan file exists at ${SYSTEM_REMINDER.planFilePath} from your previous planning session.
>
> **Before proceeding with any new planning, you should:**
> 1. Read the existing plan file to understand what was previously planned
> 2. Evaluate the user's current request against that plan
> 3. Decide how to proceed:
>    - **Different task**: start fresh by overwriting the existing plan
>    - **Same task, continuing**: modify the existing plan while cleaning up outdated sections
> 4. Continue on with the plan process and edit the plan file before calling ${EXIT_PLAN_MODE_TOOL_OBJECT.name}
>
> Treat this as a fresh planning session. Do not assume the existing plan is relevant without evaluating it first.

## 中文翻译

> **原文：**
> You are returning to plan mode after having previously exited it. A plan file exists at ${SYSTEM_REMINDER.planFilePath} from your previous planning session.

**翻译：**
你正在重新进入计划模式（之前已退出过）。你之前的计划会话中的计划文件位于 ${SYSTEM_REMINDER.planFilePath}。

> **原文：**
> Treat this as a fresh planning session. Do not assume the existing plan is relevant without evaluating it first.

**翻译：**
将此视为一次全新的计划会话。不要在评估之前就假设现有计划是相关的。

**操作步骤：**
1. 阅读现有计划文件以了解之前的计划内容
2. 将用户当前请求与该计划进行对比评估
3. 决定如何继续：
   - **不同任务**：通过覆盖现有计划重新开始
   - **同一任务，继续推进**：修改现有计划并清理过时的部分
4. 继续计划流程，并在调用 ${EXIT_PLAN_MODE_TOOL_OBJECT.name} 之前编辑计划文件

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 状态恢复协议 | "You are returning to plan mode after having previously exited it" | 明确告知模型当前是"重新进入"状态，触发不同于首次进入的处理流程 |
| 2 | 评估优先原则 | "Do not assume the existing plan is relevant without evaluating it first" | 防止模型盲目延续旧计划，强制要求先评估再行动 |
| 3 | 分支决策框架 | "Different task: start fresh" vs "Same task, continuing: modify" | 提供清晰的二分决策框架，使模型能根据具体情况选择正确的处理路径 |
