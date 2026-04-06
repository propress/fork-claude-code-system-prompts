# exitworktree

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: ExitWorktree |
| 分类 | Tool Descriptions → 计划模式 |
| 文件路径 | `system-prompts/tool-description-exitworktree.md` |
| CC 版本 | 2.1.72 |
| 模板变量 | 无 |

## 原文

> Exit a worktree session created by EnterWorktree and return the session to the original working directory.
>
> ## Scope
>
> This tool ONLY operates on worktrees created by EnterWorktree in this session. It will NOT touch:
> - Worktrees you created manually with `git worktree add`
> - Worktrees from a previous session (even if created by EnterWorktree then)
> - The directory you're in if EnterWorktree was never called
>
> If called outside an EnterWorktree session, the tool is a **no-op**: it reports that no worktree session is active and takes no action. Filesystem state is unchanged.
>
> ## When to Use
>
> - The user explicitly asks to "exit the worktree", "leave the worktree", "go back", or otherwise end the worktree session
> - Do NOT call this proactively — only when the user asks
>
> ## Parameters
>
> - `action` (required): `"keep"` or `"remove"`
>   - `"keep"` — leave the worktree directory and branch intact on disk. Use this if the user wants to come back to the work later, or if there are changes to preserve.
>   - `"remove"` — delete the worktree directory and its branch. Use this for a clean exit when the work is done or abandoned.
> - `discard_changes` (optional, default false): only meaningful with `action: "remove"`. If the worktree has uncommitted files or commits not on the original branch, the tool will REFUSE to remove it unless this is set to `true`. If the tool returns an error listing changes, confirm with the user before re-invoking with `discard_changes: true`.
>
> ## Behavior
>
> - Restores the session's working directory to where it was before EnterWorktree
> - Clears CWD-dependent caches (system prompt sections, memory files, plans directory) so the session state reflects the original directory
> - If a tmux session was attached to the worktree: killed on `remove`, left running on `keep` (its name is returned so the user can reattach)
> - Once exited, EnterWorktree can be called again to create a fresh worktree

## 中文翻译

> **原文：**
> Exit a worktree session created by EnterWorktree and return the session to the original working directory.

**翻译：**
退出由 EnterWorktree 创建的 worktree 会话，并将会话返回到原始工作目录。

---

> **原文：**
> ## Scope
>
> This tool ONLY operates on worktrees created by EnterWorktree in this session. It will NOT touch:
> - Worktrees you created manually with `git worktree add`
> - Worktrees from a previous session (even if created by EnterWorktree then)
> - The directory you're in if EnterWorktree was never called
>
> If called outside an EnterWorktree session, the tool is a **no-op**: it reports that no worktree session is active and takes no action. Filesystem state is unchanged.

**翻译：**
## 作用范围

此工具仅操作当前会话中由 EnterWorktree 创建的 worktree。它不会触及：
- 你通过 `git worktree add` 手动创建的 worktree
- 来自上一个会话的 worktree（即使当时是由 EnterWorktree 创建的）
- 如果从未调用过 EnterWorktree，你当前所在的目录

如果在 EnterWorktree 会话之外被调用，此工具是一个**空操作**：它会报告当前没有活跃的 worktree 会话且不执行任何操作。文件系统状态保持不变。

---

> **原文：**
> ## When to Use
>
> - The user explicitly asks to "exit the worktree", "leave the worktree", "go back", or otherwise end the worktree session
> - Do NOT call this proactively — only when the user asks

**翻译：**
## 何时使用

- 用户明确要求"退出 worktree"、"离开 worktree"、"返回"或以其他方式结束 worktree 会话
- 不要主动调用此工具——仅在用户要求时使用

---

> **原文：**
> ## Parameters
>
> - `action` (required): `"keep"` or `"remove"`
>   - `"keep"` — leave the worktree directory and branch intact on disk. Use this if the user wants to come back to the work later, or if there are changes to preserve.
>   - `"remove"` — delete the worktree directory and its branch. Use this for a clean exit when the work is done or abandoned.
> - `discard_changes` (optional, default false): only meaningful with `action: "remove"`. If the worktree has uncommitted files or commits not on the original branch, the tool will REFUSE to remove it unless this is set to `true`. If the tool returns an error listing changes, confirm with the user before re-invoking with `discard_changes: true`.

**翻译：**
## 参数

- `action`（必填）：`"keep"` 或 `"remove"`
  - `"keep"` — 保留磁盘上的 worktree 目录和分支不变。当用户希望稍后继续工作或有需要保留的更改时使用。
  - `"remove"` — 删除 worktree 目录及其分支。当工作完成或放弃时用于干净退出。
- `discard_changes`（可选，默认 false）：仅在 `action: "remove"` 时有意义。如果 worktree 中有未提交的文件或不在原始分支上的提交，工具将拒绝移除，除非此值设为 `true`。如果工具返回列出变更的错误，请先与用户确认后再使用 `discard_changes: true` 重新调用。

---

> **原文：**
> ## Behavior
>
> - Restores the session's working directory to where it was before EnterWorktree
> - Clears CWD-dependent caches (system prompt sections, memory files, plans directory) so the session state reflects the original directory
> - If a tmux session was attached to the worktree: killed on `remove`, left running on `keep` (its name is returned so the user can reattach)
> - Once exited, EnterWorktree can be called again to create a fresh worktree

**翻译：**
## 行为

- 将会话的工作目录恢复到调用 EnterWorktree 之前的位置
- 清除依赖当前工作目录的缓存（系统提示词片段、记忆文件、计划目录），使会话状态反映原始目录
- 如果有 tmux 会话附加到该 worktree：`remove` 时终止，`keep` 时保持运行（返回其名称以便用户重新连接）
- 退出后，可以再次调用 EnterWorktree 创建新的 worktree

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 范围限定（Scope Limitation） | `This tool ONLY operates on worktrees created by EnterWorktree in this session` | 严格限定工具的操作范围为当前会话中创建的 worktree，防止意外影响手动创建的或其他会话的 worktree，确保操作安全。 |
| 2 | 负面约束（Negative Constraint） | `It will NOT touch:` 后跟三条排除项 / `Do NOT call this proactively` | 通过明确列出不会触及的内容和禁止的行为，构建了多层安全边界，防止数据丢失。 |
| 3 | 安全防护指令（Safety Guard） | `the tool will REFUSE to remove it unless this is set to true` / `confirm with the user before re-invoking` | 通过默认拒绝删除有未提交变更的 worktree，并要求用户确认后才能强制删除，实现了渐进式安全保护。 |
| 4 | 结构化列表（Structured Enumeration） | `Scope` / `When to Use` / `Parameters` / `Behavior` 四大章节 | 按照"能做什么→何时做→怎么做→做了之后"的逻辑递进组织信息，形成完整的使用指南。 |
| 5 | 条件逻辑注入（Conditional Logic Injection） | `only meaningful with action: "remove"` | 说明参数之间的条件依赖关系，帮助 LLM 理解参数组合的语义，避免无效的参数搭配。 |
