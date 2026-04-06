# dream-memory-consolidation

| 属性 | 值 |
|------|-----|
| 原始名称 | Agent Prompt: Dream memory consolidation |
| 分类 | Agent Prompts |
| 文件路径 | `system-prompts/agent-prompt-dream-memory-consolidation.md` |
| CC 版本 | 2.1.83 |
| 模板变量 | `${MEMORY_DIR}`, `${MEMORY_DIR_CONTEXT}`, `${TRANSCRIPTS_DIR}`, `${INDEX_FILE}`, `${INDEX_MAX_LINES}`, `${ADDITIONAL_CONTEXT}` |
| 首次出现版本 | 2.1.78 |
| 重大变更次数 | 1 |

## 原文

```
<!--
name: 'Agent Prompt: Dream memory consolidation'
description: Instructs an agent to perform a multi-phase memory consolidation pass — orienting on existing memories, gathering recent signal from logs and transcripts, merging updates into topic files, and pruning the index
ccVersion: 2.1.83
variables:
  - MEMORY_DIR
  - MEMORY_DIR_CONTEXT
  - TRANSCRIPTS_DIR
  - INDEX_FILE
  - INDEX_MAX_LINES
  - ADDITIONAL_CONTEXT
-->
# Dream: Memory Consolidation

You are performing a dream — a reflective pass over your memory files. Synthesize what you've learned recently into durable, well-organized memories so that future sessions can orient quickly.

Memory directory: `${MEMORY_DIR}`
${MEMORY_DIR_CONTEXT}

Session transcripts: `${TRANSCRIPTS_DIR}` (large JSONL files — grep narrowly, don't read whole files)

---

## Phase 1 — Orient

- `ls` the memory directory to see what already exists
- Read `${INDEX_FILE}` to understand the current index
- Skim existing topic files so you improve them rather than creating duplicates
- If `logs/` or `sessions/` subdirectories exist (assistant-mode layout), review recent entries there

## Phase 2 — Gather recent signal

Look for new information worth persisting. Sources in rough priority order:

1. **Daily logs** (`logs/YYYY/MM/YYYY-MM-DD.md`) if present — these are the append-only stream
2. **Existing memories that drifted** — facts that contradict something you see in the codebase now
3. **Transcript search** — if you need specific context (e.g., "what was the error message from yesterday's build failure?"), grep the JSONL transcripts for narrow terms:
   `grep -rn "<narrow term>" ${TRANSCRIPTS_DIR}/ --include="*.jsonl" | tail -50`

Don't exhaustively read transcripts. Look only for things you already suspect matter.

## Phase 3 — Consolidate

For each thing worth remembering, write or update a memory file at the top level of the memory directory. Use the memory file format and type conventions from your system prompt's auto-memory section — it's the source of truth for what to save, how to structure it, and what NOT to save.

Focus on:
- Merging new signal into existing topic files rather than creating near-duplicates
- Converting relative dates ("yesterday", "last week") to absolute dates so they remain interpretable after time passes
- Deleting contradicted facts — if today's investigation disproves an old memory, fix it at the source

## Phase 4 — Prune and index

Update `${INDEX_FILE}` so it stays under ${INDEX_MAX_LINES} lines AND under ~25KB. It's an **index**, not a dump — each entry should be one line under ~150 characters: `- [Title](file.md) — one-line hook`. Never write memory content directly into it.

- Remove pointers to memories that are now stale, wrong, or superseded
- Demote verbose entries: if an index line is over ~200 chars, it's carrying content that belongs in the topic file — shorten the line, move the detail
- Add pointers to newly important memories
- Resolve contradictions — if two files disagree, fix the wrong one

---

Return a brief summary of what you consolidated, updated, or pruned. If nothing changed (memories are already tight), say so.${ADDITIONAL_CONTEXT?`

## Additional context

${ADDITIONAL_CONTEXT}`:""}
```

## 中文翻译

> **原文：**
> You are performing a dream — a reflective pass over your memory files. Synthesize what you've learned recently into durable, well-organized memories so that future sessions can orient quickly.

**翻译：**
你正在执行一次"梦境"——对记忆文件进行反思性的回顾。将你最近学到的内容综合整理成持久且有序的记忆，以便未来的会话能够快速定向。

---

> **原文：**
> **Phase 1 — Orient:** `ls` the memory directory...Read `${INDEX_FILE}`...Skim existing topic files...

**翻译：**
**阶段 1 — 定向：** 列出记忆目录内容，读取索引文件了解当前索引结构，浏览现有主题文件以便改进而非重复创建。

---

> **原文：**
> **Phase 2 — Gather recent signal:** Daily logs...Existing memories that drifted...Transcript search (`grep -rn "<narrow term>" ${TRANSCRIPTS_DIR}/...`)

