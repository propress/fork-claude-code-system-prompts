# one-of-six-rules-for-using-sleep-command

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: One of six rules for using sleep command |
| 分类 | System Prompts → 命令使用规则 |
| 文件路径 | `system-prompts/system-prompt-one-of-six-rules-for-using-sleep-command.md` |
| CC 版本 | 2.1.75 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.75 |

## 原文

> Do not retry failing commands in a sleep loop — diagnose the root cause.

## 中文翻译

> **原文：**
> Do not retry failing commands in a sleep loop — diagnose the root cause.

**翻译：**
不要在 sleep 循环中重试失败的命令——诊断根本原因。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 简洁禁令 | "Do not retry failing commands in a sleep loop" | 用一句话清楚地禁止了一种常见的反模式（sleep 重试循环），不需要冗长的解释。 |
| 2 | 替代行为指引 | "diagnose the root cause" | 不仅说了「不要做什么」，还立即给出了「应该做什么」——诊断根本原因，使模型有明确的替代行为路径。 |
| 3 | 模块化规则 | 从原有的 6 条 sleep 规则中独立出来 | 作为独立文件便于条件化加载，不同场景下可以选择性地包含或排除此规则。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 前身 | 作为 Bash 工具描述中 sleep 相关规则的一部分存在 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
| 2.1.75 | 独立 | 从 Bash 工具 sleep 规则中拆分为独立的系统提示词文件 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/97ce0c2" target="_blank">97ce0c2</a> |
