# bash-sandbox-response-header

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — response header) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-response-header.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> When you see evidence of sandbox-caused failure:

## 中文翻译

> **原文：**
> When you see evidence of sandbox-caused failure:

**翻译：**
当你发现沙箱导致的失败迹象时：

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 条件逻辑注入（Conditional Logic Injection） | "When you see evidence of sandbox-caused failure:" | 使用"When"设定了触发条件——仅在检测到沙箱失败证据时才执行后续指令。这种条件化设计确保模型不会在无关场景下执行沙箱故障的应对流程。 |
| 2 | 结构化列表（Structured Enumeration） | "When you see evidence of sandbox-caused failure:" | 以冒号结尾的引导语句，为后续的具体响应步骤建立结构化框架。这使得后续指令具有清晰的层级关系和执行顺序。 |
