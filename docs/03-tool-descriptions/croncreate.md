# croncreate

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: CronCreate |
| 分类 | Tool Descriptions → 通用工具 |
| 文件路径 | `system-prompts/tool-description-croncreate.md` |
| CC 版本 | 2.1.83 |
| 模板变量 | `${CRON_DURABLE_FLAG}`, `${CANCEL_TIMEFRAME_DAYS}`, `${CRON_DELETE_TOOL_NAME}` |

## 原文

> Schedule a prompt to be enqueued at a future time. Use for both recurring schedules and one-shot reminders.
>
> Uses standard 5-field cron in the user's local timezone: minute hour day-of-month month day-of-week. "0 9 * * *" means 9am local — no timezone conversion needed.
>
> ## One-shot tasks (recurring: false)
>
> For "remind me at X" or "at <time>, do Y" requests — fire once then auto-delete.
> Pin minute/hour/day-of-month/month to specific values:
>   "remind me at 2:30pm today to check the deploy" → cron: "30 14 <today_dom> <today_month> *", recurring: false
>   "tomorrow morning, run the smoke test" → cron: "57 8 <tomorrow_dom> <tomorrow_month> *", recurring: false
>
> ## Recurring jobs (recurring: true, the default)
>
> For "every N minutes" / "every hour" / "weekdays at 9am" requests:
>   "*/5 * * * *" (every 5 min), "0 * * * *" (hourly), "0 9 * * 1-5" (weekdays at 9am local)
>
> ## Avoid the :00 and :30 minute marks when the task allows it
>
> Every user who asks for "9am" gets `0 9`, and every user who asks for "hourly" gets `0 *` — which means requests from across the planet land on the API at the same instant. When the user's request is approximate, pick a minute that is NOT 0 or 30:
>   "every morning around 9" → "57 8 * * *" or "3 9 * * *" (not "0 9 * * *")
>   "hourly" → "7 * * * *" (not "0 * * * *")
>   "in an hour or so, remind me to..." → pick whatever minute you land on, don't round
>
> Only use minute 0 or 30 when the user names that exact time and clearly means it ("at 9:00 sharp", "at half past", coordinating with a meeting). When in doubt, nudge a few minutes early or late — the user will not notice, and the fleet will.
>
> ${CRON_DURABLE_FLAG?`## Durability
>
> By default (durable: false) the job lives only in this Claude session — nothing is written to disk, and the job is gone when Claude exits. Pass durable: true to write to .claude/scheduled_tasks.json so the job survives restarts. Only use durable: true when the user explicitly asks for the task to persist ("keep doing this every day", "set this up permanently"). Most "remind me in 5 minutes" / "check back in an hour" requests should stay session-only.`:`## Session-only
>
> Jobs live only in this Claude session — nothing is written to disk, and the job is gone when Claude exits.`}
>
> ## Runtime behavior
>
> Jobs only fire while the REPL is idle (not mid-query). ${CRON_DURABLE_FLAG?"Durable jobs persist to .claude/scheduled_tasks.json and survive session restarts — on next launch they resume automatically. One-shot durable tasks that were missed while the REPL was closed are surfaced for catch-up. Session-only jobs die with the process. ":""}The scheduler adds a small deterministic jitter on top of whatever you pick: recurring tasks fire up to 10% of their period late (max 15 min); one-shot tasks landing on :00 or :30 fire up to 90 s early. Picking an off-minute is still the bigger lever.
>
> Recurring tasks auto-expire after ${CANCEL_TIMEFRAME_DAYS} days — they fire one final time, then are deleted. This bounds session lifetime. Tell the user about the ${CANCEL_TIMEFRAME_DAYS}-day limit when scheduling recurring jobs.
>
> Returns a job ID you can pass to ${CRON_DELETE_TOOL_NAME}.

## 中文翻译

> **原文：**
> Schedule a prompt to be enqueued at a future time. Use for both recurring schedules and one-shot reminders.

**翻译：**
安排一个提示在未来某个时间点入队执行。可用于周期性计划任务和一次性提醒。

---

> **原文：**
> Uses standard 5-field cron in the user's local timezone: minute hour day-of-month month day-of-week. "0 9 * * *" means 9am local — no timezone conversion needed.

**翻译：**
使用标准的 5 字段 cron 表达式，基于用户的本地时区：分钟 小时 日 月 星期。"0 9 * * *" 表示本地时间上午 9 点——无需进行时区转换。

