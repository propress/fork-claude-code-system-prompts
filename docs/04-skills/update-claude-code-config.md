# update-claude-code-config

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: Update Claude Code Config |
| 分类 | Skills → 项目配置 |
| 文件路径 | `system-prompts/skill-update-claude-code-config.md` |
| CC 版本 | 2.1.77 |
| 模板变量 | `${SETTINGS_FILE_LOCATION_PROMPT}`、`${HOOKS_CONFIGURATION_PROMPT}`、`${CONSTRUCTING_HOOK_PROMPT}` |

## 原文（摘要）

较大文件（145 行），指导修改 Claude Code 配置文件 (settings.json)。

### 何时需要 Hook（而非 Memory）

> If the user wants something to happen automatically in response to an EVENT, they need a **hook** configured in settings.json.
>
> **These require hooks:**
> - "Before compacting, ask me what to preserve" → PreCompact hook
> - "After writing files, run prettier" → PostToolUse hook with Write|Edit matcher
> - "When I run bash commands, log them" → PreToolUse hook with Bash matcher
> - "Always run tests after code changes" → PostToolUse hook

### 关键规则

> **CRITICAL: Read Before Write** — Always read the existing settings file before making changes. Merge new settings with existing ones - never replace the entire file.
>
> **CRITICAL: Use AskUserQuestion for Ambiguity** — When the user's request is ambiguous, use AskUserQuestion to clarify.

### Config Tool vs Direct Edit 决策

> **Use the Config tool** for: theme, editorMode, verbose, model, language, alwaysThinkingEnabled, permissions.defaultMode
>
> **Edit settings.json directly** for: Hooks, Complex permission rules, Environment variables, MCP server configuration, Plugin configuration

### 合并数组（重要！）

> When adding to permission arrays or hook arrays, **merge with existing**, don't replace

### 故障排查

> If a hook isn't running:
> 1. Check the settings file
> 2. Verify JSON syntax — Invalid JSON silently fails
> 3. Check the matcher
> 4. Check hook type — "command", "prompt", or "agent"
> 5. Test the command manually
> 6. Use --debug

## 中文翻译

# 更新配置 Skill

通过更新 settings.json 文件来修改 Claude Code 配置。

### 何时需要 Hook（而非 Memory）

如果用户希望在事件响应中自动执行某些操作，他们需要在 settings.json 中配置 **Hook**。Memory/偏好设置无法触发自动化操作。

**这些需要 Hook：**
- "压缩前，问我要保留什么" → PreCompact hook
- "写文件后，运行 prettier" → PostToolUse hook，匹配器为 Write|Edit
- "运行 bash 命令时，记录它们" → PreToolUse hook，匹配器为 Bash
- "代码更改后始终运行测试" → PostToolUse hook

**Hook 事件：** PreToolUse、PostToolUse、PreCompact、PostCompact、Stop、Notification、SessionStart

### 关键：先读后写

**始终在更改前读取现有设置文件。** 将新设置与现有设置合并——永远不要替换整个文件。

### 关键：对歧义使用 AskUserQuestion

当用户请求不明确时，使用 AskUserQuestion 澄清：要修改哪个设置文件（user/project/local）、是添加到现有数组还是替换、当存在多个选项时的具体值。

### 决策：Config Tool 还是直接编辑

**使用 Config tool** 处理简单设置：`theme`、`editorMode`、`verbose`、`model`、`language`、`alwaysThinkingEnabled`、`permissions.defaultMode`

**直接编辑 settings.json** 处理：Hooks（PreToolUse、PostToolUse 等）、复杂权限规则（allow/deny 数组）、环境变量、MCP 服务器配置、插件配置

### 工作流

1. **澄清意图** — 如果请求不明确则询问
2. **读取现有文件** — 使用 Read 工具读取目标设置文件
3. **谨慎合并** — 保留现有设置，特别是数组
4. **编辑文件** — 使用 Edit 工具
5. **确认** — 告诉用户更改了什么

### 合并数组（重要！）

添加到权限数组或 Hook 数组时，**与现有合并**，不要替换：

**错误**（替换现有权限）：
```json
{ "permissions": { "allow": ["Bash(npm:*)"] } }
```

**正确**（保留现有 + 添加新的）：
```json
{
  "permissions": {
    "allow": [
      "Bash(git:*)",      // 现有
      "Edit(.claude)",    // 现有
      "Bash(npm:*)"       // 新增
    ]
  }
}
```

### 示例工作流

**添加 Hook：**
用户："写代码后格式化"
1. 澄清使用哪个格式化器
2. 读取 `.claude/settings.json`
3. 合并到现有 Hooks，不替换
4. 结果包含 PostToolUse Hook，匹配器为 Write|Edit

**添加权限：**
合并 `Bash(npm:*)` 到现有 allow 数组

**环境变量：**
决定用户设置还是项目设置，合并到 env 对象

### 故障排查 Hook

如果 Hook 未运行：
1. 检查设置文件
2. 验证 JSON 语法——无效 JSON 会静默失败
3. 检查匹配器——是否匹配工具名？（如 "Bash"、"Write"、"Edit"）
4. 检查 Hook 类型——是 "command"、"prompt" 还是 "agent"？
5. 手动测试命令
6. 使用 `claude --debug` 查看 Hook 执行日志

## 📋 模板变量说明

| 变量 | 说明 |
|------|------|
| `${SETTINGS_FILE_LOCATION_PROMPT}` | 运行时注入的设置文件位置说明，包含用户/项目/本地设置文件的路径信息 |
| `${HOOKS_CONFIGURATION_PROMPT}` | 运行时注入的 Hooks 配置参考，包含 Hook 结构和事件类型的完整说明 |
| `${CONSTRUCTING_HOOK_PROMPT}` | 运行时注入的 Hook 构建指南，可能引用 7 步验证流程 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 先读后写规则 | "**CRITICAL: Read Before Write** — Always read the existing settings file before making changes" | 用 CRITICAL 标签强调，防止 LLM 直接覆写导致用户丢失现有配置 |
| 2 | 正误对比示例 | WRONG vs RIGHT 的 JSON 合并示例 | 通过对比让 LLM 理解"合并"的精确含义，而非抽象概念 |
| 3 | 意图-工具映射 | 用户意图到 Hook 事件的精确映射表 | 将自然语言需求转化为技术配置的查找表 |
| 4 | 双工具路由 | Config tool（简单设置）vs 直接编辑（复杂配置） | 防止 LLM 对所有设置使用同一种方法，简单设置用安全工具，复杂设置用灵活方式 |
| 5 | 静默失败警告 | "Invalid JSON silently fails" | 强调 JSON 错误不会报错而是静默失败，促使 LLM 验证语法 |
| 6 | 模板变量组合注入 | 三个大型模板变量注入完整的配置参考 | 通过运行时注入保持基础 Skill 简洁，按需加载详细参考信息 |
