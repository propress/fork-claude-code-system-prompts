# insights-on-the-horizon

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Insights on the horizon |
| 分类 | System Prompts → 洞察报告 |
| 文件路径 | `system-prompts/system-prompt-insights-on-the-horizon.md` |
| CC 版本 | 2.1.30 |
| 模板变量 | 无（隐式接收使用数据作为上下文） |
| 首次出现版本 | 2.1.30 |

## 原文

> Analyze this Claude Code usage data and identify future opportunities.
>
> RESPOND WITH ONLY A VALID JSON OBJECT:
> {
>   "intro": "1 sentence about evolving AI-assisted development",
>   "opportunities": [
>     {"title": "Short title (4-8 words)", "whats_possible": "2-3 ambitious sentences about autonomous workflows", "how_to_try": "1-2 sentences mentioning relevant tooling", "copyable_prompt": "Detailed prompt to try"}
>   ]
> }
>
> Include 3 opportunities. Think BIG - autonomous workflows, parallel agents, iterating against tests.

## 中文翻译

> **原文：**
> Analyze this Claude Code usage data and identify future opportunities.

**翻译：**
分析此 Claude Code 使用数据并识别未来机会。

> **原文：**
> RESPOND WITH ONLY A VALID JSON OBJECT:
> { ... }
> Include 3 opportunities. Think BIG - autonomous workflows, parallel agents, iterating against tests.

**翻译：**
仅返回一个有效的 JSON 对象：
```json
{
  "intro": "用 1 句话描述 AI 辅助开发的演进",
  "opportunities": [
    {
      "title": "简短标题（4-8 个词）",
      "whats_possible": "用 2-3 句话描述关于自主工作流的宏大愿景",
      "how_to_try": "用 1-2 句话提及相关工具",
      "copyable_prompt": "可复制的详细提示词"
    }
  ]
}
```
包含 3 个机会。大胆思考——自主工作流、并行代理、基于测试的迭代。

## 📋 模板变量说明

无显式模板变量。使用数据作为上下文在运行时附加。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 激励性指令 | "Think BIG - autonomous workflows, parallel agents, iterating against tests" | 通过大写 "BIG" 和具体方向示例，推动模型跳出保守建议，产生具有前瞻性和激发性的内容。 |
| 2 | 可操作输出 | `"copyable_prompt": "Detailed prompt to try"` | 每个机会都包含一个可直接复制使用的提示词，将洞察从「了解」层面提升到「行动」层面。 |
| 3 | 标题长度约束 | "Short title (4-8 words)" | 限制标题长度确保机会描述精炼、可扫描，适合在报告 UI 中展示。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.30 | 新增 | 首次引入未来机会分析提示词 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/87f225d" target="_blank">87f225d</a> |
