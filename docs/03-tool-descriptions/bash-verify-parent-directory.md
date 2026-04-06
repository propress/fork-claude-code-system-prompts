# bash-verify-parent-directory

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (verify parent directory) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-verify-parent-directory.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> If your command will create new directories or files, first use this tool to run `ls` to verify the parent directory exists and is the correct location.

## 中文翻译

> **原文：**
> If your command will create new directories or files, first use this tool to run `ls` to verify the parent directory exists and is the correct location.

**翻译：**
如果你的命令将创建新目录或文件，请先使用此工具运行 `ls` 来验证父目录是否存在且位置正确。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 条件逻辑注入（Conditional Logic Injection） | "If your command will create new directories or files" | 明确触发条件——仅在创建新目录或文件时需要验证，避免对所有命令都增加不必要的前置检查 |
| 2 | 优先级排序（Priority Ordering） | "first use this tool to run `ls` to verify" | "first" 强调验证步骤必须在创建操作之前执行，建立正确的操作顺序 |
| 3 | 安全防护指令（Safety Guard） | "verify the parent directory exists and is the correct location" | 通过要求验证目录存在性和正确性，防止在错误位置创建文件的潜在问题 |
