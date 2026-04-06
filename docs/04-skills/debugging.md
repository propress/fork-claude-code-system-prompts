# debugging

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: Debugging |
| 分类 | Skills → 代码质量 |
| 文件路径 | `system-prompts/skill-debugging.md` |
| CC 版本 | 2.1.71 |
| 模板变量 | `${DEBUG_LOGGING_WAS_ALREADY_ACTIVE}`、`${DEBUG_LOG_PATH}`、`${DEBUG_LOG_SUMMARY}`、`${ISSUE_DESCRIPTION}`、`${GET_SETTINGS_FILE_PATH_FN}`、`${LOG_LINE_COUNT}`、`${CLAUDE_CODE_GUIDE_SUBAGENT_NAME}` |

## 原文（摘要）

较短文件（49 行），完整收录关键内容：

> # Debug Skill
>
> Help the user debug an issue they're encountering in this current Claude Code session.

### 调试日志刚启用（条件块）

> Debug logging was OFF for this session until now. Nothing prior to this /debug invocation was captured.
>
> Tell the user that debug logging is now active at `${DEBUG_LOG_PATH}`, ask them to reproduce the issue, then re-read the log.

### 会话调试日志

> The debug log for the current session is at: `${DEBUG_LOG_PATH}`
>
> ${DEBUG_LOG_SUMMARY}
>
> For additional context, grep for [ERROR] and [WARN] lines across the full file.

### 问题描述

> ${ISSUE_DESCRIPTION||"The user did not describe a specific issue. Read the debug log and summarize any errors, warnings, or notable issues."}

### 设置

> Remember that settings are in:
> * user - ${GET_SETTINGS_FILE_PATH_FN("userSettings")}
> * project - ${GET_SETTINGS_FILE_PATH_FN("projectSettings")}
> * local - ${GET_SETTINGS_FILE_PATH_FN("localSettings")}

### 指令

> 1. Review the user's issue description
> 2. The last ${LOG_LINE_COUNT} lines show the debug file format. Look for [ERROR] and [WARN] entries, stack traces, and failure patterns across the file
> 3. Consider launching the ${CLAUDE_CODE_GUIDE_SUBAGENT_NAME} subagent to understand the relevant Claude Code features
> 4. Explain what you found in plain language
> 5. Suggest concrete fixes or next steps

## 中文翻译

# 调试 Skill

帮助用户调试他们在当前 Claude Code 会话中遇到的问题。

### 调试日志刚启用

（当 `${DEBUG_LOGGING_WAS_ALREADY_ACTIVE}` 为 false 时显示此部分）

本会话的调试日志此前处于关闭状态。在此 `/debug` 调用之前没有任何内容被捕获。

告诉用户调试日志现已在 `${DEBUG_LOG_PATH}` 激活，请他们重现问题，然后重新读取日志。如果他们无法重现，也可以使用 `claude --debug` 重新启动以从启动时捕获日志。

### 会话调试日志

当前会话的调试日志在：`${DEBUG_LOG_PATH}`

查看调试日志摘要，并在完整文件中 grep 搜索 [ERROR] 和 [WARN] 行以获取更多上下文。

### 问题描述

如果用户描述了具体问题，则使用该描述；如果用户没有描述具体问题，则阅读调试日志并总结任何错误、警告或值得注意的问题。

### 设置文件位置

- 用户设置 - `${GET_SETTINGS_FILE_PATH_FN("userSettings")}`
- 项目设置 - `${GET_SETTINGS_FILE_PATH_FN("projectSettings")}`
- 本地设置 - `${GET_SETTINGS_FILE_PATH_FN("localSettings")}`

### 操作指令

1. 审查用户的问题描述
2. 最后 ${LOG_LINE_COUNT} 行展示了调试文件格式。在文件中查找 [ERROR] 和 [WARN] 条目、堆栈跟踪和失败模式
3. 考虑启动 ${CLAUDE_CODE_GUIDE_SUBAGENT_NAME} 子 Agent 以理解相关的 Claude Code 功能
4. 用通俗语言解释发现的内容
5. 建议具体的修复方案或下一步操作

## 📋 模板变量说明

| 变量 | 说明 |
|------|------|
| `${DEBUG_LOGGING_WAS_ALREADY_ACTIVE}` | 布尔值，指示调试日志在调用 `/debug` 前是否已经激活。控制"日志刚启用"部分的显示 |
| `${DEBUG_LOG_PATH}` | 当前会话调试日志文件的文件系统路径 |
| `${DEBUG_LOG_SUMMARY}` | 调试日志的摘要内容，运行时注入 |
| `${ISSUE_DESCRIPTION}` | 用户描述的问题，如为空则使用默认的"阅读日志并总结"指令 |
| `${GET_SETTINGS_FILE_PATH_FN}` | 函数引用，接受设置类型参数返回对应文件路径 |
| `${LOG_LINE_COUNT}` | 在提示词中展示的调试日志尾部行数 |
| `${CLAUDE_CODE_GUIDE_SUBAGENT_NAME}` | Claude Code 指南子 Agent 的名称，可启动以获取 Claude Code 功能的上下文 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 条件内容注入 | `${DEBUG_LOGGING_WAS_ALREADY_ACTIVE?"":\`...\`}` | 使用三元表达式动态控制提示词内容，避免在日志已激活时显示无关指导 |
| 2 | 默认值回退 | `${ISSUE_DESCRIPTION\|\|"The user did not describe a specific issue..."}` | 为空输入提供有意义的回退行为，确保即使用户未描述问题也能有效工作 |
| 3 | 函数式模板变量 | `${GET_SETTINGS_FILE_PATH_FN("userSettings")}` | 使用函数引用而非静态路径，适应不同系统的设置文件位置 |
| 4 | 分步调试流程 | 五步骤：审查 → 查找日志 → 启动子 Agent → 解释 → 建议 | 结构化调试流程防止 LLM 跳过关键步骤直接给出推测性答案 |
| 5 | 子 Agent 委托 | "Consider launching the ${CLAUDE_CODE_GUIDE_SUBAGENT_NAME} subagent" | 将 Claude Code 功能理解委托给专门的子 Agent，避免当前 Skill 承载过多上下文 |
