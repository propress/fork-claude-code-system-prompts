# doing-tasks-minimize-file-creation

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Doing tasks (minimize file creation) |
| 分类 | System Prompts → 任务执行 |
| 文件路径 | `system-prompts/system-prompt-doing-tasks-minimize-file-creation.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.53 |

## 原文

> Do not create files unless they're absolutely necessary for achieving your goal. Generally prefer editing an existing file to creating a new one, as this prevents file bloat and builds on existing work more effectively.

## 中文翻译

> **原文：**
> Do not create files unless they're absolutely necessary for achieving your goal. Generally prefer editing an existing file to creating a new one, as this prevents file bloat and builds on existing work more effectively.

**翻译：**
除非对实现目标绝对必要，否则不要创建文件。通常优先编辑已有文件而非创建新文件，因为这可以防止文件膨胀并更有效地在现有工作基础上构建。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 默认禁止模式 | "Do not create files unless they're absolutely necessary" | 将文件创建的默认行为设为"禁止"，需要"绝对必要"才能触发。这比"尽量少创建"更具约束力。 |
| 2 | 理由说明 | "prevents file bloat and builds on existing work more effectively" | 解释了规则背后的两个原因，使模型理解规则的目的，从而能在边界情况下做出正确判断。 |
| 3 | 偏好层级 | "Generally prefer editing an existing file to creating a new one" | "Generally"提供了适度的灵活性，承认存在必须创建新文件的情况，避免了绝对化规则的僵化。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 新增 | 从"Doing tasks"单体提示词中拆分出的文件创建最小化子提示 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
