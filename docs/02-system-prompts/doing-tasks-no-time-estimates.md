# doing-tasks-no-time-estimates

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Doing tasks (no time estimates) |
| 分类 | System Prompts → 任务执行 |
| 文件路径 | `system-prompts/system-prompt-doing-tasks-no-time-estimates.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.53（源自更早版本的"No time estimates"部分） |

## 原文

> Avoid giving time estimates or predictions for how long tasks will take, whether for your own work or for users planning projects. Focus on what needs to be done, not how long it might take.

## 中文翻译

> **原文：**
> Avoid giving time estimates or predictions for how long tasks will take, whether for your own work or for users planning projects. Focus on what needs to be done, not how long it might take.

**翻译：**
避免给出任务耗时的时间估计或预测，无论是针对你自己的工作还是用户的项目规划。专注于需要做什么，而不是可能需要多长时间。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 双范围禁止 | "whether for your own work or for users planning projects" | 明确禁止两个方向的时间估计：(1) Claude 自身工作的估时，如"这大约需要5分钟"；(2) 帮用户做项目规划时的估时。覆盖了所有可能的场景。 |
| 2 | 注意力重定向 | "Focus on what needs to be done, not how long it might take" | 不只是禁止某个行为，还将注意力重定向到正确的行为上。这比单纯的"不要做X"更有效，因为它给了模型替代行为。 |
| 3 | 不确定性认知 | 隐含理由：LLM 无法可靠地预估任务耗时 | 这条规则反映了一个务实的认知——LLM 的时间估计不可靠，给出不准确的估计比不给更糟糕。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.9 | 修改 | 在主系统提示词中将"Planning without timelines"重命名为"No time estimates"，扩展为同时禁止 Claude 自身工作的时间估计 | — |
| 2.1.53 | 新增 | 从"Doing tasks"（原"Tone and style"）单体提示词中拆分为独立子提示 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
