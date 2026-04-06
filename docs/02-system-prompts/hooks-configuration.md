# hooks-configuration

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Hooks Configuration |
| 分类 | System Prompts → 配置与扩展 |
| 文件路径 | `system-prompts/system-prompt-hooks-configuration.md` |
| CC 版本 | 2.1.77 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.9 |

## 原文

> ## Hooks Configuration
>
> Hooks run commands at specific points in Claude Code's lifecycle.
>
> ### Hook Structure
> ```json
> {
>   "hooks": {
>     "EVENT_NAME": [
>       {
>         "matcher": "ToolName|OtherTool",
>         "hooks": [
>           {
>             "type": "command",
>             "command": "your-command-here",
>             "timeout": 60,
>             "statusMessage": "Running..."
>           }
>         ]
>       }
>     ]
>   }
> }
> ```
>
> ### Hook Events
>
> | Event | Matcher | Purpose |
> |-------|---------|---------|
> | PermissionRequest | Tool name | Run before permission prompt |
> | PreToolUse | Tool name | Run before tool, can block |
> | PostToolUse | Tool name | Run after successful tool |
> | PostToolUseFailure | Tool name | Run after tool fails |
> | Notification | Notification type | Run on notifications |
> | Stop | - | Run when Claude stops (including clear, resume, compact) |
> | PreCompact | "manual"/"auto" | Before compaction |
> | PostCompact | "manual"/"auto" | After compaction (receives summary) |
> | UserPromptSubmit | - | When user submits |
> | SessionStart | - | When session starts |
>
> **Common tool matchers:** `Bash`, `Write`, `Edit`, `Read`, `Glob`, `Grep`
>
> ### Hook Types
>
> **1. Command Hook** - Runs a shell command:
> ```json
> { "type": "command", "command": "prettier --write $FILE", "timeout": 30 }
> ```
>
> **2. Prompt Hook** - Evaluates a condition with LLM:
> ```json
> { "type": "prompt", "prompt": "Is this safe? $ARGUMENTS" }
> ```
> Only available for tool events: PreToolUse, PostToolUse, PermissionRequest.
>
> **3. Agent Hook** - Runs an agent with tools:
> ```json
> { "type": "agent", "prompt": "Verify tests pass: $ARGUMENTS" }
> ```
> Only available for tool events: PreToolUse, PostToolUse, PermissionRequest.
>
> ### Hook Input (stdin JSON)
> ```json
> {
>   "session_id": "abc123",
>   "tool_name": "Write",
>   "tool_input": { "file_path": "/path/to/file.txt", "content": "..." },
>   "tool_response": { "success": true }  // PostToolUse only
> }
> ```
>
> ### Hook JSON Output
>
> Hooks can return JSON to control behavior:
>
> ```json
> {
>   "systemMessage": "Warning shown to user in UI",
>   "continue": false,
>   "stopReason": "Message shown when blocking",
>   "suppressOutput": false,
>   "decision": "block",
>   "reason": "Explanation for decision",
>   "hookSpecificOutput": {
>     "hookEventName": "PostToolUse",
>     "additionalContext": "Context injected back to model"
>   }
> }
> ```
>
> **Fields:**
> - `systemMessage` - Display a message to the user (all hooks)
> - `continue` - Set to `false` to block/stop (default: true)
> - `stopReason` - Message shown when `continue` is false
> - `suppressOutput` - Hide stdout from transcript (default: false)
> - `decision` - "block" for PostToolUse/Stop/UserPromptSubmit hooks (deprecated for PreToolUse, use hookSpecificOutput.permissionDecision instead)
> - `reason` - Explanation for decision
> - `hookSpecificOutput` - Event-specific output (must include `hookEventName`):
>   - `additionalContext` - Text injected into model context
>   - `permissionDecision` - "allow", "deny", or "ask" (PreToolUse only)
>   - `permissionDecisionReason` - Reason for the permission decision (PreToolUse only)
>   - `updatedInput` - Modified tool input (PreToolUse only)
>
> ### Common Patterns
>
> **Auto-format after writes:**
> ```json
> {
>   "hooks": {
>     "PostToolUse": [{
>       "matcher": "Write|Edit",
>       "hooks": [{
>         "type": "command",
>         "command": "jq -r '.tool_response.filePath // .tool_input.file_path' | { read -r f; prettier --write \"$f\"; } 2>/dev/null || true"
>       }]
>     }]
>   }
> }
> ```
>
> **Log all bash commands:**
> ```json
> {
>   "hooks": {
>     "PreToolUse": [{
>       "matcher": "Bash",
>       "hooks": [{
>         "type": "command",
>         "command": "jq -r '.tool_input.command' >> ~/.claude/bash-log.txt"
>       }]
>     }]
>   }
> }
> ```
>
> **Stop hook that displays message to user:**
>
> Command must output JSON with `systemMessage` field:
> ```bash
> # Example command that outputs: {"systemMessage": "Session complete!"}
> echo '{"systemMessage": "Session complete!"}'
> ```
>
> **Run tests after code changes:**
> ```json
> {
>   "hooks": {
>     "PostToolUse": [{
>       "matcher": "Write|Edit",
>       "hooks": [{
>         "type": "command",
>         "command": "jq -r '.tool_input.file_path // .tool_response.filePath' | grep -E '\\.(ts|js)$' && npm test || true"
>       }]
>     }]
>   }
> }
> ```

