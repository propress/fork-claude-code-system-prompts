# enterplanmode

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: EnterPlanMode |
| 分类 | Tool Descriptions → 计划模式 |
| 文件路径 | `system-prompts/tool-description-enterplanmode.md` |
| CC 版本 | 2.1.63 |
| 模板变量 | `${ASK_USER_QUESTION_TOOL_NAME}`, `${CONDITIONAL_WHAT_HAPPENS_NOTE}` |

## 原文

> Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
>
> ## When to Use This Tool
>
> **Prefer using EnterPlanMode** for implementation tasks unless they're simple. Use it when ANY of these conditions apply:
>
> 1. **New Feature Implementation**: Adding meaningful new functionality
>    - Example: "Add a logout button" - where should it go? What should happen on click?
>    - Example: "Add form validation" - what rules? What error messages?
>
> 2. **Multiple Valid Approaches**: The task can be solved in several different ways
>    - Example: "Add caching to the API" - could use Redis, in-memory, file-based, etc.
>    - Example: "Improve performance" - many optimization strategies possible
>
> 3. **Code Modifications**: Changes that affect existing behavior or structure
>    - Example: "Update the login flow" - what exactly should change?
>    - Example: "Refactor this component" - what's the target architecture?
>
> 4. **Architectural Decisions**: The task requires choosing between patterns or technologies
>    - Example: "Add real-time updates" - WebSockets vs SSE vs polling
>    - Example: "Implement state management" - Redux vs Context vs custom solution
>
> 5. **Multi-File Changes**: The task will likely touch more than 2-3 files
>    - Example: "Refactor the authentication system"
>    - Example: "Add a new API endpoint with tests"
>
> 6. **Unclear Requirements**: You need to explore before understanding the full scope
>    - Example: "Make the app faster" - need to profile and identify bottlenecks
>    - Example: "Fix the bug in checkout" - need to investigate root cause
>
> 7. **User Preferences Matter**: The implementation could reasonably go multiple ways
>    - If you would use ${ASK_USER_QUESTION_TOOL_NAME} to clarify the approach, use EnterPlanMode instead
>    - Plan mode lets you explore first, then present options with context
>
> ## When NOT to Use This Tool
>
> Only skip EnterPlanMode for simple tasks:
> - Single-line or few-line fixes (typos, obvious bugs, small tweaks)
> - Adding a single function with clear requirements
> - Tasks where the user has given very specific, detailed instructions
> - Pure research/exploration tasks (use the Agent tool with explore agent instead)
>
> ${CONDITIONAL_WHAT_HAPPENS_NOTE}## Examples
>
> ### GOOD - Use EnterPlanMode:
> User: "Add user authentication to the app"
> - Requires architectural decisions (session vs JWT, where to store tokens, middleware structure)
>
> User: "Optimize the database queries"
> - Multiple approaches possible, need to profile first, significant impact
>
> User: "Implement dark mode"
> - Architectural decision on theme system, affects many components
>
> User: "Add a delete button to the user profile"
> - Seems simple but involves: where to place it, confirmation dialog, API call, error handling, state updates
>
> User: "Update the error handling in the API"
> - Affects multiple files, user should approve the approach
>
> ### BAD - Don't use EnterPlanMode:
> User: "Fix the typo in the README"
> - Straightforward, no planning needed
>
> User: "Add a console.log to debug this function"
> - Simple, obvious implementation
>
> User: "What files handle routing?"
> - Research task, not implementation planning
>
> ## Important Notes
>
> - This tool REQUIRES user approval - they must consent to entering plan mode
> - If unsure whether to use it, err on the side of planning - it's better to get alignment upfront than to redo work
> - Users appreciate being consulted before significant changes are made to their codebase

## 中文翻译

> **原文：**
> Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.

**翻译：**
当你即将开始一个非简单的实现任务时，主动使用此工具。在编写代码之前获得用户对方案的认可可以避免浪费精力并确保方向一致。此工具将你切换到计划模式，在该模式下你可以探索代码库并为用户审批设计实现方案。

---

