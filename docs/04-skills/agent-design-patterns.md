# agent-design-patterns

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: Agent Design Patterns |
| 分类 | Skills → API 开发 |
| 文件路径 | `system-prompts/skill-agent-design-patterns.md` |
| CC 版本 | 2.1.91 |
| 模板变量 | 无 |

## 原文（摘要）

> This file covers decision heuristics for building agents on the Claude API: which primitives to reach for, how to design your tool surface, and how to manage context and cost over long runs.

### 关键章节

- **Model Parameters**：讨论 `thinking: {type: "adaptive"}` 和 `output_config: {effort: ...}` 参数的使用场景
- **Designing Your Tool Surface**：Bash 工具 vs 专用工具的选择，何时将操作提升为专用工具
- **Anthropic-Provided Tools**：列出 Bash、Text editor、Computer use、Code execution、Web search/fetch、Memory 六种工具
- **Composing Tool Calls: Programmatic Tool Calling (PTC)**：组合工具调用以减少往返延迟和 token 消耗
- **Scaling the Tool and Instruction Set**：Tool search 和 Skills 模式
- **Long-Running Agents: Managing Context**：Context editing、Compaction、Memory 三种上下文管理模式
- **Caching for Agents**：Agent 特有的缓存策略和约束规避方案

> "A **bash tool** gives Claude broad programmatic leverage — it can perform almost any action. But it gives the harness only an opaque command string... Promoting an action to a **dedicated tool** gives the harness an action-specific hook with typed arguments it can intercept, gate, render, or audit."

> "Start with bash for breadth. Promote to dedicated tools when you need to gate, render, audit, or parallelize the action."

> "Context editing and compaction operate within a session — editing prunes stale turns, compaction summarizes when you're near the limit. Memory is for cross-session persistence. Many long-running agents use all three."

## 中文翻译

### 模型参数

| 参数 | 何时使用 | 预期效果 |
| --- | --- | --- |
| **自适应思考** (`thinking: {type: "adaptive"}`) | 当你希望 Claude 自行控制思考的时机和深度时 | Claude 根据每个请求确定思考深度，并自动在工具调用之间穿插思考。无需调整 token 预算。 |
| **努力程度** (`output_config: {effort: ...}`) | 当需要调整彻底性与 token 效率之间的平衡时 | 较低的努力程度意味着更少且更集中的工具调用、更少的前言、更简洁的确认。`medium` 通常是较好的平衡点。当正确性比成本更重要时使用 `max`。 |

### 设计工具表面

Claude 不了解你的应用安全边界、审批策略或用户体验。Claude 发出工具调用，你的框架处理它们。这些工具调用的形态决定了框架能做什么。

**Bash 工具** 给予 Claude 广泛的编程能力——它几乎可以执行任何操作。但它只给框架一个不透明的命令字符串，对每个操作都是同样的形态。将操作提升为**专用工具**则给予框架一个特定操作的钩子，带有可拦截、审批、渲染或审计的类型化参数。

**何时将操作提升为专用工具：**

- **安全边界**：需要审批控制的操作是天然候选。可逆性是有用的判断标准：难以逆转的操作（外部 API 调用、发送消息、删除数据）可以通过用户确认来控制。`send_email` 工具易于控制；`bash -c "curl -X POST ..."` 则不然。
- **过期检查**：专用 `edit` 工具可以在文件自 Claude 上次读取后发生变化时拒绝写入。Bash 无法强制执行这个不变量。
- **渲染**：某些操作受益于自定义 UI。
- **调度**：只读工具如 `glob` 和 `grep` 可标记为并行安全。当同样的操作通过 bash 执行时，框架无法区分并行安全的 `grep` 和并行不安全的 `git push`，因此必须串行化。

**经验法则：** 从 bash 开始以获得广度。当需要审批、渲染、审计或并行化操作时，提升为专用工具。

### Anthropic 提供的工具

