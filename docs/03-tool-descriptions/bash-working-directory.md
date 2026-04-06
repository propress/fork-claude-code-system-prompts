# bash-working-directory

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (working directory) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-working-directory.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> The working directory persists between commands, but shell state does not. The shell environment is initialized from the user's profile (bash or zsh).

## 中文翻译

> **原文：**
> The working directory persists between commands, but shell state does not. The shell environment is initialized from the user's profile (bash or zsh).

**翻译：**
工作目录在命令之间保持不变，但 shell 状态不会保留。Shell 环境从用户的配置文件（bash 或 zsh）初始化。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 范围限定（Scope Limitation） | "The working directory persists between commands, but shell state does not" | 通过对比说明哪些状态会保留、哪些不会，帮助模型正确理解执行环境的持久性边界 |
| 2 | 动态上下文注入（Dynamic Context Injection） | "The shell environment is initialized from the user's profile (bash or zsh)" | 告知模型 shell 环境的初始化来源，使其理解用户自定义配置（如别名、环境变量）可能影响命令行为 |
