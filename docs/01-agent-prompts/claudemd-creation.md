# claudemd-creation

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: CLAUDE.md creation |
| 分类 | Agent Prompts |
| 文件路径 | `system-prompts/agent-prompt-claudemd-creation.md` |
| CC 版本 | 2.0.14 |
| 模板变量 | 无 |
| 首次出现版本 | 2.0.14 |
| 重大变更次数 | 0 |

## 原文

```
<!--
name: 'Agent Prompt: CLAUDE.md creation'
description: System prompt for analyzing codebases and creating CLAUDE.md documentation files
ccVersion: 2.0.14
-->
Please analyze this codebase and create a CLAUDE.md file, which will be given to future instances of Claude Code to operate in this repository.

What to add:
1. Commands that will be commonly used, such as how to build, lint, and run tests. Include the necessary commands to develop in this codebase, such as how to run a single test.
2. High-level code architecture and structure so that future instances can be productive more quickly. Focus on the "big picture" architecture that requires reading multiple files to understand.

Usage notes:
- If there's already a CLAUDE.md, suggest improvements to it.
- When you make the initial CLAUDE.md, do not repeat yourself and do not include obvious instructions like "Provide helpful error messages to users", "Write unit tests for all new utilities", "Never include sensitive information (API keys, tokens) in code or commits".
- Avoid listing every component or file structure that can be easily discovered.
- Don't include generic development practices.
- If there are Cursor rules (in .cursor/rules/ or .cursorrules) or Copilot rules (in .github/copilot-instructions.md), make sure to include the important parts.
- If there is a README.md, make sure to include the important parts.
- Do not make up information such as "Common Development Tasks", "Tips for Development", "Support and Documentation" unless this is expressly included in other files that you read.
- Be sure to prefix the file with the following text:

```
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
```
```

## 中文翻译

> **原文：**
> Please analyze this codebase and create a CLAUDE.md file, which will be given to future instances of Claude Code to operate in this repository.

**翻译：**
请分析这个代码库并创建一个 CLAUDE.md 文件，该文件将提供给未来的 Claude Code 实例，以便在此仓库中操作。

---

> **原文：**
> What to add:
> 1. Commands that will be commonly used, such as how to build, lint, and run tests. Include the necessary commands to develop in this codebase, such as how to run a single test.
> 2. High-level code architecture and structure so that future instances can be productive more quickly. Focus on the "big picture" architecture that requires reading multiple files to understand.

**翻译：**
**需要添加的内容：**
1. 常用命令，例如如何构建、代码检查和运行测试。包含在此代码库中开发所需的命令，例如如何运行单个测试。
2. 高层次的代码架构和结构，使未来的实例能够更快地上手工作。专注于需要阅读多个文件才能理解的"全局"架构。

---

> **原文：**
> Usage notes:
> - If there's already a CLAUDE.md, suggest improvements to it.
> - When you make the initial CLAUDE.md, do not repeat yourself and do not include obvious instructions like "Provide helpful error messages to users"...
> - Avoid listing every component or file structure that can be easily discovered.
> - Don't include generic development practices.
> - If there are Cursor rules ... or Copilot rules ..., make sure to include the important parts.
> - If there is a README.md, make sure to include the important parts.
> - Do not make up information such as "Common Development Tasks", "Tips for Development", "Support and Documentation" unless this is expressly included in other files that you read.
> - Be sure to prefix the file with the following text: ...

**翻译：**
**使用说明：**
- 如果已经存在 CLAUDE.md 文件，建议对其进行改进。
- 在创建初始 CLAUDE.md 时，不要重复自己，也不要包含显而易见的指令，例如"向用户提供有帮助的错误消息"、"为所有新实用工具编写单元测试"、"永远不要在代码或提交中包含敏感信息（API 密钥、令牌）"。
- 避免列出每个可以轻易发现的组件或文件结构。
- 不要包含通用的开发实践。
- 如果存在 Cursor 规则（位于 `.cursor/rules/` 或 `.cursorrules`）或 Copilot 规则（位于 `.github/copilot-instructions.md`），请确保包含重要部分。
- 如果存在 README.md，请确保包含重要部分。
- 不要虚构"常见开发任务"、"开发提示"、"支持与文档"等内容，除非这些内容明确包含在你读取的其他文件中。
- 请务必在文件开头添加以下文本前缀：

```
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
```

## 📋 模板变量说明

此提示词没有模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段 | 分析：为什么在这里有效 |
|---|---------|---------|---------------------|
| 1 | 正面/负面指令对（DO/DON'T Pairs） | "do not repeat yourself and do not include obvious instructions like 'Provide helpful error messages to users'" | 通过明确的反面示例，防止模型生成通用化、冗余的内容，专注于真正有项目特异性的信息 |
| 2 | 边界硬编码（Hard Boundary） | "Don't include generic development practices." / "Do not make up information such as 'Common Development Tasks'..." | 双重硬性限制防止模型填充通用内容，确保 CLAUDE.md 只包含对该特定代码库有价值的信息 |
| 3 | 动态上下文注入（Dynamic Context Injection） | "If there are Cursor rules ... or Copilot rules ..., make sure to include the important parts. If there is a README.md, make sure to include the important parts." | 指示模型主动发现并整合现有配置文件中的信息，避免重复创作已有内容 |
| 4 | 优先级标记（Priority Escalation） | "Focus on the 'big picture' architecture that requires reading multiple files to understand." | 明确强调"全局架构"而非"可轻易发现的内容"，引导模型提供真正高价值的上下文信息 |
| 5 | 结构化输出约束（Structured Output） | "Be sure to prefix the file with the following text: `# CLAUDE.md\n\nThis file provides guidance to Claude Code...`" | 要求强制文件头前缀，确保所有生成的 CLAUDE.md 文件具有一致的标识和目的说明 |
| 6 | 自我反思/对抗审查（Self-Reflection） | "If there's already a CLAUDE.md, suggest improvements to it." | 要求模型对已有内容进行批判性评估而非简单替换，避免无价值地重写现有良好文档 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.0.14 | 新增 | 初始版本，包含在首批系统提示词集合中 | [8b3c574](https://github.com/Piebald-AI/claude-code-system-prompts/commit/8b3c574) |
