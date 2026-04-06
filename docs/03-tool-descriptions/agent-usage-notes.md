# agent-usage-notes

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Agent (usage notes) |
| 分类 | Tool Descriptions → Agent 工具 |
| 文件路径 | `system-prompts/tool-description-agent-usage-notes.md` |
| CC 版本 | 2.1.88 |
| 模板变量 | `${TOOL_BASE_DESCRIPTION}`, `${TOOL_PARAMETERS_DESCRIPTION}`, `${GET_TIER_FN}`, `${IS_TRUTHY_FN}`, `${PROCESS_OBJECT}`, `${IS_SUBAGENT_CONTEXT_FN}`, `${HAS_SUBAGENT_TYPES}`, `${SEND_MESSAGE_TOOL_NAME}`, `${TOOL_OBJECT}`, `${IS_TEAMMATE_CONTEXT_FN}`, `${ADDITIONAL_USAGE_NOTES}`, `${EXTRA_USAGE_NOTES}`, `${SUBAGENT_TYPE_DEFINITIONS}`, `${DEFAULT_AGENT_DESCRIPTION}` |

## 原文

> ${TOOL_BASE_DESCRIPTION}
> ${TOOL_PARAMETERS_DESCRIPTION}
>
> Usage notes:
> - Always include a short description (3-5 words) summarizing what the agent will do${GET_TIER_FN}
> - When the agent is done, it will return a single message back to you. The result returned by the agent is not visible to the user. To show the user the result, you should send a text message back to the user with a concise summary of the result.${!IS_TRUTHY_FN(PROCESS_OBJECT.env.CLAUDE_CODE_DISABLE_BACKGROUND_TASKS)&&!IS_SUBAGENT_CONTEXT_FN()&&!HAS_SUBAGENT_TYPES?`
> - You can optionally run agents in the background using the run_in_background parameter. When an agent runs in the background, you will be automatically notified when it completes — do NOT sleep, poll, or proactively check on its progress. Continue with other work or respond to the user instead.
> - **Foreground vs background**: Use foreground (default) when you need the agent's results before you can proceed — e.g., research agents whose findings inform your next steps. Use background when you have genuinely independent work to do in parallel.`:""}
> - To continue a previously spawned agent, use ${SEND_MESSAGE_TOOL_NAME} with the agent's ID or name as the `to` field. The agent resumes with its full context preserved. ${HAS_SUBAGENT_TYPES?"Each fresh Agent invocation with a subagent_type starts without context — provide a complete task description.":"Each Agent invocation starts fresh — provide a complete task description."}
> - The agent's outputs should generally be trusted
> - Clearly tell the agent whether you expect it to write code or just to do research (search, file reads, web fetches, etc.)${HAS_SUBAGENT_TYPES?"":", since it is not aware of the user's intent"}
> - If the agent description mentions that it should be used proactively, then you should try your best to use it without the user having to ask for it first. Use your judgement.
> - If the user specifies that they want you to run agents "in parallel", you MUST send a single message with multiple ${TOOL_OBJECT} tool use content blocks. For example, if you need to launch both a build-validator agent and a test-runner agent in parallel, send a single message with both tool calls.
> - You can optionally set `isolation: "worktree"` to run the agent in a temporary git worktree, giving it an isolated copy of the repository. The worktree is automatically cleaned up if the agent makes no changes; if changes are made, the worktree path and branch are returned in the result.${IS_SUBAGENT_CONTEXT_FN()?`
> - The run_in_background, name, team_name, and mode parameters are not available in this context. Only synchronous subagents are supported.`:IS_TEAMMATE_CONTEXT_FN()?`
> - The name, team_name, and mode parameters are not available in this context — teammates cannot spawn other teammates. Omit them to spawn a subagent.`:""}${ADDITIONAL_USAGE_NOTES}${EXTRA_USAGE_NOTES}
>
> ${HAS_SUBAGENT_TYPES?SUBAGENT_TYPE_DEFINITIONS:DEFAULT_AGENT_DESCRIPTION}

## 中文翻译

> **原文：**
> ${TOOL_BASE_DESCRIPTION}
> ${TOOL_PARAMETERS_DESCRIPTION}

**翻译：**
${TOOL_BASE_DESCRIPTION}
${TOOL_PARAMETERS_DESCRIPTION}

---

> **原文：**
> Usage notes:
> - Always include a short description (3-5 words) summarizing what the agent will do${GET_TIER_FN}
> - When the agent is done, it will return a single message back to you. The result returned by the agent is not visible to the user. To show the user the result, you should send a text message back to the user with a concise summary of the result.

**翻译：**
使用说明：
- 始终包含一个简短的描述（3-5 个词）来概括智能体将要执行的操作${GET_TIER_FN}
- 当智能体完成任务后，它会返回一条消息给你。智能体返回的结果对用户不可见。要向用户展示结果，你应该发送一条文本消息给用户，简要总结结果。

---

> **原文：**
> - You can optionally run agents in the background using the run_in_background parameter. When an agent runs in the background, you will be automatically notified when it completes — do NOT sleep, poll, or proactively check on its progress. Continue with other work or respond to the user instead.
> - **Foreground vs background**: Use foreground (default) when you need the agent's results before you can proceed — e.g., research agents whose findings inform your next steps. Use background when you have genuinely independent work to do in parallel.

**翻译：**
- 你可以选择使用 run_in_background 参数在后台运行智能体。当智能体在后台运行时，完成后你会自动收到通知——不要使用 sleep、轮询或主动检查其进度。请继续处理其他工作或回复用户。
- **前台与后台**：当你需要智能体的结果才能继续时，使用前台模式（默认）——例如，研究型智能体的发现会影响你的下一步操作。当你确实有可以并行处理的独立工作时，使用后台模式。

