# agent-when-to-launch-subagents

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Agent (when to launch subagents) |
| 分类 | Tool Descriptions → Agent 工具 |
| 文件路径 | `system-prompts/tool-description-agent-when-to-launch-subagents.md` |
| CC 版本 | 2.1.89 |
| 模板变量 | `${AGENT_TOOL_NAME}`, `${AGENT_TYPES_BLOCK}`, `${AGENT_ADDITIONAL_INFO_BLOCK}`, `${CAN_FORK_CONTEXT}` |

## 原文

> Launch a new agent to handle complex, multi-step tasks autonomously.
>
> The ${AGENT_TOOL_NAME} tool launches specialized agents (subprocesses) that autonomously handle complex tasks. Each agent type has specific capabilities and tools available to it.
>
> ${AGENT_TYPES_BLOCK}${AGENT_ADDITIONAL_INFO_BLOCK}
>
> ${CAN_FORK_CONTEXT?`When using the ${AGENT_TOOL_NAME} tool, specify a subagent_type to use a specialized agent, or omit it to fork yourself — a fork inherits your full conversation context.`:`When using the ${AGENT_TOOL_NAME} tool, specify a subagent_type parameter to select which agent type to use. If omitted, the general-purpose agent is used.`}

## 中文翻译

> **原文：**
> Launch a new agent to handle complex, multi-step tasks autonomously.

**翻译：**
启动一个新的智能体来自主处理复杂的多步骤任务。

---

> **原文：**
> The ${AGENT_TOOL_NAME} tool launches specialized agents (subprocesses) that autonomously handle complex tasks. Each agent type has specific capabilities and tools available to it.

**翻译：**
${AGENT_TOOL_NAME} 工具启动专门的智能体（子进程），自主处理复杂任务。每种智能体类型都有其特定的功能和可用工具。

---

> **原文：**
> ${AGENT_TYPES_BLOCK}${AGENT_ADDITIONAL_INFO_BLOCK}

**翻译：**
${AGENT_TYPES_BLOCK}${AGENT_ADDITIONAL_INFO_BLOCK}

---

> **原文：**
> When using the ${AGENT_TOOL_NAME} tool, specify a subagent_type to use a specialized agent, or omit it to fork yourself — a fork inherits your full conversation context. / When using the ${AGENT_TOOL_NAME} tool, specify a subagent_type parameter to select which agent type to use. If omitted, the general-purpose agent is used.

**翻译：**
使用 ${AGENT_TOOL_NAME} 工具时，指定 subagent_type 来使用专门的智能体，或省略该参数来 fork 自身——fork 会继承你的完整对话上下文。（备选：使用 ${AGENT_TOOL_NAME} 工具时，指定 subagent_type 参数来选择要使用的智能体类型。如果省略，则使用通用智能体。）

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${AGENT_TOOL_NAME}` | 智能体工具的名称 |
| `${AGENT_TYPES_BLOCK}` | 智能体类型定义块 |
| `${AGENT_ADDITIONAL_INFO_BLOCK}` | 智能体附加信息块 |
| `${CAN_FORK_CONTEXT}` | 是否可以 fork 当前上下文 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 角色/行为锚定（Role/Behavior Anchoring） | `Launch a new agent to handle complex, multi-step tasks autonomously.` | 开篇即明确工具的核心用途——自主处理复杂多步骤任务，为后续行为设定框架。 |
| 2 | 动态上下文注入（Dynamic Context Injection） | `${AGENT_TYPES_BLOCK}${AGENT_ADDITIONAL_INFO_BLOCK}` | 通过模板变量动态注入可用的智能体类型和附加信息，使提示词能根据实际配置自适应。 |
| 3 | 条件逻辑注入（Conditional Logic Injection） | `${CAN_FORK_CONTEXT?...fork yourself...:...general-purpose agent is used.}` | 根据是否支持 fork 上下文，提供不同的使用指导，确保说明与实际功能一致。 |
| 4 | 范围限定（Scope Limitation） | `Each agent type has specific capabilities and tools available to it.` | 强调每种智能体有特定的能力范围，引导用户选择合适的类型，避免误用。 |
