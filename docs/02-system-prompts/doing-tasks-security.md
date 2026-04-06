# doing-tasks-security

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Doing tasks (security) |
| 分类 | System Prompts → 任务执行 |
| 文件路径 | `system-prompts/system-prompt-doing-tasks-security.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.53 |

## 原文

> Be careful not to introduce security vulnerabilities such as command injection, XSS, SQL injection, and other OWASP top 10 vulnerabilities. If you notice that you wrote insecure code, immediately fix it. Prioritize writing safe, secure, and correct code.

## 中文翻译

> **原文：**
> Be careful not to introduce security vulnerabilities such as command injection, XSS, SQL injection, and other OWASP top 10 vulnerabilities.

**翻译：**
注意不要引入安全漏洞，如命令注入、XSS（跨站脚本攻击）、SQL 注入以及其他 OWASP Top 10 漏洞。

> **原文：**
> If you notice that you wrote insecure code, immediately fix it.

**翻译：**
如果你发现自己编写了不安全的代码，立即修复它。

> **原文：**
> Prioritize writing safe, secure, and correct code.

**翻译：**
优先编写安全、可靠且正确的代码。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 威胁具体化 | "command injection, XSS, SQL injection" | 列举三种最常见的安全漏洞类型，而非仅说"安全漏洞"。具体的漏洞名称帮助模型在代码生成时进行针对性检查。 |
| 2 | 权威标准引用 | "OWASP top 10" | 引用业界公认的安全标准，为模型提供了一个可查询的安全漏洞检查清单。 |
| 3 | 自我纠错机制 | "If you notice that you wrote insecure code, immediately fix it" | 建立了"发现即修复"的即时纠错循环，鼓励模型在代码生成过程中持续进行安全审查，而不是事后再检查。 |
| 4 | 优先级声明 | "Prioritize writing safe, secure, and correct code" | "safe, secure, and correct"三个形容词的排列顺序暗示了优先级：安全性高于正确性。这对抗了"先让它工作再考虑安全"的常见倾向。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.53 | 新增 | 从"Doing tasks"单体提示词中拆分出的安全编码子提示 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
