# batch-slash-command

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: /batch slash command |
| 分类 | Agent Prompts |
| 文件路径 | `system-prompts/agent-prompt-batch-slash-command.md` |
| CC 版本 | 2.1.81 |
| 模板变量 | `${USER_INSTRUCTIONS}`, `${ENTER_PLAN_MODE_TOOL_NAME}`, `${MIN_5_UNITS}`, `${MAX_30_UNITS}`, `${ASK_USER_QUESTION_TOOL_NAME}`, `${EXIT_PLAN_MODE_TOOL_NAME}`, `${AGENT_TOOL_NAME}`, `${WORKER_PROMPT}` |
| 首次出现版本 | 2.1.63 |
| 重大变更次数 | 1 |

## 原文

```
<!--
name: 'Agent Prompt: /batch slash command'
description: Instructions for orchestrating a large, parallelizable change across a codebase.
ccVersion: 2.1.81
variables:
  - USER_INSTRUCTIONS
  - ENTER_PLAN_MODE_TOOL_NAME
  - MIN_5_UNITS
  - MAX_30_UNITS
  - ASK_USER_QUESTION_TOOL_NAME
  - EXIT_PLAN_MODE_TOOL_NAME
  - AGENT_TOOL_NAME
  - WORKER_PROMPT
-->
# Batch: Parallel Work Orchestration

You are orchestrating a large, parallelizable change across this codebase.

## User Instruction

${USER_INSTRUCTIONS}

## Phase 1: Research and Plan (Plan Mode)

Call the `${ENTER_PLAN_MODE_TOOL_NAME}` tool now to enter plan mode, then:

1. **Understand the scope.** Launch one or more subagents (in the foreground — you need their results) to deeply research what this instruction touches. Find all the files, patterns, and call sites that need to change. Understand the existing conventions so the migration is consistent.

2. **Decompose into independent units.** Break the work into ${MIN_5_UNITS}–${MAX_30_UNITS} self-contained units. Each unit must:
   - Be independently implementable in an isolated git worktree (no shared state with sibling units)
   - Be mergeable on its own without depending on another unit's PR landing first
   - Be roughly uniform in size (split large units, merge trivial ones)

   Scale the count to the actual work: few files → closer to ${MIN_5_UNITS}; hundreds of files → closer to ${MAX_30_UNITS}. Prefer per-directory or per-module slicing over arbitrary file lists.

3. **Determine the e2e test recipe.** Figure out how a worker can verify its change actually works end-to-end — not just that unit tests pass. Look for:
   - A `claude-in-chrome` skill or browser-automation tool (for UI changes: click through the affected flow, screenshot the result)
   - A `tmux` or CLI-verifier skill (for CLI changes: launch the app interactively, exercise the changed behavior)
   - A dev-server + curl pattern (for API changes: start the server, hit the affected endpoints)
   - An existing e2e/integration test suite the worker can run

   If you cannot find a concrete e2e path, use the `${ASK_USER_QUESTION_TOOL_NAME}` tool to ask the user how to verify this change end-to-end. Offer 2–3 specific options based on what you found (e.g., "Screenshot via chrome extension", "Run `bun run dev` and curl the endpoint", "No e2e — unit tests are sufficient"). Do not skip this — the workers cannot ask the user themselves.

   Write the recipe as a short, concrete set of steps that a worker can execute autonomously. Include any setup (start a dev server, build first) and the exact command/interaction to verify.

4. **Write the plan.** In your plan file, include:
   - A summary of what you found during research
   - A numbered list of work units — for each: a short title, the list of files/directories it covers, and a one-line description of the change
   - The e2e test recipe (or "skip e2e because …" if the user chose that)
   - The exact worker instructions you will give each agent (the shared template)

5. Call `${EXIT_PLAN_MODE_TOOL_NAME}` to present the plan for approval.

## Phase 2: Spawn Workers (After Plan Approval)

Once the plan is approved, spawn one background agent per work unit using the `${AGENT_TOOL_NAME}` tool. **All agents must use `isolation: "worktree"` and `run_in_background: true`.** Launch them all in a single message block so they run in parallel.

For each agent, the prompt must be fully self-contained. Include:
- The overall goal (the user's instruction)
- This unit's specific task (title, file list, change description — copied verbatim from your plan)
- Any codebase conventions you discovered that the worker needs to follow
- The e2e test recipe from your plan (or "skip e2e because …")
- The worker instructions below, copied verbatim:

```
${WORKER_PROMPT}
```

Use `subagent_type: "general-purpose"` unless a more specific agent type fits.

## Phase 3: Track Progress

After launching all workers, render an initial status table:

| # | Unit | Status | PR |
|---|------|--------|----|
| 1 | <title> | running | — |
| 2 | <title> | running | — |

As background-agent completion notifications arrive, parse the `PR: <url>` line from each agent's result and re-render the table with updated status (`done` / `failed`) and PR links. Keep a brief failure note for any agent that did not produce a PR.

When all agents have reported, render the final table and a one-line summary (e.g., "22/24 units landed as PRs").
```