---

> **原文：**
> ## One-shot tasks (recurring: false)
>
> For "remind me at X" or "at <time>, do Y" requests — fire once then auto-delete.
> Pin minute/hour/day-of-month/month to specific values:
>   "remind me at 2:30pm today to check the deploy" → cron: "30 14 <today_dom> <today_month> *", recurring: false
>   "tomorrow morning, run the smoke test" → cron: "57 8 <tomorrow_dom> <tomorrow_month> *", recurring: false

**翻译：**
## 一次性任务（recurring: false）

用于"在 X 时间提醒我"或"在某个时间做 Y"的请求——触发一次后自动删除。
将分钟/小时/日/月固定为具体值：
  "今天下午 2:30 提醒我检查部署" → cron: "30 14 <today_dom> <today_month> *", recurring: false
  "明天早上运行冒烟测试" → cron: "57 8 <tomorrow_dom> <tomorrow_month> *", recurring: false

---

> **原文：**
> ## Recurring jobs (recurring: true, the default)
>
> For "every N minutes" / "every hour" / "weekdays at 9am" requests:
>   "*/5 * * * *" (every 5 min), "0 * * * *" (hourly), "0 9 * * 1-5" (weekdays at 9am local)

**翻译：**
## 周期性任务（recurring: true，默认值）

用于"每 N 分钟"/"每小时"/"工作日上午 9 点"的请求：
  "*/5 * * * *"（每 5 分钟），"0 * * * *"（每小时），"0 9 * * 1-5"（工作日本地时间上午 9 点）

---

> **原文：**
> ## Avoid the :00 and :30 minute marks when the task allows it
>
> Every user who asks for "9am" gets `0 9`, and every user who asks for "hourly" gets `0 *` — which means requests from across the planet land on the API at the same instant. When the user's request is approximate, pick a minute that is NOT 0 or 30:
>   "every morning around 9" → "57 8 * * *" or "3 9 * * *" (not "0 9 * * *")
>   "hourly" → "7 * * * *" (not "0 * * * *")
>   "in an hour or so, remind me to..." → pick whatever minute you land on, don't round
>
> Only use minute 0 or 30 when the user names that exact time and clearly means it ("at 9:00 sharp", "at half past", coordinating with a meeting). When in doubt, nudge a few minutes early or late — the user will not notice, and the fleet will.

**翻译：**
## 在任务允许时避免使用 :00 和 :30 分钟标记

每个要求"上午 9 点"的用户都会得到 `0 9`，每个要求"每小时"的用户都会得到 `0 *`——这意味着来自全球各地的请求会在同一瞬间到达 API。当用户的请求是近似的时候，选择一个不是 0 或 30 的分钟数：
  "每天早上 9 点左右" → "57 8 * * *" 或 "3 9 * * *"（而非 "0 9 * * *"）
  "每小时" → "7 * * * *"（而非 "0 * * * *"）
  "大约一小时后提醒我……" → 选择你当前所在的任意分钟数，不要取整

只有当用户明确指定了精确时间并且确实需要精确执行时（如"9:00 整"、"半点"、配合会议时间），才使用分钟 0 或 30。有疑问时，提前或推迟几分钟——用户不会察觉，但整个系统会受益。

---

> **原文：**
> ${CRON_DURABLE_FLAG?`## Durability
>
> By default (durable: false) the job lives only in this Claude session — nothing is written to disk, and the job is gone when Claude exits. Pass durable: true to write to .claude/scheduled_tasks.json so the job survives restarts. Only use durable: true when the user explicitly asks for the task to persist ("keep doing this every day", "set this up permanently"). Most "remind me in 5 minutes" / "check back in an hour" requests should stay session-only.`:`## Session-only
>
> Jobs live only in this Claude session — nothing is written to disk, and the job is gone when Claude exits.`}

**翻译：**
（当 CRON_DURABLE_FLAG 为真时）
## 持久性

默认情况下（durable: false），任务仅存在于当前 Claude 会话中——不会写入磁盘，Claude 退出后任务就消失了。传入 durable: true 可将任务写入 .claude/scheduled_tasks.json，使其在重启后仍然存在。仅在用户明确要求任务持久化时使用 durable: true（如"每天都这样做"、"永久设置"）。大多数"5 分钟后提醒我"/"一小时后回来检查"的请求应保持仅会话级别。

