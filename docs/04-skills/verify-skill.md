# verify-skill

| 属性 | 值 |
|------|-----|
| 原始名称 | Skill: Verify skill |
| 分类 | Skills → 代码质量 |
| 文件路径 | `system-prompts/skill-verify-skill.md` |
| CC 版本 | 2.1.91 |
| 模板变量 | 无 |

## 原文（摘要）

大型文件（191 行），定义代码变更验证的核心理念和工作流。这是 Claude Code 最具特色的 Skill 之一。

### 核心理念

> **Verification is runtime observation.** You build the app, run it, drive it to where the changed code executes, and capture what you see. That capture is your evidence. Nothing else is.
>
> **Don't run tests. Don't typecheck.** CI ran both before you got here — green checks on the PR mean they passed. Running them again proves you can run CI. Not as a warm-up, not "just to be sure," not as a regression sweep after.
>
> **Don't import-and-call.** `import { foo } from './src/...'` then `console.log(foo(x))` is a unit test you wrote. The app never ran.

### Find the change

> ```bash
> git log --oneline @{u}..              # count commits
> git diff @{u}.. --stat                # full range, not HEAD~1
> gh pr diff                            # if in a PR context
> ```
>
> **The diff is ground truth. The PR description is a claim about it.** Read both. If they disagree, that's a finding.

### Surface（验证表面）

> | Change reaches | Surface | You |
> |---|---|---|
> | CLI / TUI | terminal | type the command, capture the pane |
> | Server / API | socket | send the request, capture the response |
> | GUI | pixels | drive it under xvfb/Playwright, screenshot |
> | Library | package boundary | sample code through the public export |
> | Prompt / agent config | the agent | run the agent, capture its behavior |
> | CI workflow | Actions | dispatch it, read the run |
>
> **Internal function? Not a surface.** Something in the repo calls it and that caller ends at one of the rows above. Follow it there.
>
> **Tests in the diff are the author's evidence, not a surface.** CI runs them.

### Get a handle

> - **`.claude/skills/*verifier*/`** — route to matching verifier
> - **`.claude/skills/run-*/`** — knows how to build and launch
> - **Neither** — cold start from README/package.json/Makefile. Timebox ~15min.

### Drive it

