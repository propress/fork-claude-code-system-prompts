# askuserquestion

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: AskUserQuestion |
| 分类 | Tool Descriptions → 用户交互 |
| 文件路径 | `system-prompts/tool-description-askuserquestion.md` |
| CC 版本 | 2.1.47 |
| 模板变量 | `${EXIT_PLAN_MODE_TOOL_NAME}` |

## 原文

> Use this tool when you need to ask the user questions during execution. This allows you to:
> 1. Gather user preferences or requirements
> 2. Clarify ambiguous instructions
> 3. Get decisions on implementation choices as you work
> 4. Offer choices to the user about what direction to take.
>
> Usage notes:
> - Users will always be able to select "Other" to provide custom text input
> - Use multiSelect: true to allow multiple answers to be selected for a question
> - If you recommend a specific option, make that the first option in the list and add "(Recommended)" at the end of the label
>
> Plan mode note: In plan mode, use this tool to clarify requirements or choose between approaches BEFORE finalizing your plan. Do NOT use this tool to ask "Is my plan ready?" or "Should I proceed?" - use ${EXIT_PLAN_MODE_TOOL_NAME} for plan approval. IMPORTANT: Do not reference "the plan" in your questions (e.g., "Do you have feedback about the plan?", "Does the plan look good?") because the user cannot see the plan in the UI until you call ${EXIT_PLAN_MODE_TOOL_NAME}. If you need plan approval, use ${EXIT_PLAN_MODE_TOOL_NAME} instead.

## 中文翻译

> **原文：**
> Use this tool when you need to ask the user questions during execution. This allows you to:
> 1. Gather user preferences or requirements
> 2. Clarify ambiguous instructions
> 3. Get decisions on implementation choices as you work
> 4. Offer choices to the user about what direction to take.

**翻译：**
当你在执行过程中需要向用户提问时，使用此工具。它允许你：
1. 收集用户的偏好或需求
2. 澄清模糊的指令
3. 在工作过程中获取实现方案的决策
4. 向用户提供关于方向选择的选项。

---

> **原文：**
> Usage notes:
> - Users will always be able to select "Other" to provide custom text input
> - Use multiSelect: true to allow multiple answers to be selected for a question
> - If you recommend a specific option, make that the first option in the list and add "(Recommended)" at the end of the label

**翻译：**
使用说明：
- 用户始终可以选择"其他"来提供自定义文本输入
- 使用 multiSelect: true 来允许对一个问题选择多个答案
- 如果你推荐某个特定选项，请将其设为列表中的第一个选项，并在标签末尾添加"(Recommended)"

---

> **原文：**
> Plan mode note: In plan mode, use this tool to clarify requirements or choose between approaches BEFORE finalizing your plan. Do NOT use this tool to ask "Is my plan ready?" or "Should I proceed?" - use ${EXIT_PLAN_MODE_TOOL_NAME} for plan approval. IMPORTANT: Do not reference "the plan" in your questions (e.g., "Do you have feedback about the plan?", "Does the plan look good?") because the user cannot see the plan in the UI until you call ${EXIT_PLAN_MODE_TOOL_NAME}. If you need plan approval, use ${EXIT_PLAN_MODE_TOOL_NAME} instead.

**翻译：**
计划模式说明：在计划模式下，使用此工具在最终确定计划之前澄清需求或在不同方案之间做出选择。不要使用此工具询问"我的计划准备好了吗？"或"我应该继续吗？"——使用 ${EXIT_PLAN_MODE_TOOL_NAME} 来获取计划批准。重要：不要在问题中引用"计划"（例如，"你对计划有反馈吗？"、"计划看起来好吗？"），因为在你调用 ${EXIT_PLAN_MODE_TOOL_NAME} 之前，用户在 UI 中看不到计划。如果你需要计划批准，请使用 ${EXIT_PLAN_MODE_TOOL_NAME} 代替。

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${EXIT_PLAN_MODE_TOOL_NAME}` | 退出计划模式工具的名称 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 结构化列表（Structured Enumeration） | `1. Gather user preferences... 2. Clarify ambiguous instructions... 3. Get decisions... 4. Offer choices...` | 通过编号列表清晰地列出工具的四个用途，使模型能快速判断何时使用此工具。 |
| 2 | 负面约束（Negative Constraint） | `Do NOT use this tool to ask "Is my plan ready?" or "Should I proceed?"` | 明确禁止在计划模式下用此工具请求批准，防止错误的工具使用模式。 |
| 3 | 示例引导（Example-driven Guidance） | `"Do you have feedback about the plan?", "Does the plan look good?"` | 通过反面示例说明不应出现的问题模式，帮助模型理解边界。 |
| 4 | 优先级排序（Priority Ordering） | `make that the first option in the list and add "(Recommended)"` | 指导推荐选项的放置位置和标记方式，确保用户体验的一致性。 |
| 5 | 安全防护指令（Safety Guard） | `the user cannot see the plan in the UI until you call ${EXIT_PLAN_MODE_TOOL_NAME}` | 解释约束背后的原因（用户无法在 UI 中看到计划），使模型理解为何不能引用"计划"。 |
