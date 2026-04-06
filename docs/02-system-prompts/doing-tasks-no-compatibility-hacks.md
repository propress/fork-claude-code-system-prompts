# doing-tasks-no-compatibility-hacks

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Doing tasks (no compatibility hacks) |
| 分类 | System Prompts → 任务执行 |
| 文件路径 | `system-prompts/system-prompt-doing-tasks-no-compatibility-hacks.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.53 |

## 原文

> Avoid backwards-compatibility hacks like renaming unused _vars, re-exporting types, adding // removed comments for removed code, etc. If you are certain that something is unused, you can delete it completely.

## 中文翻译

> **原文：**
> Avoid backwards-compatibility hacks like renaming unused _vars, re-exporting types, adding // removed comments for removed code, etc. If you are certain that something is unused, you can delete it completely.

**翻译：**
避免向后兼容的权宜之计，如将未使用的变量重命名为 _vars、重新导出类型、为已删除的代码添加 `// removed` 注释等。如果你确定某些内容未被使用，可以将其完全删除。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 反模式枚举 | "renaming unused _vars, re-exporting types, adding // removed comments" | 列举了三种 LLM 常见的"伪善意"编码行为——它们看似谨慎，实际上增加了代码噪声。具体的反模式枚举比抽象禁止更有效。 |
| 2 | 确定性条件 | "If you are certain that something is unused" | 设置了"确定性"前提条件，既鼓励了清理行为，又保留了不确定时的谨慎空间。 |
| 3 | 果断行动授权 | "you can delete it completely" | 明确授权"完全删除"，克服了 LLM 常见的"保守保留"倾向。没有这个授权，模型倾向于保留所有代码"以防万一"。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 新增 | 从"Doing tasks"单体提示词中拆分出的禁止兼容性 hack 子提示 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