## 中文翻译

> **原文：**
> Hooks run commands at specific points in Claude Code's lifecycle.

**翻译：**
Hooks 在 Claude Code 生命周期的特定时刻运行命令。

> **原文：**
> Hook Events table

**翻译：**
Hook 事件表：

| 事件 | 匹配器 | 用途 |
|------|--------|------|
| PermissionRequest | 工具名称 | 在权限提示前运行 |
| PreToolUse | 工具名称 | 在工具执行前运行，可阻止执行 |
| PostToolUse | 工具名称 | 在工具成功执行后运行 |
| PostToolUseFailure | 工具名称 | 在工具执行失败后运行 |
| Notification | 通知类型 | 在通知时运行 |
| Stop | - | 当 Claude 停止时运行（包括清除、恢复、压缩） |
| PreCompact | "manual"/"auto" | 压缩前 |
| PostCompact | "manual"/"auto" | 压缩后（接收摘要） |
| UserPromptSubmit | - | 用户提交时 |
| SessionStart | - | 会话开始时 |

> **原文：**
> Hook Types: Command Hook, Prompt Hook, Agent Hook

**翻译：**
Hook 类型：
1. **Command Hook** - 运行 shell 命令
2. **Prompt Hook** - 使用 LLM 评估条件（仅适用于工具事件：PreToolUse、PostToolUse、PermissionRequest）
3. **Agent Hook** - 使用工具运行代理（仅适用于工具事件：PreToolUse、PostToolUse、PermissionRequest）

> **原文：**
> Hook JSON Output fields

**翻译：**
Hook JSON 输出字段：
- `systemMessage` - 向用户显示消息（所有 hooks）
- `continue` - 设为 `false` 可阻止/停止（默认：true）
- `stopReason` - 当 `continue` 为 false 时显示的消息
- `suppressOutput` - 隐藏 stdout 不进入转录记录（默认：false）
- `decision` - PostToolUse/Stop/UserPromptSubmit hooks 使用 "block"（PreToolUse 已弃用，改用 hookSpecificOutput.permissionDecision）
- `reason` - 决策解释
- `hookSpecificOutput` - 事件特定输出（必须包含 `hookEventName`）：
  - `additionalContext` - 注入模型上下文的文本
  - `permissionDecision` - "allow"、"deny" 或 "ask"（仅 PreToolUse）
  - `permissionDecisionReason` - 权限决策原因（仅 PreToolUse）
  - `updatedInput` - 修改后的工具输入（仅 PreToolUse）

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 结构化参考文档 | 整体采用标题→表格→代码→示例的结构 | 作为配置参考，采用技术文档结构比自然语言描述更高效，模型可以直接提取 JSON 模式用于生成配置。 |
| 2 | 可复制的示例 | "Auto-format after writes"、"Log all bash commands" 等完整 JSON 示例 | 提供端到端的可复制代码块，让模型可以直接适配而非从零构建，减少生成错误。 |
| 3 | 匹配器管道语法 | `"matcher": "Write\|Edit"` | 使用管道符分隔多工具匹配的简洁语法，降低配置复杂度。 |
| 4 | 弃用标注 | "deprecated for PreToolUse, use hookSpecificOutput.permissionDecision instead" | 清晰地标注 API 迁移路径，防止模型生成使用旧 API 的配置。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.9 | 新增 | 首次引入 Hooks 配置系统提示词 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/0f37d97" target="_blank">0f37d97</a> |
| 2.1.30 | 更新 | 重大重构 hook 响应格式，增加 `suppressOutput`、`decision`、`reason`、`hookSpecificOutput` 等字段 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/87f225d" target="_blank">87f225d</a> |
| 2.1.76 | 更新 | 增加 `PostCompact` hook 事件 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/6cc7a81" target="_blank">6cc7a81</a> |
| 2.1.77 | 更新 | prettier 示例命令从 `xargs` 改为 `read -r f` 以安全处理文件名 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/87fae2a" target="_blank">87fae2a</a> |