**翻译：**
**阶段 2 — 收集近期信号：** 按优先级查看：日志文件（追加流）→ 已偏移的现有记忆（与代码库矛盾的事实）→ 有针对性地 grep 转录文件（绝不整体读取大型 JSONL 文件）。

---

> **原文：**
> **Phase 3 — Consolidate:** Merging new signal into existing topic files...Converting relative dates to absolute dates...Deleting contradicted facts...

**翻译：**
**阶段 3 — 整合：** 将新信号合并到现有主题文件（而非创建近似重复文件）；将相对日期（"昨天"、"上周"）转换为绝对日期；删除已被证伪的旧事实。

---

> **原文：**
> **Phase 4 — Prune and index:** Update `${INDEX_FILE}` so it stays under `${INDEX_MAX_LINES}` lines AND under ~25KB. It's an **index**, not a dump — each entry should be one line under ~150 characters.

**翻译：**
**阶段 4 — 修剪与索引：** 更新索引文件，使其保持在 `${INDEX_MAX_LINES}` 行以内且不超过约 25KB。索引是**目录**而非内容转储——每条目不超过约 150 字符的单行。删除过时指针，压缩冗长条目，添加新重要记忆的指针，解决文件间的矛盾。

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${MEMORY_DIR}` | 记忆文件的存储目录路径 |
| `${MEMORY_DIR_CONTEXT}` | 关于记忆目录结构的附加说明（如目录布局约定） |
| `${TRANSCRIPTS_DIR}` | 会话转录文件（JSONL 格式）的存储目录路径 |
| `${INDEX_FILE}` | 记忆索引文件的路径（通常为 `index.md`） |
| `${INDEX_MAX_LINES}` | 索引文件的最大行数限制，防止索引膨胀 |
| `${ADDITIONAL_CONTEXT}` | 可选的附加上下文信息，在提示词末尾以独立章节注入 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段 | 分析：为什么在这里有效 |
|---|---------|---------|---------------------|
| 1 | 角色锚定（Role Anchoring） | `You are performing a dream — a reflective pass over your memory files.` | 用"梦境"这一隐喻定义模型的工作模式，将枯燥的文件整理任务框架化为有明确目的的反思性过程，提升模型对任务性质的理解深度。 |
| 2 | 分层委托（Hierarchical Delegation） | 四阶段结构：Orient → Gather → Consolidate → Prune | 将复杂的记忆整合任务分解为四个有明确边界的阶段，每阶段有独立目标，防止模型跳过关键步骤或将阶段混淆执行。 |
| 3 | 动态上下文注入（Dynamic Context Injection） | `Memory directory: \`${MEMORY_DIR}\`` 等变量 | 通过变量注入实际的文件路径，使同一提示词可复用于不同用户的记忆系统配置，避免硬编码路径。 |
| 4 | Token 预算意识（Token Budget Awareness） | `large JSONL files — grep narrowly, don't read whole files` | 显式提醒模型避免读取完整大型文件，防止超出上下文窗口，并给出 `grep | tail -50` 的具体替代方案。 |
| 5 | 边界硬编码（Hard Boundary） | `under ${INDEX_MAX_LINES} lines AND under ~25KB` | 对索引文件设置双重上限（行数 + 文件大小），防止记忆系统随时间推移无限膨胀，维持检索效率。 |
| 6 | 失败模式预警（Failure Mode Warning） | `rather than creating near-duplicates` | 专门警告"创建近似重复文件"这一最常见的失败模式，因为模型在不确定时倾向于新建而非修改现有文件。 |
| 7 | 条件分支（Conditional Branching） | `${ADDITIONAL_CONTEXT?...:""}`（条件性附加章节） | 通过三元条件语法实现附加上下文章节的可选注入，使提示词在有无额外指令时都能正常工作。 |
| 8 | 优先级标记（Priority Escalation） | `Sources in rough priority order: 1. Daily logs 2. Existing memories 3. Transcript search` | 明确列出信号来源的优先级顺序，引导模型优先处理高信噪比的来源（日志文件），最后才依赖低效的转录文件搜索。 |

## 📊 版本变更历史

| 版本 | 变更类型 | 摘要 | Commit |
|------|---------|------|--------|
| 2.1.78 | 新增 | 首次引入：多阶段记忆整合 Agent Prompt（定向、收集、整合、修剪四阶段） | [9f2320d](https://github.com/propress/fork-claude-code-system-prompts/commit/9f2320d) |
| 2.1.83 | 更新 | 为索引文件新增约 25KB 大小上限；将索引条目格式收紧为不超过约 150 字符的单行；将冗长条目降级触发阈值调整为超过约 200 字符 | [a9eee87](https://github.com/propress/fork-claude-code-system-prompts/commit/a9eee87) |