> **Read your plan back before running.** If every step is build / typecheck / run test file — you've planned a CI rerun, not a verification.
>
> Once the claim checks out, keep going: break it (empty input, huge input, interrupt mid-op), combine it (new thing + old thing), wander (what's adjacent?).
>
> **The verdict is table stakes. Your observations are the signal.** A PASS with three sharp "hey, I noticed…" lines is worth more than a bare PASS.
>
> **End-to-end, through the real interface.** Pieces passing in isolation doesn't mean the flow works — seams are where bugs hide.

### Report 格式

> ```
> ## Verification: <one-line what changed>
> **Verdict:** PASS | FAIL | BLOCKED | SKIP
> **Claim:** <what it's supposed to do>
> **Method:** <how you got a handle>
> ### Steps
> 1. ✅/❌/⚠️ <what you did> → <what you observed>
> ### Findings
> <Things you noticed...>
> ```

### 判定标准

> - **PASS** — you ran the app, the change did what it should at its surface.
> - **FAIL** — you ran it and it doesn't. Or it breaks something else.
> - **BLOCKED** — couldn't reach a state where the change is observable.
> - **SKIP** — no runtime surface exists.
>
> **When in doubt, FAIL.** False PASS ships broken code; false FAIL costs one more human look.

## 中文翻译

### 核心理念

**验证是运行时观察。** 你构建应用、运行它、驱动它到变更代码执行的地方、捕获你看到的。那个捕获就是你的证据。没有其他东西是。

**不要运行测试。不要类型检查。** CI 在你到达之前已经运行了两者——PR 上的绿色检查意味着它们通过了。再次运行只是证明你能运行 CI。不是热身，不是"以防万一"，不是之后的回归扫描。

**不要导入并调用。** `import { foo } from './src/...'` 然后 `console.log(foo(x))` 是你写的单元测试。函数做了函数做的事——你从阅读它就知道了。应用从未运行过。

### 找到变更

确定完整范围——一个分支可能有很多提交：

```bash
git log --oneline @{u}..              # 计算提交数
git diff @{u}.. --stat                # 完整范围，不是 HEAD~1
gh pr diff                            # 如果在 PR 上下文中
```

在报告中注明提交数。大的 diff 被截断？重定向：`git diff @{u}.. > /tmp/d` 然后 Read 它。完全没有 diff → 说明，停止。

**diff 是基本事实。PR 描述是关于它的声明。** 两者都读。如果它们不一致，那就是一个发现。

### 表面（Surface）

表面是用户——人类或程序——遇到变更的地方。那就是你观察的地方。

| 变更到达 | 表面 | 你 |
|---|---|---|
| CLI / TUI | 终端 | 输入命令，捕获窗格 |
| 服务器 / API | 套接字 | 发送请求，捕获响应 |
| GUI | 像素 | 在 xvfb/Playwright 下驱动，截图 |
| 库 | 包边界 | 通过公共导出的示例代码 |
| Prompt / Agent 配置 | Agent | 运行 Agent，捕获其行为 |
| CI 工作流 | Actions | 分发它，读取运行结果 |

**内部函数？不是表面。** 仓库中的某些东西调用它，那个调用者在上面某一行结束。跟踪到那里。

**没有运行时表面** — 仅文档、无输出的类型声明、不产生行为差异的构建配置 — 报告 **SKIP — 无运行时表面：（原因）。** 不要运行测试来填补空白。

**diff 中的测试是作者的证据，不是表面。** CI 运行它们。纯测试 PR → SKIP，一行说明。混合 src+tests → 验证 src，忽略测试文件。阅读测试以了解要检查什么是可以的——它是规格说明。但然后去运行应用。

### 获取句柄

在冷启动前检查现有知识：

- **`.claude/skills/*verifier*/`** — 如果有匹配你表面的验证器，路由到它。
- **`.claude/skills/run-*/`** — 知道如何构建和启动。
- **都没有** — 从 README/package.json/Makefile 冷启动。限时约 15 分钟。卡住 → 报告 BLOCKED。

### 驱动它

使变更代码执行的最小路径：

- 变更了标志？带它运行。
- 变更了处理器？命中那个路由。
- 变更了错误处理？触发错误。
- 变更了内部函数？找到到达它的 CLI 命令/请求/渲染。运行那个。

**运行前回读你的计划。** 如果每一步都是构建/类型检查/运行测试文件——你计划的是 CI 重跑，不是验证。

声明验证通过后，继续：打破它（空输入、巨大输入、中途中断）、组合它（新功能 + 旧功能）、探索（什么是相邻的？什么看起来不对？）。

**判定是基本门槛。你的观察才是信号。** 带有三行精辟"我注意到…"的 PASS 比空白 PASS 更有价值。你是唯一真正*运行*了这个东西的审查者——任何让你停顿、绕路或感到"嗯？"的都是作者没有的信息。

**端到端，通过真实接口。** 各部分独立通过并不意味着流程有效——接缝是 bug 隐藏的地方。

### 捕获

Stdout、响应体、截图、窗格转储。捕获的输出是证据；你的记忆不是。意外的东西？不要绕过它——捕获、记录、决定是变更还是环境的问题。

### 报告

```
## Verification: <一行描述变更了什么>

**Verdict:** PASS | FAIL | BLOCKED | SKIP

**Claim:** <应该做什么——你对 diff 和/或声明的理解；注意任何不匹配>

**Method:** <如何获取句柄——哪个 verifier/run-skill，或冷启动；你启动了什么>

### Steps
1. ✅/❌/⚠️ <你对运行中的应用做了什么> → <你观察到了什么>
   <证据：应用自身的输出>

### Findings
<你注意到的事情。不仅仅是 bug——摩擦、意外、首次用户会绊倒的任何东西。>
```

### 判定标准

- **PASS** — 你运行了应用，变更在其表面做了它应该做的。
- **FAIL** — 你运行了它但它没有。或者它破坏了其他东西。
- **BLOCKED** — 无法到达变更可观察的状态。
- **SKIP** — 不存在运行时表面。

没有部分通过。"4 个中 3 个通过"是 FAIL，直到 4 个都通过或被解释。

**有疑问时，FAIL。** 假 PASS 会发布破损代码；假 FAIL 只需要多一次人工查看。

## 📋 模板变量说明

无模板变量。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 反直觉禁令 | "Don't run tests. Don't typecheck." | 直接挑战 LLM 的默认倾向（运行测试=验证），强制将注意力转向运行时观察 |
| 2 | 表面矩阵 | Change reaches → Surface → You 的映射表 | 将抽象的"验证"概念转化为按变更类型的具体操作查找表 |
| 3 | 不对称风险评估 | "False PASS ships broken code; false FAIL costs one more human look" | 量化两种错误的成本差异，建立"有疑问时 FAIL"的决策偏向 |
| 4 | 计划自审 | "Read your plan back... If every step is build/typecheck/run test file — you've planned a CI rerun" | 教会 LLM 在执行前自检计划质量的元认知技巧 |
| 5 | 超越判定 | "The verdict is table stakes. Your observations are the signal." | 将 LLM 的角色从"通过/失败判断者"提升为"第一手观察者"，鼓励发现超出声明范围的问题 |
| 6 | 声明 vs 事实对抗 | "The diff is ground truth. The PR description is a claim about it." | 建立批判性验证心态，防止 LLM 简单信任 PR 描述 |
| 7 | 绝不部分通过 | "No partial pass. '3 of 4 passed' is FAIL" | 消除模糊地带，防止 LLM 在部分失败时给出模棱两可的判定 |
| 8 | 探索性驱动 | "break it (empty input, huge input, interrupt mid-op), combine it, wander" | 鼓励 LLM 超越声明范围进行创造性测试，发现边界情况 |
