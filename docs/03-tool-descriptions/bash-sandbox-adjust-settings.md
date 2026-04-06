# bash-sandbox-adjust-settings

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (sandbox — adjust settings) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-sandbox-adjust-settings.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> If a command fails due to sandbox restrictions, work with the user to adjust sandbox settings instead.

## 中文翻译

> **原文：**
> If a command fails due to sandbox restrictions, work with the user to adjust sandbox settings instead.

**翻译：**
如果命令因沙箱限制而失败，请与用户协作调整沙箱设置。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 条件逻辑注入（Conditional Logic Injection） | `If a command fails due to sandbox restrictions` | 设定触发条件，仅在沙箱限制导致命令失败时才执行后续操作，避免不必要的干预。 |
| 2 | 角色/行为锚定（Role/Behavior Anchoring） | `work with the user to adjust sandbox settings instead` | 将模型定位为协作者角色，强调与用户共同解决问题而非单方面绕过沙箱限制。 |
