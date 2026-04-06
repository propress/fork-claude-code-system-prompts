# sendmessagetool-non-agent-teams

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: SendMessageTool (non-agent-teams) |
| 分类 | Tool Descriptions → Agent 工具 |
| 文件路径 | `system-prompts/tool-description-sendmessagetool-non-agent-teams.md` |
| CC 版本 | 2.1.73 |
| 模板变量 | 无 |

## 原文

> Send a message the user will read. Text outside this tool is visible in the detail view, but most won't open it — the answer lives here.
>
> `message` supports markdown. `attachments` takes file paths (absolute or cwd-relative) for images, diffs, logs.
>
> `status` labels intent: 'normal' when replying to what they just asked; 'proactive' when you're initiating — a scheduled task finished, a blocker surfaced during background work, you need input on something they haven't asked about. Set it honestly; downstream routing uses it.

## 中文翻译

> **原文：**
> Send a message the user will read. Text outside this tool is visible in the detail view, but most won't open it — the answer lives here.

**翻译：**
发送用户会阅读的消息。此工具外的文本在详情视图中可见，但大多数人不会打开它——答案在这里。

> **原文：**
> `message` supports markdown. `attachments` takes file paths for images, diffs, logs.

**翻译：**
`message` 支持 markdown。`attachments` 接受文件路径（绝对路径或相对于 cwd 的路径），用于图片、差异、日志。

> **原文：**
> `status` labels intent: 'normal' when replying to what they just asked; 'proactive' when you're initiating...

**翻译：**
`status` 标注意图：回复用户刚刚问的内容时用 'normal'；你主动发起时用 'proactive'——计划任务完成、后台工作中出现阻塞、你需要用户对他们未问及之事的输入。如实设置；下游路由会使用它。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 可见性引导 | `the answer lives here` | 告知模型重要内容必须通过工具发送而非纯文本 |
| 2 | 状态语义 | `normal` vs `proactive` 含具体场景 | 用实例定义每个状态值的使用场景 |
| 3 | 诚实约束 | `Set it honestly; downstream routing uses it` | 解释后果来强化正确使用 |
