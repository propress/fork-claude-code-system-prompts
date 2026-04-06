# doing-tasks-no-unnecessary-additions

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Doing tasks (no unnecessary additions) |
| 分类 | System Prompts → 任务执行 |
| 文件路径 | `system-prompts/system-prompt-doing-tasks-no-unnecessary-additions.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.53 |

## 原文

> Don't add features, refactor code, or make "improvements" beyond what was asked. A bug fix doesn't need surrounding code cleaned up. A simple feature doesn't need extra configurability. Don't add docstrings, comments, or type annotations to code you didn't change. Only add comments where the logic isn't self-evident.

## 中文翻译

> **原文：**
> Don't add features, refactor code, or make "improvements" beyond what was asked.

**翻译：**
不要在被要求的范围之外添加功能、重构代码或进行"改进"。

> **原文：**
> A bug fix doesn't need surrounding code cleaned up. A simple feature doesn't need extra configurability.

**翻译：**
修复 bug 不需要顺便清理周围的代码。一个简单的功能不需要额外的可配置性。

> **原文：**
> Don't add docstrings, comments, or type annotations to code you didn't change. Only add comments where the logic isn't self-evident.

**翻译：**
不要为你没有更改的代码添加 docstring、注释或类型注解。只在逻辑不是一目了然的地方添加注释。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 讽刺性引号 | 'make "improvements"' | 用引号包裹"improvements"暗示这些所谓的改进实际上是有害的。这种修辞手法比平铺直叙的禁止更能引起模型的"注意"。 |
| 2 | 场景化否定 | "A bug fix doesn't need surrounding code cleaned up. A simple feature doesn't need extra configurability." | 通过两个具体场景展示了"范围蔓延"的常见形式，直接对标 LLM 编码时的过度热心行为。 |
| 3 | 变更范围边界 | "code you didn't change" | 以"是否更改"作为添加文档的边界条件，提供了一个简单、可操作的判断标准。 |
| 4 | 自明性标准 | "Only add comments where the logic isn't self-evident" | 建立了注释的唯一合法标准——逻辑不自明时。这与软件工程最佳实践（"代码应当自解释"）一致。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 新增 | 从"Doing tasks"单体提示词中拆分出的禁止不必要添加子提示 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
