# invoked-skills

| 属性 | 值 |
|------|-----|
| 原始名称 | System Reminder: Invoked skills |
| 分类 | System Reminders → 技能与工具 |
| 文件路径 | `system-prompts/system-reminder-invoked-skills.md` |
| CC 版本 | 2.1.18 |
| 模板变量 | `${FORMATTED_SKILLS_LIST}` |

## 原文

> The following skills were invoked in this session. Continue to follow these guidelines:
>
> ${FORMATTED_SKILLS_LIST}

## 中文翻译

> **原文：**
> The following skills were invoked in this session. Continue to follow these guidelines:

**翻译：**
本会话中已调用了以下技能。请继续遵循这些指导方针：

${FORMATTED_SKILLS_LIST}

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 持续性指令 | "Continue to follow these guidelines" | 使用"Continue"强调这些技能指南不仅适用于过去，还需要在后续操作中持续遵守 |
| 2 | 动态技能注入 | "${FORMATTED_SKILLS_LIST}" | 通过模板变量动态注入会话中已激活的技能列表，使提示词适应不同的工作场景 |
