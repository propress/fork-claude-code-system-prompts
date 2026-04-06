# bash-command-description-writer

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: Bash command description writer |
| 分类 | Agent Prompts |
| 文件路径 | `system-prompts/agent-prompt-bash-command-description-writer.md` |
| CC 版本 | 2.1.3 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.3 |
| 重大变更次数 | 0 |

## 原文

```
<!--
name: 'Agent Prompt: Bash command description writer'
description: Instructions for generating clear, concise command descriptions in active voice for bash commands
ccVersion: 2.1.3
-->
Clear, concise description of what this command does in active voice. Never use words like "complex" or "risk" in the description - just describe what it does.

For simple commands (git, npm, standard CLI tools), keep it brief (5-10 words):
- ls → "List files in current directory"
- git status → "Show working tree status"
- npm install → "Install package dependencies"

For commands that are harder to parse at a glance (piped commands, obscure flags, etc.), add enough context to clarify what it does:
- find . -name "*.tmp" -exec rm {} \; → "Find and delete all .tmp files recursively"
- git reset --hard origin/main → "Discard all local changes and match remote main"
- curl -s url | jq '.data[]' → "Fetch JSON from URL and extract data array elements"
```

## 中文翻译

> **原文：**
> Clear, concise description of what this command does in active voice. Never use words like "complex" or "risk" in the description - just describe what it does.

**翻译：**
用主动语态简洁清晰地描述该命令的功能。描述中绝对不要使用"complex（复杂）"或"risk（风险）"等词——只需描述它做了什么。

---

> **原文：**
> For simple commands (git, npm, standard CLI tools), keep it brief (5-10 words):
> - ls → "List files in current directory"
> - git status → "Show working tree status"
> - npm install → "Install package dependencies"

**翻译：**
对于简单命令（git、npm、标准 CLI 工具），保持简短（5-10 个词）：
- `ls` → "List files in current directory"（列出当前目录中的文件）
- `git status` → "Show working tree status"（显示工作树状态）
- `npm install` → "Install package dependencies"（安装包依赖项）

---

> **原文：**
> For commands that are harder to parse at a glance (piped commands, obscure flags, etc.), add enough context to clarify what it does:
> - find . -name "*.tmp" -exec rm {} \; → "Find and delete all .tmp files recursively"
> - git reset --hard origin/main → "Discard all local changes and match remote main"
> - curl -s url | jq '.data[]' → "Fetch JSON from URL and extract data array elements"

**翻译：**
对于一眼难以理解的命令（管道命令、晦涩标志等），添加足够的上下文以阐明其功能：
- `find . -name "*.tmp" -exec rm {} \;` → "Find and delete all .tmp files recursively"（递归查找并删除所有 .tmp 文件）
- `git reset --hard origin/main` → "Discard all local changes and match remote main"（丢弃所有本地更改并与远程 main 分支同步）
- `curl -s url | jq '.data[]'` → "Fetch JSON from URL and extract data array elements"（从 URL 获取 JSON 并提取 data 数组元素）

## 📋 模板变量说明

此提示词没有模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段 | 分析：为什么在这里有效 |
|---|---------|---------|---------------------|
| 1 | 边界硬编码（Hard Boundary） | "Never use words like 'complex' or 'risk' in the description" | 明确禁止带有主观评判色彩的词汇，确保描述保持中立客观，专注于功能而非评价，适合自动化工具的界面展示 |
| 2 | Few-shot 示例（Few-shot Examples） | `ls → "List files in current directory"` / `find . -name "*.tmp" ... → "Find and delete all .tmp files recursively"` | 通过简单命令和复杂命令的对比示例，建立长度分级规则，减少模糊性，模型可直接模仿输出格式 |
| 3 | 条件分支（Conditional Branching） | "For simple commands...keep it brief (5-10 words)" / "For commands that are harder to parse at a glance...add enough context" | 按命令复杂度分两个级别指定描述长度策略，避免所有命令采用统一长度导致简单命令冗长或复杂命令信息不足 |
| 4 | 正面/负面指令对（DO/DON'T Pairs） | "just describe what it does" vs "Never use words like 'complex' or 'risk'" | 同时告知应该做什么（描述功能）和不应该做什么（避免风险/复杂词汇），双向约束使输出更精准 |
| 5 | 上下文压缩指令（Context Compaction） | "keep it brief (5-10 words)" | 对简单命令限定精确字数范围，防止模型过度解释，符合 UI 工具提示（tooltip）的展示需求 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.3 | 新增 | 首次引入 Bash 命令描述写作器，提供以主动语态生成简洁命令描述的指令 | [3b9438c](https://github.com/Piebald-AI/claude-code-system-prompts/commit/3b9438c) |
