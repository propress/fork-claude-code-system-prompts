# init-claudemd-and-skill-setup-new-version

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: /init CLAUDE.md and skill setup (new version) |
| 分类 | Skills → 项目配置 |
| 文件路径 | `system-prompts/skill-init-claudemd-and-skill-setup-new-version.md` |
| CC 版本 | 2.1.81 |
| 模板变量 | 无 |

## 原文（摘要）

大型文件（202 行），八阶段综合引导流程，用于设置 CLAUDE.md 及相关 Skills/Hooks。

### Phase 1: Ask what to set up
> "Which CLAUDE.md files should /init set up?" Options: "Project CLAUDE.md" | "Personal CLAUDE.local.md" | "Both project + personal"
>
> "Also set up skills and hooks?" Options: "Skills + hooks" | "Skills only" | "Hooks only" | "Neither, just CLAUDE.md"

### Phase 2: Explore the codebase
> Launch a subagent to survey the codebase... Detect: Build, test, and lint commands... Languages, frameworks... Project structure... Code style rules... Formatter configuration... Git worktree usage

### Phase 3: Fill in the gaps
> Use AskUserQuestion to gather what you still need... Ask only things the code can't answer.

提出提案时使用 AskUserQuestion 的 `preview` 字段。项（Hook/Skill/CLAUDE.md note）类型必须严格遵循 Phase 1 的 Skills+Hooks 选择。

### Phase 4: Write CLAUDE.md
> Every line must pass this test: "Would removing this cause Claude to make mistakes?" If no, cut it.

包含：不可猜测的构建/测试/lint 命令、与语言默认不同的代码风格、测试指令和怪癖、仓库礼仪、必需的环境变量。
排除：文件结构列表、标准语言约定、通用建议、详细 API 文档。

### Phase 5: Write CLAUDE.local.md
个人偏好文件，包含角色、熟悉度、沙盒 URL、工作流偏好。Git worktree 场景的特殊处理。

### Phase 6: Suggest and create skills
> Skills add capabilities Claude can use on demand without bloating every session.

### Phase 7: Suggest additional optimizations
检查 GitHub CLI、Linting、Hooks 的安装情况，包含 7 步 Hook 构建流程的集成。

### Phase 8: Summary and next steps
推荐插件（frontend-design、playwright、skill-creator）和后续操作。

## 中文翻译

设置一个最小化的 CLAUDE.md（以及可选的 Skills 和 Hooks）用于此仓库。CLAUDE.md 在每个 Claude Code 会话中加载，因此必须简洁——只包含 Claude 没有它就会出错的内容。

### 第一阶段：询问要设置什么

使用 AskUserQuestion 了解用户需求：

- "哪些 CLAUDE.md 文件需要 /init 设置？"
  选项："Project CLAUDE.md" | "Personal CLAUDE.local.md" | "Both"
  项目版本描述：团队共享指令，提交到源码控制——架构、编码标准、常见工作流。
  个人版本描述：你在此项目的私有偏好（gitignored，不共享）——角色、沙盒 URL、测试数据。

- "也要设置 Skills 和 Hooks 吗？"
  选项："Skills + hooks" | "Skills only" | "Hooks only" | "Neither"

### 第二阶段：探索代码库

启动子 Agent 调查代码库，读取关键文件：manifest 文件（package.json、Cargo.toml 等）、README、构建配置、CI 配置、现有 CLAUDE.md、各种 AI 工具配置文件。

检测项目：构建/测试/lint 命令、语言和框架、项目结构（monorepo/多模块/单项目）、代码风格规则、格式化器配置、Git worktree 使用情况。

记录代码无法回答的问题——这些成为访谈问题。

### 第三阶段：填补空白

使用 AskUserQuestion 收集编写好的 CLAUDE.md 和 Skills 所需信息。只问代码无法回答的问题。

**从第二阶段发现综合提案**——例如，如果存在格式化器则建议编辑时自动格式化，如果存在测试则建议 `/verify` Skill。为每项选择匹配的产物类型：

- **Hook**（更严格）— 工具事件上的确定性 shell 命令；Claude 不能跳过。适合机械、快速、每次编辑的步骤。
- **Skill**（按需）— 用户或 Claude 在需要时调用。适合不属于每次编辑的工作流。
- **CLAUDE.md 注释**（更宽松）— 影响 Claude 行为但不强制。适合沟通/思考偏好。

**严格遵守第一阶段的 Skills+Hooks 选择作为硬过滤器**。

### 第四阶段：编写 CLAUDE.md

在项目根目录编写最小化的 CLAUDE.md。每行必须通过测试："移除这行会导致 Claude 犯错吗？"如果不会，就删掉。

**包含：** 非标准构建/测试/lint 命令、与语言默认不同的代码风格、测试指令和怪癖、仓库礼仪、必需环境变量、非显而易见的陷阱。

**排除：** 文件结构列表、标准语言约定、通用建议（"写干净的代码"）、详细 API 文档（改用 `@path/to/import`）、频繁变化的信息。

具体优于模糊："Use 2-space indentation in TypeScript" 优于 "Format code properly."

### 第五阶段：编写 CLAUDE.local.md

个人偏好文件，包含角色和熟悉度、个人沙盒 URL/测试账户、个人工作流或沟通偏好。创建后将 `CLAUDE.local.md` 加入 .gitignore。

对于使用兄弟/外部 Git worktree 的场景：将实际内容写入 `~/.claude/<project-name>-instructions.md`，CLAUDE.local.md 只包含一行导入。

### 第六阶段：建议和创建 Skills

首先消费第三阶段队列中的 Skill 项。然后在检测到参考知识或可重复工作流时建议额外 Skills。

### 第七阶段：建议额外优化

检查环境并询问每个发现的空白：GitHub CLI 安装、Linting 设置、Hook 构建（使用 7 步验证流程）。

### 第八阶段：总结和后续步骤

回顾设置内容，提供待办事项列表。推荐安装：
- 前端代码检测到时：`/plugin install frontend-design@claude-plugins-official` 和 `/plugin install playwright@claude-plugins-official`
- Skill 创建器：`/plugin install skill-creator@claude-plugins-official`
- 浏览官方插件：`/plugin`

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 最小化原则 | "Every line must pass this test: 'Would removing this cause Claude to make mistakes?' If no, cut it." | 提供了明确的内容筛选标准，防止 LLM 生成冗长无用的 CLAUDE.md |
| 2 | 排除列表 | 详细列出 CLAUDE.md 中不应包含的内容类型 | 负面约束比正面指导更能减少 LLM 的过度生成倾向 |
| 3 | 八阶段结构化流程 | Phase 1-8 从询问到总结的完整流程 | 将极其复杂的引导任务分解为可管理的步骤，每步有明确输入输出 |
| 4 | 硬过滤器约束 | "Respect Phase 1's skills+hooks choice as a hard filter" | 将用户早期选择作为后续所有阶段的约束，保持一致性 |
| 5 | 三层产物分类 | Hook（强制）、Skill（按需）、CLAUDE.md note（建议） | 清晰的分类标准帮助 LLM 为每个需求选择正确的产物类型 |
| 6 | 预览交互设计 | "Show the proposal via AskUserQuestion's `preview` field, not as a separate text message" | 利用工具能力优化用户体验，避免提案文本被对话覆盖 |
| 7 | 具体性要求 | "'Use 2-space indentation in TypeScript' is better than 'Format code properly'" | 用对比示例教会 LLM 什么是足够具体的指导 |