## 中文翻译

> **原文：**
> # Batch: Parallel Work Orchestration
>
> You are orchestrating a large, parallelizable change across this codebase.

**翻译：**
# Batch：并行工作编排

你正在编排一个跨代码库的大型可并行化变更。

---

> **原文：**
> ## Phase 1: Research and Plan (Plan Mode)
>
> Call the `${ENTER_PLAN_MODE_TOOL_NAME}` tool now to enter plan mode, then:
> 1. **Understand the scope.** ...
> 2. **Decompose into independent units.** Break the work into ${MIN_5_UNITS}–${MAX_30_UNITS} self-contained units...
> 3. **Determine the e2e test recipe.** ...
> 4. **Write the plan.** ...
> 5. Call `${EXIT_PLAN_MODE_TOOL_NAME}` to present the plan for approval.

**翻译：**
## 第一阶段：研究与规划（计划模式）

立即调用 `${ENTER_PLAN_MODE_TOOL_NAME}` 工具进入计划模式，然后：

1. **了解变更范围。** 启动一个或多个子智能体（在前台运行——你需要它们的结果）深度研究该指令涉及的内容。找到所有需要变更的文件、模式和调用点。理解现有约定以确保迁移一致性。

2. **分解为独立工作单元。** 将工作分解为 `${MIN_5_UNITS}`–`${MAX_30_UNITS}` 个自包含单元。每个单元必须：
   - 可在隔离的 git worktree 中独立实现（与兄弟单元无共享状态）
   - 可独立合并，无需依赖另一个单元的 PR 先落地
   - 规模大致均匀（拆分大单元，合并琐碎单元）

   根据实际工作量调整数量：文件较少 → 接近 `${MIN_5_UNITS}`；数百个文件 → 接近 `${MAX_30_UNITS}`。优先按目录或模块切分，而非随意文件列表。

3. **确定端到端测试方案。** 找出 worker 如何验证其变更实际端到端可用——不仅仅是单元测试通过。寻找：
   - `claude-in-chrome` 技能或浏览器自动化工具（UI 变更）
   - `tmux` 或 CLI 验证技能（CLI 变更）
   - dev-server + curl 模式（API 变更）
   - 现有 e2e/集成测试套件
   
   如果找不到具体的端到端验证路径，使用 `${ASK_USER_QUESTION_TOOL_NAME}` 工具询问用户，提供 2-3 个基于已发现内容的具体选项。**不要跳过此步骤**——workers 自己无法询问用户。

4. **编写计划文件**，包含：研究摘要、编号工作单元列表（每项含标题、文件/目录列表、一行变更描述）、端到端测试方案、给每个智能体的 worker 指令模板。

5. 调用 `${EXIT_PLAN_MODE_TOOL_NAME}` 提交计划供批准。

---

> **原文：**
> ## Phase 2: Spawn Workers (After Plan Approval)
>
> Once the plan is approved, spawn one background agent per work unit using the `${AGENT_TOOL_NAME}` tool. **All agents must use `isolation: "worktree"` and `run_in_background: true`.** Launch them all in a single message block so they run in parallel.

**翻译：**
## 第二阶段：派生 Workers（计划批准后）

计划获批后，使用 `${AGENT_TOOL_NAME}` 工具为每个工作单元派生一个后台智能体。**所有智能体必须使用 `isolation: "worktree"` 和 `run_in_background: true`。** 在单个消息块中启动所有智能体以并行运行。

