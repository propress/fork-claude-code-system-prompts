# git-status

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Git status |
| 分类 | System Prompts → 环境上下文 |
| 文件路径 | `system-prompts/system-prompt-git-status.md` |
| CC 版本 | 2.1.88 |
| 模板变量 | 无 |
| 首次出现版本 | ≤ 2.1.88（v2.1.88 中简化为当前形式） |

## 原文

> This is the git status at the start of the conversation. Note that this status is a snapshot in time, and will not update during the conversation.

## 中文翻译

> **原文：**
> This is the git status at the start of the conversation. Note that this status is a snapshot in time, and will not update during the conversation.

**翻译：**
这是对话开始时的 git 状态。请注意，此状态是一个时间点快照，在对话过程中不会更新。

## 📋 模板变量说明

无模板变量。（v2.1.88 之前的版本包含 branch、status、recent commits 等内联变量模板，已被移除。）

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 时效性声明 | "a snapshot in time, and will not update during the conversation" | 明确告知模型此信息是静态的，防止模型在后续操作中依赖可能已过时的 git 状态信息，从而鼓励在需要时主动运行 git 命令获取最新状态。 |
| 2 | 极简上下文注入 | 整个提示词仅一句话 | 以最小的 token 开销提供必要的元信息，不浪费上下文窗口。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.88 | 简化 | 移除了内联变量模板（branch、status、recent commits），仅保留介绍性说明 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/7d7c728" target="_blank">7d7c728</a> |
