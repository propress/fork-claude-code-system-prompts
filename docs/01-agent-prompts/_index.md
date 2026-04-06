# Agent Prompts 索引

> 本目录收录了 Claude Code 中全部 **32 个 Agent Prompt**（代理提示词）的中文文档。
> Agent Prompt 是 Claude Code 分配给各个子代理（subagent）的系统提示词，每个子代理执行一项专门任务。

| 统计 | 值 |
|------|-----|
| 源文件总数 | 32 |
| 文档文件总数 | 33（其中 determine-memory-files 有两个文档版本） |
| 源目录 | `system-prompts/agent-prompt-*.md` |
| 最新 CC 版本 | 2.1.92 |

---

## 📂 按类别索引

### 🔧 核心子代理（Core Subagents）

用于探索代码库、执行通用任务和并行工作的基础子代理。

| 文档 | 源文件 | 简述 |
|------|--------|------|
| [explore](explore.md) | `agent-prompt-explore.md` | 探索子代理，专门用于快速搜索和理解代码库 |
| [general-purpose](general-purpose.md) | `agent-prompt-general-purpose.md` | 通用子代理，拥有完整工具集，用于复杂多步骤任务 |
| [worker-fork-execution](worker-fork-execution.md) | `agent-prompt-worker-fork-execution.md` | Worker fork 执行代理，用于并行任务执行 |

### 💬 会话管理（Session Management）

处理会话标题、搜索、摘要和对话压缩的代理。

| 文档 | 源文件 | 简述 |
|------|--------|------|
| [session-search-assistant](session-search-assistant.md) | `agent-prompt-session-search-assistant.md` | 会话搜索助手，根据用户查询查找相关会话 |
| [session-title-and-branch](session-title-and-branch.md) | `agent-prompt-session-title-and-branch-generation.md` | 会话标题与分支生成，为编码会话生成简洁标题和 git 分支名 |
| [coding-session-title-generator](coding-session-title-generator.md) | `agent-prompt-coding-session-title-generator.md` | 编码会话标题生成器（早期版本） |
| [conversation-summarization](conversation-summarization.md) | `agent-prompt-conversation-summarization.md` | 对话摘要代理，压缩长对话以节省上下文窗口 |
| [recent-message-summarization](recent-message-summarization.md) | `agent-prompt-recent-message-summarization.md` | 近期消息摘要代理，摘要最近的对话消息 |

### 🧠 记忆与上下文（Memory & Context）

管理记忆文件选择、更新和合并的代理。

| 文档 | 源文件 | 简述 |
|------|--------|------|
| [determine-memory-files](determine-memory-files.md) | `agent-prompt-determine-which-memory-files-to-attach.md` | 记忆文件筛选代理（简称版文档） |
| [determine-which-memory-files-to-attach](determine-which-memory-files-to-attach.md) | `agent-prompt-determine-which-memory-files-to-attach.md` | 记忆文件筛选代理（完整名称版文档，含详细技巧分析） |
| [session-memory-update](session-memory-update.md) | `agent-prompt-session-memory-update-instructions.md` | 会话记忆更新指令，管理会话结束时的记忆持久化 |
| [dream-memory-consolidation](dream-memory-consolidation.md) | `agent-prompt-dream-memory-consolidation.md` | 梦境记忆合并代理，离线合并和整理记忆文件 |

### 🔀 Git 与代码操作（Git & Code Operations）

处理 git 提交、PR 创建和代码审查的代理。

| 文档 | 源文件 | 简述 |
|------|--------|------|
| [quick-git-commit](quick-git-commit.md) | `agent-prompt-quick-git-commit.md` | 快速 git 提交代理，自动生成 commit message 并提交 |
| [quick-pr-creation](quick-pr-creation.md) | `agent-prompt-quick-pr-creation.md` | 快速 PR 创建代理，自动生成 pull request |
| [review-pr-slash-command](review-pr-slash-command.md) | `agent-prompt-review-pr-slash-command.md` | `/review` 斜杠命令代理，审查 pull request |
| [batch-slash-command](batch-slash-command.md) | `agent-prompt-batch-slash-command.md` | `/batch` 斜杠命令代理，批量处理多个任务 |

### 🔒 安全（Security）

安全监控、自主操作审查和安全审计代理。

