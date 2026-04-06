# insights-session-facets-extraction

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Insights session facets extraction |
| 分类 | System Prompts → 洞察报告 |
| 文件路径 | `system-prompts/system-prompt-insights-session-facets-extraction.md` |
| CC 版本 | 2.1.30 |
| 模板变量 | 无（会话转录作为上下文在运行时附加） |
| 首次出现版本 | 2.1.30 |

## 原文

> Analyze this Claude Code session and extract structured facets.
>
> CRITICAL GUIDELINES:
>
> 1. **goal_categories**: Count ONLY what the USER explicitly asked for.
>    - DO NOT count Claude's autonomous codebase exploration
>    - DO NOT count work Claude decided to do on its own
>    - ONLY count when user says "can you...", "please...", "I need...", "let's..."
>
> 2. **user_satisfaction_counts**: Base ONLY on explicit user signals.
>    - "Yay!", "great!", "perfect!" → happy
>    - "thanks", "looks good", "that works" → satisfied
>    - "ok, now let's..." (continuing without complaint) → likely_satisfied
>    - "that's not right", "try again" → dissatisfied
>    - "this is broken", "I give up" → frustrated
>
> 3. **friction_counts**: Be specific about what went wrong.
>    - misunderstood_request: Claude interpreted incorrectly
>    - wrong_approach: Right goal, wrong solution method
>    - buggy_code: Code didn't work correctly
>    - user_rejected_action: User said no/stop to a tool call
>    - excessive_changes: Over-engineered or changed too much
>
> 4. If very short or just warmup, use warmup_minimal for goal_category
>
> SESSION:

## 中文翻译

> **原文：**
> Analyze this Claude Code session and extract structured facets.

**翻译：**
分析此 Claude Code 会话并提取结构化的维度信息。

> **原文：**
> CRITICAL GUIDELINES:
> 1. **goal_categories**: Count ONLY what the USER explicitly asked for.

**翻译：**
关键指南：
1. **goal_categories（目标类别）**：仅计算用户**明确要求**的内容。
   - 不要计算 Claude 的自主代码库探索
   - 不要计算 Claude 自行决定完成的工作
   - 仅在用户说 "can you..."、"please..."、"I need..."、"let's..." 时计算

> **原文：**
> 2. **user_satisfaction_counts**: Base ONLY on explicit user signals.

**翻译：**
2. **user_satisfaction_counts（用户满意度计数）**：仅基于明确的用户信号。
   - "Yay!"、"great!"、"perfect!" → happy（开心）
   - "thanks"、"looks good"、"that works" → satisfied（满意）
   - "ok, now let's..."（无抱怨地继续）→ likely_satisfied（可能满意）
   - "that's not right"、"try again" → dissatisfied（不满意）
   - "this is broken"、"I give up" → frustrated（沮丧）

> **原文：**
> 3. **friction_counts**: Be specific about what went wrong.

**翻译：**
3. **friction_counts（摩擦计数）**：具体说明出了什么问题。
   - misunderstood_request：Claude 理解错误
   - wrong_approach：目标正确，但方案方法错误
   - buggy_code：代码未正确运行
   - user_rejected_action：用户对工具调用说了不/停止
   - excessive_changes：过度工程化或改动过多

> **原文：**
> 4. If very short or just warmup, use warmup_minimal for goal_category

**翻译：**
4. 如果会话非常短或只是热身，目标类别使用 warmup_minimal。

## 📋 模板变量说明

无显式模板变量。会话转录（SESSION）在运行时附加在提示词末尾。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 信号映射表 | "'Yay!' → happy, 'thanks' → satisfied, 'this is broken' → frustrated" | 提供从自然语言到分类标签的明确映射，消除情感分析中的主观判断，确保标注一致性。 |
| 2 | 排除规则 | "DO NOT count Claude's autonomous codebase exploration" | 用大写 "DO NOT" 明确排除常见的过度计数来源，防止将 Claude 的主动行为误归为用户目标。 |
| 3 | 摩擦分类学 | "misunderstood_request, wrong_approach, buggy_code, user_rejected_action, excessive_changes" | 预定义的摩擦分类体系确保跨会话分析的一致性，便于后续聚合分析。 |
| 4 | 边界情况处理 | "If very short or just warmup, use warmup_minimal" | 为极端情况（极短会话）提供了兜底方案，防止分析器在数据不足时生成无意义结果。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.30 | 新增 | 首次引入会话维度提取提示词 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/87f225d" target="_blank">87f225d</a> |