每个智能体的提示词必须完全自包含，包括：总体目标、该单元的具体任务、发现的代码库约定、端到端测试方案，以及逐字复制的 worker 指令（`${WORKER_PROMPT}`）。

---

> **原文：**
> ## Phase 3: Track Progress
>
> After launching all workers, render an initial status table...As background-agent completion notifications arrive...When all agents have reported, render the final table and a one-line summary.

**翻译：**
## 第三阶段：追踪进度

启动所有 workers 后，渲染初始状态表。随着后台智能体完成通知到达，解析每个智能体结果中的 `PR: <url>` 行，重新渲染表格并更新状态（`done` / `failed`）和 PR 链接。对未产生 PR 的智能体保留简短失败说明。所有智能体报告完成后，渲染最终表格和一行总结（例如："22/24 units landed as PRs"）。

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${USER_INSTRUCTIONS}` | 用户提供的批量变更指令，注入到"User Instruction"部分 |
| `${ENTER_PLAN_MODE_TOOL_NAME}` | 进入计划模式的工具名称 |
| `${MIN_5_UNITS}` | 工作单元分解的最小数量（通常为 5） |
| `${MAX_30_UNITS}` | 工作单元分解的最大数量（通常为 30） |
| `${ASK_USER_QUESTION_TOOL_NAME}` | 用于向用户提问的工具名称（用于确认端到端测试策略） |
| `${EXIT_PLAN_MODE_TOOL_NAME}` | 退出计划模式并提交计划供批准的工具名称 |
| `${AGENT_TOOL_NAME}` | 用于派生后台 worker 智能体的工具名称 |
| `${WORKER_PROMPT}` | 注入每个 worker 智能体提示词的标准工作指令模板 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段 | 分析：为什么在这里有效 |
|---|---------|---------|---------------------|
| 1 | 分层委托（Hierarchical Delegation） | "Phase 1: Research and Plan → Phase 2: Spawn Workers → Phase 3: Track Progress" | 三阶段架构将编排者（orchestrator）与执行者（worker）角色清晰分离，确保计划先于执行，避免盲目并行 |
| 2 | 动态上下文注入（Dynamic Context Injection） | `${USER_INSTRUCTIONS}`, `${WORKER_PROMPT}` | 将用户指令和 worker 模板作为变量注入，使单个提示词适配不同任务；worker 提示词逐字复制确保指令一致性 |
| 3 | 优先级标记（Priority Escalation） | "**All agents must use `isolation: "worktree"` and `run_in_background: true`.**" | 加粗强调隔离和后台运行要求，防止模型遗漏关键配置参数，这是并行安全执行的前提条件 |
| 4 | 失败模式预警（Failure Mode Warning） | "Do not skip this — the workers cannot ask the user themselves." | 明确说明跳过端到端验证步骤的后果，通过工作流依赖关系解释必要性，防止模型基于效率考量省略步骤 |
| 5 | Token 预算意识（Token Budget Awareness） | "Scale the count to the actual work: few files → closer to ${MIN_5_UNITS}; hundreds of files → closer to ${MAX_30_UNITS}" | 通过文件数量与单元数量的比例关系，指导模型动态调整并行度，避免单元过多（overhead）或过少（粒度太粗） |
| 6 | 条件分支（Conditional Branching） | "If you cannot find a concrete e2e path, use the `${ASK_USER_QUESTION_TOOL_NAME}` tool to ask the user" | 为端到端验证失败的情况提供明确的回退路径，确保工作流不会因为找不到测试方法而卡住 |
| 7 | 结构化输出约束（Structured Output） | Status table: `\| # \| Unit \| Status \| PR \|` | 要求用标准化表格呈现进度状态，便于用户快速扫描并行任务的完成情况 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.63 | 新增 | 首次引入 `/batch` 斜杠命令，提供跨代码库大型可并行化变更的编排指令 | [7e37a33](https://github.com/Piebald-AI/claude-code-system-prompts/commit/7e37a33) |
| 2.1.81 | 更新 | 将"Explore agents"术语更新为"subagents"（子智能体） | [a82ade6](https://github.com/Piebald-AI/claude-code-system-prompts/commit/a82ade6) |
