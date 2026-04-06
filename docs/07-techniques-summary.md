# 07 — 提示词技巧汇总

> 从 Claude Code 全部 251 个提示词文件中提取的提示词工程技巧分类体系。

---

## 目录

1. [技巧频次排行](#1-技巧频次排行)
2. [分类体系](#2-分类体系)
3. [高频技巧详解](#3-高频技巧详解)
4. [技巧组合模式](#4-技巧组合模式)
5. [按文件类型分布](#5-按文件类型分布)

---

## 1. 技巧频次排行

以下统计来自 251 个文档中的"提示词技巧分析"表格，按出现次数降序排列：

| 排名 | 技巧名称 | 出现次数 | 占比 |
|------|---------|----------|------|
| 1 | 负面约束（Negative Constraint） | 34 | 15.2% |
| 2 | 动态上下文注入（Dynamic Context Injection） | 30 | 13.4% |
| 3 | 范围限定（Scope Limitation） | 24 | 10.7% |
| 4 | 条件逻辑注入（Conditional Logic Injection） | 24 | 10.7% |
| 5 | 简洁指令（Concise Instruction） | 23 | 10.3% |
| 6 | 边界硬编码（Hard Boundary） | 19 | 8.5% |
| 7 | 结构化列表（Structured Enumeration） | 19 | 8.5% |
| 8 | 示例引导（Example-driven Guidance） | 19 | 8.5% |
| 9 | 安全防护指令（Safety Guard） | 19 | 8.5% |
| 10 | 失败模式预警（Failure Mode Warning） | 17 | 7.6% |
| 11 | 角色锚定（Role Anchoring） | 16 | 7.1% |
| 12 | 优先级排序（Priority Ordering） | 14 | 6.3% |
| 13 | 正面/负面指令对（DO/DON'T Pairs） | 13 | 5.8% |
| 14 | 优先级标记（Priority Escalation） | 13 | 5.8% |
| 15 | 条件分支（Conditional Branching） | 11 | 4.9% |

---

## 2. 分类体系

### 2.1 约束类技巧

**目的**：限制模型行为边界，防止越界。

| 技巧 | 典型用法 | 代表文件 |
|------|---------|---------|
| **负面约束** | `NEVER do X`、`Do NOT ...` | tool-description-write（永不创建未请求的 .md） |
| **边界硬编码** | 用具体数字/路径定义边界 | tool-description-bash-sandbox-*（沙箱路径白名单） |
| **范围限定** | `Only when ...`、`Skip if ...` | system-prompt-tool-usage-*（工具适用场景） |
| **安全防护** | `IMPORTANT`、`CRITICAL` 级别 | agent-prompt-security-monitor-*（安全检查） |

### 2.2 引导类技巧

**目的**：主动引导模型走向期望行为。

| 技巧 | 典型用法 | 代表文件 |
|------|---------|---------|
| **角色锚定** | `You are a ...` 开头 | agent-prompt-explore（你是代码库探索者） |
| **示例引导** | 用 `<example>` 标签包裹示例 | tool-description-todowrite（4 个使用/不使用示例） |
| **Few-shot** | 提供输入→输出对 | agent-prompt-coding-session-title-generator |
| **正面/负面对** | DO this / DON'T do that | system-prompt-doing-tasks-*（做什么 vs 不做什么） |

### 2.3 结构类技巧

**目的**：组织信息以提高模型的处理效率。

| 技巧 | 典型用法 | 代表文件 |
|------|---------|---------|
| **结构化列表** | 编号列表、表格 | tool-description-teammatetool（7 步工作流） |
| **优先级排序** | 按重要性/频率排列规则 | system-prompt-tool-usage-*（工具偏好顺序） |
| **XML 分隔** | `<thinking>`、`<example>` | agent-prompt-security-monitor-*（结构化推理输出） |
| **YAML/JSON 输出** | 强制结构化输出格式 | agent-prompt-dream-memory-consolidation |

### 2.4 动态类技巧

**目的**：根据运行时条件调整提示内容。

| 技巧 | 典型用法 | 代表文件 |
|------|---------|---------|
| **动态上下文注入** | `${VARIABLE}` 模板变量 | system-prompt-git-status（注入当前 git 状态） |
| **条件逻辑注入** | 变量控制段落的有无 | tool-description-taskcreate（`${CONDITIONAL_TASK_NOTES}`） |
| **条件分支** | `if X then Y else Z` | system-reminder-plan-mode-is-active-*（不同计划模式） |
| **Token 预算** | 动态注入消耗/预算数据 | system-reminder-token-usage |

### 2.5 防御类技巧

**目的**：预防常见错误和失败模式。

| 技巧 | 典型用法 | 代表文件 |
|------|---------|---------|
| **失败模式预警** | `This will fail if ...` | tool-description-teamdelete（活跃成员时失败） |
| **优先级标记** | `CRITICAL`、`IMPORTANT`、`MUST` | tool-description-websearch（CRITICAL REQUIREMENT） |
| **自我反思** | 检查自己的假设 | agent-prompt-verification-specialist（对抗性验证） |
| **思维链** | 分步推理 | agent-prompt-security-monitor-*（多步安全评估） |

---

## 3. 高频技巧详解

### 3.1 负面约束（Negative Constraint）

> 出现 34 次，是 Claude Code 提示词中最频繁使用的技巧。

**原理**：LLM 对"不要做 X"比"做 Y"有更高的遵守率，尤其是配合大写强调词时。

**典型模式**：
```
NEVER create documentation files unless explicitly requested.
Do NOT use terminal tools to view team activity.
NEVER mark a task as completed if tests are failing.
```

**关键观察**：负面约束在 Claude Code 中的三个层级：
1. **绝对禁止**：`NEVER`、`Do NOT` —— 无条件禁止
2. **条件禁止**：`unless explicitly requested` —— 有例外的禁止
3. **偏好抑制**：`Avoid X unless Y` —— 软性约束

### 3.2 动态上下文注入（Dynamic Context Injection）

> 出现 30 次，是 Claude Code 的核心架构特色。

**原理**：通过 `${VARIABLE}` 模板变量在运行时注入上下文，使同一个提示词模板能适应不同环境。

**三类变量**：
1. **环境变量**：`${CWD}`（工作目录）、`${OS}`（操作系统）
2. **状态变量**：`${GIT_STATUS}`（git 状态）、`${TOKEN_USAGE}`（token 消耗）
3. **条件变量**：`${CONDITIONAL_*}`（控制段落的有无）

### 3.3 安全防护指令（Safety Guard）

> 出现 19 次，集中在安全监控相关文件中。

**分层安全模型**：
```
BLOCK 规则 → ALLOW 例外 → 用户意图修正
```

安全防护使用"默认阻断"（default-deny）策略，只有明确列入白名单的操作才被允许。

---

## 4. 技巧组合模式

Claude Code 中的提示词很少使用单一技巧，而是组合多种技巧形成"技巧栈"：

### 组合 A：角色锚定 + 结构化列表 + 负面约束
```
You are a [ROLE].              ← 角色锚定
You should:                     ← 结构化列表
  1. Do X
  2. Do Y
You should NOT:                 ← 负面约束
  - Do Z
```
**典型应用**：agent-prompt-explore、agent-prompt-general-purpose

### 组合 B：动态注入 + 条件分支 + 优先级标记
```
${CONDITIONAL_NOTE}            ← 动态注入
IMPORTANT: If X then Y.       ← 优先级标记 + 条件分支
```
**典型应用**：tool-description-taskcreate、system-reminder-plan-mode-*

### 组合 C：示例引导 + 正面/负面对 + 失败预警
```
<example>Good: ...</example>   ← 示例引导
<example>Bad: ...</example>    ← 正面/负面对
NOTE: This will fail if ...    ← 失败预警
```
**典型应用**：tool-description-todowrite、skill-verify-skill

---

## 5. 按文件类型分布

| 文件类型 | 最常用技巧 | 原因 |
|----------|-----------|------|
| Agent Prompts | 角色锚定、结构化列表、思维链 | 子智能体需要明确身份和推理流程 |
| System Prompts | 负面约束、优先级排序、范围限定 | 核心行为规则需要精确边界 |
| Tool Descriptions | 示例引导、失败预警、边界硬编码 | 工具使用需要具体示例和错误预防 |
| Skills | Few-shot、条件分支、结构化输出 | 复杂技能需要详细的执行路径 |
| System Reminders | 动态注入、简洁指令、条件逻辑 | 运行时提醒需要轻量且上下文感知 |
| Data | 代码示例驱动、内置参考数据 | 作为参考材料直接注入上下文 |

---

## 关键发现

1. **负面约束是第一大技巧** —— Claude Code 通过大量"不要做什么"来约束模型行为
2. **动态注入是架构核心** —— 251 个文件中有约 80 个使用模板变量，使提示词高度可配置
3. **安全防护集中而非分散** —— 安全相关指令主要集中在 security-monitor 系列，而非散布各处
4. **示例和负面约束总是成对出现** —— 几乎所有包含示例的文件都同时包含负面约束
5. **技巧栈优于单一技巧** —— 高质量的提示词段平均使用 3-5 种技巧的组合