| 文档 | 源文件 | 简述 |
|------|--------|------|
| [security-monitor-first-part](security-monitor-first-part.md) | `agent-prompt-security-monitor-for-autonomous-agent-actions-first-part.md` | 自主代理操作安全监控（第一部分）：BLOCK/ALLOW 规则和用户意图分析 |
| [security-monitor-second-part](security-monitor-second-part.md) | `agent-prompt-security-monitor-for-autonomous-agent-actions-second-part.md` | 自主代理操作安全监控（第二部分）：具体的安全规则和判定逻辑 |
| [security-review-slash-command](security-review-slash-command.md) | `agent-prompt-security-review-slash-command.md` | `/security-review` 斜杠命令代理，执行代码安全审查 |
| [auto-mode-rule-reviewer](auto-mode-rule-reviewer.md) | `agent-prompt-auto-mode-rule-reviewer.md` | 自动模式规则审查代理，审查和验证自动执行规则 |

### ⚙️ 配置与设置（Configuration & Setup）

状态栏配置、CLAUDE.md 创建和 Hook 管理代理。

| 文档 | 源文件 | 简述 |
|------|--------|------|
| [status-line-setup](status-line-setup.md) | `agent-prompt-status-line-setup.md` | 状态栏设置代理，配置 Claude Code 终端状态栏显示 |
| [claudemd-creation](claudemd-creation.md) | `agent-prompt-claudemd-creation.md` | CLAUDE.md 创建代理，生成项目配置文件 |
| [agent-creation-architect](agent-creation-architect.md) | `agent-prompt-agent-creation-architect.md` | 代理创建架构师，设计和创建自定义代理 |
| [agent-hook](agent-hook.md) | `agent-prompt-agent-hook.md` | 代理 Hook 管理，处理代理生命周期钩子 |
| [hook-condition-evaluator-stop](hook-condition-evaluator-stop.md) | `agent-prompt-hook-condition-evaluator-stop.md` | Hook 条件评估器（停止），评估 Hook 是否应阻止操作 |
| [schedule-slash-command](schedule-slash-command.md) | `agent-prompt-schedule-slash-command.md` | `/schedule` 斜杠命令代理，管理定时任务调度 |

### 📄 界面与内容（UI & Content）

处理网页内容摘要、提示建议和用户引导的代理。

| 文档 | 源文件 | 简述 |
|------|--------|------|
| [webfetch-summarizer](webfetch-summarizer.md) | `agent-prompt-webfetch-summarizer.md` | WebFetch 摘要代理，将网页内容精炼后返回给主模型 |
| [prompt-suggestion-generator-v2](prompt-suggestion-generator-v2.md) | `agent-prompt-prompt-suggestion-generator-v2.md` | 提示建议生成器 v2，为用户生成后续操作建议 |
| [claude-guide-agent](claude-guide-agent.md) | `agent-prompt-claude-guide-agent.md` | Claude 使用指南代理，帮助用户了解 Claude Code 功能 |

### 📋 规划与验证（Planning & Verification）

任务规划和结果验证代理。

| 文档 | 源文件 | 简述 |
|------|--------|------|
| [plan-mode-enhanced](plan-mode-enhanced.md) | `agent-prompt-plan-mode-enhanced.md` | 增强计划模式代理，执行深度任务分析和规划 |
| [verification-specialist](verification-specialist.md) | `agent-prompt-verification-specialist.md` | 验证专家代理，验证任务完成质量和正确性 |

### 🖥️ Bash 与工具（Bash & Tools）

Bash 命令分析和处理相关代理。

| 文档 | 源文件 | 简述 |
|------|--------|------|
| [bash-command-description-writer](bash-command-description-writer.md) | `agent-prompt-bash-command-description-writer.md` | Bash 命令描述生成器，为 bash 命令生成人类可读描述 |
| [bash-command-prefix-detection](bash-command-prefix-detection.md) | `agent-prompt-bash-command-prefix-detection.md` | Bash 命令前缀检测器，识别命令中的环境变量前缀 |

---

## 📊 按首次出现版本排序

