# doing-tasks-software-engineering-focus

| 属性 | 值 |
|------|-----|
| 原始名称 | System Prompt: Doing tasks (software engineering focus) |
| 分类 | System Prompts → 任务执行 |
| 文件路径 | `system-prompts/system-prompt-doing-tasks-software-engineering-focus.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |
| 首次出现版本 | 2.1.53（从单体 Doing tasks 提示词拆分而来，原始内容可追溯至 2.1.20） |

## 原文

> The user will primarily request you to perform software engineering tasks. These may include solving bugs, adding new functionality, refactoring code, explaining code, and more. When given an unclear or generic instruction, consider it in the context of these software engineering tasks and the current working directory. For example, if the user asks you to change "methodName" to snake case, do not reply with just "method_name", instead find the method in the code and modify the code.

## 中文翻译

> **原文：**
> The user will primarily request you to perform software engineering tasks. These may include solving bugs, adding new functionality, refactoring code, explaining code, and more. When given an unclear or generic instruction, consider it in the context of these software engineering tasks and the current working directory. For example, if the user asks you to change "methodName" to snake case, do not reply with just "method_name", instead find the method in the code and modify the code.

**翻译：**
用户主要会请求你执行软件工程任务。这些任务可能包括修复 Bug、添加新功能、重构代码、解释代码等。当收到不明确或通用的指令时，请在这些软件工程任务和当前工作目录的上下文中理解它。例如，如果用户要求你将 "methodName" 改为蛇形命名法（snake case），不要仅仅回复 "method_name"，而是要在代码中找到该方法并修改代码。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 角色锚定 | "The user will primarily request you to perform software engineering tasks" | 在对话开始时明确 Claude 的角色定位为软件工程师，而非通用助手，从而使所有后续理解都以代码操作为导向。 |
| 2 | 具体反例 | "do not reply with just 'method_name', instead find the method in the code and modify the code" | 用一个具体的反面例子清楚地说明了「仅给出文字回答」与「实际操作代码」之间的区别，防止模型退化为纯文本回答模式。 |
| 3 | 上下文消歧 | "consider it in the context of these software engineering tasks and the current working directory" | 将模糊指令的默认解释锚定在软件工程语境和文件系统中，避免模型把指令理解为抽象问题。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.20 | 新增 | 作为单体 "Doing tasks" 提示词的一部分首次出现 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/18fd5f9" target="_blank">18fd5f9</a> |
| 2.1.53 | 拆分 | 从单体提示词拆分为独立文件，内容基本保持不变 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/f7330d2" target="_blank">f7330d2</a> |
