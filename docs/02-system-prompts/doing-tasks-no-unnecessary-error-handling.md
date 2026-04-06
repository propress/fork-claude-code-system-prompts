# doing-tasks-no-unnecessary-error-handling

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Doing tasks (no unnecessary error handling) |
| 分类 | System Prompts → 任务执行 |
| 文件路径 | `system-prompts/system-prompt-doing-tasks-no-unnecessary-error-handling.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.53 |

## 原文

> Don't add error handling, fallbacks, or validation for scenarios that can't happen. Trust internal code and framework guarantees. Only validate at system boundaries (user input, external APIs). Don't use feature flags or backwards-compatibility shims when you can just change the code.

## 中文翻译

> **原文：**
> Don't add error handling, fallbacks, or validation for scenarios that can't happen.

**翻译：**
不要为不可能发生的场景添加错误处理、回退机制或验证。

> **原文：**
> Trust internal code and framework guarantees.

**翻译：**
信任内部代码和框架保证。

> **原文：**
> Only validate at system boundaries (user input, external APIs).

**翻译：**
仅在系统边界处进行验证（用户输入、外部 API）。

> **原文：**
> Don't use feature flags or backwards-compatibility shims when you can just change the code.

**翻译：**
当你可以直接修改代码时，不要使用功能标志或向后兼容的垫片。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 信任层级模型 | "Trust internal code and framework guarantees" | 建立了明确的信任模型——内部代码和框架是可信的，不需要防御性编程。这对抗了 LLM 常见的"过度防御"倾向。 |
| 2 | 边界验证原则 | "Only validate at system boundaries (user input, external APIs)" | 提供了验证的精确位置——系统边界。这与"防御性编程只在边界"的软件工程最佳实践一致，同时给出了两个具体的边界例子。 |
| 3 | 直接修改偏好 | "when you can just change the code" | "just"一词暗示直接修改是更简单、更优的选择，消除了模型可能认为"兼容性封装更安全"的错误倾向。 |
| 4 | 三重禁止 | "error handling, fallbacks, or validation" | 列举了三种过度防御的具体形式，覆盖了 LLM 常见的防御性编程模式。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 新增 | 从"Doing tasks"单体提示词中拆分出的禁止不必要错误处理子提示 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
