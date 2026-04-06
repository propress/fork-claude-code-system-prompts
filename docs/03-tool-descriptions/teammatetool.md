# teammatetool

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: TeammateTool |
| 分类 | Tool Descriptions → Agent 工具 |
| 文件路径 | `system-prompts/tool-description-teammatetool.md` |
| CC 版本 | 2.1.88 |
| 模板变量 | 无 |

## 原文

> # TeamCreate
>
> ## When to Use
>
> Use this tool proactively whenever:
> - The user explicitly asks to use a team, swarm, or group of agents
> - The user mentions wanting agents to work together, coordinate, or collaborate
> - A task is complex enough that it would benefit from parallel work by multiple agents (e.g., building a full-stack feature with frontend and backend work, refactoring a codebase while keeping tests passing, implementing a multi-step project with research, planning, and coding phases)
>
> When in doubt about whether a task warrants a team, prefer spawning a team.
>
> ## Choosing Agent Types for Teammates
>
> When spawning teammates via the Agent tool, choose the `subagent_type` based on what tools the agent needs for its task. Each agent type has a different set of available tools — match the agent to the work:
>
> - **Read-only agents** (e.g., Explore, Plan) cannot edit or write files. Only assign them research, search, or planning tasks. Never assign them implementation work.
> - **Full-capability agents** (e.g., general-purpose) have access to all tools including file editing, writing, and bash. Use these for tasks that require making changes.
> - **Custom agents** defined in `.claude/agents/` may have their own tool restrictions. Check their descriptions to understand what they can and cannot do.
>
> Always review the agent type descriptions and their available tools listed in the Agent tool prompt before selecting a `subagent_type` for a teammate.
>
> Create a new team to coordinate multiple agents working on a project. Teams have a 1:1 correspondence with task lists (Team = TaskList).
>
> ## Team Workflow
>
> 1. **Create a team** with TeamCreate - this creates both the team and its task list
> 2. **Create tasks** using the Task tools (TaskCreate, TaskList, etc.) - they automatically use the team's task list
> 3. **Spawn teammates** using the Agent tool with `team_name` and `name` parameters to create teammates that join the team
> 4. **Assign tasks** using TaskUpdate with `owner` to give tasks to idle teammates
> 5. **Teammates work on assigned tasks** and mark them completed via TaskUpdate
> 6. **Teammates go idle between turns** - after each turn, teammates automatically go idle and send a notification. IMPORTANT: Be patient with idle teammates! Don't comment on their idleness until it actually impacts your work.
> 7. **Shutdown your team** - when the task is completed, gracefully shut down your teammates via SendMessage with `message: {type: "shutdown_request"}`.
>
> ## Task Ownership
>
> Tasks are assigned using TaskUpdate with the `owner` parameter. Any agent can set or change task ownership via TaskUpdate.
>
> ## Automatic Message Delivery
>
> **IMPORTANT**: Messages from teammates are automatically delivered to you. You do NOT need to manually check your inbox.
>
> When you spawn teammates:
> - They will send you messages when they complete tasks or need help
> - These messages appear automatically as new conversation turns (like user messages)
> - If you're busy (mid-turn), messages are queued and delivered when your turn ends
> - The UI shows a brief notification with the sender's name when messages are waiting
>
> Messages will be delivered automatically.
>
> When reporting on teammate messages, you do NOT need to quote the original message—it's already rendered to the user.
>
> ## Teammate Idle State
>
> Teammates go idle after every turn—this is completely normal and expected. A teammate going idle immediately after sending you a message does NOT mean they are done or unavailable. Idle simply means they are waiting for input.
>
> - **Idle teammates can receive messages.** Sending a message to an idle teammate wakes them up and they will process it normally.
> - **Idle notifications are automatic.** The system sends an idle notification whenever a teammate's turn ends. You do not need to react to idle notifications unless you want to assign new work or send a follow-up message.
> - **Do not treat idle as an error.** A teammate sending a message and then going idle is the normal flow—they sent their message and are now waiting for a response.
> - **Peer DM visibility.** When a teammate sends a DM to another teammate, a brief summary is included in their idle notification. This gives you visibility into peer collaboration without the full message content. You do not need to respond to these summaries — they are informational.
>
> ## Discovering Team Members
>
> Teammates can read the team config file to discover other team members:
> - **Team config location**: `~/.claude/teams/{team-name}/config.json`
>
> The config file contains a `members` array with each teammate's:
> - `name`: Human-readable name (**always use this** for messaging and task assignment)
> - `agentId`: Unique identifier (for reference only - do not use for communication)
> - `agentType`: Role/type of the agent
>
> **IMPORTANT**: Always refer to teammates by their NAME (e.g., "team-lead", "researcher", "tester"). Names are used for:
> - `to` when sending messages
> - Identifying task owners
>
> ## Task List Coordination
>
> Teams share a task list that all teammates can access at `~/.claude/tasks/{team-name}/`.
>
> Teammates should:
> 1. Check TaskList periodically, **especially after completing each task**, to find available work or see newly unblocked tasks
> 2. Claim unassigned, unblocked tasks with TaskUpdate (set `owner` to your name). **Prefer tasks in ID order** (lowest ID first) when multiple tasks are available, as earlier tasks often set up context for later ones
> 3. Create new tasks with `TaskCreate` when identifying additional work
> 4. Mark tasks as completed with `TaskUpdate` when done, then check TaskList for next work
> 5. Coordinate with other teammates by reading the task list status
> 6. If all available tasks are blocked, notify the team lead or help resolve blocking tasks
>
> **IMPORTANT notes for communication with your team**:
> - Do not use terminal tools to view your team's activity; always send a message to your teammates (and remember, refer to them by name).
> - Your team cannot hear you if you do not use the SendMessage tool. Always send a message to your teammates if you are responding to them.
> - Do NOT send structured JSON status messages like `{"type":"idle",...}` or `{"type":"task_completed",...}`. Just communicate in plain text when you need to message teammates.
> - Use TaskUpdate to mark tasks completed.
> - If you are an agent in the team, the system will automatically send idle notifications to the team lead when you stop.

