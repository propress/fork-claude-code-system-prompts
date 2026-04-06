# insights-friction-analysis

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Insights friction analysis |
| 分类 | System Prompts → 洞察报告 |
| 文件路径 | `system-prompts/system-prompt-insights-friction-analysis.md` |
| CC 版本 | 2.1.30 |
| 模板变量 | 无（隐式接收使用数据作为上下文） |
| 首次出现版本 | 2.1.30 |

## 原文

> Analyze this Claude Code usage data and identify friction points for this user. Use second person ("you").
>
> RESPOND WITH ONLY A VALID JSON OBJECT:
> {
>   "intro": "1 sentence summarizing friction patterns",
>   "categories": [
>     {"category": "Concrete category name", "description": "1-2 sentences explaining this category and what could be done differently. Use 'you' not 'the user'.", "examples": ["Specific example with consequence", "Another example"]}
>   ]
> }
>
> Include 3 friction categories with 2 examples each.

## 中文翻译

> **原文：**
> Analyze this Claude Code usage data and identify friction points for this user. Use second person ("you").

**翻译：**
分析此 Claude Code 使用数据并识别该用户的摩擦点。使用第二人称（"you"）。

> **原文：**
> RESPOND WITH ONLY A VALID JSON OBJECT:
> {
>   "intro": "1 sentence summarizing friction patterns",
>   "categories": [...]
> }
>
> Include 3 friction categories with 2 examples each.

**翻译：**
仅返回一个有效的 JSON 对象：
```json
{
  "intro": "用 1 句话总结摩擦模式",
  "categories": [
    {"category": "具体类别名称", "description": "用 1-2 句话解释该类别以及可以做出的改变。使用 'you' 而非 'the user'。", "examples": ["带有后果的具体示例", "另一个示例"]}
  ]
}
```
包含 3 个摩擦类别，每个类别 2 个示例。

## 📋 模板变量说明

无显式模板变量。使用数据作为上下文在运行时附加。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 精确数量约束 | "Include 3 friction categories with 2 examples each" | 明确的数量要求（3 类 × 2 例）防止输出过多或过少，确保报告的信息密度一致。 |
| 2 | 人称指定 | "Use second person ('you')" | 第二人称使报告感觉像个人化的反馈而非第三方分析，增强用户参与感。 |
| 3 | JSON 唯一输出 | "RESPOND WITH ONLY A VALID JSON OBJECT" | 排除任何非 JSON 内容，确保输出可直接被程序解析。 |
| 4 | 结果导向示例 | "Specific example with consequence" | 要求每个示例包含后果说明，使反馈从描述性变为行动导向。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.30 | 新增 | 首次引入摩擦分析提示词 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/87f225d" target="_blank">87f225d</a> |
