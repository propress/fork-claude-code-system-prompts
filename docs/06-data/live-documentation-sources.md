# live-documentation-sources

| 属性 | 值 |
|------|-----|
| 原始名称 | Data: Live documentation sources |
| 分类 | Data → 会话管理 |
| 文件路径 | `system-prompts/data-live-documentation-sources.md` |
| CC 版本 | 2.1.91 |
| 模板变量 | 无 |

## 概述

WebFetch URL 集合，用于从官方源获取最新的 Claude API 和 Agent SDK 文档。此文件共 133 行，主要作为 Claude Code 的内置参考数据。

## 原文（摘要）

此数据文件包含以下主要章节：

- ## When to Use WebFetch
- ## Claude API Documentation URLs
- ## Claude API SDK Repositories
- ## Agent SDK Documentation URLs
- ## Fallback Strategy

## 内容结构

此文件是 Claude Code 内置的参考数据文件，在技能（Skill）被调用时作为上下文注入。包含代码示例、API 端点说明和最佳实践指导。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 内置参考数据 | 完整 SDK/API 文档作为上下文 | 将官方文档直接注入上下文，避免模型凭记忆生成可能过时的 API 用法 |
| 2 | 代码示例驱动 | 包含可直接使用的代码片段 | 减少模型推理负担，提供可复制粘贴的参考实现 |
