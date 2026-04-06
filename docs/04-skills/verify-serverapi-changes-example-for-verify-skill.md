# verify-serverapi-changes-example-for-verify-skill

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: Verify server/API changes (example for Verify skill) |
| 分类 | Skills → 代码质量 |
| 文件路径 | `system-prompts/skill-verify-serverapi-changes-example-for-verify-skill.md` |
| CC 版本 | 2.1.83 |
| 模板变量 | 无 |

## 原文（摘要）

较短文件（68 行），作为 Verify Skill 的服务器/API 变更验证示例。完整收录：

> # Verifying a server/API change
>
> The handle is `curl` (or equivalent). The evidence is the response.

### 模式

> 1. Start the server (background, with a readiness poll)
> 2. `curl` the route the diff touches, with inputs that hit the changed branch
> 3. Capture the full response (status + headers + body)
> 4. Compare to expected

### 生命周期

> ```bash
> <start-command> &> /tmp/server.log &
> SERVER_PID=$!
> for i in {1..30}; do curl -sf localhost:PORT/health >/dev/null && break; sleep 1; done
> # ... your curls ...
> kill $SERVER_PID
> ```

### 实际示例

> **Diff:** adds a `Retry-After` header to 429 responses in `rateLimit.ts`.
> **Claim (PR body):** "clients can now back off correctly."
> **Inference:** hitting the rate limit should now return `Retry-After: <n>` in the response headers.
>
> **Execute:**
> ```bash
> for i in {1..10}; do curl -s -o /dev/null -w "%{http_code}\n" localhost:3000/api/thing; done
> curl -si localhost:3000/api/thing | head -20
> ```
>
> **Verdict:** PASS — `Retry-After: 12` present, positive integer.

### FAIL 的样子

> - Header absent → the diff didn't take effect
> - Header present but value is `NaN` / `undefined` / negative → the logic is wrong
> - You got 200s all the way through → you never triggered the changed path

## 中文翻译

# 验证服务器/API 变更

句柄是 `curl`（或等效工具）。证据是响应。

### 模式

1. 启动服务器（后台运行，带就绪轮询——见下文）
2. `curl` 请求 diff 触及的路由，使用命中变更分支的输入
3. 捕获完整响应（状态码 + 头部 + 响应体）
4. 与预期比较

### 生命周期

如果有 run-skill 则由它处理。如果没有：

```bash
<start-command> &> /tmp/server.log &
SERVER_PID=$!
for i in {1..30}; do curl -sf localhost:PORT/health >/dev/null && break; sleep 1; done
# ... 你的 curl 请求 ...
kill $SERVER_PID
```

没有就绪端点？轮询你即将测试的路由，直到它不再返回连接拒绝，然后等一拍。

### 实际示例

**Diff：** 在 `rateLimit.ts` 中为 429 响应添加了 `Retry-After` 头部。

**声明（PR 正文）：** "客户端现在可以正确退避。"

**推断：** 触发速率限制后现在应返回响应头中的 `Retry-After: <n>`。之前没有。

**计划：**
1. 启动服务器
2. 多次请求速率限制端点以触发 429
3. 检查 429 响应是否有 `Retry-After` 头部
4. 检查值是否为正整数

**执行：**
```bash
# 触发限制——10 个快速请求，根据 diff 限制为 5/秒
for i in {1..10}; do curl -s -o /dev/null -w "%{http_code}\n" localhost:3000/api/thing; done
# → 200 200 200 200 200 429 429 429 429 429

# 捕获 429 头部
curl -si localhost:3000/api/thing | head -20
# → HTTP/1.1 429 Too Many Requests
# → Retry-After: 12
# → ...
```

**判定：** PASS — `Retry-After: 12` 存在，正整数。

### FAIL 的样子

- 头部缺失 → diff 没有生效，或者你没有真正命中 429 路径（先检查状态码）
- 头部存在但值为 `NaN` / `undefined` / 负数 → 逻辑错误
- 一路都是 200 → 你从未触发变更路径。加紧请求突发频率或检查速率限制配置。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 就绪轮询模式 | `for i in {1..30}; do curl -sf localhost:PORT/health >/dev/null && break; sleep 1; done` | 提供可直接使用的服务器就绪检测脚本，解决 LLM 容易忽略的异步启动问题 |
| 2 | 端到端验证流程 | Diff → Claim → Inference → Plan → Execute → Verdict | 与 CLI 示例保持一致的结构化验证流程，建立跨 Skill 的统一心智模型 |
| 3 | 路径触发验证 | "you never triggered the changed path" | 强调验证的核心：不仅要运行，还要确保命中了变更的代码路径 |
| 4 | 响应全捕获 | "Capture the full response (status + headers + body)" | 防止 LLM 只检查响应体而遗漏头部等关键信号 |
| 5 | 生命周期管理 | 后台启动 + PID 保存 + 就绪轮询 + 清理 kill | 教会 LLM 完整的服务器测试生命周期，避免遗留进程或竞态条件 |
| 6 | 失败诊断指引 | 每种 FAIL 场景都附带诊断建议 | 不仅告诉 LLM "这是失败"，还教它如何诊断失败根因 |
