# sendmessagetool

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: SendMessageTool |
| 分类 | Tool Descriptions → Agent 工具 |
| 文件路径 | `system-prompts/tool-description-sendmessagetool.md` |
| CC 版本 | 2.1.83 |
| 模板变量 | 无 |

## 原文

> # SendMessage
>
> Send a message to another agent.
>
> ```json
> {"to": "researcher", "summary": "assign task 1", "message": "start on task #1"}
> ```
>
> | `to` | |
> |---|---|
> | `"researcher"` | Teammate by name |
> | `"*"` | Broadcast to all teammates — expensive (linear in team size), use only when everyone genuinely needs it |
>
> Your plain text output is NOT visible to other agents — to communicate, you MUST call this tool. Messages from teammates are delivered automatically; you don't check an inbox. Refer to teammates by name, never by UUID. When relaying, don't quote the original — it's already rendered to the user.
>
> ## Protocol responses (legacy)
>
> If you receive a JSON message with `type: "shutdown_request"` or `type: "plan_approval_request"`, respond with the matching `_response` type — echo the `request_id`, set `approve` true/false.
>
> Approving shutdown terminates your process. Rejecting plan sends the teammate back to revise. Don't originate `shutdown_request` unless asked. Don't send structured JSON status messages — use TaskUpdate.

## 中文翻译

> **原文：**
> Send a message to another agent.

**翻译：**
向另一个代理发送消息。

> **原文：**
> Your plain text output is NOT visible to other agents — to communicate, you MUST call this tool.

**翻译：**
你的纯文本输出对其他代理不可见——要通信，你必须调用此工具。消息会自动从队友处投递；你不需要检查收件箱。通过名称引用队友，不要用 UUID。转发时不要引用原文——它已经渲染给用户了。

> **原文：**
> Protocol responses (legacy): If you receive a JSON message with `type: "shutdown_request"` or `type: "plan_approval_request"`, respond with the matching `_response` type.

**翻译：**
协议响应（遗留）：如果收到带有 `type: "shutdown_request"` 或 `type: "plan_approval_request"` 的 JSON 消息，用匹配的 `_response` 类型回应——回显 `request_id`，设置 `approve` 为 true/false。批准关闭会终止你的进程。拒绝计划会让队友回去修改。除非被要求，不要发起 `shutdown_request`。不要发送结构化 JSON 状态消息——使用 TaskUpdate。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 不可见性强调 | `plain text output is NOT visible` | 大写 NOT 强调通信必须使用工具 |
| 2 | 广播成本 | `expensive (linear in team size)` | 用技术术语解释广播代价，抑制滥用 |
| 3 | 协议规范 | shutdown/approval 的 JSON 格式 | 提供精确的协议交互格式 |