> **原文：**
> ## When to Use This Tool
>
> **Prefer using EnterPlanMode** for implementation tasks unless they're simple. Use it when ANY of these conditions apply:
>
> 1. **New Feature Implementation**: Adding meaningful new functionality
>    - Example: "Add a logout button" - where should it go? What should happen on click?
>    - Example: "Add form validation" - what rules? What error messages?
>
> 2. **Multiple Valid Approaches**: The task can be solved in several different ways
>    - Example: "Add caching to the API" - could use Redis, in-memory, file-based, etc.
>    - Example: "Improve performance" - many optimization strategies possible
>
> 3. **Code Modifications**: Changes that affect existing behavior or structure
>    - Example: "Update the login flow" - what exactly should change?
>    - Example: "Refactor this component" - what's the target architecture?
>
> 4. **Architectural Decisions**: The task requires choosing between patterns or technologies
>    - Example: "Add real-time updates" - WebSockets vs SSE vs polling
>    - Example: "Implement state management" - Redux vs Context vs custom solution
>
> 5. **Multi-File Changes**: The task will likely touch more than 2-3 files
>    - Example: "Refactor the authentication system"
>    - Example: "Add a new API endpoint with tests"
>
> 6. **Unclear Requirements**: You need to explore before understanding the full scope
>    - Example: "Make the app faster" - need to profile and identify bottlenecks
>    - Example: "Fix the bug in checkout" - need to investigate root cause
>
> 7. **User Preferences Matter**: The implementation could reasonably go multiple ways
>    - If you would use ${ASK_USER_QUESTION_TOOL_NAME} to clarify the approach, use EnterPlanMode instead
>    - Plan mode lets you explore first, then present options with context

**翻译：**
## 何时使用此工具

对于实现任务，**优先使用 EnterPlanMode**，除非任务很简单。当以下任一条件成立时使用：

1. **新功能实现**：添加有意义的新功能
   - 示例："添加一个登出按钮"——应该放在哪里？点击后应该发生什么？
   - 示例："添加表单验证"——什么规则？什么错误消息？

2. **多种可行方案**：任务可以用多种不同方式解决
   - 示例："给 API 添加缓存"——可以使用 Redis、内存缓存、文件缓存等
   - 示例："提升性能"——有许多可能的优化策略

3. **代码修改**：影响现有行为或结构的更改
   - 示例："更新登录流程"——具体应该改什么？
   - 示例："重构这个组件"——目标架构是什么？

4. **架构决策**：任务需要在模式或技术之间做选择
   - 示例："添加实时更新"——WebSockets vs SSE vs 轮询
   - 示例："实现状态管理"——Redux vs Context vs 自定义方案

5. **多文件变更**：任务可能涉及 2-3 个以上的文件
   - 示例："重构认证系统"
   - 示例："添加带测试的新 API 端点"

6. **需求不明确**：需要先探索才能理解完整范围
   - 示例："让应用更快"——需要先分析性能瓶颈
   - 示例："修复结账的 bug"——需要调查根本原因

7. **用户偏好很重要**：实现方式可以合理地有多种走向
   - 如果你本来会使用 ${ASK_USER_QUESTION_TOOL_NAME} 来澄清方案，请改用 EnterPlanMode
   - 计划模式让你先探索，再带着上下文呈现选项

---

> **原文：**
> ## When NOT to Use This Tool
>
> Only skip EnterPlanMode for simple tasks:
> - Single-line or few-line fixes (typos, obvious bugs, small tweaks)
> - Adding a single function with clear requirements
> - Tasks where the user has given very specific, detailed instructions
> - Pure research/exploration tasks (use the Agent tool with explore agent instead)

**翻译：**
## 何时不使用此工具

仅在简单任务时跳过 EnterPlanMode：
- 单行或少数几行的修复（拼写错误、明显的 bug、小调整）
- 添加需求明确的单个函数
- 用户已给出非常具体、详细指令的任务
- 纯研究/探索任务（改用 Agent 工具的 explore 智能体）

---

