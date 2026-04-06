# session-continuation

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Session continuation |
| 分类 | System Reminders → 会话管理 |
| 文件路径 | `system-prompts/system-reminder-session-continuation.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${GET_CWD_FN}` |

## 原文

> This session is being continued from another machine. Application state may have changed. The updated working directory is ${GET_CWD_FN()}

## 中文翻译

> **原文：**
> This session is being continued from another machine. Application state may have changed. The updated working directory is ${GET_CWD_FN()}

**翻译：**
此会话正在从另一台机器继续。应用程序状态可能已发生变化。更新后的工作目录为 ${GET_CWD_FN()}

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 状态失效警告 | "Application state may have changed" | 提醒模型之前的状态假设可能不再有效，促使其重新验证关键信息 |
| 2 | 环境更新 | "The updated working directory is ${GET_CWD_FN()}" | 提供新的工作目录路径，确保后续文件操作使用正确的基准路径 |
