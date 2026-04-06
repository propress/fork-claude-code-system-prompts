# bash-timeout

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (timeout) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-timeout.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | `${GET_MAX_TIMEOUT_MS()}`, `${GET_DEFAULT_TIMEOUT_MS()}` |

## 原文

> You may specify an optional timeout in milliseconds (up to ${GET_MAX_TIMEOUT_MS()}ms / ${GET_MAX_TIMEOUT_MS()/60000} minutes). By default, your command will timeout after ${GET_DEFAULT_TIMEOUT_MS()}ms (${GET_DEFAULT_TIMEOUT_MS()/60000} minutes).

## 中文翻译

> **原文：**
> You may specify an optional timeout in milliseconds (up to ${GET_MAX_TIMEOUT_MS()}ms / ${GET_MAX_TIMEOUT_MS()/60000} minutes). By default, your command will timeout after ${GET_DEFAULT_TIMEOUT_MS()}ms (${GET_DEFAULT_TIMEOUT_MS()/60000} minutes).

**翻译：**
你可以指定一个可选的超时时间（以毫秒为单位），最大为 ${GET_MAX_TIMEOUT_MS()} 毫秒 / ${GET_MAX_TIMEOUT_MS()/60000} 分钟。默认情况下，命令将在 ${GET_DEFAULT_TIMEOUT_MS()} 毫秒（${GET_DEFAULT_TIMEOUT_MS()/60000} 分钟）后超时。

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${GET_MAX_TIMEOUT_MS()}` | 最大超时时间（毫秒） |
| `${GET_DEFAULT_TIMEOUT_MS()}` | 默认超时时间（毫秒） |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 动态上下文注入（Dynamic Context Injection） | "${GET_MAX_TIMEOUT_MS()}" / "${GET_DEFAULT_TIMEOUT_MS()}" | 使用函数调用形式的模板变量动态注入超时配置值，使提示词能适应不同的运行时环境 |
| 2 | 范围限定（Scope Limitation） | "up to ${GET_MAX_TIMEOUT_MS()}ms" | 通过明确最大值限制，防止模型设置过长的超时时间 |
| 3 | 简洁指令（Concise Instruction） | "You may specify an optional timeout" | "optional" 一词明确了该参数非必需，减少不必要的工具调用复杂度 |
