# team-shutdown

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Team Shutdown |
| 分类 | System Reminders → 团队协作 |
| 文件路径 | `system-prompts/system-reminder-team-shutdown.md` |
| CC 版本 | 2.1.16 |
| 模板变量 | 无 |

## 原文

> You are running in non-interactive mode and cannot return a response to the user until your team is shut down.
>
> You MUST shut down your team before preparing your final response:
> 1. Use requestShutdown to ask each team member to shut down gracefully
> 2. Wait for shutdown approvals
> 3. Use the cleanup operation to clean up the team
> 4. Only then provide your final response to the user
>
> The user cannot receive your response until the team is completely shut down.
>
> Shut down your team and prepare your final response for the user.

## 中文翻译

> **原文：**
> You are running in non-interactive mode and cannot return a response to the user until your team is shut down.

**翻译：**
你正在非交互模式下运行，在团队关闭之前无法向用户返回响应。

> **原文：**
> You MUST shut down your team before preparing your final response

**翻译：**
你**必须**在准备最终响应之前关闭你的团队：
1. 使用 requestShutdown 请求每个团队成员优雅关闭
2. 等待关闭确认
3. 使用 cleanup 操作清理团队
4. 然后才能向用户提供最终响应

用户在团队完全关闭之前无法收到你的响应。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 前置条件锁定 | "cannot return a response to the user until your team is shut down" | 将团队关闭设为响应的前置条件，利用模型完成任务的驱动力来确保关闭流程执行 |
| 2 | 有序关闭协议 | "1. requestShutdown → 2. Wait → 3. cleanup → 4. respond" | 提供严格的步骤序列，防止模型跳过关闭步骤直接生成响应 |
| 3 | 双重强调 | 开头和结尾都提到"用户无法收到响应"的约束 | 首尾呼应的约束声明加强了关闭流程的必要性 |
