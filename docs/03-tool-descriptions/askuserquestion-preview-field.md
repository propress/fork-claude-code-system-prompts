# askuserquestion-preview-field

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: AskUserQuestion (preview field) |
| 分类 | Tool Descriptions → 用户交互 |
| 文件路径 | `system-prompts/tool-description-askuserquestion-preview-field.md` |
| CC 版本 | 2.1.69 |
| 模板变量 | 无 |

## 原文

> Preview feature:
> Use the optional `preview` field on options when presenting concrete artifacts that users need to visually compare:
> - HTML mockups of UI layouts or components
> - Formatted code snippets showing different implementations
> - Visual comparisons or diagrams
>
> Preview content must be a self-contained HTML fragment (no <html>/<body> wrapper, no <script> or <style> tags — use inline style attributes instead). Do not use previews for simple preference questions where labels and descriptions suffice. Note: previews are only supported for single-select questions (not multiSelect).

## 中文翻译

> **原文：**
> Preview feature:
> Use the optional `preview` field on options when presenting concrete artifacts that users need to visually compare:
> - HTML mockups of UI layouts or components
> - Formatted code snippets showing different implementations
> - Visual comparisons or diagrams

**翻译：**
预览功能：
在呈现用户需要进行视觉比较的具体产物时，使用选项上的可选 `preview` 字段：
- UI 布局或组件的 HTML 模型
- 展示不同实现方式的格式化代码片段
- 视觉比较或图表

---

> **原文：**
> Preview content must be a self-contained HTML fragment (no <html>/<body> wrapper, no <script> or <style> tags — use inline style attributes instead). Do not use previews for simple preference questions where labels and descriptions suffice. Note: previews are only supported for single-select questions (not multiSelect).

**翻译：**
预览内容必须是自包含的 HTML 片段（无需 <html>/<body> 包装器，不使用 <script> 或 <style> 标签——改用内联 style 属性）。对于标签和描述已足够的简单偏好问题，不要使用预览。注意：预览仅支持单选问题（不支持 multiSelect）。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 结构化列表（Structured Enumeration） | `- HTML mockups... - Formatted code snippets... - Visual comparisons...` | 通过列表明确列出预览功能的三个适用场景，使模型清楚何时应使用此功能。 |
| 2 | 负面约束（Negative Constraint） | `no <html>/<body> wrapper, no <script> or <style> tags` | 明确禁止使用特定 HTML 标签，确保预览内容的安全性和自包含性。 |
| 3 | 范围限定（Scope Limitation） | `Do not use previews for simple preference questions where labels and descriptions suffice` | 限定预览功能的使用范围，避免在不必要的场景中过度使用，保持简洁的用户体验。 |
| 4 | 示例引导（Example-driven Guidance） | `use inline style attributes instead` | 提供替代方案指导，告诉模型在不能使用 <style> 标签时应如何实现样式。 |
