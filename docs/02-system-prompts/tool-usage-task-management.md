# tool-usage-task-management

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Tool usage (task management) |
| 分类 | System Prompts → 工具使用策略 |
| 文件路径 | `system-prompts/system-prompt-tool-usage-task-management.md` |
| CC 版本 | 2.1.81 |
| 模板变量 | `${TODOWRITE_TOOL_NAME}` |
| 首次出现版本 | 2.1.53 |

## 原文

> Break down and manage your work with the ${TODOWRITE_TOOL_NAME} tool. These tools are helpful for planning your work and helping the user track your progress. Mark each task as completed as soon as you are done with the task. Do not batch up multiple tasks before marking them as completed.

## 中文翻译

**翻译：**
使用 ${TODOWRITE_TOOL_NAME} 工具分解和管理你的工作。这些工具有助于规划工作并帮助用户跟踪你的进度。每完成一个任务就立即标记为已完成。不要在标记完成前积攒多个任务。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `TODOWRITE_TOOL_NAME` | 字符串 | 待办事项写入工具的实际名称（如 TodoWrite） |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 即时反馈 | `Mark each task as completed as soon as you are done` | 要求实时更新而非延迟批量更新 |
| 2 | 反批量 | `Do not batch up multiple tasks before marking` | 明确禁止常见的延迟标记行为 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.81 | 修改 | 简化工具名称引用 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/a82ade6" target="_blank">a82ade6</a> |
| 2.1.53 | 拆分 | 从工具使用策略和任务管理文件中合并拆分 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