| 工具 | 侧 | 何时使用 | 预期效果 |
| --- | --- | --- | --- |
| **Bash** | 客户端 | Claude 需要执行 shell 命令 | Claude 发出命令，你的框架执行。提供参考实现。 |
| **Text editor** | 客户端 | Claude 需要读取或编辑文件 | Claude 通过你的实现查看、创建和编辑文件。 |
| **Computer use** | 客户端或服务端 | Claude 需要与 GUI、Web 应用或可视界面交互 | Claude 截屏并发出鼠标/键盘命令。 |
| **Code execution** | 服务端 | Claude 需要在你不想管理的沙箱中运行代码 | Anthropic 托管的容器，内置文件和 bash 子工具。 |
| **Web search / fetch** | 服务端 | Claude 需要训练截止日期之后的信息 | Claude 发出查询或 URL，Anthropic 执行并返回带引用的结果。 |
| **Memory** | 客户端 | Claude 需要跨会话保存上下文 | Claude 读写 `/memories` 目录。你实现存储后端。 |

### 组合工具调用：编程式工具调用 (PTC)

在标准工具使用中，每次工具调用都是一次往返。**编程式工具调用 (PTC)** 让 Claude 将这些调用组合成脚本。脚本在代码执行容器中运行。当脚本调用工具时，容器暂停，调用被执行，结果返回给正在运行的代码——而不是 Claude 的上下文。只有脚本的最终输出返回给 Claude。Token 成本随最终输出而非中间结果增长。

### 长时间运行的 Agent：管理上下文

| 模式 | 何时使用 | 预期效果 |
| --- | --- | --- |
| **上下文编辑** | 上下文在多轮对话后变得陈旧 | 根据可配置的阈值清除工具结果和思考块。 |
| **压缩** | 对话可能达到或超过上下文窗口限制 | 早期上下文在服务端被总结为压缩块。 |
| **记忆** | 状态必须跨会话持久化 | Claude 读写记忆目录中的文件。 |

**选择策略：** 上下文编辑和压缩在会话内运作——编辑修剪陈旧的轮次，压缩在接近限制时进行总结。记忆用于跨会话持久化。许多长时间运行的 Agent 三种都使用。

### Agent 缓存策略

| 约束 | Agent 特定的规避方案 |
| --- | --- |
| 会话中编辑系统提示会使缓存失效 | 在 `messages` 数组中追加 `<system-reminder>` 块。缓存前缀保持完整。 |
| 会话中切换模型会使缓存失效 | 为子任务生成使用较便宜模型的**子 Agent**；主循环保持一个模型。 |
| 会话中添加/移除工具会使缓存失效 | 使用 **tool search** 进行动态发现——它追加工具 schema 而非替换，保留现有前缀。 |

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 决策表格化 | 多处使用 `When to use it / What to expect` 表格结构 | 表格格式让 LLM 快速匹配用户需求到正确的工具/模式，减少推理步骤 |
| 2 | 经验法则总结 | "Start with bash for breadth. Promote to dedicated tools when you need to gate, render, audit, or parallelize" | 提供简洁的默认决策路径，避免 LLM 在多选项中犹豫不决 |
| 3 | 对比框架 | Bash 工具 vs 专用工具的 "opaque command string" vs "action-specific hook with typed arguments" | 通过明确的对比让 LLM 理解两种选择的本质差异，而非只列功能 |
| 4 | 约束-方案配对 | Caching 章节用 "Constraint → Agent-specific workaround" 结构 | 先陈述限制再给出解决方案，让 LLM 理解为什么需要这个方案而非盲目执行 |
| 5 | 分层策略 | Context editing / Compaction / Memory 三层模式及其选择指南 | 明确三者的适用范围（会话内 vs 跨会话），避免 LLM 混用不同层次的解决方案 |
| 6 | 外部参考指引 | "Read `prompt-caching.md` first" 和 "See `SKILL.md` §..." | 避免在单一提示词中重复所有信息，通过精确引用保持上下文精简 |
