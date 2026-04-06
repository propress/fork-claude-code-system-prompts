# new-diagnostics-detected

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: New diagnostics detected |
| 分类 | System Reminders → 技能与工具 |
| 文件路径 | `system-prompts/system-reminder-new-diagnostics-detected.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${DIAGNOSTICS_SUMMARY}` |

## 原文

> `<new-diagnostics>`The following new diagnostic issues were detected:
>
> ${DIAGNOSTICS_SUMMARY}`</new-diagnostics>`

## 中文翻译

> **原文：**
> The following new diagnostic issues were detected:

**翻译：**
检测到以下新的诊断问题：

${DIAGNOSTICS_SUMMARY}

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 专用 XML 标签 | `<new-diagnostics>...</new-diagnostics>` | 使用语义化的自定义 XML 标签包裹诊断信息，使模型能明确区分诊断内容与其他系统消息 |
| 2 | 增量通知 | "new diagnostic issues" | 使用"new"强调这些是新增的诊断问题，引导模型关注最新变化而非历史问题 |
