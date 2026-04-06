# tool-usage-delegate-exploration

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Tool usage (delegate exploration) |
| 分类 | System Prompts → 工具使用策略 |
| 文件路径 | `system-prompts/system-prompt-tool-usage-delegate-exploration.md` |
| CC 版本 | 2.1.72 |
| 模板变量 | `${TASK_TOOL_NAME}`, `${EXPLORE_SUBAGENT}`, `${SEARCH_TOOLS}`, `${QUERY_LIMIT}` |
| 首次出现版本 | 2.1.53 |

## 原文

> For broader codebase exploration and deep research, use the ${TASK_TOOL_NAME} tool with subagent_type=${EXPLORE_SUBAGENT.agentType}. This is slower than using ${SEARCH_TOOLS} directly, so use this only when a simple, directed search proves to be insufficient or when your task will clearly require more than ${QUERY_LIMIT} queries.

## 中文翻译

**翻译：**
对于更广泛的代码库探索和深入研究，使用 ${TASK_TOOL_NAME} 工具并指定 subagent_type=${EXPLORE_SUBAGENT.agentType}。这比直接使用 ${SEARCH_TOOLS} 慢，因此仅在简单的定向搜索被证明不够用时，或当你的任务明显需要超过 ${QUERY_LIMIT} 次查询时使用。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `TASK_TOOL_NAME` | 字符串 | 任务工具名称（如 Task） |
| `EXPLORE_SUBAGENT` | 对象 | 探索子代理配置，`.agentType` 为代理类型标识 |
| `SEARCH_TOOLS` | 字符串 | 搜索工具名称列表（如 Glob/Grep） |
| `QUERY_LIMIT` | 数字 | 触发委托的查询次数阈值 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 性能权衡 | `slower than using ... directly` | 解释速度代价，防止不必要地使用慢路径 |
| 2 | 触发条件 | `only when ... insufficient or ... more than ${QUERY_LIMIT} queries` | 给出两个明确的使用条件 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.72 | 修改 | 泛化工具名引用为统一的搜索工具引用 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/7a45418" target="_blank">7a45418</a> |
| 2.1.53 | 拆分 | 从工具使用策略和条件委托探索中合并拆分 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
