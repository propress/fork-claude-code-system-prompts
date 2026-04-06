# tool-usage-reserve-bash

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Tool usage (reserve Bash) |
| 分类 | System Prompts → 工具使用策略 |
| 文件路径 | `system-prompts/system-prompt-tool-usage-reserve-bash.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${BASH_TOOL_NAME}` |
| 首次出现版本 | 2.1.53 |

## 原文

> Reserve using the ${BASH_TOOL_NAME} exclusively for system commands and terminal operations that require shell execution. If you are unsure and there is a relevant dedicated tool, default to using the dedicated tool and only fallback on using the ${BASH_TOOL_NAME} tool for these if it is absolutely necessary.

## 中文翻译

**翻译：**
将 ${BASH_TOOL_NAME} 专门保留给需要 shell 执行的系统命令和终端操作。如果不确定且有相关的专用工具，默认使用专用工具，仅在绝对必要时才回退使用 ${BASH_TOOL_NAME} 工具。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `BASH_TOOL_NAME` | 字符串 | Bash 工具的实际名称（如 Bash） |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 最后手段原则 | `only fallback ... if it is absolutely necessary` | 建立明确的工具优先级层次 |
| 2 | 默认值设定 | `default to using the dedicated tool` | 在不确定时选择更安全的默认行为 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 拆分 | 从工具使用策略大文件中拆分 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
