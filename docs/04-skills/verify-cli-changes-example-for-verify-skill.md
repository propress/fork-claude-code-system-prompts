# verify-cli-changes-example-for-verify-skill

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: Verify CLI changes (example for Verify skill) |
| 分类 | Skills → 代码质量 |
| 文件路径 | `system-prompts/skill-verify-cli-changes-example-for-verify-skill.md` |
| CC 版本 | 2.1.83 |
| 模板变量 | 无 |

## 原文（摘要）

较短文件（73 行），作为 Verify Skill 的 CLI 变更验证示例。完整收录：

> # Verifying a CLI change
>
> The handle is direct invocation. The evidence is stdout/stderr/exit code.

### 模式

> 1. Build (if the CLI needs building)
> 2. Run with arguments that exercise the changed code
> 3. Capture output and exit code
> 4. Compare to expected

> CLIs are usually the simplest to verify — no lifecycle, no ports.

### 实际示例

> **Diff:** adds a `--json` flag to the `status` subcommand.
> **Claim (commit msg):** "machine-readable status output."
> **Inference:** `tool status --json` now exists, emits valid JSON with the same fields the human output shows.
>
> **Plan:**
> 1. Build
> 2. `tool status` → human output, same as before (non-regression)
> 3. `tool status --json` → valid JSON, parseable
> 4. JSON fields match human output fields
>
> **Execute:**
> ```bash
> go build -o /tmp/tool ./cmd/tool
> /tmp/tool status
> /tmp/tool status --json
> /tmp/tool status --json | jq -e .status
> echo $?
> ```
>
> **Verdict:** PASS — flag works, JSON is valid, fields line up.

### FAIL 的样子

> - `unknown flag: --json` → not wired up, or you're running a stale build
> - Output isn't valid JSON → serialization bug
> - `tool status` (no flag) changed → regression
> - JSON has different field names than expected → claim/code mismatch

### 从 stdin 读取、破坏性命令

> If the CLI reads stdin → pipe in test data.
> If it writes files / hits a network / deletes things → point it at a tmp dir / a mock / a dry-run flag.

## 中文翻译

# 验证 CLI 变更

句柄是直接调用。证据是 stdout/stderr/退出码。

### 模式

1. 构建（如果 CLI 需要构建）
2. 使用能执行变更代码的参数运行
3. 捕获输出和退出码
4. 与预期比较

CLI 通常是最容易验证的——没有生命周期，没有端口。

### 实际示例

**Diff：** 为 `status` 子命令添加了 `--json` 标志。新的标志解析在 `cmd/status.go`，新的输出分支。

**声明（提交信息）：** "机器可读的状态输出。"

**推断：** `tool status --json` 现在存在，发出与人类输出相同字段的有效 JSON。`tool status` 不带标志时行为不变。

**计划：**
1. 构建
2. `tool status` → 人类输出，与之前相同（非回归）
3. `tool status --json` → 有效 JSON，可解析
4. JSON 字段与人类输出字段匹配

**执行：**
```bash
go build -o /tmp/tool ./cmd/tool

/tmp/tool status
# → Status: healthy
# → Uptime: 3h12m
# → Connections: 47

/tmp/tool status --json
# → {"status":"healthy","uptime_seconds":11520,"connections":47}

/tmp/tool status --json | jq -e .status
# → "healthy"
# (jq -e 在路径为 null/false 时以非零退出——便宜的有效性检查)

echo $?
# → 0
```

**判定：** PASS — 标志有效，JSON 有效，字段对应。

### FAIL 的样子

- `unknown flag: --json` → 未连接，或你运行的是过时的构建
- 输出不是有效 JSON（`jq` 报错）→ 序列化 bug
- `tool status`（无标志）发生变化 → 回归；diff 触及的范围超出预期
- JSON 字段名与预期不同 → 声明/代码不匹配，可能没问题，记录下来

### 从 stdin 读取、破坏性命令

如果 CLI 从 stdin 读取 → 管道传入测试数据。

如果它写文件 / 访问网络 / 删除内容 → 将其指向临时目录 / mock / dry-run 标志。如果没有安全模式且 diff 触及了破坏性路径，说明情况并验证你能验证的部分。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 完整实例教学 | Diff → Claim → Inference → Plan → Execute → Verdict 的完整流程 | 通过详尽的端到端示例教会 LLM 验证的完整思维过程，而非抽象规则 |
| 2 | 声明 vs 推断分离 | "Claim (commit msg)" 与 "Inference" 作为不同字段 | 明确区分作者声称的内容和验证者推断的预期行为，训练批判性思维 |
| 3 | 失败模式枚举 | "What FAIL looks like" 列出四种具体失败场景和根因 | 不仅教会 LLM 如何判定通过，还教会如何诊断不同的失败模式 |
| 4 | 安全验证降级 | "verify what you can around it" | 承认不是所有路径都能安全验证，允许部分验证而非放弃 |
| 5 | jq 作为验证工具 | `jq -e .status` 作为 JSON 有效性的便宜检查 | 引入具体的验证工具和技巧，提升 LLM 的实际验证能力 |
