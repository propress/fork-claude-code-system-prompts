# simplify

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: Simplify |
| 分类 | Skills → 代码质量 |
| 文件路径 | `system-prompts/skill-simplify.md` |
| CC 版本 | 2.1.81 |
| 模板变量 | `${AGENT_TOOL_NAME}` |

## 原文（摘要）

中等长度文件（56 行），指导三个并行审查 Agent 审查代码变更。

> # Simplify: Code Review and Cleanup
>
> Review all changed files for reuse, quality, and efficiency. Fix any issues found.

### Phase 1: Identify Changes
> Run `git diff` (or `git diff HEAD` if there are staged changes) to see what changed.

### Phase 2: Launch Three Review Agents in Parallel
> Use the ${AGENT_TOOL_NAME} tool to launch all three agents concurrently in a single message. Pass each agent the full diff so it has the complete context.

**Agent 1: Code Reuse Review** — 搜索可替代新写代码的现有工具函数和辅助函数
**Agent 2: Code Quality Review** — 审查冗余状态、参数膨胀、复制粘贴变体、泄漏抽象、字符串类型代码、不必要的 JSX 嵌套、不必要的注释
**Agent 3: Efficiency Review** — 审查不必要的工作、错过的并发、热路径膨胀、循环无操作更新、不必要的存在检查（TOCTOU）、内存问题、过于宽泛的操作

### Phase 3: Fix Issues
> Wait for all three agents to complete. Aggregate their findings and fix each issue directly. If a finding is a false positive or not worth addressing, note it and move on.

## 中文翻译

# 简化：代码审查和清理

审查所有变更文件的复用性、质量和效率。修复发现的任何问题。

### 第一阶段：识别变更

运行 `git diff`（如果有暂存更改则运行 `git diff HEAD`）查看变更内容。如果没有 git 变更，审查用户提到的或你在本次对话中编辑过的最近修改文件。

### 第二阶段：并行启动三个审查 Agent

使用 ${AGENT_TOOL_NAME} 工具在单条消息中并发启动所有三个 Agent。将完整 diff 传递给每个 Agent 以获取完整上下文。

#### Agent 1：代码复用审查

对每个变更：

1. **搜索现有工具函数和辅助函数** 以替代新写的代码。在代码库中查找类似模式——常见位置包括工具目录、共享模块和变更文件的相邻文件。
2. **标记任何重复现有功能的新函数。** 建议使用现有函数。
3. **标记任何可以使用现有工具函数的内联逻辑** — 手写的字符串操作、手动路径处理、自定义环境检查、临时类型守卫等模式是常见候选。

#### Agent 2：代码质量审查

审查同样的变更，检查不规范的模式：

1. **冗余状态**：重复现有状态的状态、可以派生的缓存值、可以直接调用的观察者/效果
2. **参数膨胀**：向函数添加新参数而不是泛化或重构现有参数
3. **微变复制粘贴**：应通过共享抽象统一的近似重复代码块
4. **泄漏抽象**：暴露应封装的内部细节，或打破现有的抽象边界
5. **字符串类型化代码**：在代码库中已存在常量、枚举（字符串联合）或品牌类型的地方使用原始字符串
6. **不必要的 JSX 嵌套**：不增加布局价值的包装 Box/元素——检查内部组件 props 是否已提供所需行为
7. **不必要的注释**：解释代码"做什么"的注释（命名良好的标识符已经做到了）、描述变更的注释、引用任务/调用者的注释——删除；只保留非显而易见的"为什么"（隐藏约束、微妙不变量、变通方案）

#### Agent 3：效率审查

审查同样的变更，检查效率问题：

1. **不必要的工作**：冗余计算、重复文件读取、重复网络/API 调用、N+1 模式
2. **错过的并发**：可以并行运行的独立操作顺序执行
3. **热路径膨胀**：添加到启动或每请求/每渲染热路径的新阻塞工作
4. **循环无操作更新**：轮询循环、定时器或事件处理器中无条件触发的状态/存储更新——添加变更检测守卫
5. **不必要的存在检查**：在操作前预检查文件/资源存在（TOCTOU 反模式）——直接操作并处理错误
6. **内存**：无界数据结构、缺少清理、事件监听器泄漏
7. **过于宽泛的操作**：在只需要一部分时读取整个文件、在筛选一项时加载所有项

### 第三阶段：修复问题

等待所有三个 Agent 完成。汇总发现并直接修复每个问题。如果发现是误报或不值得处理，记录并继续——不要与发现争论，直接跳过。

完成后，简要总结修复了什么（或确认代码已经很干净）。

## 📋 模板变量说明

| 变量 | 说明 |
|------|------|
| `${AGENT_TOOL_NAME}` | 启动子 Agent 的工具名称，用于并行启动三个审查 Agent |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 并行 Agent 委托 | "launch all three agents concurrently in a single message" | 利用并行执行加速审查，同时将复杂的审查分解为专注的子任务 |
| 2 | 枚举式检查清单 | 每个 Agent 有 3-7 个编号的检查项 | 将代码审查的隐性知识转化为明确的检查清单，确保 LLM 不遗漏审查维度 |
| 3 | 误报容忍策略 | "If a finding is a false positive or not worth addressing, note it and move on — do not argue with the finding" | 防止 LLM 在误报上花费过多时间辩论，保持审查效率 |
| 4 | 反模式命名 | "TOCTOU anti-pattern"、"N+1 patterns"、"Stringly-typed code" | 使用业界已知的反模式名称，利用 LLM 训练数据中对这些模式的理解 |
| 5 | 完整 diff 上下文 | "Pass each agent the full diff so it has the complete context" | 确保每个审查 Agent 都有全局视角，避免因上下文不足而产生误判 |
| 6 | 具体技术示例 | "wrapper Boxes/elements that add no layout value — check if inner component props (flexShrink, alignItems, etc.) already provide the needed behavior" | 用具体的 CSS/React props 示例让 LLM 理解精确的检查标准 |
