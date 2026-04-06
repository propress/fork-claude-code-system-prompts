# 08 — 设计哲学分析

> 从 Claude Code 251 个提示词文件中提炼的设计原则与哲学体系。

---

## 目录

1. [核心设计原则](#1-核心设计原则)
2. [安全哲学](#2-安全哲学)
3. [智能体协作哲学](#3-智能体协作哲学)
4. [工具使用哲学](#4-工具使用哲学)
5. [用户交互哲学](#5-用户交互哲学)
6. [提示词工程哲学](#6-提示词工程哲学)

---

## 1. 核心设计原则

### 1.1 最小权限原则（Principle of Least Privilege）

Claude Code 的每个组件只获得完成其任务所需的最小能力集：

| 组件 | 能力约束 | 体现 |
|------|---------|------|
| Explore 子智能体 | 只读，无编辑/写入权限 | agent-prompt-explore |
| Bash 沙箱 | 路径白名单、禁止写入敏感目录 | tool-description-bash-sandbox-* |
| Plan Mode | 只分析不执行 | system-reminder-plan-mode-* |
| 安全监控 | 只评估不拦截（评估后由系统拦截） | agent-prompt-security-monitor-* |

### 1.2 防御性编程（Defensive Programming）

提示词设计假设模型**会**犯错，因此在多个层面设置防线：

```
第 1 层：角色锚定 — 定义身份和职责
第 2 层：正面指令 — 告诉模型该做什么
第 3 层：负面约束 — 明确告诉模型不该做什么
第 4 层：失败预警 — 预警常见错误模式
第 5 层：安全监控 — 独立的安全审查子智能体
```

### 1.3 渐进式复杂度（Progressive Complexity）

Claude Code 不一次性加载所有提示词，而是根据需要渐进加载：

```
启动时       → 核心 System Prompts（≈67 个片段）
用户请求     → 按需加载 Tool Descriptions
复杂任务     → 加载 Skills + Data 参考
运行中事件   → 动态注入 System Reminders
多智能体     → 加载 Agent Prompts + Team 协调
```

### 1.4 关注点分离（Separation of Concerns）

每个提示词文件只负责一个清晰的职责：

- **系统提示词**：定义"是什么"（行为规则）
- **工具描述**：定义"怎么做"（操作指南）
- **技能**：定义"做什么"（任务流程）
- **系统提醒**：定义"注意什么"（上下文状态）
- **数据文件**：定义"参考什么"（参考资料）

这种分离使得每个片段可以独立版本化、独立更新、独立测试。

---

## 2. 安全哲学

### 2.1 默认阻断（Default Deny）

安全监控采用"默认阻断"策略——所有操作默认被认为有风险，只有明确匹配 ALLOW 列表的操作才被放行：

```
评估流程：
  BLOCK 规则检查 → 匹配 → 阻断
                  → 不匹配 → ALLOW 例外检查 → 匹配 → 放行
                                              → 不匹配 → 默认阻断
```

### 2.2 双向用户意图框架

v2.1.90 引入了双向用户意图框架——用户意图既可以**授权**（解除阻断），也可以**约束**（创建新阻断）：

| 方向 | 证据要求 | 示例 |
|------|---------|------|
| 授权（解除阻断） | 高证据标准 | 用户明确要求"删除 production 数据库" |
| 约束（创建阻断） | 低证据标准 | 用户说"等我审查后再推送" |

### 2.3 不可逆操作的特殊处理

对不可逆操作的保守态度贯穿整个系统：

- **git force push**：禁止（tool-description-bash-git-*）
- **删除外部资源**：需要用户确认（agent-prompt-security-monitor-*）
- **覆盖未跟踪文件**：视为不可逆破坏（v2.1.89 扩展）
- **发布到公共注册表**：新增 BLOCK 规则（v2.1.89）

### 2.4 记忆投毒防护

v2.1.91 新增了记忆投毒（Memory Poisoning）防护——阻止向记忆目录写入会充当权限授予、绕过 BLOCK 规则或伪造用户授权的内容。

---

## 3. 智能体协作哲学

### 3.1 层级式委托（Hierarchical Delegation）

Claude Code 采用清晰的委托层级：

```
用户
 └── 主智能体（Leader）
      ├── Explore 子智能体（只读研究）
      ├── General-purpose 子智能体（全能力执行）
      ├── Verification 子智能体（验证审查）
      └── 团队模式
           ├── Team Lead（协调分配）
           └── Teammates（执行任务）
```

### 3.2 显式通信（Explicit Communication）

**核心哲学**：智能体间的通信必须通过工具调用，而非假设可见：

> "Your plain text output is NOT visible to other agents — to communicate, you MUST call this tool."

这一设计确保所有通信都被系统记录和路由。

### 3.3 任务优先级与依赖

任务管理采用简单但有效的规则：
- **ID 优先**：优先选取最小 ID 的任务（隐式依赖排序）
- **单任务约束**：同一时间只有一个 in_progress 任务
- **立即完成**：完成后立即标记，不批量更新

---

## 4. 工具使用哲学

### 4.1 工具层级偏好

Claude Code 为工具建立了明确的偏好层级：

```
修改文件：Edit（差异） > Write（全文覆写）
读取文件：Read（内置） > Bash cat（外部命令）
搜索文件：Glob（文件名） > Grep（内容） > Bash find
搜索内容：Grep（内置） > Bash grep
网页获取：MCP 工具 > WebFetch（内置）
GitHub：gh CLI > WebFetch
```

### 4.2 Bash 作为"最后手段"

Bash 被定位为其他工具都不适用时的后备方案：

> "Reserve Bash for system commands, build steps, and tasks that no specialized tool can handle."

这种设计减少了 Bash 注入风险，同时确保工具调用可被系统追踪和审计。

### 4.3 延迟加载（Lazy Loading）

工具描述支持延迟加载——运行时只有工具名称可见，完整的参数 schema 通过 ToolSearch 按需获取。这减少了初始 token 消耗。

---

## 5. 用户交互哲学

### 5.1 简洁优先

```
Be direct and technical
Default to the shortest answer
Skip preambles and filler phrases
```

Claude Code 明确要求模型避免冗余输出，这与通用聊天机器人的"友好详细"风格形成鲜明对比。

### 5.2 行动优先于计划

除非用户明确要求计划或处于计划模式，否则 Claude Code 偏向直接执行：

> "Do not explain what you're going to do — just do it."

### 5.3 用户意图推断

Claude Code 在多处要求模型推断用户的隐含意图：
- 用户说"运行测试"→ 测试失败时自动修复
- 用户说"添加暗色模式"→ 推断需要运行测试和构建验证
- 用户说"等我审查"→ 推断为条件性约束

---

## 6. 提示词工程哲学

### 6.1 原子化（Atomization）

251 个文件，每个文件只包含一个聚焦的指令集。这使得：
- 版本控制粒度最细
- 可以按需组合加载
- 修改一个行为不影响其他

### 6.2 可配置性（Configurability）

通过 `${VARIABLE}` 模板变量，同一提示词可适应不同：
- 操作系统（macOS vs Windows vs Linux）
- 编辑器（VS Code vs Vim vs Terminal）
- 功能开关（团队模式开/关）
- 运行时状态（git 状态、token 使用量）

### 6.3 迭代式演进

CHANGELOG 显示提示词经历了密集的迭代：
- v2.0.14 到 v2.1.92 跨越 46 个版本
- 平均每个版本修改 5-10 个文件
- 安全相关文件更新最频繁

### 6.4 经验驱动

提示词设计并非理论化的，而是基于实际使用中发现的问题：
- 发现模型主动创建 .md 文件 → 添加"NEVER create documentation files"
- 发现模型发送 JSON 状态消息 → 添加"Do NOT send structured JSON status messages"
- 发现模型对空闲状态过度反应 → 添加"completely normal and expected"
- 发现模型跳过验证步骤 → 添加对抗性验证协议

---

## 总结

Claude Code 的设计哲学可以概括为：

> **"最小权限 + 默认安全 + 渐进加载 + 原子化提示"**

这是一个工程化的提示词系统，而非简单的指令集合。它通过分层架构、动态注入和持续迭代，在功能性和安全性之间取得平衡。
