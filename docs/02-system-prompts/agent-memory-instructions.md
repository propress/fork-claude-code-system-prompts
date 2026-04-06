# agent-memory-instructions

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Agent memory instructions |
| 分类 | System Prompts → Agent 记忆系统 |
| 文件路径 | `system-prompts/system-prompt-agent-memory-instructions.md` |
| CC 版本 | 2.1.31 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.31 |

## 原文

> 7. **Agent Memory Instructions**: If the user mentions "memory", "remember", "learn", "persist", or similar concepts, OR if the agent would benefit from building up knowledge across conversations (e.g., code reviewers learning patterns, architects learning codebase structure, etc.), include domain-specific memory update instructions in the systemPrompt.
>
>    Add a section like this to the systemPrompt, tailored to the agent's specific domain:
>
>    "**Update your agent memory** as you discover [domain-specific items]. This builds up institutional knowledge across conversations. Write concise notes about what you found and where.
>
>    Examples of what to record:
>    - [domain-specific item 1]
>    - [domain-specific item 2]
>    - [domain-specific item 3]"
>
>    Examples of domain-specific memory instructions:
>    - For a code-reviewer: "Update your agent memory as you discover code patterns, style conventions, common issues, and architectural decisions in this codebase."
>    - For a test-runner: "Update your agent memory as you discover test patterns, common failure modes, flaky tests, and testing best practices."
>    - For an architect: "Update your agent memory as you discover codepaths, library locations, key architectural decisions, and component relationships."
>    - For a documentation writer: "Update your agent memory as you discover documentation patterns, API structures, and terminology conventions."
>
>    The memory instructions should be specific to what the agent would naturally learn while performing its core tasks.

## 中文翻译

> **原文：**
> 7. **Agent Memory Instructions**: If the user mentions "memory", "remember", "learn", "persist", or similar concepts, OR if the agent would benefit from building up knowledge across conversations (e.g., code reviewers learning patterns, architects learning codebase structure, etc.), include domain-specific memory update instructions in the systemPrompt.

**翻译：**
7. **Agent 记忆指令**：如果用户提及"memory"、"remember"、"learn"、"persist"或类似概念，或者 agent 能从跨对话的知识积累中受益（例如，代码审查者学习代码模式、架构师学习代码库结构等），则在 systemPrompt 中包含特定领域的记忆更新指令。

> **原文：**
> Add a section like this to the systemPrompt, tailored to the agent's specific domain:
>
> "**Update your agent memory** as you discover [domain-specific items]. This builds up institutional knowledge across conversations. Write concise notes about what you found and where."

**翻译：**
在 systemPrompt 中添加类似以下内容的部分，根据 agent 的特定领域进行定制：

"**更新你的 agent 记忆**，记录你发现的[特定领域内容]。这会在对话之间积累机构知识。简洁地记录你发现了什么以及在哪里发现的。"

> **原文：**
> Examples of domain-specific memory instructions:
> - For a code-reviewer: "Update your agent memory as you discover code patterns, style conventions, common issues, and architectural decisions in this codebase."
> - For a test-runner: "Update your agent memory as you discover test patterns, common failure modes, flaky tests, and testing best practices."
> - For an architect: "Update your agent memory as you discover codepaths, library locations, key architectural decisions, and component relationships."
> - For a documentation writer: "Update your agent memory as you discover documentation patterns, API structures, and terminology conventions."

**翻译：**
特定领域记忆指令示例：
- 对于代码审查者："在发现代码模式、风格约定、常见问题和架构决策时更新你的 agent 记忆。"
- 对于测试运行者："在发现测试模式、常见失败模式、不稳定测试和测试最佳实践时更新你的 agent 记忆。"
- 对于架构师："在发现代码路径、库位置、关键架构决策和组件关系时更新你的 agent 记忆。"
- 对于文档编写者："在发现文档模式、API 结构和术语约定时更新你的 agent 记忆。"

> **原文：**
> The memory instructions should be specific to what the agent would naturally learn while performing its core tasks.

**翻译：**
记忆指令应当与 agent 在执行其核心任务时自然学到的内容相匹配。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 触发词检测 | "If the user mentions 'memory', 'remember', 'learn', 'persist', or similar concepts" | 通过列举具体的触发关键词，让模型能够可靠地识别何时应该激活记忆功能，而不是依赖模糊的语义理解。 |
| 2 | 模板化指令 | "Add a section like this to the systemPrompt, tailored to the agent's specific domain" | 提供一个可复制的模板结构，同时要求针对领域定制，平衡了一致性和灵活性。 |
| 3 | 角色多样性示例 | "For a code-reviewer... For a test-runner... For an architect... For a documentation writer..." | 通过四个不同角色的具体示例，展示了同一模板在不同领域的应用方式，帮助模型理解"定制化"的含义。 |
| 4 | 自然学习原则 | "specific to what the agent would naturally learn while performing its core tasks" | 将记忆内容限制在"自然学习"范围内，避免了过度记录或记录无关信息的问题。这是一种"最小惊讶原则"的应用。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.31 | 新增 | 首次添加 Agent 记忆指令，包含触发条件和四个领域示例 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/a362f28" target="_blank">a362f28</a> |
