# bash-git-prefer-new-commits

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Bash (git — prefer new commits) |
| 分类 | Tool Descriptions → Bash 工具 |
| 文件路径 | `system-prompts/tool-description-bash-git-prefer-new-commits.md` |
| CC 版本 | 2.1.53 |
| 模板变量 | 无 |

## 原文

> Prefer to create a new commit rather than amending an existing commit.

## 中文翻译

> **原文：**
> Prefer to create a new commit rather than amending an existing commit.

**翻译：**
优先创建新的提交，而不是修改（amend）现有提交。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 优先级排序（Priority Ordering） | `Prefer to create a new commit rather than amending` | 通过"prefer...rather than"句式明确操作的优先级，引导模型默认选择创建新提交而非修改已有提交。 |
| 2 | 简洁指令（Concise Instruction） | 整句 | 用一句话清晰表达行为偏好，简洁直接，便于模型准确执行，同时保留了在用户明确要求时使用 amend 的灵活性。 |
