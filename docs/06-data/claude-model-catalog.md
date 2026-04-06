# claude-model-catalog

| 属性 | 值 |
|------|-----|
| 原始名称 | Data: Claude model catalog |
| 分类 | Data → 模型信息 |
| 文件路径 | `system-prompts/data-claude-model-catalog.md` |
| CC 版本 | 2.1.79 |
| 模板变量 | 无 |

## 概述

Claude 模型目录，包含当前和旧版模型的精确 ID、别名、上下文窗口和定价。此文件共 124 行，主要作为 Claude Code 的内置参考数据。

## 原文（摘要）

此数据文件包含以下主要章节：

- ## Programmatic Model Discovery
- ## Current Models (recommended)
- ## Legacy Models (still active)
- ## Deprecated Models (retiring soon)
- ## Retired Models (no longer available)
- ## Resolving User Requests

## 内容结构

此文件是 Claude Code 内置的参考数据文件，在技能（Skill）被调用时作为上下文注入。包含代码示例、API 端点说明和最佳实践指导。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 内置参考数据 | 完整 SDK/API 文档作为上下文 | 将官方文档直接注入上下文，避免模型凭记忆生成可能过时的 API 用法 |
| 2 | 代码示例驱动 | 包含可直接使用的代码片段 | 减少模型推理负担，提供可复制粘贴的参考实现 |