---

> **原文：**
> - To continue a previously spawned agent, use ${SEND_MESSAGE_TOOL_NAME} with the agent's ID or name as the `to` field. The agent resumes with its full context preserved. Each Agent invocation starts fresh — provide a complete task description.
> - The agent's outputs should generally be trusted

**翻译：**
- 要继续先前生成的智能体，使用 ${SEND_MESSAGE_TOOL_NAME}，将智能体的 ID 或名称作为 `to` 字段。智能体会恢复执行，其完整上下文得以保留。每次新的 Agent 调用都是全新开始——请提供完整的任务描述。
- 智能体的输出通常应被信任

---

> **原文：**
> - Clearly tell the agent whether you expect it to write code or just to do research (search, file reads, web fetches, etc.), since it is not aware of the user's intent
> - If the agent description mentions that it should be used proactively, then you should try your best to use it without the user having to ask for it first. Use your judgement.

**翻译：**
- 明确告诉智能体你期望它编写代码还是仅进行研究（搜索、文件读取、网页获取等），因为它不了解用户的意图
- 如果智能体描述中提到应主动使用，那么你应该尽量在用户提出要求之前就使用它。请运用你的判断力。

---

> **原文：**
> - If the user specifies that they want you to run agents "in parallel", you MUST send a single message with multiple ${TOOL_OBJECT} tool use content blocks. For example, if you need to launch both a build-validator agent and a test-runner agent in parallel, send a single message with both tool calls.
> - You can optionally set `isolation: "worktree"` to run the agent in a temporary git worktree, giving it an isolated copy of the repository. The worktree is automatically cleaned up if the agent makes no changes; if changes are made, the worktree path and branch are returned in the result.

**翻译：**
- 如果用户指定要"并行"运行智能体，你必须发送一条包含多个 ${TOOL_OBJECT} 工具使用内容块的消息。例如，如果你需要同时启动构建验证器智能体和测试运行器智能体，请在一条消息中发送两个工具调用。
- 你可以选择设置 `isolation: "worktree"` 来在临时 git worktree 中运行智能体，为其提供仓库的隔离副本。如果智能体没有做出更改，worktree 会自动清理；如果有更改，worktree 路径和分支会在结果中返回。

---

> **原文：**
> ${HAS_SUBAGENT_TYPES?SUBAGENT_TYPE_DEFINITIONS:DEFAULT_AGENT_DESCRIPTION}

**翻译：**
${HAS_SUBAGENT_TYPES?SUBAGENT_TYPE_DEFINITIONS:DEFAULT_AGENT_DESCRIPTION}

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${TOOL_BASE_DESCRIPTION}` | 工具的基础描述文本 |
| `${TOOL_PARAMETERS_DESCRIPTION}` | 工具参数的描述文本 |
| `${GET_TIER_FN}` | 获取用户订阅层级的函数 |
| `${IS_TRUTHY_FN}` | 判断值是否为真的辅助函数 |
| `${PROCESS_OBJECT}` | Node.js 进程对象，用于访问环境变量等 |
| `${IS_SUBAGENT_CONTEXT_FN}` | 判断当前是否在子智能体上下文中的函数 |
| `${HAS_SUBAGENT_TYPES}` | 是否有可用的子智能体类型定义 |
| `${SEND_MESSAGE_TOOL_NAME}` | 发送消息工具的名称 |
| `${TOOL_OBJECT}` | 工具对象引用 |
| `${IS_TEAMMATE_CONTEXT_FN}` | 判断当前是否在团队成员上下文中的函数 |
| `${ADDITIONAL_USAGE_NOTES}` | 附加的使用说明 |
| `${EXTRA_USAGE_NOTES}` | 额外的使用提示 |
| `${SUBAGENT_TYPE_DEFINITIONS}` | 子智能体类型的定义列表 |
| `${DEFAULT_AGENT_DESCRIPTION}` | 默认智能体描述文本 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 结构化列表（Structured Enumeration） | `Usage notes: - Always include... - When the agent is done...` | 通过编号和分点列出所有使用说明，确保每条规则清晰可辨，避免遗漏。 |
| 2 | 条件逻辑注入（Conditional Logic Injection） | `${!IS_TRUTHY_FN(...)&&!IS_SUBAGENT_CONTEXT_FN()...?...:""}` | 根据运行时上下文（是否禁用后台任务、是否在子智能体中）动态插入或隐藏后台运行相关的说明，实现精准的上下文感知。 |
| 3 | 负面约束（Negative Constraint） | `do NOT sleep, poll, or proactively check on its progress` | 通过明确禁止特定行为（轮询、sleep），防止智能体产生不必要的资源消耗。 |
| 4 | 优先级排序（Priority Ordering） | `Use foreground (default) when you need... Use background when you have genuinely independent work` | 明确区分前台和后台使用场景的优先级，帮助模型做出正确的调度决策。 |
| 5 | 示例引导（Example-driven Guidance） | `if you need to launch both a build-validator agent and a test-runner agent in parallel` | 通过具体示例说明并行启动多个智能体的场景，使抽象概念更易理解。 |
| 6 | 动态上下文注入（Dynamic Context Injection） | `${IS_SUBAGENT_CONTEXT_FN()?...:IS_TEAMMATE_CONTEXT_FN()?...:""}` | 根据调用者身份（子智能体、团队成员或主智能体）动态调整可用参数的说明，避免在受限上下文中提供不可用的功能。 |
| 7 | 范围限定（Scope Limitation） | `Only synchronous subagents are supported` | 在子智能体上下文中明确限定功能范围，防止尝试使用不支持的特性。 |
