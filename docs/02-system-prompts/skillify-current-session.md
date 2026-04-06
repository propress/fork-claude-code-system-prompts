# skillify-current-session

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Skillify Current Session |
| 分类 | System Prompts → 其他功能 |
| 文件路径 | `system-prompts/system-prompt-skillify-current-session.md` |
| CC 版本 | 2.1.41 |
| 模板变量 | `{{userDescriptionBlock}}`, `{{sessionMemory}}`, `{{userMessages}}`, `{{skill-name}}` |
| 首次出现版本 | 2.1.41 |

## 原文

> # Skillify {{userDescriptionBlock}}
>
> You are capturing this session's repeatable process as a reusable skill.
>
> ## Your Session Context
>
> Here is the session memory summary:
> \<session_memory\>
> {{sessionMemory}}
> \</session_memory\>
>
> Here are the user's messages during this session...
>
> ## Your Task
>
> ### Step 1: Analyze the Session
> Before asking any questions, analyze the session to identify:
> - What repeatable process was performed
> - What the inputs/parameters were
> - The distinct steps (in order)
> - The success artifacts/criteria for each step
> - Where the user corrected or steered you
> - What tools and permissions were needed
> - What agents were used
> - What the goals and success artifacts were
>
> ### Step 2: Interview the User
> **Round 1: High level confirmation** — Suggest a name and description for the skill.
> **Round 2: More details** — Present high-level steps, suggest arguments, ask about inline vs forked, ask where to save (repo vs personal).
> **Round 3: Breaking down each step** — For each major step, ask about outputs, success criteria, human checkpoints, parallelism, execution method, and hard constraints.
> **Round 4: Final questions** — Confirm when the skill should be invoked and trigger phrases.
>
> ### Step 3: Write the SKILL.md
> Create the skill directory and file at the user-chosen location using the structured format with frontmatter (name, description, allowed-tools, when_to_use, arguments) and body (Inputs, Goal, Steps with success criteria).
>
> ### Step 4: Confirm and Save
> Output the SKILL.md as a YAML code block, ask for confirmation, then write and tell the user where to find it and how to invoke it.

## 中文翻译

> **原文：**
> You are capturing this session's repeatable process as a reusable skill.

**翻译：**
你正在将此会话的可重复流程捕获为可复用的技能。

> **原文：**
> ### Step 1: Analyze the Session

**翻译：**
### 步骤 1：分析会话
在提问之前，先分析会话以识别：
- 执行了什么可重复的流程
- 输入/参数是什么
- 不同的步骤（按顺序）
- 每个步骤的成功产物/标准
- 用户在哪里进行了纠正或引导
- 需要什么工具和权限
- 使用了什么代理
- 目标和成功产物是什么

> **原文：**
> ### Step 2: Interview the User (4 rounds)

**翻译：**
### 步骤 2：采访用户
**第 1 轮：高层确认** —— 建议技能名称和描述，提出目标和成功标准。
**第 2 轮：更多细节** —— 展示步骤列表，建议参数，询问内联/分叉执行模式，询问保存位置（仓库/个人）。
**第 3 轮：逐步分解** —— 对每个主要步骤，询问输出物、成功标准、人工检查点、并行性、执行方式、硬性约束。
**第 4 轮：最终问题** —— 确认调用时机和触发短语。

> **原文：**
> ### Step 3: Write the SKILL.md

**翻译：**
### 步骤 3：编写 SKILL.md
在用户选择的位置创建技能目录和文件，使用结构化格式：frontmatter（name, description, allowed-tools, when_to_use, arguments）和正文（Inputs, Goal, Steps 含 success criteria）。

> **原文：**
> ### Step 4: Confirm and Save

**翻译：**
### 步骤 4：确认和保存
将完整的 SKILL.md 内容作为 YAML 代码块输出供用户审阅，使用 AskUserQuestion 请求确认，然后写入文件并告知用户保存位置和调用方式。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `{{userDescriptionBlock}}` | 字符串 | 用户对技能的描述（可选） |
| `{{sessionMemory}}` | 字符串 | 会话记忆摘要 |
| `{{userMessages}}` | 字符串 | 会话中用户的所有消息 |
| `{{skill-name}}` | 字符串 | 技能名称（在 SKILL.md 模板中使用） |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 四轮采访 | Round 1-4 结构 | 渐进式信息收集，从高层到细节，避免信息过载 |
| 2 | 用户纠正追踪 | `Pay special attention to places where the user corrected you` | 将用户纠正行为转化为技能规则，避免重蹈覆辙 |
| 3 | 成功标准强制 | `Success criteria is REQUIRED on every step` | 确保每个步骤都有可验证的完成条件 |
| 4 | 保存位置选择 | `This repo` vs `Personal` | 给用户明确的二选一，而非开放性问题 |
| 5 | 预览确认 | `output the complete SKILL.md content as a yaml code block` | 在写入文件前让用户审阅，减少返工 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.66 | 修改 | 添加 Round 2 保存位置选择，更新 Step 3 使用用户选择的位置 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/c55bb75" target="_blank">c55bb75</a> |
| 2.1.41 | 新增 | 首次添加将会话转化为可复用技能的系统提示词 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/91732e4" target="_blank">91732e4</a> |
