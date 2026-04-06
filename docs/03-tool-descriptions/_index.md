# 03 — Tool Descriptions 索引

本目录包含 Claude Code 所有 73 个工具描述的中文解读文档。

## 分类总览

### Bash 工具 (40 files)
核心 Bash 工具描述及其约束，包括：
- **概述**: [bash-overview](bash-overview.md)
- **替代方案**: bash-alternative-* (6 files) — 通信、内容搜索、编辑文件、文件搜索、读文件、写文件
- **Git 操作**: bash-git-* (4 files) — 避免破坏性操作、提交与 PR、不跳过 hooks、优先新提交
- **沙箱**: bash-sandbox-* (16 files) — 完整的沙箱安全策略
- **Sleep 控制**: bash-sleep-* (4 files) — 保持短暂、禁止轮询、立即运行、使用检查命令
- **其他**: 维护 cwd、无换行、并行/顺序命令、引用路径、超时、验证父目录、工作目录

### Agent 工具 (11 files)
| 文件 | 说明 |
|------|------|
| [agent-usage-notes](agent-usage-notes.md) | Agent 使用说明 |
| [agent-when-to-launch-subagents](agent-when-to-launch-subagents.md) | 何时启动子代理 |
| [sendmessagetool](sendmessagetool.md) | 发送消息（团队版） |
| [sendmessagetool-non-agent-teams](sendmessagetool-non-agent-teams.md) | 发送消息（非团队版） |
| [skill](skill.md) | 技能执行工具 |
| [taskcreate](taskcreate.md) | 创建任务 |
| [tasklist-teammate-workflow](tasklist-teammate-workflow.md) | 队友工作流 |
| [teamdelete](teamdelete.md) | 删除团队 |
| [teammatetool](teammatetool.md) | 团队管理 |
| [todowrite](todowrite.md) | 待办列表管理 |
| [toolsearch-second-part](toolsearch-second-part.md) | 工具搜索（延迟加载） |

### 文件操作 (4 files)
| 文件 | 说明 |
|------|------|
| [edit](edit.md) | 编辑文件 |
| [write](write.md) | 写入文件 |
| [readfile](readfile.md) | 读取文件 |
| [notebookedit](notebookedit.md) | Notebook 编辑 |

### 搜索工具 (2 files)
| 文件 | 说明 |
|------|------|
| [grep](grep.md) | 内容搜索 |
| [lsp](lsp.md) | 语言服务协议 |

### 计划模式 (4 files)
| 文件 | 说明 |
|------|------|
| [enterplanmode](enterplanmode.md) | 进入计划模式 |
| [exitplanmode](exitplanmode.md) | 退出计划模式 |
| [enterworktree](enterworktree.md) | 进入工作树 |
| [exitworktree](exitworktree.md) | 退出工作树 |

### 通用工具 (6 files)
| 文件 | 说明 |
|------|------|
| [computer](computer.md) | 计算机使用 |
| [config](config.md) | 配置管理 |
| [croncreate](croncreate.md) | 定时任务 |
| [powershell](powershell.md) | PowerShell |
| [webfetch](webfetch.md) | 网页获取 |
| [websearch](websearch.md) | 网络搜索 |

### 用户交互 (2 files)
| 文件 | 说明 |
|------|------|
| [askuserquestion](askuserquestion.md) | 向用户提问 |
| [askuserquestion-preview-field](askuserquestion-preview-field.md) | 提问预览字段 |
| [request_teach_access-part-of-teach-mode](request_teach_access-part-of-teach-mode.md) | 请求教学访问 |
