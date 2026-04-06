# bash-sleep-use-check-commands

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sleep — use check commands) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sleep-use-check-commands.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> If you must poll an external process, use a check command (e.g. `gh run view`) rather than sleeping first.

## 中文翻译

> **原文：**
> If you must poll an external process, use a check command (e.g. `gh run view`) rather than sleeping first.

**翻译：**
如果必须轮询外部进程，请使用检查命令（例如 `gh run view`）而不是先使用 sleep。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 示例引导（Example-driven Guidance） | "e.g. `gh run view`" | 通过具体的命令示例说明"检查命令"的含义，降低模型理解歧义 |
| 2 | 优先级排序（Priority Ordering） | "use a check command ... rather than sleeping first" | 明确优先级：先使用检查命令获取状态，而非先 sleep 再检查，优化执行效率 |
| 3 | 条件逻辑注入（Conditional Logic Injection） | "If you must poll an external process" | "must" 限定了轮询是不得已的情况，引导模型尽量避免轮询 |
