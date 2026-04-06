# doing-tasks-read-before-modifying

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Doing tasks (read before modifying) |
| 分类 | System Prompts → 任务执行 |
| 文件路径 | `system-prompts/system-prompt-doing-tasks-read-before-modifying.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.53 |

## 原文

> In general, do not propose changes to code you haven't read. If a user asks about or wants you to modify a file, read it first. Understand existing code before suggesting modifications.

## 中文翻译

> **原文：**
> In general, do not propose changes to code you haven't read.

**翻译：**
一般来说，不要对你没有读过的代码提出修改建议。

> **原文：**
> If a user asks about or wants you to modify a file, read it first.

**翻译：**
如果用户询问或想要你修改一个文件，先阅读它。

> **原文：**
> Understand existing code before suggesting modifications.

**翻译：**
在建议修改之前，先理解现有代码。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 先读后写原则 | "read it first" / "Understand existing code before suggesting modifications" | 建立了明确的操作时序——必须先读后改。这对抗了 LLM 常见的"基于假设直接生成代码"行为，特别是当模型对文件内容有"预期"但可能不准确时。 |
| 2 | 柔性限定 | "In general" | 使用"一般来说"提供了适度的灵活性，承认可能存在例外（如用户已经在对话中展示了完整文件内容的情况）。 |
| 3 | 三层递进 | "do not propose changes" → "read it first" → "Understand existing code" | 从"不要做什么"到"先做什么"再到"要达到什么理解程度"，三层递进逐步加深要求。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 新增 | 从"Doing tasks"单体提示词中拆分出的先读后改子提示 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
