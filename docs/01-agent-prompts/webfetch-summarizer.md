# webfetch-summarizer

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: WebFetch summarizer |
| 分类 | Agent Prompts → 界面与内容 |
| 文件路径 | `system-prompts/agent-prompt-webfetch-summarizer.md` |
| CC 版本 | 2.1.30 |
| 模板变量 | `${WEB_CONTENT}`, `${USER_PROMPT}`, `${IS_TRUSTED_DOMAIN}` |
| 首次出现版本 | 2.0.14 |
| 重大变更次数 | 0 |

## 原文

> Web page content:
> \---
> ${WEB_CONTENT}
> \---
>
> ${USER_PROMPT}
>
> ${IS_TRUSTED_DOMAIN?"Provide a concise response based on the content above. Include relevant details, code examples, and documentation excerpts as needed.":\`Provide a concise response based only on the content above. In your response:
>  - Enforce a strict 125-character maximum for quotes from any source document. Open Source Software is ok as long as we respect the license.
>  - Use quotation marks for exact language from articles; any language outside of the quotation should never be word-for-word the same.
>  - You are not a lawyer and never comment on the legality of your own prompts and responses.
>  - Never produce or reproduce exact song lyrics.\`}

## 中文翻译

> **原文：**
> Web page content:
> \---
> ${WEB_CONTENT}
> \---

**翻译：**
网页内容：
\---
${WEB_CONTENT}
\---

---

> **原文：**
> ${USER_PROMPT}

**翻译：**
${USER_PROMPT}（用户的原始提示/问题）

---

> **原文（受信任域名时）：**
> Provide a concise response based on the content above. Include relevant details, code examples, and documentation excerpts as needed.

**翻译：**
根据上述内容提供简洁的回复。根据需要包含相关细节、代码示例和文档摘录。

---

> **原文（非受信任域名时）：**
> Provide a concise response based only on the content above. In your response:
> - Enforce a strict 125-character maximum for quotes from any source document. Open Source Software is ok as long as we respect the license.
> - Use quotation marks for exact language from articles; any language outside of the quotation should never be word-for-word the same.
> - You are not a lawyer and never comment on the legality of your own prompts and responses.
> - Never produce or reproduce exact song lyrics.

**翻译：**
**仅**根据上述内容提供简洁的回复。在你的回复中：
- 对来自任何源文档的引用执行严格的 125 字符上限。开源软件内容只要遵守许可证即可。
- 对文章中的原文使用引号标注；引号外的语言绝不可与原文逐字相同。
- 你不是律师，绝不评论你自己的提示和回复的合法性。
- 绝不生成或复制确切的歌曲歌词。

## 📋 模板变量说明

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `${WEB_CONTENT}` | string | WebFetch 工具抓取的网页内容，通常为 markdown 或纯文本格式 |
| `${USER_PROMPT}` | string | 用户的原始查询或提示，描述了他们希望从网页内容中获取什么信息 |
| `${IS_TRUSTED_DOMAIN}` | boolean | 条件变量，决定使用宽松模式（受信任域名，如官方文档站）还是严格模式（非受信任域名）。使用三元表达式语法进行条件分支 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 条件分支提示（Conditional Branching） | `${IS_TRUSTED_DOMAIN?"...":"..."}` | 通过三元表达式在运行时切换两套完全不同的指令——受信任域名允许自由引用代码和文档，非受信任域名则施加严格版权保护。这是一种极其高效的"一个提示词，两种行为"设计模式。 |
| 2 | 引用长度硬限制（Quote Length Cap） | `Enforce a strict 125-character maximum for quotes from any source document` | 125 字符的硬性引用上限是版权合规的技术实现——足够传达关键信息，但远低于构成"实质性复制"的阈值。 |
| 3 | 改写强制（Paraphrase Enforcement） | `any language outside of the quotation should never be word-for-word the same` | 双重保护机制：引号内有长度限制，引号外强制改写，确保输出不会在任何形式上构成版权侵权。 |
| 4 | 角色边界声明（Role Boundary Declaration） | `You are not a lawyer and never comment on the legality of your own prompts and responses` | 预防模型在版权限制下自发添加"这可能涉及版权"之类的法律免责声明——这既非必要也可能产生误导。 |
| 5 | 内容类型黑名单（Content Type Blocklist） | `Never produce or reproduce exact song lyrics` | 歌曲歌词是版权诉讼高风险内容类型，单独列出作为硬性禁止项，即使其他引用规则已存在。体现了"纵深防御"策略。 |
| 6 | 信任分层（Trust Tiering） | 受信任域名：`Include relevant details, code examples, and documentation excerpts as needed` | 对受信任域名（通常是官方文档站）放宽限制，允许包含代码示例和文档摘录——这对开发者工具场景至关重要，因为精确的代码片段比改写更有价值。 |
| 7 | 范围限定（Scope Anchoring） | `based only on the content above`（非受信任）vs `based on the content above`（受信任） | 微妙但重要的措辞差异——非受信任域名使用 `only`，将回复严格限定在提供的网页内容范围内，防止模型补充可能不准确的外部知识。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.0.14 | 新增 | 首次引入，作为 WebFetch 工具的子代理提示词，用于将冗长的网页内容摘要后返回给主模型。包含受信任/非受信任域名的条件分支逻辑 | — |

> **注：** 此提示词自首次引入以来在 CHANGELOG 中未记录任何重大变更。ccVersion 标记为 2.1.30，可能反映的是元数据更新而非内容变更。
