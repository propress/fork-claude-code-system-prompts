# bash-sandbox-no-sensitive-paths

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — no sensitive paths) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-no-sensitive-paths.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Do not suggest adding sensitive paths like ~/.bashrc, ~/.zshrc, ~/.ssh/*, or credential files to the sandbox allowlist.

## 中文翻译

> **原文：**
> Do not suggest adding sensitive paths like ~/.bashrc, ~/.zshrc, ~/.ssh/*, or credential files to the sandbox allowlist.

**翻译：**
不要建议将敏感路径（如 ~/.bashrc、~/.zshrc、~/.ssh/* 或凭证文件）添加到沙箱允许列表中。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | "Do not suggest adding sensitive paths" | 以"Do not"开头的直接禁止指令，防止模型在帮助用户解决沙箱问题时提出可能危及系统安全的建议。 |
| 2 | 示例引导（Example-driven Guidance） | "~/.bashrc, ~/.zshrc, ~/.ssh/*, or credential files" | 通过列举具体的敏感路径示例，帮助模型建立"敏感路径"的概念边界。这些示例涵盖了 shell 配置文件、SSH 密钥和凭证文件等关键类别，使模型能够推断出类似性质的其他路径也不应被建议添加。 |
| 3 | 安全防护指令（Safety Guard） | "Do not suggest adding sensitive paths ... to the sandbox allowlist" | 这条指令从安全角度防止沙箱的安全机制被用户或模型自身不慎削弱。即使允许列表功能可以解决某些沙箱限制问题，也不应以牺牲安全性为代价。 |
