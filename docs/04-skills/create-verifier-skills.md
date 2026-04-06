# create-verifier-skills

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: Create verifier skills |
| 分类 | Skills → 代码质量 |
| 文件路径 | `system-prompts/skill-create-verifier-skills.md` |
| CC 版本 | 2.1.69 |
| 模板变量 | 无 |

## 原文（摘要）

大型文件（246 行），指导创建验证器 Skill 供 Verify Agent 自动验证代码变更。分为五个阶段：

### Phase 1: Auto-Detection
> Analyze the project to detect what's in different subdirectories. The project may contain multiple sub-projects or areas that need different verification approaches.

扫描项目类型（Web 应用、CLI 工具、API 服务）、技术栈、现有验证工具、开发服务器配置。

> **Do NOT create verifiers for unit tests or typechecking.** Those are already handled by the standard build/test workflow. Focus on functional verification: web UI (Playwright), CLI (Tmux), and API (HTTP) verifiers.

### Phase 2: Verification Tool Setup
为 Web 应用检查/安装 Playwright 或 Chrome DevTools MCP；为 CLI 工具检查 Tmux/asciinema；为 API 服务检查 curl/httpie。

### Phase 3: Interactive Q&A
确认验证器名称（单项目用 `verifier-playwright`，多项目用 `verifier-<project>-<type>`）、项目特定问题、认证与登录配置。

> Custom names are allowed but MUST include "verifier" in the name — the Verify agent discovers skills by looking for "verifier" in the folder name.

### Phase 4: Generate Verifier Skill
生成 SKILL.md 模板，包含项目上下文、设置指令、认证步骤、报告格式、清理步骤和自我更新机制。

### Phase 5: Confirm Creation
通知用户技能创建位置和 Verify Agent 发现方式。

## 中文翻译

### 目标

创建一个或多个验证器 Skill，供 Verify Agent 自动验证此项目或文件夹中的代码变更。如果项目有不同的验证需求（例如 Web UI 和 API 端点），可以创建多个验证器。

**不要为单元测试或类型检查创建验证器。** 这些已由标准构建/测试工作流处理，不需要专用验证器 Skill。专注于功能验证：Web UI（Playwright）、CLI（Tmux）和 API（HTTP）验证器。

### 第一阶段：自动检测

分析项目以检测不同子目录中的内容：

1. **扫描顶级目录** 识别不同的项目区域
2. **对每个区域检测：**
   - 项目类型和技术栈（语言、框架、包管理器）
   - 应用类型（Web → Playwright 验证器、CLI → Tmux 验证器、API → HTTP 验证器）
   - 现有验证工具（测试框架、E2E 工具）
   - 开发服务器配置（启动命令、URL、就绪信号）
3. **已安装的验证包**（Playwright、MCP 配置等）

### 第二阶段：验证工具设置

**Web 应用：**
- 如已安装浏览器自动化工具，询问用户使用哪个
- 如未检测到，提供安装选项：Playwright（推荐）、Chrome DevTools MCP、Claude Chrome Extension、无
- 根据包管理器运行安装命令

**CLI 工具：** 检查 asciinema 和 Tmux 可用性

**API 服务：** 检查 curl 和 httpie 可用性

### 第三阶段：交互式问答

1. **验证器名称**
   - 单项目区域：`verifier-playwright`、`verifier-cli`、`verifier-api`
   - 多项目区域：`verifier-<project>-<type>`（如 `verifier-frontend-playwright`）
   - 自定义名称必须包含 "verifier"

2. **项目特定问题**（开发服务器命令/URL/就绪信号、CLI 入口点、API 基础 URL 等）

3. **认证与登录**：询问是否需要认证，如需要则收集登录方法、测试凭据（建议使用环境变量）和登录后确认方式

### 第四阶段：生成验证器 Skill

所有验证器 Skill 创建在项目根目录的 `.claude/skills/` 目录中。

**允许的工具（按类型）：**
- **verifier-playwright**：`Bash(npm:*)`、`mcp__playwright__*`、`Read`、`Glob`、`Grep`
- **verifier-cli**：`Tmux`、`Bash(asciinema:*)`、`Read`、`Glob`、`Grep`
- **verifier-api**：`Bash(curl:*)`、`Bash(http:*)`、`Read`、`Glob`、`Grep`

Skill 模板结构包含：验证执行者角色声明、项目上下文、设置指令、认证步骤（如适用）、报告格式、清理步骤和自我更新机制。

### 第五阶段：确认创建

告知用户每个 Skill 的创建位置、Verify Agent 如何发现它们（文件夹名必须包含 "verifier"）、可以编辑自定义、以及验证器会在检测到自身指令过时时提供自我更新。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面范围限定 | "Do NOT create verifiers for unit tests or typechecking" | 在开头明确排除项，避免 LLM 过度生成不必要的验证器 |
| 2 | 阶段化工作流 | Phase 1-5 结构化流程 | 将复杂的多步骤任务分解为清晰的阶段，每个阶段有明确的输入和输出 |
| 3 | 条件分支命名规则 | 单项目 `verifier-type` vs 多项目 `verifier-project-type` | 提供不同场景下的精确命名约定，避免 LLM 在命名上犹豫不决 |
| 4 | 发现机制约束 | "MUST include 'verifier' in the name — the Verify agent discovers skills by looking for 'verifier'" | 将技术限制作为硬约束传达，确保生成的 Skill 能被自动发现 |
| 5 | 自我修复机制 | "Self-Update: If verification fails because this skill's instructions are outdated... Edit this SKILL.md" | 赋予验证器自我更新能力，减少因环境变化导致的误报 |
| 6 | 安全凭据实践 | "Suggest the user use environment variables for secrets (e.g., `TEST_USER`, `TEST_PASSWORD`) rather than hardcoding" | 在 Skill 生成模板中嵌入安全最佳实践 |