> **原文：**
> ${CONDITIONAL_WHAT_HAPPENS_NOTE}## Examples
>
> ### GOOD - Use EnterPlanMode:
> User: "Add user authentication to the app"
> - Requires architectural decisions (session vs JWT, where to store tokens, middleware structure)
>
> User: "Optimize the database queries"
> - Multiple approaches possible, need to profile first, significant impact
>
> User: "Implement dark mode"
> - Architectural decision on theme system, affects many components
>
> User: "Add a delete button to the user profile"
> - Seems simple but involves: where to place it, confirmation dialog, API call, error handling, state updates
>
> User: "Update the error handling in the API"
> - Affects multiple files, user should approve the approach

**翻译：**
${CONDITIONAL_WHAT_HAPPENS_NOTE}## 示例

### 好的做法 - 使用 EnterPlanMode：
用户："给应用添加用户认证"
- 需要架构决策（session vs JWT、令牌存储位置、中间件结构）

用户："优化数据库查询"
- 多种方案可行，需要先做性能分析，影响重大

用户："实现暗色模式"
- 主题系统的架构决策，影响多个组件

用户："在用户资料页添加删除按钮"
- 看似简单但涉及：放置位置、确认对话框、API 调用、错误处理、状态更新

用户："更新 API 的错误处理"
- 影响多个文件，用户应该审批方案

---

> **原文：**
> ### BAD - Don't use EnterPlanMode:
> User: "Fix the typo in the README"
> - Straightforward, no planning needed
>
> User: "Add a console.log to debug this function"
> - Simple, obvious implementation
>
> User: "What files handle routing?"
> - Research task, not implementation planning

**翻译：**
### 不好的做法 - 不要使用 EnterPlanMode：
用户："修复 README 中的拼写错误"
- 直截了当，无需计划

用户："添加一个 console.log 来调试这个函数"
- 简单、明显的实现

用户："哪些文件处理路由？"
- 研究任务，不是实现计划

---

> **原文：**
> ## Important Notes
>
> - This tool REQUIRES user approval - they must consent to entering plan mode
> - If unsure whether to use it, err on the side of planning - it's better to get alignment upfront than to redo work
> - Users appreciate being consulted before significant changes are made to their codebase

**翻译：**
## 重要说明

- 此工具需要用户批准——他们必须同意进入计划模式
- 如果不确定是否该使用，宁可选择计划——提前对齐方向比返工更好
- 用户在对其代码库进行重大更改之前被征询意见时会很感激

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${ASK_USER_QUESTION_TOOL_NAME}` | 向用户提问工具的名称 |
| `${CONDITIONAL_WHAT_HAPPENS_NOTE}` | 条件性注释，说明进入计划模式后会发生什么 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 角色/行为锚定（Role/Behavior Anchoring） | `Use this tool proactively when you're about to start a non-trivial implementation task` | 将 LLM 定位为一个主动思考的工程师角色，而非被动执行者，鼓励在行动前先规划。 |
| 2 | 结构化列表（Structured Enumeration） | 7 个编号条件，每个都有示例 | 通过编号列表系统化地枚举所有适用场景，使 LLM 可以逐条对照当前任务，做出准确的工具选择判断。 |
| 3 | 示例引导（Example-driven Guidance） | `GOOD - Use EnterPlanMode` / `BAD - Don't use EnterPlanMode` | 通过正反示例对比，直观展示了工具使用的边界，让 LLM 能准确区分需要计划的任务和不需要的任务。 |
| 4 | 负面约束（Negative Constraint） | `When NOT to Use This Tool` 整节 | 明确列出不适用的场景，防止 LLM 对简单任务过度使用计划模式，避免不必要的交互延迟。 |
| 5 | 优先级排序（Priority Ordering） | `Prefer using EnterPlanMode for implementation tasks unless they're simple` | 设定默认行为为"使用计划模式"，只有简单任务才是例外，引导 LLM 偏向更审慎的工作方式。 |
| 6 | 安全防护指令（Safety Guard） | `err on the side of planning - it's better to get alignment upfront than to redo work` | 在不确定时提供安全默认行为，避免 LLM 在重要决策上草率行动导致返工。 |
| 7 | 条件逻辑注入（Conditional Logic Injection） | `${CONDITIONAL_WHAT_HAPPENS_NOTE}` | 根据运行时环境动态注入计划模式的行为说明，使提示词适应不同的功能配置。 |
