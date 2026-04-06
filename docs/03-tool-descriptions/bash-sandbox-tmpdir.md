# bash-sandbox-tmpdir

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — tmpdir) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-tmpdir.md` |
| CC 版本 | 2.1.86 |
| 模板变量 | 无 |

## 原文

> For temporary files, always use the `$TMPDIR` environment variable. TMPDIR is automatically set to the correct sandbox-writable directory in sandbox mode. Do NOT use `/tmp` directly - use `$TMPDIR` instead.

## 中文翻译

> **原文：**
> For temporary files, always use the `$TMPDIR` environment variable. TMPDIR is automatically set to the correct sandbox-writable directory in sandbox mode. Do NOT use `/tmp` directly - use `$TMPDIR` instead.

**翻译：**
对于临时文件，请始终使用 `$TMPDIR` 环境变量。在沙箱模式下，TMPDIR 会自动设置为正确的沙箱可写目录。不要直接使用 `/tmp`——请改用 `$TMPDIR`。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | "Do NOT use `/tmp` directly" | 通过明确禁止直接使用 `/tmp`，防止模型在沙箱环境中使用错误的临时目录路径，避免权限问题 |
| 2 | 动态上下文注入（Dynamic Context Injection） | "TMPDIR is automatically set to the correct sandbox-writable directory" | 解释了 `$TMPDIR` 变量的自动设置机制，帮助模型理解为什么应使用该变量而非硬编码路径 |
| 3 | 简洁指令（Concise Instruction） | "always use the `$TMPDIR` environment variable" | 用简短明确的语言给出唯一正确的操作方式，不留歧义空间 |