（当 CRON_DURABLE_FLAG 为假时）
## 仅会话

任务仅存在于当前 Claude 会话中——不会写入磁盘，Claude 退出后任务就消失了。

---

> **原文：**
> ## Runtime behavior
>
> Jobs only fire while the REPL is idle (not mid-query). ${CRON_DURABLE_FLAG?"Durable jobs persist to .claude/scheduled_tasks.json and survive session restarts — on next launch they resume automatically. One-shot durable tasks that were missed while the REPL was closed are surfaced for catch-up. Session-only jobs die with the process. ":""}The scheduler adds a small deterministic jitter on top of whatever you pick: recurring tasks fire up to 10% of their period late (max 15 min); one-shot tasks landing on :00 or :30 fire up to 90 s early. Picking an off-minute is still the bigger lever.

**翻译：**
## 运行时行为

任务仅在 REPL 空闲时触发（不在查询执行过程中）。（当 CRON_DURABLE_FLAG 为真时：持久任务会持久化到 .claude/scheduled_tasks.json 并在会话重启后继续——下次启动时会自动恢复。错过的一次性持久任务会在下次启动时补执行。仅会话任务随进程终止而消失。）调度器会在你选定的时间上添加少量确定性抖动：周期性任务最多延迟其周期的 10%（最长 15 分钟）；落在 :00 或 :30 的一次性任务最多提前 90 秒触发。选择非整点分钟仍然是更有效的调节手段。

---

> **原文：**
> Recurring tasks auto-expire after ${CANCEL_TIMEFRAME_DAYS} days — they fire one final time, then are deleted. This bounds session lifetime. Tell the user about the ${CANCEL_TIMEFRAME_DAYS}-day limit when scheduling recurring jobs.

**翻译：**
周期性任务在 ${CANCEL_TIMEFRAME_DAYS} 天后自动过期——它们会最后执行一次，然后被删除。这限制了会话的生命周期。在安排周期性任务时，需告知用户 ${CANCEL_TIMEFRAME_DAYS} 天的限制。

---

> **原文：**
> Returns a job ID you can pass to ${CRON_DELETE_TOOL_NAME}.

**翻译：**
返回一个任务 ID，可传递给 ${CRON_DELETE_TOOL_NAME} 使用。

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${CRON_DURABLE_FLAG}` | 布尔标志，控制是否显示持久化相关说明 |
| `${CANCEL_TIMEFRAME_DAYS}` | 周期性任务自动过期的天数 |
| `${CRON_DELETE_TOOL_NAME}` | 定时任务删除工具的名称 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 示例引导（Example-driven Guidance） | `"remind me at 2:30pm today to check the deploy" → cron: "30 14 <today_dom> <today_month> *"` | 通过自然语言到 cron 表达式的映射示例，让 LLM 准确学习如何将用户口语化的时间请求转换为正确的 cron 格式。 |
| 2 | 负面约束（Negative Constraint） | `Avoid the :00 and :30 minute marks when the task allows it` | 明确禁止使用整点和半点，并解释了原因（全球请求同时到达 API），这是一种系统级负载均衡策略，引导 LLM 主动分散请求时间。 |
| 3 | 条件逻辑注入（Conditional Logic Injection） | `${CRON_DURABLE_FLAG?...Durability...Session-only...}` | 通过条件模板根据功能可用性动态切换显示持久化或仅会话的说明，避免向 LLM 暴露不可用的功能选项。 |
| 4 | 范围限定（Scope Limitation） | `Only use durable: true when the user explicitly asks for the task to persist` | 明确限制持久化功能的使用条件，防止 LLM 过度使用磁盘写入，保护用户的文件系统。 |
| 5 | 安全防护指令（Safety Guard） | `Only use minute 0 or 30 when the user names that exact time and clearly means it` | 设置默认安全行为（避免整点），仅在用户明确意图时才允许例外，兼顾用户体验和系统健康。 |
| 6 | 优先级排序（Priority Ordering） | 一次性任务在前，周期性任务在后，然后是高级配置 | 按使用频率和复杂度递增排列各章节，帮助 LLM 优先匹配最常见的场景。 |
| 7 | 动态上下文注入（Dynamic Context Injection） | `${CANCEL_TIMEFRAME_DAYS}`, `${CRON_DELETE_TOOL_NAME}` | 通过变量注入实际的过期天数和删除工具名称，确保提示词与运行时环境保持一致。 |
