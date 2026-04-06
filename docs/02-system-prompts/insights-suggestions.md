# insights-suggestions

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Insights suggestions |
| 分类 | System Prompts → 洞察报告 |
| 文件路径 | `system-prompts/system-prompt-insights-suggestions.md` |
| CC 版本 | 2.1.30 |
| 模板变量 | 无（隐式接收使用数据作为上下文） |
| 首次出现版本 | 2.1.30 |

## 原文

> Analyze this Claude Code usage data and suggest improvements.
>
> ## CC FEATURES REFERENCE (pick from these for features_to_try):
> 1. **MCP Servers**: Connect Claude to external tools, databases, and APIs via Model Context Protocol.
>    - How to use: Run `claude mcp add <server-name> -- <command>`
>    - Good for: database queries, Slack integration, GitHub issue lookup, connecting to internal APIs
>
> 2. **Custom Skills**: Reusable prompts you define as markdown files that run with a single /command.
>    - How to use: Create `.claude/skills/commit/SKILL.md` with instructions. Then type `/commit` to run it.
>    - Good for: repetitive workflows - /commit, /review, /test, /deploy, /pr, or complex multi-step workflows
>
> 3. **Hooks**: Shell commands that auto-run at specific lifecycle events.
>    - How to use: Add to `.claude/settings.json` under "hooks" key.
>    - Good for: auto-formatting code, running type checks, enforcing conventions
>
> 4. **Headless Mode**: Run Claude non-interactively from scripts and CI/CD.
>    - How to use: `claude -p "fix lint errors" --allowedTools "Edit,Read,Bash"`
>    - Good for: CI/CD integration, batch code fixes, automated reviews
>
> 5. **Task Agents**: Claude spawns focused sub-agents for complex exploration or parallel work.
>    - How to use: Claude auto-invokes when helpful, or ask "use an agent to explore X"
>    - Good for: codebase exploration, understanding complex systems
>
> RESPOND WITH ONLY A VALID JSON OBJECT:
> {
>   "claude_md_additions": [...],
>   "features_to_try": [...],
>   "usage_patterns": [...]
> }
>
> IMPORTANT for claude_md_additions: PRIORITIZE instructions that appear MULTIPLE TIMES in the user data. If user told Claude the same thing in 2+ sessions (e.g., 'always run tests', 'use TypeScript'), that's a PRIME candidate - they shouldn't have to repeat themselves.
>
> IMPORTANT for features_to_try: Pick 2-3 from the CC FEATURES REFERENCE above. Include 2-3 items for each category.

## 中文翻译

> **原文：**
> Analyze this Claude Code usage data and suggest improvements.

**翻译：**
分析此 Claude Code 使用数据并建议改进方案。

> **原文：**
> CC FEATURES REFERENCE (pick from these for features_to_try):
> 1. MCP Servers... 2. Custom Skills... 3. Hooks... 4. Headless Mode... 5. Task Agents...

**翻译：**
CC 功能参考（从中选择 features_to_try）：
1. **MCP Servers（MCP 服务器）**：通过 Model Context Protocol 将 Claude 连接到外部工具、数据库和 API。
2. **Custom Skills（自定义技能）**：定义为 Markdown 文件的可复用提示词，通过单个 /command 运行。
3. **Hooks（钩子）**：在特定生命周期事件时自动运行的 shell 命令。
4. **Headless Mode（无头模式）**：从脚本和 CI/CD 非交互式地运行 Claude。
5. **Task Agents（任务代理）**：Claude 为复杂探索或并行工作生成专注的子代理。

> **原文：**
> IMPORTANT for claude_md_additions: PRIORITIZE instructions that appear MULTIPLE TIMES in the user data.

**翻译：**
claude_md_additions 的重要说明：优先考虑在用户数据中**多次出现**的指令。如果用户在 2 个以上的会话中告诉 Claude 相同的事情（例如 "always run tests"、"use TypeScript"），这就是首要候选——他们不应该需要反复重复自己。

> **原文：**
> IMPORTANT for features_to_try: Pick 2-3 from the CC FEATURES REFERENCE above. Include 2-3 items for each category.

**翻译：**
features_to_try 的重要说明：从上方的 CC 功能参考中选择 2-3 个。每个类别包含 2-3 个条目。

## 📋 模板变量说明

无显式模板变量。使用数据作为上下文在运行时附加。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 封闭式功能列表 | "CC FEATURES REFERENCE (pick from these for features_to_try)" | 提供固定的功能参考列表并要求从中选择，防止模型推荐不存在或不相关的功能。 |
| 2 | 频率优先规则 | "PRIORITIZE instructions that appear MULTIPLE TIMES in the user data" | 将重复出现的指令作为优先信号，确保建议解决用户最持久的需求，而非一次性问题。 |
| 3 | 可操作建议格式 | `"example_code": "Actual command or config to copy"` | 每个建议都包含可直接复制的代码/命令，降低用户的采用门槛。 |
| 4 | 用户视角框架 | "they shouldn't have to repeat themselves" | 从用户痛点角度解释优先级规则，使建议生成更具同理心。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.30 | 新增 | 首次引入改进建议生成提示词 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/87f225d" target="_blank">87f225d</a> |
