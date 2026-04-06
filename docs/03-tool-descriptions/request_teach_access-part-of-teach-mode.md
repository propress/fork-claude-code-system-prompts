# request_teach_access-part-of-teach-mode

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: request_teach_access (part of teach mode) |
| 分类 | Tool Descriptions → 用户交互 |
| 文件路径 | `system-prompts/tool-description-request_teach_access-part-of-teach-mode.md` |
| CC 版本 | 2.1.84 |
| 模板变量 | 无 |

## 原文

> Request permission to guide the user through a task step-by-step with on-screen tooltips. Use this INSTEAD OF request_access when the user wants to LEARN how to do something (phrases like "teach me", "walk me through", "show me how", "help me learn"). On approval the main Claude window hides and a fullscreen tooltip overlay appears. You then call teach_step repeatedly; each call shows one tooltip and waits for the user to click Next. Same app-allowlist semantics as request_access, but no clipboard/system-key flags. Teach mode ends automatically when your turn ends.

## 中文翻译

> **原文：**
> Request permission to guide the user through a task step-by-step with on-screen tooltips. Use this INSTEAD OF request_access when the user wants to LEARN how to do something (phrases like "teach me", "walk me through", "show me how", "help me learn"). On approval the main Claude window hides and a fullscreen tooltip overlay appears. You then call teach_step repeatedly; each call shows one tooltip and waits for the user to click Next. Same app-allowlist semantics as request_access, but no clipboard/system-key flags. Teach mode ends automatically when your turn ends.

**翻译：**
请求许可，通过屏幕提示逐步引导用户完成任务。当用户想要学习如何做某事时（例如"教我"、"带我走一遍"、"告诉我怎么做"、"帮我学习"等表述），使用此工具代替 request_access。批准后，Claude 主窗口会隐藏，出现全屏提示覆盖层。然后你重复调用 teach_step；每次调用显示一个提示，等待用户点击"下一步"。与 request_access 相同的应用白名单语义，但没有剪贴板/系统键标志。教学模式在你的回合结束时自动结束。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 条件逻辑注入（Conditional Logic Injection） | Use this INSTEAD OF request_access when the user wants to LEARN | 明确区分了该工具与 request_access 的使用场景，通过条件判断（用户想学习时）引导模型选择正确工具 |
| 2 | 示例引导（Example-driven Guidance） | phrases like "teach me", "walk me through", "show me how" | 提供了具体的触发短语示例，帮助模型识别何时应使用此工具 |
| 3 | 结构化列表（Structured Enumeration） | call teach_step repeatedly; each call shows one tooltip and waits | 描述了工具的使用流程，确保模型理解操作步骤 |
| 4 | 范围限定（Scope Limitation） | Teach mode ends automatically when your turn ends | 明确了工具的生命周期限制，防止模型误以为需要手动结束 |
