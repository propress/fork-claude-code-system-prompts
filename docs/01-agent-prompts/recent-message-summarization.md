# recent-message-summarization

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: Recent Message Summarization |
| 分类 | Agent Prompts → 对话管理 |
| 文件路径 | `system-prompts/agent-prompt-recent-message-summarization.md` |
| CC 版本 | 2.1.84 |
| 模板变量 | 无（使用模板字符串内联条件） |
| 首次出现版本 | 早期版本 |
| 重大变更次数 | 较少 |

## 原文

Your task is to create a detailed summary of the RECENT portion of the conversation...

（完整原文见 `system-prompts/agent-prompt-recent-message-summarization.md`）

## 中文翻译

> **原文：**
> Your task is to create a detailed summary of the RECENT portion of the conversation — the messages that follow earlier retained context. The earlier messages are being kept intact and do NOT need to be summarized.

**翻译：**
你的任务是对对话的**近期部分**创建详细摘要——即紧随早期已保留上下文之后的消息。早期消息将保持完整，**不需要**进行摘要。

> **原文：**
> Before providing your final summary, wrap your analysis in `<analysis>` tags to organize your thoughts and ensure you've covered all necessary points.

**翻译：**
在提供最终摘要之前，请将你的分析过程包裹在 `<analysis>` 标签中，以整理思路并确保覆盖所有必要要点。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段 | 分析 |
|---|---------|---------|------|
| 1 | XML 标签分隔 | `<analysis>` 标签 | 强制模型先进行内部分析再输出最终结果，防止遗漏关键细节 |
| 2 | 思维链（CoT） | "analyze the recent messages chronologically" | 要求按时间顺序逐步分析，确保摘要的完整性和准确性 |
| 3 | 优先级标记 | "Pay special attention to specific user feedback" | IMPORTANT 标记提升用户反馈的权重，避免摘要遗漏用户纠正信息 |
| 4 | 上下文压缩指令 | "RECENT portion...earlier messages...kept intact" | 明确划分压缩边界，防止误摘要已保留的历史内容 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 |
|------|---------|------|
| v2.1.84 | 当前版本 | 最新版本 |
