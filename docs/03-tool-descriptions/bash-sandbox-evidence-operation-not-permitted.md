# bash-sandbox-evidence-operation-not-permitted

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — evidence: operation not permitted) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-evidence-operation-not-permitted.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> "Operation not permitted" errors for file/network operations

## 中文翻译

> **原文：**
> "Operation not permitted" errors for file/network operations

**翻译：**
文件/网络操作中出现的"Operation not permitted"错误

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 简洁指令（Concise Instruction） | "\"Operation not permitted\" errors for file/network operations" | 用一个简短的短语精确描述一种沙箱失败特征。直接引用了操作系统层面的错误信息文本，使模型能够对命令输出中的具体错误字符串进行模式匹配。 |
| 2 | 范围限定（Scope Limitation） | "for file/network operations" | 将错误范围限定在文件和网络操作上，帮助模型理解"Operation not permitted"在这个上下文中特指沙箱对文件系统和网络访问的限制，而非其他类型的权限错误。 |
