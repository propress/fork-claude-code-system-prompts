# update-config-7-step-verification-flow

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: update-config (7-step verification flow) |
| 分类 | Skills → 项目配置 |
| 文件路径 | `system-prompts/skill-update-config-7-step-verification-flow.md` |
| CC 版本 | 2.1.77 |
| 模板变量 | 无 |

## 原文（摘要）

较短文件（41 行），定义 Hook 构建和验证的 7 步流程。完整收录：

> ## Constructing a Hook (with verification)
>
> Given an event, matcher, target file, and desired behavior, follow this flow. Each step catches a different failure class — a hook that silently does nothing is worse than no hook.

> 1. **Dedup check.** Read the target file. If a hook already exists on the same event+matcher, show the existing command and ask: keep it, replace it, or add alongside.
>
> 2. **Construct the command for THIS project — don't assume.** The hook receives JSON on stdin. Build a command that extracts payload safely with `jq -r`, invokes the tool the way this project runs it, skips inputs the tool doesn't handle, stays RAW for now.
>
> 3. **Pipe-test the raw command.** Synthesize the stdin payload and pipe it directly. Check exit code AND side effect.
>
> 4. **Write the JSON.** Merge into the target file.
>
> 5. **Validate syntax + schema in one shot:** `jq -e '.hooks.<event>[] | select(.matcher == "<matcher>") | .hooks[] | select(.type == "command") | .command' <target-file>`
>
> 6. **Prove the hook fires** — only for `Pre|PostToolUse` on triggerable matchers. For a formatter: introduce a detectable violation, re-read, confirm the hook fixed it.
>
> 7. **Handoff.** Tell the user the hook is live. Point them at `/hooks` to review, edit, or disable.

## 中文翻译

## 构建 Hook（带验证）

给定事件、匹配器、目标文件和期望行为，按此流程执行。每个步骤捕获不同的失败类别——一个静默什么都不做的 Hook 比没有 Hook 更糟糕。

### 1. 去重检查

读取目标文件。如果同一 event+matcher 上已存在 Hook，显示现有命令并询问：保留、替换还是并列添加。

### 2. 为此项目构建命令——不要假设

Hook 在 stdin 上接收 JSON。构建一个命令：

- 使用 `jq -r` 安全提取需要的载荷到带引号的变量或 `{ read -r f; ... "$f"; }` 中，**不要** 使用未加引号的 `| xargs`（会按空格分割）
- 以此项目运行工具的方式调用底层工具（npx/bunx/yarn/pnpm？Makefile 目标？全局安装？）
- 跳过工具不处理的输入（格式化器通常有 `--ignore-unknown`；如果没有，按扩展名守卫）
- 暂时保持原始状态——不加 `|| true`，不抑制 stderr。管道测试通过后再包装。

### 3. 管道测试原始命令

合成 Hook 将接收的 stdin 载荷并直接管道传输：

- `Pre|PostToolUse` 的 `Write|Edit`：`echo '{"tool_name":"Edit","tool_input":{"file_path":"<此仓库的真实文件>"}}' | <cmd>`
- `Pre|PostToolUse` 的 `Bash`：`echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}' | <cmd>`
- `Stop`/`UserPromptSubmit`/`SessionStart`：大多数命令不读 stdin，`echo '{}' | <cmd>` 即可

检查退出码**和**副作用（文件确实被格式化了，测试确实运行了）。如果失败你会得到真实错误——修复（错误的包管理器？工具未安装？jq 路径错误？）并重新测试。通过后，用 `2>/dev/null || true` 包装（除非用户需要阻塞检查）。

### 4. 写入 JSON

合并到目标文件（schema 形状参见上方"Hook Structure"章节）。如果首次创建 `.claude/settings.local.json`，将其加入 .gitignore——Write 工具不会自动 gitignore 它。

### 5. 一次性验证语法和 schema

```bash
jq -e '.hooks.<event>[] | select(.matcher == "<matcher>") | .hooks[] | select(.type == "command") | .command' <target-file>
```

退出 0 + 打印你的命令 = 正确。退出 4 = 匹配器不匹配。退出 5 = JSON 格式错误或嵌套错误。损坏的 settings.json 会静默禁用该文件的所有设置——也修复任何预先存在的格式错误。

### 6. 证明 Hook 触发

仅适用于可在轮内触发的匹配器上的 `Pre|PostToolUse`（`Write|Edit` 通过 Edit 触发，`Bash` 通过 Bash 触发）。`Stop`/`UserPromptSubmit`/`SessionStart` 在此轮外触发——跳到第 7 步。

对于 `PostToolUse`/`Write|Edit` 上的**格式化器**：通过 Edit 引入可检测的违规（两个连续空行、错误缩进、缺少分号——格式化器会纠正的问题；**不是** 尾部空格，Edit 在写入前就会去除），重新读取，确认 Hook **修复了** 它。

**始终清理**——还原违规、去除哨兵前缀——无论证明是否通过。

**如果证明失败但管道测试和 `jq -e` 都通过了**：设置监视器没有在监视 `.claude/`——它只监视会话启动时已有设置文件的目录。Hook 已正确写入。告诉用户打开 `/hooks` 一次（重新加载配置）或重启。

### 7. 移交

告诉用户 Hook 已生效（或需要 `/hooks`/重启）。指引他们到 `/hooks` 查看、编辑或禁用。UI 只在 Hook 出错或慢时才显示"Ran N hooks"——静默成功在设计上是不可见的。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 分层失败捕获 | "Each step catches a different failure class" | 将验证分解为 7 步，每步针对不同的失败类别，确保全面覆盖 |
| 2 | 先裸后包装策略 | "Stays RAW for now — no `\|\| true`... You'll wrap it after the pipe-test passes" | 分阶段构建命令，先验证裸命令有效，再添加错误抑制，避免掩盖真实错误 |
| 3 | 合成载荷测试 | 为每种匹配器类型提供精确的 stdin 测试载荷 | 提供可直接复制使用的测试命令，确保 LLM 用正确格式测试 |
| 4 | jq 退出码语义 | "Exit 0 = correct. Exit 4 = matcher doesn't match. Exit 5 = malformed JSON" | 精确的退出码含义映射，让 LLM 能正确诊断验证失败的原因 |
| 5 | 实证验证 | "introduce a detectable violation... re-read, confirm the hook fixed it" | 要求 LLM 用真实副作用证明 Hook 工作，而非仅靠配置正确性推断 |
| 6 | 设置监视器注意事项 | "settings watcher isn't watching `.claude/` — it only watches directories that had a settings file when this session started" | 揭示隐藏的系统行为，防止 LLM 在证明失败时误判为 Hook 配置错误 |
