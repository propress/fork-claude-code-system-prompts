# 05 — System Reminders 索引

本目录包含 Claude Code 所有 37 个系统提醒（System Reminder）的中文解读文档。

系统提醒是在对话过程中动态注入的消息，用于向模型提供上下文、状态变更通知或行为指导。

## 分类总览

### 计划模式 (7 files)
| 文件 | 说明 |
|------|------|
| [plan-mode-is-active-5-phase](plan-mode-is-active-5-phase.md) | 5 阶段计划模式激活 |
| [plan-mode-is-active-iterative](plan-mode-is-active-iterative.md) | 迭代式计划模式 |
| [plan-mode-is-active-subagent](plan-mode-is-active-subagent.md) | 子代理计划模式 |
| [plan-mode-re-entry](plan-mode-re-entry.md) | 计划模式重入 |
| [plan-file-reference](plan-file-reference.md) | 计划文件引用 |
| [exited-plan-mode](exited-plan-mode.md) | 已退出计划模式 |
| [ultraplan-mode](ultraplan-mode.md) | Ultraplan 模式 |
| [verify-plan-reminder](verify-plan-reminder.md) | 验证计划提醒 |

### 文件状态 (6 files)
| 文件 | 说明 |
|------|------|
| [file-exists-but-empty](file-exists-but-empty.md) | 文件存在但为空 |
| [file-modified-by-user-or-linter](file-modified-by-user-or-linter.md) | 文件被用户/linter 修改 |
| [file-opened-in-ide](file-opened-in-ide.md) | 文件在 IDE 中打开 |
| [file-shorter-than-offset](file-shorter-than-offset.md) | 文件短于偏移量 |
| [file-truncated](file-truncated.md) | 文件被截断 |
| [compact-file-reference](compact-file-reference.md) | 压缩文件引用 |

### 团队协作 (5 files)
| 文件 | 说明 |
|------|------|
| [agent-mention](agent-mention.md) | 代理被 @ 提及 |
| [team-coordination](team-coordination.md) | 团队协调 |
| [team-shutdown](team-shutdown.md) | 团队关闭 |
| [task-tools-reminder](task-tools-reminder.md) | 任务工具提醒 |
| [todowrite-reminder](todowrite-reminder.md) | TodoWrite 提醒 |

### Hook 系统 (5 files)
| 文件 | 说明 |
|------|------|
| [hook-additional-context](hook-additional-context.md) | Hook 附加上下文 |
| [hook-blocking-error](hook-blocking-error.md) | Hook 阻塞错误 |
| [hook-stopped-continuation](hook-stopped-continuation.md) | Hook 停止继续 |
| [hook-stopped-continuation-prefix](hook-stopped-continuation-prefix.md) | Hook 停止继续前缀 |
| [hook-success](hook-success.md) | Hook 成功 |

### 会话管理 (5 files)
| 文件 | 说明 |
|------|------|
| [session-continuation](session-continuation.md) | 会话继续 |
| [token-usage](token-usage.md) | Token 使用量 |
| [usd-budget](usd-budget.md) | USD 预算 |
| [output-style-active](output-style-active.md) | 输出风格激活 |
| [btw-side-question](btw-side-question.md) | 顺便问一下（旁问） |

### 技能与工具 (8 files)
| 文件 | 说明 |
|------|------|
| [invoked-skills](invoked-skills.md) | 已调用的技能 |
| [lines-selected-in-ide](lines-selected-in-ide.md) | IDE 中选中的行 |
| [mcp-resource-no-content](mcp-resource-no-content.md) | MCP 资源无内容 |
| [mcp-resource-no-displayable-content](mcp-resource-no-displayable-content.md) | MCP 资源无可显示内容 |
| [memory-file-contents](memory-file-contents.md) | 记忆文件内容 |
| [nested-memory-contents](nested-memory-contents.md) | 嵌套记忆内容 |
| [new-diagnostics-detected](new-diagnostics-detected.md) | 检测到新诊断 |
| [malware-analysis-after-read-tool-call](malware-analysis-after-read-tool-call.md) | 读取后恶意软件分析 |
