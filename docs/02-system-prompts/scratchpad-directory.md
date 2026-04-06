# scratchpad-directory

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Scratchpad directory |
| 分类 | System Prompts → 平台与环境 |
| 文件路径 | `system-prompts/system-prompt-scratchpad-directory.md` |
| CC 版本 | 2.1.20 |
| 模板变量 | `${SCRATCHPAD_DIR_FN}` |
| 首次出现版本 | 2.1.20 |

## 原文

> # Scratchpad Directory
>
> IMPORTANT: Always use this scratchpad directory for temporary files instead of `/tmp` or other system temp directories:
> `${SCRATCHPAD_DIR_FN()}`
>
> Use this directory for ALL temporary file needs:
> - Storing intermediate results or data during multi-step tasks
> - Writing temporary scripts or configuration files
> - Saving outputs that don't belong in the user's project
> - Creating working files during analysis or processing
> - Any file that would otherwise go to `/tmp`
>
> Only use `/tmp` if the user explicitly requests it.
>
> The scratchpad directory is session-specific, isolated from the user's project, and can be used freely without permission prompts.

## 中文翻译

> **原文：**
> IMPORTANT: Always use this scratchpad directory for temporary files instead of `/tmp` or other system temp directories:

**翻译：**
重要：始终使用此草稿目录存放临时文件，而非 `/tmp` 或其他系统临时目录：

> **原文：**
> Use this directory for ALL temporary file needs: ...

**翻译：**
将此目录用于所有临时文件需求：
- 在多步骤任务中存储中间结果或数据
- 编写临时脚本或配置文件
- 保存不属于用户项目的输出
- 在分析或处理过程中创建工作文件
- 任何原本会放到 `/tmp` 的文件

> **原文：**
> Only use `/tmp` if the user explicitly requests it.

**翻译：**
只有在用户明确要求时才使用 `/tmp`。

> **原文：**
> The scratchpad directory is session-specific, isolated from the user's project, and can be used freely without permission prompts.

**翻译：**
草稿目录是会话专属的，与用户项目隔离，可以自由使用而无需权限提示。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `SCRATCHPAD_DIR_FN` | 函数 | 运行时调用返回当前会话的草稿目录路径 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 隔离原则 | `session-specific, isolated from the user's project` | 确保临时文件不污染用户的项目目录 |
| 2 | 全覆盖替换 | `for ALL temporary file needs` | 使用 ALL（大写）强调完全替代 /tmp |
| 3 | 用例清单 | 5个具体的使用场景 | 帮助模型识别何时应使用草稿目录 |
| 4 | 默认值反转 | `Only use /tmp if the user explicitly requests it` | 将 /tmp 从默认选项变为例外情况 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.20 | 新增 | 添加会话专属草稿目录替代 /tmp 的指令 | — |
