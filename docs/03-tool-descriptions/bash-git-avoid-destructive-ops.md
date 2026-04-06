# bash-git-avoid-destructive-ops

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (git — avoid destructive ops) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-git-avoid-destructive-ops.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Before running destructive operations (e.g., git reset --hard, git push --force, git checkout --), consider whether there is a safer alternative that achieves the same goal. Only use destructive operations when they are truly the best approach.

## 中文翻译

> **原文：**
> Before running destructive operations (e.g., git reset --hard, git push --force, git checkout --), consider whether there is a safer alternative that achieves the same goal. Only use destructive operations when they are truly the best approach.

**翻译：**
在执行破坏性操作（例如 git reset --hard、git push --force、git checkout --）之前，请考虑是否有更安全的替代方案可以达到相同目标。仅在破坏性操作确实是最佳方案时才使用它们。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 安全防护指令（Safety Guard） | `Before running destructive operations... consider whether there is a safer alternative` | 要求在执行破坏性操作前先评估替代方案，建立了安全优先的决策流程。 |
| 2 | 示例引导（Example-driven Guidance） | `e.g., git reset --hard, git push --force, git checkout --` | 通过列举三个具体的破坏性 git 命令示例，帮助模型识别哪些操作属于"破坏性"范畴。 |
| 3 | 范围限定（Scope Limitation） | `Only use destructive operations when they are truly the best approach` | 用"truly the best approach"限定使用条件，设置了高门槛，确保破坏性操作不会被轻易使用。 |
