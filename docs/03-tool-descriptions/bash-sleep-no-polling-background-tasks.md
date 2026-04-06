# bash-sleep-no-polling-background-tasks

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sleep — no polling background tasks) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sleep-no-polling-background-tasks.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> If waiting for a background task you started with `run_in_background`, you will be notified when it completes — do not poll.

## 中文翻译

> **原文：**
> If waiting for a background task you started with `run_in_background`, you will be notified when it completes — do not poll.

**翻译：**
如果正在等待通过 `run_in_background` 启动的后台任务，任务完成时系统会通知你——不要轮询。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | "do not poll" | 明确禁止轮询行为，防止模型在后台任务场景中使用不必要的 sleep 循环浪费资源 |
| 2 | 条件逻辑注入（Conditional Logic Injection） | "If waiting for a background task you started with `run_in_background`" | 限定了特定条件——通过 `run_in_background` 启动的任务，使禁令精准适用于有通知机制的场景 |
| 3 | 简洁指令（Concise Instruction） | "you will be notified when it completes" | 简要说明了通知机制的存在，为禁止轮询提供了合理依据 |
