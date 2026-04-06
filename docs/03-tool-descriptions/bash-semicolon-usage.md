# bash-semicolon-usage

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (semicolon usage) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-semicolon-usage.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Use ';' only when you need to run commands sequentially but don't care if earlier commands fail.

## 中文翻译

> **原文：**
> Use ';' only when you need to run commands sequentially but don't care if earlier commands fail.

**翻译：**
仅在需要按顺序运行命令但不关心前面的命令是否失败时，才使用 `;`。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 条件逻辑注入（Conditional Logic Injection） | "only when you need to run commands sequentially but don't care if earlier commands fail" | 通过明确的条件约束（顺序执行 + 不关心失败），精确限定了 `;` 的适用场景，与 `&&` 的使用场景形成对比区分 |
| 2 | 范围限定（Scope Limitation） | "Use ';' only when" | "only" 一词严格限制了使用范围，避免模型在需要错误检查的场景中误用分号 |
