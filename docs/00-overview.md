# 00 — Claude Code 系统提示词仓库总览

> 本文档面向提示词工程师与 AI 研究人员，系统介绍 `propress/fork-claude-code-system-prompts` 仓库的背景、架构、文件组织、版本演进以及运行时机制。

---

## 目录

1. [仓库背景](#1-仓库背景)
2. [架构图](#2-架构图)
3. [文件分类统计](#3-文件分类统计)
4. [版本演进时间线](#4-版本演进时间线)
5. [文件命名规范详解](#5-文件命名规范详解)
6. [运行时提示词组装机制](#6-运行时提示词组装机制)
7. [关键术语表](#7-关键术语表)

---

## 1. 仓库背景

### Claude Code 是什么

[Claude Code](https://github.com/anthropics/claude-code) 是 Anthropic 推出的 **AI 代理式编程 CLI 工具**，通过 npm 包 `@anthropic-ai/claude-code` 分发。它将 Claude 大语言模型与终端环境深度集成，支持：

- 自然语言驱动的代码编写、重构与调试
- 多智能体协作（子智能体编排、任务并行化）
- 计划模式（Plan Mode）：先制定方案再执行
- Hook 系统：在工具调用前后插入自定义逻辑
- 技能（Skills）系统：按需加载专项指令套件
- 记忆（Memory）系统：跨会话持久化上下文

Claude Code **不开放源码**，官方 GitHub 仓库仅托管 Issues 和 Releases。

### 本仓库的意义

`propress/fork-claude-code-system-prompts`（上游：`Piebald-AI/claude-code-system-prompts`）是一个**逆向工程提取项目**。维护者通过脚本从 Claude Code npm 包的**编译后 JavaScript 源码**中提取系统提示词，以 Markdown 文件形式存档，供以下用途：

- **研究参考**：了解 Claude Code 使用哪些提示词及其版本变化
- **本地定制**：配合 [tweakcc](https://github.com/Piebald-AI/tweakcc) 工具修改本地 Claude Code 安装的提示词片段
- **功能溯源**：对照 CHANGELOG，追踪每个版本引入或移除的行为规则

> ⚠️ **重要说明**：修改本仓库中的文件**不会**改变 Claude Code 的实际行为。这些文件是提取出的参考材料，不是可修改的源码。

### 版本覆盖范围

本仓库当前文档追踪范围：**v2.1.32 — v2.1.92**（共收录 **252 个文件**）。

---

## 2. 架构图

下图展示 Claude Code 在运行时如何将各类提示词片段组装为完整上下文，发送给 Claude 模型：

```
┌─────────────────────────────────────────────────────────────────┐
│                    Claude Code 运行时                             │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │               System Prompt（系统提示词）                  │   │
│  │                                                            │   │
│  │  ┌─────────────────┐  ┌─────────────────────────────┐   │   │
│  │  │ 核心行为规则片段  │  │      工具描述（Tool Desc）   │   │   │
│  │  │ system-prompt-* │  │    tool-description-*        │   │   │
│  │  │                 │  │  ┌──────────┬─────────────┐  │   │   │
│  │  │ • doing-tasks   │  │  │  Bash    │  Edit/Write │  │   │   │
│  │  │ • tool-usage    │  │  │  ReadFile│  Agent      │  │   │   │
│  │  │ • tone-style    │  │  │  Grep    │  TodoWrite  │  │   │   │
│  │  │ • fork-usage    │  │  │  ...     │  ...        │  │   │   │
│  │  │ • hooks-config  │  │  └──────────┴─────────────┘  │   │   │
│  │  └─────────────────┘  └─────────────────────────────┘   │   │
│  │                                                            │   │
│  │  ┌─────────────────────────────────────────────────────┐ │   │
│  │  │               技能包（Skills）— 按需加载             │ │   │
│  │  │  skill-*                                              │ │   │
│  │  │  • build-with-claude-api  • verify-skill             │ │   │
│  │  │  • debugging              • agent-design-patterns    │ │   │
│  │  └─────────────────────────────────────────────────────┘ │   │
│  │                                                            │   │
│  │  ┌─────────────────────────────────────────────────────┐ │   │
│  │  │           内嵌数据（Data）— 按需加载                  │ │   │
│  │  │  data-*                                               │ │   │
│  │  │  • claude-api-reference-*   • agent-sdk-reference-*  │ │   │
│  │  │  • claude-model-catalog     • tool-use-concepts       │ │   │
│  │  └─────────────────────────────────────────────────────┘ │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │         Human Turn（用户消息 + 动态注入）                  │   │
│  │                                                            │   │
│  │  ┌───────────────────────┐  ┌──────────────────────────┐ │   │
│  │  │  系统提醒（Reminders） │  │  记忆文件内容（Memory）  │ │   │
│  │  │  system-reminder-*    │  │  动态读取并注入           │ │   │
│  │  │  • plan-mode-active   │  └──────────────────────────┘ │   │
│  │  │  • file-modified      │                                │   │
│  │  │  • hook-blocking      │  ┌──────────────────────────┐ │   │
│  │  │  • token-usage        │  │  用户消息                  │ │   │
│  │  └───────────────────────┘  └──────────────────────────┘ │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │        子智能体调用（Agent Prompts）                       │   │
│  │  agent-prompt-*                                            │   │
│  │  当 Claude 使用 Task/Agent 工具时，                        │   │
│  │  对应智能体的系统提示词被注入到子调用中                     │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   Claude 模型    │
                    │  (claude-opus-*  │
                    │  claude-sonnet-*)│
                    └─────────────────┘
```

**关键设计原则**：

- **原子化**：自 v2.1.53 起，大型整体提示词被拆分为数十个独立可寻址的小文件（如 Bash 工具描述被拆分为 45 个文件），支持精细化控制与独立更新。
- **条件注入**：许多片段包含模板变量（如 `${BASH_TOOL_NAME}`），在运行时由 Claude Code 动态插值；部分片段仅在特定功能标志启用时才会注入。
- **按需加载**：技能包（Skills）和内嵌数据（Data）不常驻系统提示词，而是由特定触发条件（如调用 Skill 工具）动态加载。

---

## 3. 文件分类统计

| 分类 | 文件前缀 | 文件数量 | 占比 |
|------|----------|----------|------|
| 工具描述 | `tool-description-*` | 73 | 29.0% |
| 系统提示词 | `system-prompt-*` | 67 | 26.6% |
| 系统提醒 | `system-reminder-*` | 37 | 14.7% |
| 内嵌数据 | `data-*` | 27 | 10.7% |
| 智能体提示词 | `agent-prompt-*` | 32 | 12.7% |
| 技能包 | `skill-*` | 15 | 6.0% |
| 工具参数描述 | `tool-parameter-*` | 1 | 0.4% |
| **合计** | | **252** | **100%** |

### 工具描述细分

工具描述文件数量最多（73 个），其中 Bash 工具系列独占约 45 个，涵盖沙箱策略、睡眠命令、Git 操作等细粒度规则：

| Bash 子分类 | 示例文件 | 数量（约）|
|-------------|----------|-----------|
| 沙箱策略 | `tool-description-bash-sandbox-*` | 17 |
| 睡眠命令规则 | `tool-description-bash-sleep-*` | 4 |
| Git 操作规则 | `tool-description-bash-git-*` | 4 |
| 备选工具指引 | `tool-description-bash-alternative-*` | 6 |
| 其他 Bash 规则 | `tool-description-bash-*` | ~14 |

---

## 4. 版本演进时间线

以下时间线记录了 v2.1.32 至 v2.1.92 版本中的重要里程碑，提交哈希链接指向 fork 仓库。

### 早期奠基期（v2.1.32 — v2.1.50）

| 版本 | 提交 | 关键变化 |
|------|------|----------|
| [v2.1.32](https://github.com/propress/fork-claude-code-system-prompts/commit/a362f28) | `a362f28` | 新增近期消息摘要智能体、技能化当前会话提示词 |
| [v2.1.33](https://github.com/propress/fork-claude-code-system-prompts/commit/38ebc6b) | `38ebc6b` | 新增 TeamDelete 工具描述，重构计划模式提醒 |
| [v2.1.38](https://github.com/propress/fork-claude-code-system-prompts/commit/30adcee) | `30adcee` | 新增上下文压缩摘要提示词 |
| [v2.1.39](https://github.com/propress/fork-claude-code-system-prompts/commit/11e9ec6) | `11e9ec6` | 新增技能演化智能体提示词 |
| [v2.1.41](https://github.com/propress/fork-claude-code-system-prompts/commit/91732e4) | `91732e4` | 新增探索子智能体条件委托系统提示词 |
| [v2.1.45](https://github.com/propress/fork-claude-code-system-prompts/commit/36d2856) | `36d2856` | 新增选项预览（Option Previewer）系统提示词 |
| [v2.1.47](https://github.com/propress/fork-claude-code-system-prompts/commit/f58cba9) | `f58cba9` | **重大更新**：新增 27 个内嵌数据文件（Agent SDK、Claude API 多语言参考、模型目录等）；总 token 数 +34,752 |
| [v2.1.48](https://github.com/propress/fork-claude-code-system-prompts/commit/0d57836) | `0d57836` | 新增 EnterWorktree 工具描述，移除 MCP CLI 提示词 |
| [v2.1.50](https://github.com/propress/fork-claude-code-system-prompts/commit/5fa66df) | `5fa66df` | EnterWorktree 支持非 Git 仓库，Task 工具新增 worktree 隔离选项 |

### 原子化重构期（v2.1.51 — v2.1.66）

| 版本 | 提交 | 关键变化 |
|------|------|----------|
| [v2.1.51](https://github.com/propress/fork-claude-code-system-prompts/commit/1988a63) | `1988a63` | 新增快速 PR 创建与 Git 提交智能体提示词；数据文件扩充（TypeScript SDK 参考） |
| [v2.1.53](https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2) | `f7330d2` | **里程碑**：6 个整体系统提示词与 2 个工具描述被拆分为约 70 个原子化文件；Bash 工具描述独立为 45 个子文件 |
| [v2.1.59](https://github.com/propress/fork-claude-code-system-prompts/commit/6147099) | `6147099` | 多处内部优化 |
| [v2.1.63](https://github.com/propress/fork-claude-code-system-prompts/commit/7e37a33) | `7e37a33` | 各类系统提示词细化 |
| [v2.1.64](https://github.com/propress/fork-claude-code-system-prompts/commit/ac581b8) | `ac581b8` | 安全与行为规则更新 |
| [v2.1.66](https://github.com/propress/fork-claude-code-system-prompts/commit/c55bb75) | `c55bb75` | 精简部分提示词，移除验证专家子智能体（后于 v2.1.69 重新引入） |

### 多智能体架构成熟期（v2.1.69 — v2.1.79）

| 版本 | 提交 | 关键变化 |
|------|------|----------|
| [v2.1.69](https://github.com/propress/fork-claude-code-system-prompts/commit/2fde688) | `2fde688` | 重新引入验证专家智能体；新增智能体线程备注系统提示词；引入探索智能体优势与指引 |
| [v2.1.70](https://github.com/propress/fork-claude-code-system-prompts/commit/186e12a) | `186e12a` | **新增 Fork 子智能体系统**：引入 Fork 使用指引、子智能体委托示例、编写子智能体提示词规范、工作进程提示词 |
| [v2.1.71](https://github.com/propress/fork-claude-code-system-prompts/commit/10a9b4f) | `10a9b4f` | **新增安全监控系统**：两部分自主操作安全监控智能体提示词；新增循环任务技能（/loop 斜杠命令）；CronCreate 工具描述 |
| [v2.1.72](https://github.com/propress/fork-claude-code-system-prompts/commit/7a45418) | `7a45418` | **新增自动模式（Auto Mode）**；引入 ExitWorktree 工具；ToolSearch 重构 |
| [v2.1.73](https://github.com/propress/fork-claude-code-system-prompts/commit/c02a840) | `c02a840` | **API 参考大扩充**：各语言 Claude API 参考全面更新（C#、Go、Java、PHP、Python、TypeScript、cURL）；新增 SendUserMessage 系统提示词 |
| [v2.1.74](https://github.com/propress/fork-claude-code-system-prompts/commit/93acf03) | `93acf03` | 新增编程会话标题生成器智能体；新增 /stuck 诊断技能 |
| [v2.1.75](https://github.com/propress/fork-claude-code-system-prompts/commit/97ce0c2) | `97ce0c2` | 新增记忆文件附加决策智能体（确定为用户查询附加哪些记忆文件） |
| [v2.1.76](https://github.com/propress/fork-claude-code-system-prompts/commit/6cc7a81) | `6cc7a81` | 新增 PostCompact Hook 事件支持 |
| [v2.1.77](https://github.com/propress/fork-claude-code-system-prompts/commit/87fae2a) | `87fae2a` | 新增 CLAUDE.md 初始化技能；新增 7 步 Hook 验证流程技能 |
| [v2.1.78](https://github.com/propress/fork-claude-code-system-prompts/commit/9f2320d) | `9f2320d` | 新增记忆整合（Dream Memory Consolidation）智能体 |
| [v2.1.79](https://github.com/propress/fork-claude-code-system-prompts/commit/7f0098b) | `7f0098b` | 新增 Claude 模型目录的 Models API 发现功能 |

### 功能扩展期（v2.1.80 — v2.1.92）

| 版本 | 提交 | 关键变化 |
|------|------|----------|
| [v2.1.80](https://github.com/propress/fork-claude-code-system-prompts/commit/abbb61f) | `abbb61f` | 新增远程调度（/schedule 斜杠命令）智能体提示词；Status Line 新增限流信息 |
| [v2.1.81](https://github.com/propress/fork-claude-code-system-prompts/commit/a82ade6) | `a82ade6` | 新增自动模式规则审核智能体；新增最小模式（Minimal Mode）系统提示词 |
| [v2.1.83](https://github.com/propress/fork-claude-code-system-prompts/commit/a9eee87) | `a9eee87` | **重大扩充**（+5,960 token）：新增 Prompt Caching 设计优化数据文件；新增 Advisor 工具指令；引入 Ultraplan 模式；全新 Verify 技能体系（含 CLI/API 验证示例） |
| [v2.1.84](https://github.com/propress/fork-claude-code-system-prompts/commit/a3c16f4) | `a3c16f4` | **新增 PowerShell 支持**：PowerShell 工具描述与避免 Sleep 命令规则；新增通用目的子智能体；引入 request_teach_access 工具 |
| [v2.1.85](https://github.com/propress/fork-claude-code-system-prompts/commit/6368c71) | `6368c71` | 安全监控新增「生产环境读取」阻断规则 |
| [v2.1.86](https://github.com/propress/fork-claude-code-system-prompts/commit/f7141ee) | `f7141ee` | 精简多处提示词；通用目的子智能体指令优化 |
| [v2.1.87](https://github.com/propress/fork-claude-code-system-prompts/commit/115c568) | `115c568` | 无系统提示词变更 |
| [v2.1.88](https://github.com/propress/fork-claude-code-system-prompts/commit/7d7c728) | `7d7c728` | 新增部分压缩指令；新增 PowerShell 5.1 系统提示词；新增 Config 工具描述 |
| [v2.1.89](https://github.com/propress/fork-claude-code-system-prompts/commit/0e24543) | `0e24543` | **新增 Buddy Mode（结对编程模式）**；新增 MCP 工具结果截断处理；新增 Remote Ultraplan 模式；新增 Computer Use MCP 技能 |
| [v2.1.90](https://github.com/propress/fork-claude-code-system-prompts/commit/8362366) | `8362366` | 安全监控规则双向化（用户意图既可授权也可限制） |
| [v2.1.91](https://github.com/propress/fork-claude-code-system-prompts/commit/ca9465e) | `ca9465e` | **新增智能体设计模式技能**；安全监控新增记忆投毒防护规则；扩充实时文档源数据 |
| [v2.1.92](https://github.com/propress/fork-claude-code-system-prompts/commit/0b6cc0c) | `0b6cc0c` | 专用化 Hook 条件评估器（stop 专用）；Write 工具指引优化 |

---

## 5. 文件命名规范详解

所有文件存放于 `system-prompts/` 目录，采用以下命名规范：

### 命名模式

```
{分类前缀}-{功能描述}.md
```

功能描述使用连字符分隔的小写英文单词（kebab-case）。

### 分类前缀说明

| 前缀 | 中文名称 | 说明 |
|------|----------|------|
| `agent-prompt-` | 智能体提示词 | 子智能体或功能模块的系统提示词；当 Claude 通过 Task/Agent 工具调用子智能体时注入 |
| `system-prompt-` | 系统提示词 | Claude Code 核心行为规则的原子化片段；构成主系统提示词的各个部分 |
| `system-reminder-` | 系统提醒 | 根据运行时上下文（文件状态、计划模式、Hook 事件等）动态注入对话中的提醒片段 |
| `tool-description-` | 工具描述 | 内置工具的使用说明，指导模型何时以及如何调用各工具 |
| `tool-parameter-` | 工具参数描述 | 特定工具参数的详细说明（目前仅 1 个文件：`computer` 工具的 action 参数）|
| `skill-` | 技能包 | 专项技能的提示词套件，通过 Skill 工具按需加载 |
| `data-` | 内嵌数据 | 随会话动态加载的静态参考文档（SDK 文档、API 参考等）|

### 文件内格式

每个文件的 YAML frontmatter 中注明了适用的 Claude Code 版本与模板变量：

```yaml
---
version: "2.1.92"
template_variables:
  - BASH_TOOL_NAME
  - CONDITIONAL_SANDBOX_NOTE
---
```

### 命名示例解析

| 文件名 | 分类 | 功能说明 |
|--------|------|----------|
| `agent-prompt-explore.md` | 智能体提示词 | 代码库探索子智能体的系统提示词 |
| `system-prompt-doing-tasks-security.md` | 系统提示词 | 执行任务时的安全注意事项规则 |
| `system-reminder-plan-mode-is-active-5-phase.md` | 系统提醒 | 五阶段计划模式激活时注入的提醒 |
| `tool-description-bash-sandbox-default-to-sandbox.md` | 工具描述 | Bash 工具默认沙箱策略规则 |
| `tool-description-bash-git-never-skip-hooks.md` | 工具描述 | Bash 工具 Git 操作禁止跳过 Hook 的规则 |
| `skill-verify-skill.md` | 技能包 | 代码变更验证工作流技能 |
| `data-claude-model-catalog.md` | 内嵌数据 | Claude 模型目录静态参考 |

---

## 6. 运行时提示词组装机制

Claude Code 在处理每次请求时，通过 `updatePrompts.js`（编译后的 JavaScript）动态组装系统提示词。以下是核心机制说明：

### 6.1 固定注入部分（System Prompt）

以下类型的提示词片段**始终**包含在系统提示词中：

1. **核心行为规则**（`system-prompt-doing-tasks-*`）：软件工程规范、安全规则、输出风格等
2. **工具使用策略**（`system-prompt-tool-usage-*`）：何时使用哪种工具的决策规则
3. **工具描述**（`tool-description-*`）：当前会话已启用工具的描述（未启用的工具描述不会注入）

### 6.2 条件注入部分

以下片段根据运行时条件有条件地注入：

| 条件 | 注入内容 |
|------|----------|
| 启用 Agent 功能 | `agent-prompt-*`（对应子智能体类型）|
| 计划模式激活 | `system-reminder-plan-mode-is-active-*` |
| 文件被修改 | `system-reminder-file-modified-by-user-or-linter` |
| Hook 触发 | `system-reminder-hook-*` |
| 记忆文件加载 | `system-reminder-memory-file-contents` |
| 技能被调用 | `skill-*`（对应技能名称）|
| 数据被请求 | `data-*`（对应技能/工具触发）|
| 沙箱模式 | `tool-description-bash-sandbox-*` |
| PowerShell 环境 | `tool-description-powershell`, `system-prompt-powershell-edition-for-51` |

### 6.3 模板变量插值

提示词文件中的 `${VARIABLE_NAME}` 模板变量在运行时被替换为实际值。常见变量包括：

| 变量 | 说明 |
|------|------|
| `${BASH_TOOL_NAME}` | Bash 工具的实际名称 |
| `${PLAN_MODE_TOOL_NAME}` | 计划模式工具名称 |
| `${EXPLORE_AGENT}` | 探索子智能体标识符 |
| `${CURRENT_MONTH_YEAR}` | 当前月份和年份（用于网络搜索日期感知）|
| `${CONDITIONAL_SANDBOX_NOTE}` | 沙箱相关条件内容块 |
| `${ATTRIBUTION_TEXT}` | Git 提交的署名文本 |

> 注意：模板变量以**字面字符串**形式存储于本仓库文件中，不会被展开。

### 6.4 上下文压缩（Compaction）

当对话 token 数接近上限时，Claude Code 会触发上下文压缩，注入 `system-prompt-context-compaction-summary` 或 `system-prompt-partial-compaction-instructions`，指导模型生成结构化摘要以替换旧消息。

---

## 7. 关键术语表

| 英文术语 | 中文译名 | 说明 |
|----------|----------|------|
| System Prompt | 系统提示词 | 注入对话系统角色的指令，定义模型行为 |
| Agent Prompt | 智能体提示词 | 子智能体的系统提示词，在 Task/Agent 工具调用时注入 |
| System Reminder | 系统提醒 | 动态注入对话中的上下文提醒片段 |
| Tool Description | 工具描述 | 指导模型使用内置工具的说明文本 |
| Skill | 技能（包）| 按需加载的专项指令套件，通过 `/skill:名称` 触发 |
| Fork | 派生子智能体 | 继承父智能体上下文与缓存的子进程，用于并行任务 |
| Subagent | 子智能体 | 通过 Task/Agent 工具启动的自主子进程 |
| Plan Mode | 计划模式 | 先制定执行计划、经用户确认后再执行的工作模式 |
| Ultraplan | 超级计划模式 | 多子智能体协作探索代码库后生成详细实施计划的增强计划模式 |
| Hook | 钩子 | 在工具调用前后执行用户自定义逻辑的机制 |
| Worktree | 工作树 | 基于 Git Worktree 的隔离执行环境 |
| Auto Mode | 自动模式 | 持续执行任务的后台代理模式 |
| Buddy Mode | 伙伴模式 | 在终端中实时评论开发者工作的结对编程模式 |
| Minimal Mode | 最小模式 | 跳过 Hook、LSP、记忆等功能的精简运行模式 |
| Compaction | 上下文压缩 | 对话 token 接近上限时压缩历史消息的机制 |
| Memory | 记忆 | 跨会话持久化的上下文信息（用户反馈、项目事实等）|
| Dream Memory | 记忆整合 | 定期执行的多阶段记忆整理与索引更新过程 |
| CLAUDE.md | CLAUDE 配置文件 | 项目级或用户级 Claude Code 自定义配置文件 |
| tweakcc | 提示词定制工具 | Piebald AI 开发的本地 Claude Code 提示词定制工具 |
| Template Variable | 模板变量 | 提示词文件中以 `${NAME}` 形式存在的运行时插值占位符 |
| Atomic Prompt | 原子化提示词 | v2.1.53 后将大型提示词拆分为独立可寻址小文件的设计 |
| Tool Runner | 工具执行器 | SDK 提供的工具自动执行循环封装 |
| Prompt Caching | 提示词缓存 | Anthropic API 的前缀缓存机制，降低重复调用成本 |
| Context Editing | 上下文编辑 | 从对话记录中修剪过时工具结果的功能（beta）|
| MCP | 模型上下文协议 | Model Context Protocol，连接外部工具/数据源的协议 |
| PostCompact | 压缩后钩子 | 上下文压缩完成后触发的 Hook 事件 |

---

> 本文档维护于 [propress/fork-claude-code-system-prompts](https://github.com/propress/fork-claude-code-system-prompts)，基于上游 [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) Fork 整理。
