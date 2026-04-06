# bash-sleep-keep-short

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sleep — keep short) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sleep-keep-short.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> If you must sleep, keep the duration short (1-5 seconds) to avoid blocking the user.

## 中文翻译

> **原文：**
> If you must sleep, keep the duration short (1-5 seconds) to avoid blocking the user.

**翻译：**
如果必须使用 sleep，请将持续时间保持在较短范围（1-5 秒），以避免阻塞用户。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 范围限定（Scope Limitation） | "keep the duration short (1-5 seconds)" | 提供了具体的数值范围（1-5 秒），避免模型使用过长的 sleep 时间导致用户体验下降 |
| 2 | 条件逻辑注入（Conditional Logic Injection） | "If you must sleep" | "must" 一词暗示 sleep 应作为最后手段，引导模型优先考虑其他非阻塞方案 |
