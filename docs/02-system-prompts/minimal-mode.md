# minimal-mode

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Minimal mode |
| 分类 | System Prompts → 运行模式 |
| 文件路径 | `system-prompts/system-prompt-minimal-mode.md` |
| CC 版本 | 2.1.81 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.81 |

## 原文

> Minimal mode: skip hooks, LSP, plugin sync, attribution, auto-memory, background prefetches, keychain reads, and CLAUDE.md auto-discovery. Sets CLAUDE_CODE_SIMPLE=1. Anthropic auth is strictly ANTHROPIC_API_KEY or apiKeyHelper via --settings (OAuth and keychain are never read). 3P providers (Bedrock/Vertex/Foundry) use their own credentials. Skills still resolve via /skill-name. Explicitly provide context via: --system-prompt[-file], --append-system-prompt[-file], --add-dir (CLAUDE.md dirs), --mcp-config, --settings, --agents, --plugin-dir.

## 中文翻译

> **原文：**
> Minimal mode: skip hooks, LSP, plugin sync, attribution, auto-memory, background prefetches, keychain reads, and CLAUDE.md auto-discovery.

**翻译：**
最小模式：跳过 hooks、LSP、插件同步、归因、自动记忆、后台预取、钥匙串读取和 CLAUDE.md 自动发现。

> **原文：**
> Sets CLAUDE_CODE_SIMPLE=1. Anthropic auth is strictly ANTHROPIC_API_KEY or apiKeyHelper via --settings (OAuth and keychain are never read). 3P providers (Bedrock/Vertex/Foundry) use their own credentials.

**翻译：**
设置 CLAUDE_CODE_SIMPLE=1。Anthropic 认证严格限制为 ANTHROPIC_API_KEY 或通过 --settings 使用 apiKeyHelper（OAuth 和钥匙串永远不会被读取）。第三方提供商（Bedrock/Vertex/Foundry）使用各自的凭据。

> **原文：**
> Skills still resolve via /skill-name. Explicitly provide context via: --system-prompt[-file], --append-system-prompt[-file], --add-dir (CLAUDE.md dirs), --mcp-config, --settings, --agents, --plugin-dir.

**翻译：**
技能仍通过 /skill-name 解析。通过以下方式显式提供上下文：--system-prompt[-file]、--append-system-prompt[-file]、--add-dir（CLAUDE.md 目录）、--mcp-config、--settings、--agents、--plugin-dir。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 穷举排除列表 | "skip hooks, LSP, plugin sync, attribution, auto-memory, background prefetches, keychain reads, and CLAUDE.md auto-discovery" | 逐一列出所有被跳过的功能，确保没有歧义——模型清楚知道最小模式下哪些功能不可用。 |
| 2 | 认证约束 | "Anthropic auth is strictly ANTHROPIC_API_KEY or apiKeyHelper via --settings" | 使用 "strictly" 加明确列举的认证方式，建立严格的认证边界。 |
| 3 | 例外声明 | "Skills still resolve via /skill-name" | 在大量「不可用」的声明中明确标注仍然可用的功能，防止模型过度限制自身能力。 |
| 4 | 显式上下文路径 | "Explicitly provide context via: --system-prompt[-file]..." | 列出所有可用的 CLI 标志，为模型提供在最小模式下获取上下文的完整工具集。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.81 | 新增 | 首次引入最小模式描述 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/a82ade6" target="_blank">a82ade6</a> |
