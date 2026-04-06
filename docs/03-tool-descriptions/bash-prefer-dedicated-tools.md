# bash-prefer-dedicated-tools

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (prefer dedicated tools) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-prefer-dedicated-tools.md` |
| CC 版本 | 2.1.71 |
| 模板变量 | `${READ_ONLY_SEARCHING_BASH_COMMANDS}` |

## 原文

> IMPORTANT: Avoid using this tool to run ${READ_ONLY_SEARCHING_BASH_COMMANDS} commands, unless explicitly instructed or after you have verified that a dedicated tool cannot accomplish your task. Instead, use the appropriate dedicated tool as this will provide a much better experience for the user:

## 中文翻译

> **原文：**
> IMPORTANT: Avoid using this tool to run ${READ_ONLY_SEARCHING_BASH_COMMANDS} commands, unless explicitly instructed or after you have verified that a dedicated tool cannot accomplish your task. Instead, use the appropriate dedicated tool as this will provide a much better experience for the user:

**翻译：**
重要：避免使用此工具来运行 ${READ_ONLY_SEARCHING_BASH_COMMANDS} 命令，除非收到明确指示或在你已确认专用工具无法完成任务之后。请改用适当的专用工具，因为这将为用户提供更好的体验：

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${READ_ONLY_SEARCHING_BASH_COMMANDS}` | 只读搜索类 Bash 命令列表（如 find、grep、cat 等） |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 优先级排序（Priority Ordering） | `Avoid using this tool to run... Instead, use the appropriate dedicated tool` | 明确专用工具优先于 Bash 工具，建立工具选择的层级关系，减少不必要的 Bash 调用。 |
| 2 | 条件逻辑注入（Conditional Logic Injection） | `unless explicitly instructed or after you have verified that a dedicated tool cannot accomplish your task` | 设定两个例外条件（用户明确指示、专用工具无法完成），允许在特定情况下回退到 Bash。 |
| 3 | 负面约束（Negative Constraint） | `IMPORTANT: Avoid using this tool` | 以"IMPORTANT"前缀强调禁止行为的重要性，引导模型避免不必要地使用 Bash 工具执行搜索操作。 |
| 4 | 动态上下文注入（Dynamic Context Injection） | `${READ_ONLY_SEARCHING_BASH_COMMANDS}` | 通过模板变量动态注入需要避免的命令列表，使指令能适应不同配置环境。 |
