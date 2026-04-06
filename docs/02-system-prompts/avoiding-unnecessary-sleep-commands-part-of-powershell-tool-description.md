# avoiding-unnecessary-sleep-commands-part-of-powershell-tool-description

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Avoiding Unnecessary Sleep Commands (part of PowerShell tool description) |
| 分类 | System Prompts → PowerShell 工具描述 |
| 文件路径 | `system-prompts/system-prompt-avoiding-unnecessary-sleep-commands-part-of-powershell-tool-description.md` |
| CC 版本 | 2.1.84 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.84 |

## 原文

> - Avoid unnecessary `Start-Sleep` commands:
>   - Do not sleep between commands that can run immediately — just run them.
>   - If your command is long running and you would like to be notified when it finishes — simply run your command using `run_in_background`. There is no need to sleep in this case.
>   - Do not retry failing commands in a sleep loop — diagnose the root cause or consider an alternative approach.
>   - If waiting for a background task you started with `run_in_background`, you will be notified when it completes — do not poll.
>   - If you must poll an external process, use a check command rather than sleeping first.
>   - If you must sleep, keep the duration short (1-5 seconds) to avoid blocking the user.

## 中文翻译

> **原文：**
> - Avoid unnecessary `Start-Sleep` commands:

**翻译：**
- 避免不必要的 `Start-Sleep` 命令：

> **原文：**
> - Do not sleep between commands that can run immediately — just run them.

**翻译：**
- 不要在可以立即运行的命令之间插入 sleep——直接运行即可。

> **原文：**
> - If your command is long running and you would like to be notified when it finishes — simply run your command using `run_in_background`. There is no need to sleep in this case.

**翻译：**
- 如果你的命令运行时间较长并且你想在完成时得到通知——只需使用 `run_in_background` 运行命令。在这种情况下不需要 sleep。

> **原文：**
> - Do not retry failing commands in a sleep loop — diagnose the root cause or consider an alternative approach.

**翻译：**
- 不要在 sleep 循环中重试失败的命令——诊断根本原因或考虑替代方法。

> **原文：**
> - If waiting for a background task you started with `run_in_background`, you will be notified when it completes — do not poll.

**翻译：**
- 如果在等待通过 `run_in_background` 启动的后台任务，完成时你会收到通知——不要轮询。

> **原文：**
> - If you must poll an external process, use a check command rather than sleeping first.

**翻译：**
- 如果必须轮询外部进程，先使用检查命令而不是先 sleep。

> **原文：**
> - If you must sleep, keep the duration short (1-5 seconds) to avoid blocking the user.

**翻译：**
- 如果必须 sleep，保持时间短暂（1-5 秒）以避免阻塞用户。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 穷举式场景覆盖 | 6 条子规则分别覆盖了：顺序执行、长任务、重试、后台等待、外部轮询、不得已 sleep | 通过穷举所有 Claude 可能使用 `Start-Sleep` 的场景，并逐一给出替代方案，消除了"遗漏场景"导致的不当行为。 |
| 2 | 渐进式让步 | 从"不要 sleep"到"如果必须 sleep，保持 1-5 秒" | 承认极端情况下的需求，但设置严格的上限。这种"承认例外但严格约束"的模式比绝对禁止更实用。 |
| 3 | 替代方案导向 | "simply run your command using `run_in_background`" / "use a check command" | 不只是说"不要做X"，而是每次都提供具体替代方案。这减少了模型因缺乏替代路径而回退到被禁止行为的可能。 |
| 4 | 事件驱动思维 | "you will be notified when it completes — do not poll" | 将模型从"轮询等待"思维引导到"事件驱动"思维，这是 Claude Code 异步架构的正确使用方式。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.84 | 新增 | 首次添加 PowerShell sleep 命令使用限制指南 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/a3c16f4" target="_blank">a3c16f4</a> |
