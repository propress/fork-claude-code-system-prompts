# tasklist-teammate-workflow

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: TaskList (teammate workflow) |
| 分类 | Tool Descriptions → Agent 工具 |
| 文件路径 | `system-prompts/tool-description-tasklist-teammate-workflow.md` |
| CC 版本 | 2.1.38 |
| 模板变量 | 无 |

## 原文

> ## Teammate Workflow
>
> When working as a teammate:
> 1. After completing your current task, call TaskList to find available work
> 2. Look for tasks with status 'pending', no owner, and empty blockedBy
> 3. **Prefer tasks in ID order** (lowest ID first) when multiple tasks are available, as earlier tasks often set up context for later ones
> 4. Claim an available task using TaskUpdate (set `owner` to your name), or wait for leader assignment
> 5. If blocked, focus on unblocking tasks or notify the team lead

## 中文翻译

> **原文：**
> ## Teammate Workflow
>
> When working as a teammate:

**翻译：**
## 队友工作流程

作为队友工作时：
1. 完成当前任务后，调用 TaskList 查找可用工作
2. 寻找状态为 'pending'、无所有者且 blockedBy 为空的任务
3. **优先按 ID 顺序选取任务**（最小 ID 优先），因为较早的任务通常为后续任务建立上下文
4. 使用 TaskUpdate 认领可用任务（将 `owner` 设为你的名字），或等待领导者分配
5. 如果被阻塞，专注于解除阻塞的任务或通知团队领导

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 有序工作流 | 5个编号步骤 | 为队友代理定义完成→查找→认领的标准循环 |
| 2 | ID 优先规则 | `Prefer tasks in ID order (lowest ID first)` | 避免随机选取导致依赖问题 |
| 3 | 阻塞处理 | `focus on unblocking tasks or notify the team lead` | 定义被阻塞时的两种应对策略 |
