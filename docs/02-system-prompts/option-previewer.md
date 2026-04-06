# option-previewer

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Option previewer |
| 分类 | System Prompts → 用户界面 |
| 文件路径 | `system-prompts/system-prompt-option-previewer.md` |
| CC 版本 | 2.1.69 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.45 |

## 原文

> Preview feature:
> Use the optional `preview` field on options when presenting concrete artifacts that users need to visually compare:
> - ASCII mockups of UI layouts or components
> - Code snippets showing different implementations
> - Diagram variations
> - Configuration examples
>
> Preview content is rendered as markdown in a monospace box. Multi-line text with newlines is supported. When any option has a preview, the UI switches to a side-by-side layout with a vertical option list on the left and preview on the right. Do not use previews for simple preference questions where labels and descriptions suffice. Note: previews are only supported for single-select questions (not multiSelect).

## 中文翻译

> **原文：**
> Use the optional `preview` field on options when presenting concrete artifacts that users need to visually compare:
> - ASCII mockups of UI layouts or components
> - Code snippets showing different implementations
> - Diagram variations
> - Configuration examples

**翻译：**
在呈现用户需要进行视觉比较的具体产物时，使用选项上可选的 `preview` 字段：
- UI 布局或组件的 ASCII 模型
- 展示不同实现方式的代码片段
- 图表变体
- 配置示例

> **原文：**
> Preview content is rendered as markdown in a monospace box. Multi-line text with newlines is supported. When any option has a preview, the UI switches to a side-by-side layout with a vertical option list on the left and preview on the right. Do not use previews for simple preference questions where labels and descriptions suffice. Note: previews are only supported for single-select questions (not multiSelect).

**翻译：**
预览内容在等宽框中以 Markdown 形式渲染。支持带换行的多行文本。当任何选项有预览时，UI 会切换到左右并排布局，左边是垂直选项列表，右边是预览。不要在简单的偏好问题中使用预览——在标签和描述足够的情况下无需预览。注意：预览仅支持单选问题（不支持 multiSelect）。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 正面适用场景 | "ASCII mockups... Code snippets... Diagram variations... Configuration examples" | 通过列举四种具体的适用场景，帮助模型理解何时该使用预览功能。 |
| 2 | 反面约束 | "Do not use previews for simple preference questions where labels and descriptions suffice" | 明确排除了不适合的场景，防止模型对每个选项都添加预览，导致 UI 过载。 |
| 3 | 渲染行为说明 | "rendered as markdown in a monospace box... Multi-line text with newlines is supported" | 告知模型预览的渲染方式，使其生成的内容在呈现时格式正确。 |
| 4 | 功能限制标注 | "only supported for single-select questions (not multiSelect)" | 清晰的功能边界，防止模型在不支持的场景中使用该功能。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.45 | 新增 | 首次引入选项预览功能（当时字段名为 `markdown`） | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/36d2856" target="_blank">36d2856</a> |
| 2.1.69 | 更新 | 字段从 `markdown` 重命名为 `preview`；增加了等宽框渲染和多行文本支持的描述 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/2fde688" target="_blank">2fde688</a> |
