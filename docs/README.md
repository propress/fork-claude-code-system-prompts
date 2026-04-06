# Claude Code 系统提示词文档导航

> 本文档是 [propress/fork-claude-code-system-prompts](https://github.com/propress/fork-claude-code-system-prompts) 的中文技术文档中心，面向提示词工程师、AI 研究人员以及希望深入了解 Claude Code 行为机制的开发者。

---

## 文档目录

```
docs/
├── README.md                # 本文件：文档导航总览
├── 00-overview.md           # 仓库概述：架构、版本演进、术语表
├── 01-agent-prompts/        # 智能体提示词详解
├── 02-system-prompts/       # 系统提示词详解
├── 03-tool-descriptions/    # 工具描述详解
│   └── bash/                # Bash 工具系列
├── 04-skills/               # 技能包详解
├── 05-system-reminders/     # 系统提醒详解
├── 06-data/                 # 内嵌参考数据详解
├── 07-techniques-summary.md # 提示词技巧汇总
├── 08-design-philosophy.md  # 设计哲学分析
├── 09-version-evolution.md  # 版本演进分析
└── 10-reusable-patterns.md  # 可复用模式
```

---

## 章节索引

| 章节 | 文件数量 | 说明 |
|------|----------|------|
| [00 — 总体概述](./00-overview.md) | — | 架构图、版本时间线、术语表 |
| [01 — 智能体提示词](./01-agent-prompts/) | 32 个 | 子智能体与功能模块的指令集 |
| [02 — 系统提示词](./02-system-prompts/) | 67 个 | Claude Code 核心行为规则片段 |
| [03 — 工具描述](./03-tool-descriptions/) | 73 个 | 内置工具使用说明与约束 |
| [04 — 技能包](./04-skills/) | 15 个 | 专项技能的提示词套件 |
| [05 — 系统提醒](./05-system-reminders/) | 37 个 | 运行时动态注入的上下文提醒 |
| [06 — 内嵌数据](./06-data/) | 27 个 | SDK 参考、API 文档等静态数据 |
| [07 — 提示词技巧汇总](./07-techniques-summary.md) | — | 技巧分类体系、频次排行、组合模式 |
| [08 — 设计哲学分析](./08-design-philosophy.md) | — | 核心设计原则、安全哲学、协作哲学 |
| [09 — 版本演进分析](./09-version-evolution.md) | — | 46 个版本的演进轨迹与趋势 |
| [10 — 可复用模式](./10-reusable-patterns.md) | — | 15 个可直接复用的提示词工程模式 |

---

## 分类速查表

### 智能体提示词（Agent Prompts）`agent-prompt-*`

负责驱动 Claude Code 内部各类子智能体行为，包括代码探索、安全审核、内存管理等模块。

| 文件前缀 | 功能 |
|----------|------|
| `agent-prompt-explore` | 代码库探索子智能体 |
| `agent-prompt-general-purpose` | 通用任务子智能体 |
| `agent-prompt-security-monitor-*` | 自主操作安全监控（两部分）|
| `agent-prompt-verification-specialist` | 代码变更验证专家 |
| `agent-prompt-conversation-summarization` | 对话摘要生成 |
| `agent-prompt-dream-memory-consolidation` | 记忆整合 |
| `agent-prompt-session-*` | 会话标题与搜索 |
| `agent-prompt-quick-*` | 快速 Git 提交 / PR 创建 |
| `agent-prompt-*-slash-command` | 各类斜杠命令 |

### 系统提示词（System Prompts）`system-prompt-*`

构成 Claude Code 核心行为规范的原子化片段，涵盖任务执行、工具使用、输出风格等。

| 主题分组 | 文件前缀示例 |
|----------|-------------|
| 任务执行规则 | `system-prompt-doing-tasks-*` |
| 工具使用策略 | `system-prompt-tool-usage-*` |
| 输出风格 | `system-prompt-tone-and-style-*` |
| 记忆与学习 | `system-prompt-agent-memory-*`, `system-prompt-learning-mode*` |
| 子智能体协作 | `system-prompt-fork-usage-guidelines`, `system-prompt-writing-subagent-prompts` |
| 安全与合规 | `system-prompt-censoring-assistance-*`, `system-prompt-executing-actions-with-care` |
| 特殊模式 | `system-prompt-auto-mode`, `system-prompt-buddy-mode`, `system-prompt-minimal-mode` |

### 工具描述（Tool Descriptions）`tool-description-*`

Claude Code 内置工具的详细描述，指导模型何时以及如何调用工具。

| 工具分组 | 文件前缀示例 |
|----------|-------------|
| Bash 工具系列（45 个） | `tool-description-bash-*` |
| 文件操作 | `tool-description-edit`, `tool-description-write`, `tool-description-readfile` |
| 搜索工具 | `tool-description-grep`, `tool-description-webfetch`, `tool-description-websearch` |
| 规划模式 | `tool-description-enterplanmode`, `tool-description-exitplanmode` |
| 多智能体工具 | `tool-description-agent-*`, `tool-description-sendmessagetool`, `tool-description-teammatetool` |
| 其他专项工具 | `tool-description-todowrite`, `tool-description-croncreate`, `tool-description-skill` |

### 技能包（Skills）`skill-*`

按需加载的专项指令套件，覆盖 API 开发、代码验证、调试等场景。

| 技能 | 文件 |
|------|------|
| Claude API 开发（参考指南）| `skill-build-with-claude-api-reference-guide` |
| Claude API 开发 | `skill-build-with-claude-api` |
| 代码验证工作流 | `skill-verify-skill` |
| 调试技能 | `skill-debugging` |
| 代码简化 | `skill-simplify` |
| 智能体设计模式 | `skill-agent-design-patterns` |
| 循环任务 | `skill-loop-slash-command` |
| 诊断卡住会话 | `skill-stuck-slash-command` |

### 系统提醒（System Reminders）`system-reminder-*`

运行时根据上下文动态注入的提醒片段，处理文件状态、计划模式、Hook 事件等。

| 分类 | 文件前缀示例 |
|------|-------------|
| 计划模式 | `system-reminder-plan-mode-*` |
| Hook 事件 | `system-reminder-hook-*` |
| 文件状态 | `system-reminder-file-*` |
| 内存内容 | `system-reminder-memory-file-contents` |
| 多智能体 | `system-reminder-team-*` |

### 内嵌数据（Data）`data-*`

随会话动态加载的静态参考文档，包含 SDK 参考、API 文档、模型目录等。

| 数据类型 | 文件前缀示例 |
|----------|-------------|
| Agent SDK 参考 | `data-agent-sdk-reference-*` |
| Agent SDK 模式示例 | `data-agent-sdk-patterns-*` |
| Claude API 参考（多语言）| `data-claude-api-reference-*` |
| Claude 模型目录 | `data-claude-model-catalog` |
| 工具使用文档 | `data-tool-use-*` |
| 其他 API 参考 | `data-files-api-*`, `data-message-batches-api-*`, `data-streaming-reference-*` |

---

## 建议阅读路径

### 🔰 初次了解 Claude Code 的读者

1. **[00 — 总体概述](./00-overview.md)** — 了解 Claude Code 是什么、本仓库的意义、文件组织方式
2. **[系统提示词](./02-system-prompts/)** — 了解 Claude Code 的核心行为规则（从 `doing-tasks-*` 系列开始）
3. **[工具描述](./03-tool-descriptions/)** — 了解 Claude Code 有哪些工具以及如何使用

### 🔬 提示词工程师

1. **[00 — 总体概述](./00-overview.md)** 中的「架构图」与「运行时组装机制」
2. **[智能体提示词](./01-agent-prompts/)** — 重点关注安全监控、验证专家等模块
3. **[系统提醒](./05-system-reminders/)** — 了解动态注入机制
4. **[技能包](./04-skills/)** — 了解按需加载的技能设计模式

### 🛠️ 希望使用 tweakcc 定制 Claude Code 的开发者

1. **[00 — 总体概述](./00-overview.md)** 中的「文件命名规范」与「运行时组装机制」
2. 找到目标行为对应的文件分类，定位具体文件
3. 使用 [tweakcc](https://github.com/Piebald-AI/tweakcc) 修改本地安装的对应片段

### 📊 追踪版本演进的研究者

1. **[00 — 总体概述](./00-overview.md)** 中的「版本演进时间线」
2. 仓库根目录的 **[CHANGELOG.md](../CHANGELOG.md)**

---

## 相关链接

- **本仓库（Fork）**：[propress/fork-claude-code-system-prompts](https://github.com/propress/fork-claude-code-system-prompts)
- **上游仓库**：[Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)
- **Claude Code 官方仓库**（仅 Issues/Releases）：[anthropics/claude-code](https://github.com/anthropics/claude-code)
- **tweakcc 定制工具**：[Piebald-AI/tweakcc](https://github.com/Piebald-AI/tweakcc)
- **Piebald AI**：[piebald.ai](https://piebald.ai/)

---

> ⚠️ **免责声明**：本仓库由 Piebald AI 维护，非 Anthropic 官方资料。提示词内容从 `@anthropic-ai/claude-code` npm 包的编译 JavaScript 源码中提取，仅供研究与参考。修改本仓库中的文件**不会**改变 Claude Code 的实际行为。
