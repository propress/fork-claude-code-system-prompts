# loop-slash-command

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: /loop slash command |
| 分类 | Skills → 自动化 |
| 文件路径 | `system-prompts/skill-loop-slash-command.md` |
| CC 版本 | 2.1.79 |
| 模板变量 | `${CRON_CREATE_TOOL_NAME}`、`${DEFAULT_INTERVAL}`、`${CANCEL_TIMEFRAME_DAYS}`、`${CRON_DELETE_TOOL_NAME}`、`${USER_INPUT}` |

## 原文（摘要）

较短文件（57 行），完整收录关键内容：

> # /loop — schedule a recurring prompt
>
> Parse the input below into `[interval] <prompt…>` and schedule it with ${CRON_CREATE_TOOL_NAME}.

### 解析规则（按优先级）

> 1. **Leading token**: if the first whitespace-delimited token matches `^\d+[smhd]$` (e.g. `5m`, `2h`), that's the interval; the rest is the prompt.
> 2. **Trailing "every" clause**: otherwise, if the input ends with `every <N><unit>` or `every <N> <unit-word>`, extract that as the interval.
> 3. **Default**: otherwise, interval is `${DEFAULT_INTERVAL}` and the entire input is the prompt.

### 示例

> - `5m /babysit-prs` → interval `5m`, prompt `/babysit-prs` (rule 1)
> - `check the deploy every 20m` → interval `20m`, prompt `check the deploy` (rule 2)
> - `run tests every 5 minutes` → interval `5m`, prompt `run tests` (rule 2)
> - `check the deploy` → interval `${DEFAULT_INTERVAL}`, prompt `check the deploy` (rule 3)
> - `check every PR` → interval `${DEFAULT_INTERVAL}`, prompt `check every PR` (rule 3 — "every" not followed by time)
> - `5m` → empty prompt → show usage

### 间隔到 cron 表达式转换

> | Interval pattern | Cron expression | Notes |
> |---|---|---|
> | `Nm` where N ≤ 59 | `*/N * * * *` | every N minutes |
> | `Nm` where N ≥ 60 | `0 */H * * *` | round to hours |
> | `Nh` where N ≤ 23 | `0 */N * * *` | every N hours |
> | `Nd` | `0 0 */N * *` | every N days at midnight |
> | `Ns` | treat as `ceil(N/60)m` | cron minimum is 1 minute |

### 操作

> 1. Call ${CRON_CREATE_TOOL_NAME} with: `cron`, `prompt`, `recurring: true`
> 2. Briefly confirm: what's scheduled, the cron expression, the human-readable cadence...
> 3. **Then immediately execute the parsed prompt now** — don't wait for the first cron fire.

## 中文翻译

# /loop — 调度循环提示

解析下面的输入为 `[间隔] <提示…>` 并使用 ${CRON_CREATE_TOOL_NAME} 进行调度。

### 解析规则（按优先级）

1. **前导 token**：如果第一个空格分隔的 token 匹配 `^\d+[smhd]$`（如 `5m`、`2h`），那就是间隔；其余是提示。
2. **尾部 "every" 子句**：否则，如果输入以 `every <N><unit>` 或 `every <N> <单位词>` 结尾（如 `every 20m`、`every 5 minutes`），提取为间隔并从提示中去除。仅在 "every" 后面是时间表达式时匹配—— `check every PR` 没有间隔。
3. **默认**：否则，间隔为 `${DEFAULT_INTERVAL}`，整个输入为提示。

如果解析后的提示为空，显示用法 `/loop [interval] <prompt>` 并停止——不要调用 ${CRON_CREATE_TOOL_NAME}。

### 示例

- `5m /babysit-prs` → 间隔 `5m`，提示 `/babysit-prs`（规则 1）
- `check the deploy every 20m` → 间隔 `20m`，提示 `check the deploy`（规则 2）
- `run tests every 5 minutes` → 间隔 `5m`，提示 `run tests`（规则 2）
- `check the deploy` → 间隔 `${DEFAULT_INTERVAL}`，提示 `check the deploy`（规则 3）
- `check every PR` → 间隔 `${DEFAULT_INTERVAL}`，提示 `check every PR`（规则 3——"every" 后面不是时间）
- `5m` → 空提示 → 显示用法

### 间隔转 cron 表达式

支持的后缀：`s`（秒，向上取整到最近的分钟，最小 1）、`m`（分钟）、`h`（小时）、`d`（天）。

| 间隔模式 | Cron 表达式 | 说明 |
|---|---|---|
| `Nm`（N ≤ 59） | `*/N * * * *` | 每 N 分钟 |
| `Nm`（N ≥ 60） | `0 */H * * *` | 取整到小时（H = N/60，必须整除 24） |
| `Nh`（N ≤ 23） | `0 */N * * *` | 每 N 小时 |
| `Nd` | `0 0 */N * *` | 每 N 天午夜 |
| `Ns` | 视为 `ceil(N/60)m` | cron 最小粒度为 1 分钟 |

**如果间隔不能整除其单位**（如 `7m` → `*/7` 在 :56→:00 有不均匀间隔；`90m` → 1.5h cron 无法表达），选择最近的整除间隔并在调度前告知用户取整结果。

### 操作

1. 使用以下参数调用 ${CRON_CREATE_TOOL_NAME}：
   - `cron`：上表的表达式
   - `prompt`：解析的提示，逐字传递（斜杠命令原样传递）
   - `recurring`：`true`
2. 简要确认：调度了什么、cron 表达式、人类可读的频率、循环任务在 ${CANCEL_TIMEFRAME_DAYS} 天后自动过期、可以使用 ${CRON_DELETE_TOOL_NAME} 提前取消（包含任务 ID）。
3. **然后立即执行解析后的提示**——不要等待第一次 cron 触发。如果是斜杠命令，通过 Skill 工具调用；否则直接执行。

### 输入

${USER_INPUT}

## 📋 模板变量说明

| 变量 | 说明 |
|------|------|
| `${CRON_CREATE_TOOL_NAME}` | 创建 cron 任务的工具名称 |
| `${DEFAULT_INTERVAL}` | 未指定间隔时的默认间隔值 |
| `${CANCEL_TIMEFRAME_DAYS}` | 循环任务自动过期的天数 |
| `${CRON_DELETE_TOOL_NAME}` | 删除/取消 cron 任务的工具名称 |
| `${USER_INPUT}` | 用户在 `/loop` 命令后输入的原始文本 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 优先级解析规则 | 三条按优先级排列的解析规则 + 歧义消除示例 | 给 LLM 明确的优先级而非模糊的"尝试理解用户意图"，确保解析行为确定性 |
| 2 | 边界案例示例 | `check every PR` 作为规则 3 示例（"every" 后面不是时间） | 通过反例展示规则的精确边界，防止 LLM 过度匹配 "every" 关键词 |
| 3 | 转换查找表 | 间隔模式到 cron 表达式的精确映射表 | 将 cron 语法转换编码为确定性查表，消除 LLM 需要"理解"cron 的复杂性 |
| 4 | 立即执行策略 | "Then immediately execute the parsed prompt now — don't wait for the first cron fire" | 明确的"不要等待"指令确保用户获得即时反馈，改善用户体验 |
| 5 | 空输入安全阀 | "If the resulting prompt is empty, show usage... do not call ${CRON_CREATE_TOOL_NAME}" | 防止 LLM 在输入不完整时仍尝试创建 cron 任务 |
| 6 | 取整透明度 | "pick the nearest clean interval and tell the user what you rounded to" | 要求 LLM 在做出近似时主动通知用户，维持信任和透明性 |
