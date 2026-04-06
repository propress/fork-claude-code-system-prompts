# bash-sandbox-failure-evidence-condition

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — failure evidence condition) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-failure-evidence-condition.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> A specific command just failed and you see evidence of sandbox restrictions causing the failure. Note that commands can fail for many reasons unrelated to the sandbox (missing files, wrong arguments, network issues, etc.).

## 中文翻译

> **原文：**
> A specific command just failed and you see evidence of sandbox restrictions causing the failure. Note that commands can fail for many reasons unrelated to the sandbox (missing files, wrong arguments, network issues, etc.).

**翻译：**
某个特定命令刚刚执行失败，并且你发现有证据表明沙箱限制导致了该失败。请注意，命令可能因许多与沙箱无关的原因而失败（文件缺失、参数错误、网络问题等）。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 条件逻辑注入（Conditional Logic Injection） | "A specific command just failed and you see evidence of sandbox restrictions causing the failure" | 设定了触发条件——必须同时满足"命令失败"和"存在沙箱限制的证据"两个条件。这种双重条件的设计防止模型在命令因其他原因失败时错误地归因于沙箱。 |
| 2 | 负面约束（Negative Constraint） | "Note that commands can fail for many reasons unrelated to the sandbox (missing files, wrong arguments, network issues, etc.)" | 通过列举非沙箱相关的失败原因，提醒模型不要将所有命令失败都归因于沙箱限制。括号中的具体示例帮助模型建立"排除诊断"的思维模式，提高故障归因的准确性。 |
| 3 | 示例引导（Example-driven Guidance） | "(missing files, wrong arguments, network issues, etc.)" | 提供了非沙箱失败原因的具体示例，使模型能够更好地区分沙箱问题与常规故障。这种示例引导增强了模型的判断能力。 |
