# 10 — 可复用模式

> 从 Claude Code 提示词系统中提炼的可复用提示词工程模式，可直接应用于其他 AI 智能体系统的设计。

---

## 目录

1. [架构模式](#1-架构模式)
2. [安全模式](#2-安全模式)
3. [行为控制模式](#3-行为控制模式)
4. [协作模式](#4-协作模式)
5. [输出控制模式](#5-输出控制模式)
6. [模式速查卡](#6-模式速查卡)

---

## 1. 架构模式

### 模式 1.1：原子化提示词拼装（Atomic Prompt Assembly）

**问题**：单一大型提示词难以维护、难以版本化、难以按需加载。

**解决方案**：将提示词拆分为独立的原子化片段，运行时按需组装。

**Claude Code 实践**：
- 252 个独立 .md 文件
- 每个文件只负责一个职责
- 通过模板变量（`${VAR}`）实现条件组合
- 通过 ToolSearch 实现延迟加载

**适用场景**：任何需要管理超过 20 条行为规则的 AI 系统。

**关键要素**：
- 每个文件有清晰的命名约定（前缀分类）
- 元数据头部（版本号、变量列表）
- 运行时组装器负责排序和去重

---

### 模式 1.2：渐进式上下文加载（Progressive Context Loading）

**问题**：初始 token 预算有限，不能一次加载所有指令。

**解决方案**：分三层按需加载。

```
第 1 层（启动时）：核心身份 + 基本规则     ← 始终加载
第 2 层（按需）：工具描述 + 技能          ← 用到时加载
第 3 层（事件触发）：系统提醒 + 数据参考    ← 事件驱动注入
```

**Claude Code 实践**：
- System Prompts = 第 1 层
- Tool Descriptions + Skills = 第 2 层（ToolSearch 延迟加载）
- System Reminders + Data = 第 3 层（运行时事件触发）

---

### 模式 1.3：模板变量系统（Template Variable System）

**问题**：提示词需要适应不同运行环境。

**解决方案**：使用 `${VARIABLE}` 占位符，运行时替换。

**三类变量**：

| 类型 | 示例 | 替换时机 |
|------|------|---------|
| 环境变量 | `${CWD}`、`${OS}` | 启动时 |
| 状态变量 | `${GIT_STATUS}` | 每次工具调用前 |
| 条件变量 | `${CONDITIONAL_NOTE}` | 功能开关控制 |

**关键设计**：条件变量为空字符串时，对应的段落自然消失，无需 if/else 逻辑。

---

## 2. 安全模式

### 模式 2.1：分层安全评估（Layered Security Evaluation）

**问题**：AI 智能体需要既灵活又安全地执行操作。

**解决方案**：三层安全评估管道。

```
BLOCK 规则（硬性禁止列表）
  ↓ 不匹配
ALLOW 例外（白名单放行）
  ↓ 不匹配
默认阻断（安全第一）
  ↓ 最终
用户意图修正（双向：授权 or 约束）
```

**Claude Code 实践**：agent-prompt-security-monitor-* 系列

**关键要素**：
- BLOCK 和 ALLOW 是**静态规则**，编译时确定
- 用户意图是**动态修正**，运行时评估
- 授权方向需要高证据标准，约束方向只需低证据标准

---

### 模式 2.2：独立安全审计器（Independent Security Auditor）

**问题**：执行智能体自己评估安全性会有利益冲突。

**解决方案**：部署独立的安全审计子智能体。

**Claude Code 实践**：
- 主智能体执行任务
- Security Monitor 独立评估每次工具调用
- Verification Specialist 独立验证代码变更

**关键设计**：审计器只有评估权，没有执行权。系统层面根据审计结果决定是否拦截。

---

### 模式 2.3：不可逆操作保护（Irreversible Action Guard）

**问题**：AI 执行的某些操作无法撤销。

**解决方案**：对不可逆操作施加额外保护。

**分级策略**：

| 级别 | 操作类型 | 保护措施 |
|------|---------|---------|
| 低 | git commit（可 revert） | 正常执行 |
| 中 | 删除文件（git 可恢复） | 提醒但允许 |
| 高 | force push、覆盖未跟踪文件 | 阻断 |
| 极高 | 发布到公共注册表、删除云资源 | 阻断 + 需用户确认 |

---

## 3. 行为控制模式

### 模式 3.1：DO/DON'T 对称指令（Symmetric Instruction Pairs）

**问题**：只告诉模型"做什么"不够，还需要告诉它"不做什么"。

**解决方案**：每条正面指令配对应的负面约束。

```markdown
## When to Use This Tool        ← 正面指令
- Complex multi-step tasks
- Non-trivial tasks

## When NOT to Use This Tool    ← 负面约束
- Single, straightforward task
- Trivial task
```

**Claude Code 实践**：tool-description-todowrite（4 个正面示例 + 4 个负面示例）

---

### 模式 3.2：数量阈值定义（Quantitative Threshold）

**问题**：模糊的指令（"复杂任务"）导致模型判断不一致。

**解决方案**：用具体数字定义阈值。

```
"When a task requires 3 or more distinct steps"     ← 使用阈值
"The task can be completed in less than 3 steps"     ← 不使用阈值
```

**适用场景**：任何需要模型做二元决策的场景。

---

### 模式 3.3：失败模式预警（Failure Mode Warning）

**问题**：模型不知道某些操作会失败。

**解决方案**：明确告知失败条件和后果。

```
TeamDelete will FAIL if the team still has active members.
Gracefully terminate teammates FIRST, then call TeamDelete.
```

**关键要素**：
- 明确说明**什么条件**会导致失败
- 提供**正确的操作顺序**
- 使用 FAIL、FIRST 等大写强调词

---

## 4. 协作模式

### 模式 4.1：显式通信协议（Explicit Communication Protocol）

**问题**：多智能体系统中，智能体可能假设输出对其他智能体可见。

**解决方案**：强制所有通信通过工具调用。

```
Your plain text output is NOT visible to other agents.
To communicate, you MUST call SendMessage.
```

**关键设计**：将通信从隐式（输出可见）变为显式（工具调用），确保系统可追踪和路由所有消息。

---

### 模式 4.2：空闲状态正常化（Idle State Normalization）

**问题**：协调者智能体可能对队友的空闲状态过度反应。

**解决方案**：在提示词中明确将空闲定义为正常。

```
Teammates go idle after every turn—this is completely normal and expected.
Do not treat idle as an error.
Idle teammates can receive messages.
```

**适用场景**：任何异步多智能体系统。

---

### 模式 4.3：ID 优先任务选取（ID-Ordered Task Selection）

**问题**：多个队友可能随机选取任务，导致依赖问题。

**解决方案**：优先选取最小 ID 的任务。

```
Prefer tasks in ID order (lowest ID first),
as earlier tasks often set up context for later ones.
```

**优点**：用简单的排序规则实现了隐式依赖管理，无需复杂的依赖图。

---

## 5. 输出控制模式

### 模式 5.1：双形式文本（Dual-Form Text）

**问题**：同一内容在不同 UI 上下文需要不同的文本形式。

**解决方案**：要求同时提供两种形式。

```
content: "Fix authentication bug"       ← 祈使句（列表显示）
activeForm: "Fixing authentication bug"  ← 进行时（加载动画）
```

---

### 模式 5.2：强制来源引用（Mandatory Source Citation）

**问题**：搜索结果需要可验证。

**解决方案**：将来源引用定义为"CRITICAL REQUIREMENT"。

```
CRITICAL REQUIREMENT - You MUST follow this:
After answering, you MUST include a "Sources:" section.
This is MANDATORY - never skip including sources.
```

**关键要素**：三重强调（CRITICAL + MUST + MANDATORY）确保模型不跳过。

---

### 模式 5.3：年份校正（Year Correction）

**问题**：模型可能使用训练数据中的过时年份。

**解决方案**：运行时注入当前年份并明确要求使用。

```
The current month is ${GET_CURRENT_MONTH_YEAR()}.
You MUST use this year, NOT last year.
```

---

## 6. 模式速查卡

| # | 模式名称 | 一句话描述 | 适用范围 |
|---|---------|-----------|---------|
| 1.1 | 原子化拼装 | 252 个独立文件，运行时组装 | 架构 |
| 1.2 | 渐进加载 | 三层按需加载 | 架构 |
| 1.3 | 模板变量 | ${VAR} 运行时替换 | 架构 |
| 2.1 | 分层安全 | BLOCK → ALLOW → 默认阻断 → 用户意图 | 安全 |
| 2.2 | 独立审计 | 审计器与执行器分离 | 安全 |
| 2.3 | 不可逆保护 | 按操作可逆性分级保护 | 安全 |
| 3.1 | DO/DON'T 对 | 正面指令 + 负面约束 | 行为 |
| 3.2 | 数量阈值 | 用数字定义判断边界 | 行为 |
| 3.3 | 失败预警 | 明确失败条件和正确顺序 | 行为 |
| 4.1 | 显式通信 | 强制工具调用通信 | 协作 |
| 4.2 | 空闲正常化 | 声明空闲是正常状态 | 协作 |
| 4.3 | ID 优先 | 最小 ID 优先选取 | 协作 |
| 5.1 | 双形式文本 | 同一内容两种文本形式 | 输出 |
| 5.2 | 强制引用 | 三重强调确保来源引用 | 输出 |
| 5.3 | 年份校正 | 运行时注入当前年份 | 输出 |

---

## 使用建议

1. **架构模式（1.x）** 适合构建新的 AI 智能体系统时参考
2. **安全模式（2.x）** 适合任何赋予 AI 执行权限的系统
3. **行为控制模式（3.x）** 适合优化现有提示词的精确度
4. **协作模式（4.x）** 适合多智能体系统设计
5. **输出控制模式（5.x）** 适合需要精确控制模型输出格式的场景

每个模式都可以独立使用，也可以组合使用。建议从架构模式开始，再根据需要添加安全和行为控制模式。
