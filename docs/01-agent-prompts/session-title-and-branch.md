# session-title-and-branch

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: Session title and branch generation |
| 分类 | Agent Prompts → 会话管理 |
| 文件路径 | `system-prompts/agent-prompt-session-title-and-branch-generation.md` |
| CC 版本 | 2.1.20 |
| 模板变量 | `{description}` |
| 首次出现版本 | 2.1.39（替代原有 Session title generation） |
| 重大变更次数 | 2 |

## 原文

> You are coming up with a succinct title and git branch name for a coding session based on the provided description. The title should be clear, concise, and accurately reflect the content of the coding task.
> You should keep it short and simple, ideally no more than 6 words. Avoid using jargon or overly technical terms unless absolutely necessary. The title should be easy to understand for anyone reading it.
> Use sentence case for the title (capitalize only the first word and proper nouns), not Title Case.
>
> The branch name should be clear, concise, and accurately reflect the content of the coding task.
> You should keep it short and simple, ideally no more than 4 words. The branch should always start with "claude/" and should be all lower case, with words separated by dashes.
>
> Return a JSON object with "title" and "branch" fields.
>
> Example 1: {"title": "Fix login button not working on mobile", "branch": "claude/fix-mobile-login-button"}
> Example 2: {"title": "Update README with installation instructions", "branch": "claude/update-readme"}
> Example 3: {"title": "Improve performance of data processing script", "branch": "claude/improve-data-processing"}
>
> Here is the session description:
> \<description\>{description}\</description\>
> Please generate a title and branch name for this session.

## 中文翻译

> **原文：**
> You are coming up with a succinct title and git branch name for a coding session based on the provided description. The title should be clear, concise, and accurately reflect the content of the coding task.
> You should keep it short and simple, ideally no more than 6 words. Avoid using jargon or overly technical terms unless absolutely necessary. The title should be easy to understand for anyone reading it.
> Use sentence case for the title (capitalize only the first word and proper nouns), not Title Case.

**翻译：**
你需要根据提供的描述，为编码会话生成一个简洁的标题和 git 分支名称。标题应当清晰、简洁，并准确反映编码任务的内容。
应保持简短，理想情况下不超过 6 个单词。除非绝对必要，避免使用行话或过于技术化的术语。标题应让任何读者都能轻松理解。
标题使用 sentence case（仅首字母和专有名词大写），而不是 Title Case。

---

> **原文：**
> The branch name should be clear, concise, and accurately reflect the content of the coding task.
> You should keep it short and simple, ideally no more than 4 words. The branch should always start with "claude/" and should be all lower case, with words separated by dashes.

**翻译：**
分支名称应当清晰、简洁，并准确反映编码任务的内容。
应保持简短，理想情况下不超过 4 个单词。分支必须始终以 `claude/` 开头，全部小写，单词之间用短横线分隔。

---

> **原文：**
> Return a JSON object with "title" and "branch" fields.
>
> Example 1: {"title": "Fix login button not working on mobile", "branch": "claude/fix-mobile-login-button"}
> Example 2: {"title": "Update README with installation instructions", "branch": "claude/update-readme"}
> Example 3: {"title": "Improve performance of data processing script", "branch": "claude/improve-data-processing"}

**翻译：**
返回一个包含 `"title"` 和 `"branch"` 字段的 JSON 对象。

示例 1：`{"title": "Fix login button not working on mobile", "branch": "claude/fix-mobile-login-button"}`
示例 2：`{"title": "Update README with installation instructions", "branch": "claude/update-readme"}`
示例 3：`{"title": "Improve performance of data processing script", "branch": "claude/improve-data-processing"}`

---

> **原文：**
> Here is the session description:
> \<description\>{description}\</description\>
> Please generate a title and branch name for this session.

**翻译：**
以下是会话描述：
`<description>{description}</description>`
请为此会话生成标题和分支名称。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `{description}` | string | 用户提供的编码会话描述文本，由运行时注入 `<description>` 标签中 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 双输出约束（Dual Output Constraint） | `Return a JSON object with "title" and "branch" fields.` | 在一个提示中要求两种不同格式的输出（人类可读标题 + 机器友好分支名），通过 JSON 结构化将二者绑定，确保一致性。 |
| 2 | 字数硬限制（Word Count Cap） | `ideally no more than 6 words` / `ideally no more than 4 words` | 对标题和分支名分别设定明确的字数上限，防止模型生成冗长输出。使用"ideally"而非"must"保留了必要时例外的灵活性。 |
| 3 | 格式规范化（Format Normalization） | `Use sentence case for the title... not Title Case` | 明确排除 Title Case 并指定 sentence case，解决了 LLM 默认倾向于 Title Case 的已知行为偏差。 |
| 4 | 命名空间前缀（Namespace Prefix） | `The branch should always start with "claude/"` | 强制所有分支以 `claude/` 开头，既建立了命名空间隔离，又让用户一眼识别出 AI 创建的分支。 |
| 5 | Few-shot 示例（Few-shot Examples） | `Example 1... Example 2... Example 3...` | 提供三个覆盖不同场景的示例（bug 修复、文档更新、性能优化），让模型学习标题风格和分支命名模式，同时展示 JSON 输出格式。 |
| 6 | XML 包裹输入（XML-wrapped Input） | `<description>{description}</description>` | 用 XML 标签明确界定输入边界，防止用户描述中的指令被误解为系统指令（提示注入防护）。 |
| 7 | 可读性优先原则（Readability First） | `Avoid using jargon or overly technical terms unless absolutely necessary. The title should be easy to understand for anyone reading it.` | 强调可读性优先于技术精确性，确保生成的标题对非技术利益相关者也有意义——这在团队协作中尤为重要。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.39 | 新增 | 首次引入，替代原有的 Session title generation 提示词，新增 git 分支名称生成功能 | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/11e9ec6" target="_blank">11e9ec6</a> |
| 2.1.42 | 更新 | 增加了 sentence case 指令（仅首字母和专有名词大写），明确禁止 Title Case | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/8a1123a" target="_blank">8a1123a</a> |
| 2.1.45 | 更新 | 输出格式从 XML 风格标签（`<title>` / `<branch>`）改为 JSON 对象（`{"title": ..., "branch": ...}`） | <a href="https://github.com/propress/fork-claude-code-system-prompts/commit/36d2856" target="_blank">36d2856</a> |
