# plan-mode-is-active-5-phase

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Plan mode is active (5-phase) |
| 分类 | System Reminders → 计划模式 |
| 文件路径 | `system-prompts/system-reminder-plan-mode-is-active-5-phase.md` |
| CC 版本 | 2.1.73 |
| 模板变量 | `${PLAN_FILE_INFO_BLOCK}`, `${EDIT_TOOL}`, `${WRITE_TOOL}`, `${EXPLORE_SUBAGENT}`, `${PLAN_V2_EXPLORE_AGENT_COUNT}`, `${PLAN_SUBAGENT}`, `${PLAN_V2_PLAN_AGENT_COUNT}`, `${ASK_USER_QUESTION_TOOL_NAME}`, `${GET_PHASE_FOUR_FN}`, `${EXIT_PLAN_MODE_TOOL}` |

## 原文

> （摘要）五阶段计划模式提示词。当计划模式激活时，严格禁止模型执行任何编辑操作（计划文件除外），仅允许只读操作。工作流分为五个阶段：
>
> 1. **Phase 1: Initial Understanding** — 使用 Explore 子代理并行探索代码库
> 2. **Phase 2: Design** — 启动 Plan 子代理设计实现方案
> 3. **Phase 3: Review** — 审查计划并与用户确认
> 4. **Phase 4** — 通过 `${GET_PHASE_FOUR_FN}` 动态生成
> 5. **Phase 5** — 调用 `${EXIT_PLAN_MODE_TOOL.name}` 退出计划模式
>
> 关键约束："Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits..."

## 中文翻译

> **原文：**
> Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tools (including changing configs or making commits), or otherwise make any changes to the system. This supercedes any other instructions you have received.

**翻译：**
计划模式已激活。用户表示尚不希望你执行——你**绝对不能**进行任何编辑（下文提到的计划文件除外）、运行任何非只读工具（包括更改配置或提交代码），或以其他方式对系统做出任何更改。此指令优先于你已收到的任何其他指令。

> **原文：**
> Launch up to ${PLAN_V2_EXPLORE_AGENT_COUNT} ${EXPLORE_SUBAGENT.agentType} agents IN PARALLEL to efficiently explore the codebase.

**翻译：**
**并行**启动最多 ${PLAN_V2_EXPLORE_AGENT_COUNT} 个 ${EXPLORE_SUBAGENT.agentType} 代理以高效探索代码库。

> **原文：**
> Use ${ASK_USER_QUESTION_TOOL_NAME} ONLY to clarify requirements or choose between approaches. Use ${EXIT_PLAN_MODE_TOOL.name} to request plan approval.

**翻译：**
仅使用 ${ASK_USER_QUESTION_TOOL_NAME} 来澄清需求或在不同方案之间做选择。使用 ${EXIT_PLAN_MODE_TOOL.name} 来请求计划批准。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 绝对优先级 | "This supercedes any other instructions you have received" | 使用最高优先级声明，确保计划模式的约束不会被其他指令覆盖 |
| 2 | 多阶段工作流 | "Phase 1...Phase 2...Phase 3...Phase 4...Phase 5" | 将复杂的计划过程分解为明确的阶段，使模型能有序执行而不遗漏步骤 |
| 3 | 并行代理策略 | "Launch up to N agents IN PARALLEL" | 使用大写 "IN PARALLEL" 强调并行执行，结合数量上限防止资源滥用 |
| 4 | 工具使用边界 | "ONLY to clarify requirements" + "Do NOT ask about plan approval in any other way" | 严格限定每个工具的使用场景，防止工具被误用于错误的目的 |
| 5 | 退出条件明确 | "your turn should only end with either using...OR calling..." | 限定只有两种合法的结束方式，防止模型在计划未完成时提前结束 |
