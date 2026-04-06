# enterworktree

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: EnterWorktree |
| 分类 | Tool Descriptions → 计划模式 |
| 文件路径 | `system-prompts/tool-description-enterworktree.md` |
| CC 版本 | 2.1.72 |
| 模板变量 | 无 |

## 原文

> Use this tool ONLY when the user explicitly asks to work in a worktree. This tool creates an isolated git worktree and switches the current session into it.
>
> ## When to Use
>
> - The user explicitly says "worktree" (e.g., "start a worktree", "work in a worktree", "create a worktree", "use a worktree")
>
> ## When NOT to Use
>
> - The user asks to create a branch, switch branches, or work on a different branch — use git commands instead
> - The user asks to fix a bug or work on a feature — use normal git workflow unless they specifically mention worktrees
> - Never use this tool unless the user explicitly mentions "worktree"
>
> ## Requirements
>
> - Must be in a git repository, OR have WorktreeCreate/WorktreeRemove hooks configured in settings.json
> - Must not already be in a worktree
>
> ## Behavior
>
> - In a git repository: creates a new git worktree inside `.claude/worktrees/` with a new branch based on HEAD
> - Outside a git repository: delegates to WorktreeCreate/WorktreeRemove hooks for VCS-agnostic isolation
> - Switches the session's working directory to the new worktree
> - Use ExitWorktree to leave the worktree mid-session (keep or remove). On session exit, if still in the worktree, the user will be prompted to keep or remove it
>
> ## Parameters
>
> - `name` (optional): A name for the worktree. If not provided, a random name is generated.

## 中文翻译

> **原文：**
> Use this tool ONLY when the user explicitly asks to work in a worktree. This tool creates an isolated git worktree and switches the current session into it.

**翻译：**
仅当用户明确要求在工作树中工作时才使用此工具。此工具创建一个隔离的 git worktree 并将当前会话切换到其中。

---

> **原文：**
> ## When to Use
>
> - The user explicitly says "worktree" (e.g., "start a worktree", "work in a worktree", "create a worktree", "use a worktree")

**翻译：**
## 何时使用

- 用户明确说出 "worktree"（例如："启动一个 worktree"、"在 worktree 中工作"、"创建一个 worktree"、"使用 worktree"）

---

> **原文：**
> ## When NOT to Use
>
> - The user asks to create a branch, switch branches, or work on a different branch — use git commands instead
> - The user asks to fix a bug or work on a feature — use normal git workflow unless they specifically mention worktrees
> - Never use this tool unless the user explicitly mentions "worktree"

**翻译：**
## 何时不使用

- 用户要求创建分支、切换分支或在不同分支上工作——改用 git 命令
- 用户要求修复 bug 或开发功能——使用正常的 git 工作流程，除非他们特别提到 worktree
- 除非用户明确提到 "worktree"，否则永远不要使用此工具

---

> **原文：**
> ## Requirements
>
> - Must be in a git repository, OR have WorktreeCreate/WorktreeRemove hooks configured in settings.json
> - Must not already be in a worktree

**翻译：**
## 前提条件

- 必须位于 git 仓库中，或者在 settings.json 中配置了 WorktreeCreate/WorktreeRemove 钩子
- 当前不能已在 worktree 中

---

> **原文：**
> ## Behavior
>
> - In a git repository: creates a new git worktree inside `.claude/worktrees/` with a new branch based on HEAD
> - Outside a git repository: delegates to WorktreeCreate/WorktreeRemove hooks for VCS-agnostic isolation
> - Switches the session's working directory to the new worktree
> - Use ExitWorktree to leave the worktree mid-session (keep or remove). On session exit, if still in the worktree, the user will be prompted to keep or remove it

**翻译：**
## 行为

- 在 git 仓库中：在 `.claude/worktrees/` 内创建一个新的 git worktree，基于 HEAD 创建新分支
- 在 git 仓库外：委托给 WorktreeCreate/WorktreeRemove 钩子进行与 VCS 无关的隔离
- 将会话的工作目录切换到新的 worktree
- 使用 ExitWorktree 在会话中途离开 worktree（保留或移除）。会话退出时，如果仍在 worktree 中，将提示用户选择保留或移除

---

> **原文：**
> ## Parameters
>
> - `name` (optional): A name for the worktree. If not provided, a random name is generated.

**翻译：**
## 参数

- `name`（可选）：worktree 的名称。如果未提供，将生成一个随机名称。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | `ONLY when the user explicitly asks` / `Never use this tool unless the user explicitly mentions "worktree"` | 通过大写 ONLY 和重复强调"明确提到"，严格限制工具的触发条件，防止 LLM 在用户仅提到分支操作时误用此工具。 |
| 2 | 结构化列表（Structured Enumeration） | `When to Use` / `When NOT to Use` / `Requirements` / `Behavior` / `Parameters` | 通过清晰的章节划分，系统性地覆盖了工具使用的所有方面，便于 LLM 快速查阅。 |
| 3 | 示例引导（Example-driven Guidance） | `"start a worktree", "work in a worktree", "create a worktree", "use a worktree"` | 列出用户可能使用的多种表述方式，帮助 LLM 进行意图识别和关键词匹配。 |
| 4 | 范围限定（Scope Limitation） | `The user asks to create a branch, switch branches — use git commands instead` | 明确划分 worktree 工具和普通 git 命令的职责边界，避免功能混淆。 |
| 5 | 安全防护指令（Safety Guard） | `Must not already be in a worktree` | 设置前置条件检查，防止在已有 worktree 中重复创建，避免嵌套导致的混乱状态。 |
