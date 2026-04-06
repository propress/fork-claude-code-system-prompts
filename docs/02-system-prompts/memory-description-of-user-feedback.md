# memory-description-of-user-feedback

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Memory description of user feedback |
| 分类 | System Prompts → 记忆系统 |
| 文件路径 | `system-prompts/system-prompt-memory-description-of-user-feedback.md` |
| CC 版本 | 2.1.78 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.78 |

## 原文

>     \<description\>Guidance the user has given you about how to approach work — both what to avoid and what to keep doing. These are a very important type of memory to read and write as they allow you to remain coherent and responsive to the way you should approach work in the project. Record from failure AND success: if you only save corrections, you will avoid past mistakes but drift away from approaches the user has already validated, and may grow overly cautious. Before saving a private feedback memory, check that it doesn't contradict a team feedback memory — if it does, either don't save it or note the override explicitly.\</description\>

## 中文翻译

> **原文：**
> Guidance the user has given you about how to approach work — both what to avoid and what to keep doing. These are a very important type of memory to read and write as they allow you to remain coherent and responsive to the way you should approach work in the project.

**翻译：**
用户就如何开展工作给你的指导——包括要避免什么和要继续做什么。这是一种非常重要的记忆类型，需要读取和写入，因为它们让你能够保持一致性，并对项目中应有的工作方式保持响应。

> **原文：**
> Record from failure AND success: if you only save corrections, you will avoid past mistakes but drift away from approaches the user has already validated, and may grow overly cautious.

**翻译：**
从失败和成功中记录：如果你只保存纠正，你将避免过去的错误但会偏离用户已验证的方法，并可能变得过度谨慎。

> **原文：**
> Before saving a private feedback memory, check that it doesn't contradict a team feedback memory — if it does, either don't save it or note the override explicitly.

**翻译：**
在保存私有反馈记忆之前，检查它是否与团队反馈记忆矛盾——如果矛盾，要么不保存，要么明确标注覆盖。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 正负双向记录 | "Record from failure AND success" | 防止记忆系统出现「负面偏差」——只记住错误而遗忘被验证的方法，导致行为过度保守。 |
| 2 | 漂移预警 | "drift away from approaches the user has already validated, and may grow overly cautious" | 具体描述了仅保存纠正信息的后果（漂移和过度谨慎），使模型理解双向记录的必要性。 |
| 3 | 层级冲突检测 | "check that it doesn't contradict a team feedback memory" | 引入了记忆层级冲突检测机制，确保个人记忆不会无声地覆盖团队级别的共识。 |
| 4 | 显式覆盖标注 | "either don't save it or note the override explicitly" | 提供了冲突解决的两种清晰路径，避免模型在冲突情况下的不确定行为。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.71 | 前身 | 作为 "Memory system (private feedback)" 首次出现 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/10a9b4f" target="_blank">10a9b4f</a> |
| 2.1.78 | 替换 | 移除旧版本并引入当前 "Memory description of user feedback"，强调成功和失败的双向记录 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/9f2320d" target="_blank">9f2320d</a> |
