# computer

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Computer |
| 分类 | Tool Descriptions → 通用工具 |
| 文件路径 | `system-prompts/tool-description-computer.md` |
| CC 版本 | 2.0.71 |
| 模板变量 | 无 |

## 原文

> Use a mouse and keyboard to interact with a web browser, and take screenshots. If you don't have a valid tab ID, use tabs_context_mcp first to get available tabs.
> * Whenever you intend to click on an element like an icon, you should consult a screenshot to determine the coordinates of the element before moving the cursor.
> * If you tried clicking on a program or link but it failed to load, even after waiting, try adjusting your click location so that the tip of the cursor visually falls on the element that you want to click.
> * Make sure to click any buttons, links, icons, etc with the cursor tip in the center of the element. Don't click boxes on their edges unless asked.

## 中文翻译

> **原文：**
> Use a mouse and keyboard to interact with a web browser, and take screenshots. If you don't have a valid tab ID, use tabs_context_mcp first to get available tabs.

**翻译：**
使用鼠标和键盘与 Web 浏览器交互，并进行截图。如果没有有效的标签页 ID，请先使用 tabs_context_mcp 获取可用标签页。

---

> **原文：**
> * Whenever you intend to click on an element like an icon, you should consult a screenshot to determine the coordinates of the element before moving the cursor.

**翻译：**
* 每当你打算点击图标等元素时，应先查看截图以确定元素的坐标，然后再移动光标。

---

> **原文：**
> * If you tried clicking on a program or link but it failed to load, even after waiting, try adjusting your click location so that the tip of the cursor visually falls on the element that you want to click.

**翻译：**
* 如果你尝试点击某个程序或链接但加载失败，即使等待之后仍然如此，请尝试调整点击位置，使光标尖端在视觉上落在你想要点击的元素上。

---

> **原文：**
> * Make sure to click any buttons, links, icons, etc with the cursor tip in the center of the element. Don't click boxes on their edges unless asked.

**翻译：**
* 确保点击任何按钮、链接、图标等时，光标尖端位于元素的中心位置。除非被要求，否则不要点击方框的边缘。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 角色/行为锚定（Role/Behavior Anchoring） | "Use a mouse and keyboard to interact with a web browser, and take screenshots" | 开头即定义了工具的核心功能和交互模式，为后续指令建立行为框架 |
| 2 | 优先级排序（Priority Ordering） | "consult a screenshot to determine the coordinates ... before moving the cursor" | 强调"先截图后操作"的顺序，确保模型在点击前获取准确的元素位置信息 |
| 3 | 条件逻辑注入（Conditional Logic Injection） | "If you don't have a valid tab ID, use tabs_context_mcp first" | 为缺少标签页 ID 的情况提供了明确的前置操作步骤，避免工具调用失败 |
| 4 | 负面约束（Negative Constraint） | "Don't click boxes on their edges unless asked" | 明确禁止边缘点击行为，降低因点击位置不精确导致的交互失败率 |
| 5 | 结构化列表（Structured Enumeration） | 使用 `*` 项目符号列出多条操作规则 | 以列表形式组织多条指令，使每条规则独立且易于解析和遵循 |
