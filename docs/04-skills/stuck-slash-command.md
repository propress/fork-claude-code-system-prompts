# stuck-slash-command

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: /stuck slash command |
| 分类 | Skills → 自动化 |
| 文件路径 | `system-prompts/skill-stuck-slash-command.md` |
| CC 版本 | 2.1.77 |
| 模板变量 | 无 |

## 原文（摘要）

中等长度文件（58 行），完整收录关键内容：

> # /stuck — diagnose frozen/slow Claude Code sessions
>
> The user thinks another Claude Code session on this machine is frozen, stuck, or very slow. Investigate and post a report to #claude-code-feedback.

### 检查指标

> - **High CPU (≥90%) sustained** — likely an infinite loop.
> - **Process state `D` (uninterruptible sleep)** — often an I/O hang.
> - **Process state `T` (stopped)** — user probably hit Ctrl+Z by accident.
> - **Process state `Z` (zombie)** — parent isn't reaping.
> - **Very high RSS (≥4GB)** — possible memory leak.
> - **Stuck child process** — a hung `git`, `node`, or shell subprocess can freeze the parent.

### 调查步骤

> 1. **List all Claude Code processes** (macOS/Linux):
>    `ps -axo pid=,pcpu=,rss=,etime=,state=,comm=,command= | grep -E '(claude|cli)' | grep -v grep`
> 2. **For anything suspicious**, gather more context (child processes, CPU sample, debug logs)
> 3. **Consider a stack dump** for a truly frozen process

### 报告

> **Only post to Slack if you actually found something stuck.** If every session looks healthy, tell the user that directly.
>
> **Use a two-message structure:**
> 1. **Top-level message** — one short line: hostname, Claude Code version, terse symptom
> 2. **Thread reply** — full diagnostic dump with PID, CPU%, RSS, state, diagnosis, debug log

### 注意事项

> Don't kill or signal any processes — this is diagnostic only.

## 中文翻译

# /stuck — 诊断冻结/缓慢的 Claude Code 会话

用户认为本机上的另一个 Claude Code 会话冻结、卡住或非常慢。调查并向 #claude-code-feedback 发布报告。

### 检查内容

扫描其他 Claude Code 进程（排除当前进程）。进程名通常为 `claude`（已安装版本）或 `cli`（原生开发构建）。

卡住会话的迹象：

- **持续高 CPU（≥90%）** — 可能是无限循环。采样两次，间隔 1-2 秒，确认不是瞬态峰值。
- **进程状态 `D`（不可中断睡眠）** — 通常是 I/O 挂起。
- **进程状态 `T`（已停止）** — 用户可能不小心按了 Ctrl+Z。
- **进程状态 `Z`（僵尸）** — 父进程未回收。
- **非常高的 RSS（≥4GB）** — 可能的内存泄漏导致会话缓慢。
- **卡住的子进程** — 挂起的 `git`、`node` 或 shell 子进程可能冻结父进程。检查 `pgrep -lP <pid>`。

### 调查步骤

1. **列出所有 Claude Code 进程**（macOS/Linux）：
   ```
   ps -axo pid=,pcpu=,rss=,etime=,state=,comm=,command= | grep -E '(claude|cli)' | grep -v grep
   ```
   过滤 `comm` 为 `claude` 或（`cli` 且命令路径包含 "claude"）的行。

2. **对可疑进程**，收集更多上下文：
   - 子进程：`pgrep -lP <pid>`
   - 如果高 CPU：1-2 秒后再次采样确认持续性
   - 如果子进程看起来挂起，用 `ps -p <child_pid> -o command=` 记录完整命令行
   - 检查会话的调试日志：`~/.claude/debug/<session-id>.txt`

3. **考虑栈转储**（高级，可选）：
   - macOS：`sample <pid> 3` 提供 3 秒原生栈采样

### 报告

**只在确实发现卡住的会话时才发布到 Slack。** 如果每个会话看起来都健康，直接告诉用户——不要向频道发布"一切正常"。

如果确实发现了卡住/慢的会话，使用 Slack MCP 工具发布到 **#claude-code-feedback**（频道 ID：`C07VBSHV7EV`）。

**使用两条消息结构** 保持频道可扫描：

1. **顶层消息** — 一行简短信息：主机名、Claude Code 版本和简洁的症状描述
2. **线程回复** — 完整诊断转储。将顶层消息的 `ts` 作为 `thread_ts` 传递。包括：PID、CPU%、RSS、状态、运行时间、命令行、子进程、诊断结论、相关调试日志尾部

如果 Slack MCP 不可用，将报告格式化为用户可复制粘贴到 #claude-code-feedback 的消息。

### 注意事项

- 不要杀死或发信号给任何进程——这仅是诊断性的。
- 如果用户给出了参数（如特定 PID 或症状），优先关注那里。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 仅诊断约束 | "Don't kill or signal any processes — this is diagnostic only" | 关键的安全约束，防止 LLM 在诊断时采取破坏性操作 |
| 2 | 量化阈值 | "≥90% CPU"、"≥4GB RSS"、进程状态字母编码 | 提供精确数字阈值而非模糊的"高/低"，让 LLM 的判断有明确标准 |
| 3 | 条件报告 | "Only post to Slack if you actually found something stuck" | 防止 LLM 发送无意义的"一切正常"报告占用团队注意力 |
| 4 | 两层消息结构 | 顶层简洁摘要 + 线程详细转储 | 优化信息密度：快速扫描者看摘要，深入调查者看线程 |
| 5 | 双次采样确认 | "Sample twice, 1-2s apart, to confirm it's not a transient spike" | 防止因瞬态 CPU 峰值导致误判，是诊断最佳实践 |
| 6 | 精确的 ps 命令 | 完整的 `ps -axo` 格式化字符串和过滤链 | 提供可直接执行的命令，避免 LLM 猜测正确的 ps 参数组合 |