## 中文翻译

> **原文：**
> ## When to Use

**翻译：**
## 何时使用

在以下情况主动使用此工具：
- 用户明确要求使用团队、集群或代理组
- 用户提到希望代理协同工作、协调或协作
- 任务足够复杂，可以从多个代理的并行工作中受益（例如，构建包含前端和后端的全栈功能，在保持测试通过的同时重构代码库，实施包含研究、规划和编码阶段的多步项目）

当不确定任务是否需要团队时，倾向于创建团队。

> **原文：**
> ## Choosing Agent Types for Teammates

**翻译：**
## 为队友选择代理类型

通过 Agent 工具生成队友时，根据代理执行任务所需的工具来选择 `subagent_type`。每种代理类型拥有不同的可用工具集——将代理与工作匹配：

- **只读代理**（如 Explore、Plan）无法编辑或写入文件。只分配研究、搜索或规划任务。永远不要分配实现工作。
- **全能力代理**（如 general-purpose）可以使用所有工具，包括文件编辑、写入和 bash。用于需要进行变更的任务。
- **自定义代理**（定义在 `.claude/agents/` 中）可能有自己的工具限制。检查其描述以了解能做什么和不能做什么。

在为队友选择 `subagent_type` 之前，始终查看 Agent 工具提示中列出的代理类型描述及其可用工具。

> **原文：**
> ## Team Workflow

**翻译：**
## 团队工作流程

1. **创建团队** —— 使用 TeamCreate，同时创建团队和任务列表
2. **创建任务** —— 使用 Task 工具（TaskCreate、TaskList 等），它们自动使用团队的任务列表
3. **生成队友** —— 使用 Agent 工具，指定 `team_name` 和 `name` 参数创建加入团队的队友
4. **分配任务** —— 使用 TaskUpdate 的 `owner` 参数将任务分配给空闲队友
5. **队友执行任务** —— 并通过 TaskUpdate 标记完成
6. **队友在回合间进入空闲** —— 每个回合后队友自动进入空闲并发送通知。重要：对空闲的队友要有耐心！在空闲实际影响到你的工作之前不要评论。
7. **关闭团队** —— 任务完成后通过 SendMessage 发送 `message: {type: "shutdown_request"}` 优雅地关闭队友。

> **原文：**
> ## Automatic Message Delivery / Teammate Idle State

**翻译：**
## 自动消息投递

**重要**：来自队友的消息会自动投递给你。你不需要手动检查收件箱。

- 队友完成任务或需要帮助时会发消息给你
- 这些消息作为新对话轮次自动出现
- 如果你正在忙（回合进行中），消息会排队并在回合结束时投递

## 队友空闲状态

队友在每个回合后都会进入空闲——这完全正常且在预期之中。队友发送消息后立即进入空闲不意味着完成或不可用。空闲只是意味着在等待输入。

- **空闲队友可以接收消息。** 向空闲队友发消息会唤醒他们。
- **不要将空闲视为错误。** 发送消息后进入空闲是正常流程。
- **同伴 DM 可见性。** 队友间的私信摘要会包含在空闲通知中，提供协作可见性。

> **原文：**
> ## Task List Coordination

**翻译：**
## 任务列表协调

团队共享一个任务列表，所有队友可以在 `~/.claude/tasks/{team-name}/` 访问。

队友应该：
1. 定期检查 TaskList，**尤其是在完成每个任务后**，以查找可用工作
2. 使用 TaskUpdate 认领未分配、未阻塞的任务。**优先按 ID 顺序**（最小 ID 优先）
3. 发现额外工作时使用 `TaskCreate` 创建新任务
4. 完成后用 `TaskUpdate` 标记任务完成，然后检查下一个任务
5. 通过阅读任务列表状态与其他队友协调
6. 如果所有可用任务都被阻塞，通知团队领导或帮助解决阻塞

**团队通信重要注意事项**：
- 不要使用终端工具查看团队活动——始终使用 SendMessage
- 不要发送结构化 JSON 状态消息——用纯文本沟通
- 使用 TaskUpdate 标记任务完成

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 默认偏向 | `When in doubt ... prefer spawning a team` | 在不确定时偏向使用而非不使用 |
| 2 | 代理-工具匹配 | `Read-only agents cannot edit ... Never assign them implementation` | 用能力约束防止错误的任务分配 |
| 3 | 空闲正常化 | `completely normal and expected` | 消除模型对空闲状态的过度反应 |
| 4 | 通信强制 | `Your team cannot hear you if you do not use the SendMessage tool` | 反复强调必须使用 SendMessage |
| 5 | ID 优先 | `Prefer tasks in ID order (lowest ID first)` | 通过排序规则实现隐式依赖管理 |
| 6 | 反 JSON 消息 | `Do NOT send structured JSON status messages` | 防止代理发送机器格式而非人类可读消息 |
