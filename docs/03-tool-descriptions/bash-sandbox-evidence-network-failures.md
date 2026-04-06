# bash-sandbox-evidence-network-failures

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — evidence: network failures) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-evidence-network-failures.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Network connection failures to non-whitelisted hosts

## 中文翻译

> **原文：**
> Network connection failures to non-whitelisted hosts

**翻译：**
连接未加入白名单的主机时出现网络连接失败

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 简洁指令（Concise Instruction） | "Network connection failures to non-whitelisted hosts" | 作为证据列表中的一项，使用简洁的短语描述一种特定的沙箱失败模式。无需完整句子，直接给出关键特征，帮助模型快速匹配和识别此类错误。 |
| 2 | 范围限定（Scope Limitation） | "non-whitelisted hosts" | 明确限定了网络失败的范围——仅针对"未加入白名单的主机"。这种精确的范围限定帮助模型区分真正由沙箱引起的网络错误与其他原因导致的网络问题。 |
