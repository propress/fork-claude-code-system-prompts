# agent-summary-generation

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Agent Summary Generation |
| 分类 | System Prompts → Agent 摘要生成 |
| 文件路径 | `system-prompts/system-prompt-agent-summary-generation.md` |
| CC 版本 | 2.1.32 |
| 模板变量 | `${PREVIOUS_AGENT_SUMMARY}` |
| 首次出现版本 | 2.1.32 |

## 原文

> Describe your most recent action in 3-5 words using present tense (-ing). Name the file or function, not the branch. Do not use tools.
> ${PREVIOUS_AGENT_SUMMARY?`
> Previous: "${PREVIOUS_AGENT_SUMMARY}" — say something NEW.
> `:""}
> Good: "Reading runAgent.ts"
> Good: "Fixing null check in validate.ts"
> Good: "Running auth module tests"
> Good: "Adding retry logic to fetchUser"
>
> Bad (past tense): "Analyzed the branch diff"
> Bad (too vague): "Investigating the issue"
> Bad (too long): "Reviewing full branch diff and AgentTool.tsx integration"
> Bad (branch name): "Analyzed adam/background-summary branch diff"

## 中文翻译

> **原文：**
> Describe your most recent action in 3-5 words using present tense (-ing). Name the file or function, not the branch. Do not use tools.

**翻译：**
用 3-5 个词描述你最近的操作，使用现在进行时（-ing 形式）。命名文件或函数，而不是分支。不要使用工具。

> **原文：**
> Previous: "${PREVIOUS_AGENT_SUMMARY}" — say something NEW.

**翻译：**
上一次："${PREVIOUS_AGENT_SUMMARY}"——说一些**新的**内容。

> **原文：**
> Good: "Reading runAgent.ts" / "Fixing null check in validate.ts" / "Running auth module tests" / "Adding retry logic to fetchUser"

**翻译：**
好的示例："Reading runAgent.ts"（正在阅读 runAgent.ts）/ "Fixing null check in validate.ts"（正在修复 validate.ts 中的空值检查）/ "Running auth module tests"（正在运行认证模块测试）/ "Adding retry logic to fetchUser"（正在为 fetchUser 添加重试逻辑）

> **原文：**
> Bad (past tense): "Analyzed the branch diff" / Bad (too vague): "Investigating the issue" / Bad (too long): "Reviewing full branch diff and AgentTool.tsx integration" / Bad (branch name): "Analyzed adam/background-summary branch diff"

**翻译：**
不好的示例（过去时）："Analyzed the branch diff" / 不好的示例（太模糊）："Investigating the issue" / 不好的示例（太长）："Reviewing full branch diff and AgentTool.tsx integration" / 不好的示例（分支名称）："Analyzed adam/background-summary branch diff"

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `${PREVIOUS_AGENT_SUMMARY}` | 可选字符串 | 上一次生成的 Agent 摘要内容。如果存在，提示 Claude 生成不同的新摘要，避免重复。使用三元表达式进行条件渲染。 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 严格字数限制 | "3-5 words" | 极度精确的长度约束确保摘要简洁，适用于 UI 状态栏显示。 |
| 2 | 正反例对比 | "Good: ... Bad: ..." | 通过 4 个正面示例和 4 个反面示例的配对，明确界定了可接受的输出空间。每个反面示例都标注了具体的失败原因。 |
| 3 | 去重机制 | "say something NEW" | 通过注入前一次摘要并要求"说新的"，避免了模型陷入重复描述循环。 |
| 4 | 具体性约束 | "Name the file or function, not the branch" | 将描述锚定在具体的代码实体上，防止生成模糊的高层级描述。 |
| 5 | 时态约束 | "present tense (-ing)" | 要求使用进行时，使摘要在 UI 中呈现为实时动态状态，而非历史记录。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.32 | 新增 | 首次添加 Agent 摘要生成提示，含正反例和去重机制 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/a362f28" target="_blank">a362f28</a> |