| 版本 | 新增的 Agent Prompt |
|------|-------------------|
| 2.0.14 | explore, general-purpose, agent-creation-architect, claudemd-creation, conversation-summarization, coding-session-title-generator, review-pr-slash-command, security-review-slash-command, status-line-setup, webfetch-summarizer, bash-command-prefix-detection |
| 2.1.32 | recent-message-summarization |
| 2.1.39 | session-title-and-branch（替代 session title generation）, claude-guide-agent |
| 2.1.42 | prompt-suggestion-generator-v2 |
| 2.1.47 | quick-git-commit |
| 2.1.50 | worker-fork-execution |
| 2.1.51 | quick-pr-creation |
| 2.1.53 | plan-mode-enhanced |
| 2.1.59 | batch-slash-command |
| 2.1.63 | verification-specialist |
| 2.1.64 | bash-command-description-writer |
| 2.1.66 | session-memory-update |
| 2.1.70 | agent-hook |
| 2.1.71 | hook-condition-evaluator-stop |
| 2.1.72 | security-monitor-first-part, security-monitor-second-part |
| 2.1.73 | session-search-assistant |
| 2.1.74 | auto-mode-rule-reviewer |
| 2.1.80 | schedule-slash-command |
| 2.1.83 | determine-which-memory-files-to-attach（替代 Memory selection） |
| 2.1.85 | dream-memory-consolidation |

---

## 📁 完整文件对照表

| # | 文档文件名 | 源文件名 |
|---|-----------|---------|
| 1 | agent-creation-architect.md | agent-prompt-agent-creation-architect.md |
| 2 | agent-hook.md | agent-prompt-agent-hook.md |
| 3 | auto-mode-rule-reviewer.md | agent-prompt-auto-mode-rule-reviewer.md |
| 4 | bash-command-description-writer.md | agent-prompt-bash-command-description-writer.md |
| 5 | bash-command-prefix-detection.md | agent-prompt-bash-command-prefix-detection.md |
| 6 | batch-slash-command.md | agent-prompt-batch-slash-command.md |
| 7 | claude-guide-agent.md | agent-prompt-claude-guide-agent.md |
| 8 | claudemd-creation.md | agent-prompt-claudemd-creation.md |
| 9 | coding-session-title-generator.md | agent-prompt-coding-session-title-generator.md |
| 10 | conversation-summarization.md | agent-prompt-conversation-summarization.md |
| 11 | determine-memory-files.md | agent-prompt-determine-which-memory-files-to-attach.md |
| 12 | determine-which-memory-files-to-attach.md | agent-prompt-determine-which-memory-files-to-attach.md |
| 13 | dream-memory-consolidation.md | agent-prompt-dream-memory-consolidation.md |
| 14 | explore.md | agent-prompt-explore.md |
| 15 | general-purpose.md | agent-prompt-general-purpose.md |
| 16 | hook-condition-evaluator-stop.md | agent-prompt-hook-condition-evaluator-stop.md |
| 17 | plan-mode-enhanced.md | agent-prompt-plan-mode-enhanced.md |
| 18 | prompt-suggestion-generator-v2.md | agent-prompt-prompt-suggestion-generator-v2.md |
| 19 | quick-git-commit.md | agent-prompt-quick-git-commit.md |
| 20 | quick-pr-creation.md | agent-prompt-quick-pr-creation.md |
| 21 | recent-message-summarization.md | agent-prompt-recent-message-summarization.md |
| 22 | review-pr-slash-command.md | agent-prompt-review-pr-slash-command.md |
| 23 | schedule-slash-command.md | agent-prompt-schedule-slash-command.md |
| 24 | security-monitor-first-part.md | agent-prompt-security-monitor-for-autonomous-agent-actions-first-part.md |
| 25 | security-monitor-second-part.md | agent-prompt-security-monitor-for-autonomous-agent-actions-second-part.md |
| 26 | security-review-slash-command.md | agent-prompt-security-review-slash-command.md |
| 27 | session-memory-update.md | agent-prompt-session-memory-update-instructions.md |
| 28 | session-search-assistant.md | agent-prompt-session-search-assistant.md |
| 29 | session-title-and-branch.md | agent-prompt-session-title-and-branch-generation.md |
| 30 | status-line-setup.md | agent-prompt-status-line-setup.md |
| 31 | verification-specialist.md | agent-prompt-verification-specialist.md |
| 32 | webfetch-summarizer.md | agent-prompt-webfetch-summarizer.md |
| 33 | worker-fork-execution.md | agent-prompt-worker-fork-execution.md |
