# teamdelete

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: TeamDelete |
| 分类 | Tool Descriptions → Agent 工具 |
| 文件路径 | `system-prompts/tool-description-teamdelete.md` |
| CC 版本 | 2.1.33 |
| 模板变量 | 无 |

## 原文

> # TeamDelete
>
> Remove team and task directories when the swarm work is complete.
>
> This operation:
> - Removes the team directory (`~/.claude/teams/{team-name}/`)
> - Removes the task directory (`~/.claude/tasks/{team-name}/`)
> - Clears team context from the current session
>
> **IMPORTANT**: TeamDelete will fail if the team still has active members. Gracefully terminate teammates first, then call TeamDelete after all teammates have shut down.
>
> Use this when all teammates have finished their work and you want to clean up the team resources. The team name is automatically determined from the current session's team context.

## 中文翻译

> **原文：**
> Remove team and task directories when the swarm work is complete.

**翻译：**
当集群工作完成时，移除团队和任务目录。

> **原文：**
> This operation:
> - Removes the team directory (`~/.claude/teams/{team-name}/`)
> - Removes the task directory (`~/.claude/tasks/{team-name}/`)
> - Clears team context from the current session

**翻译：**
此操作：
- 移除团队目录（`~/.claude/teams/{team-name}/`）
- 移除任务目录（`~/.claude/tasks/{team-name}/`）
- 清除当前会话中的团队上下文

> **原文：**
> **IMPORTANT**: TeamDelete will fail if the team still has active members. Gracefully terminate teammates first, then call TeamDelete after all teammates have shut down.

**翻译：**
**重要**：如果团队仍有活跃成员，TeamDelete 会失败。先优雅地终止队友，然后在所有队友关闭后再调用 TeamDelete。

> **原文：**
> Use this when all teammates have finished their work and you want to clean up the team resources.

**翻译：**
当所有队友完成工作且你想清理团队资源时使用此工具。团队名称从当前会话的团队上下文自动确定。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 前置条件 | `will fail if the team still has active members` | 明确说明失败条件，防止错误调用 |
| 2 | 操作顺序 | `Gracefully terminate ... first, then call TeamDelete` | 强调必须先终止后删除的顺序 |
| 3 | 资源清单 | 列出三个具体的清理操作 | 让模型理解此工具的完整影响范围 |
