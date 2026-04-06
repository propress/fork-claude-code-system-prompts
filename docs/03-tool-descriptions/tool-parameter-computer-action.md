# tool-parameter-computer-action

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Parameter: Computer action |
| 分类 | Tool Descriptions → 工具参数 |
| 文件路径 | `system-prompts/tool-parameter-computer-action.md` |
| CC 版本 | 2.0.71 |
| 模板变量 | 无 |
| 首次出现版本 | 2.0.71 |
| 关联文件 | [`tool-description-computer.md`](computer.md)（Computer 工具主描述） |

> **注：** 本文件是 Computer 工具（Chrome 浏览器自动化工具）的 `action` 参数描述。它定义了该工具支持的所有操作类型，与 [computer.md](computer.md) 中的主工具描述互为补充。

## 原文

> The action to perform:
> * `left_click`: Click the left mouse button at the specified coordinates.
> * `right_click`: Click the right mouse button at the specified coordinates to open context menus.
> * `double_click`: Double-click the left mouse button at the specified coordinates.
> * `triple_click`: Triple-click the left mouse button at the specified coordinates.
> * `type`: Type a string of text.
> * `screenshot`: Take a screenshot of the screen.
> * `wait`: Wait for a specified number of seconds.
> * `scroll`: Scroll up, down, left, or right at the specified coordinates.
> * `key`: Press a specific keyboard key.
> * `left_click_drag`: Drag from start_coordinate to coordinate.
> * `zoom`: Take a screenshot of a specific region for closer inspection.
> * `scroll_to`: Scroll an element into view using its element reference ID from read_page or find tools.
> * `hover`: Move the mouse cursor to the specified coordinates or element without clicking. Useful for revealing tooltips, dropdown menus, or triggering hover states.

## 中文翻译

> **原文：**
> The action to perform:

**翻译：**
要执行的操作：

---

> **原文：**
> * `left_click`: Click the left mouse button at the specified coordinates.

**翻译：**
* `left_click`：在指定坐标处点击鼠标左键。

---

> **原文：**
> * `right_click`: Click the right mouse button at the specified coordinates to open context menus.

**翻译：**
* `right_click`：在指定坐标处点击鼠标右键以打开上下文菜单。

---

> **原文：**
> * `double_click`: Double-click the left mouse button at the specified coordinates.

**翻译：**
* `double_click`：在指定坐标处双击鼠标左键。

---

> **原文：**
> * `triple_click`: Triple-click the left mouse button at the specified coordinates.

**翻译：**
* `triple_click`：在指定坐标处三击鼠标左键。

---

> **原文：**
> * `type`: Type a string of text.

**翻译：**
* `type`：输入一段文本字符串。

---

> **原文：**
> * `screenshot`: Take a screenshot of the screen.

**翻译：**
* `screenshot`：对屏幕进行截图。

---

> **原文：**
> * `wait`: Wait for a specified number of seconds.

**翻译：**
* `wait`：等待指定的秒数。

---

> **原文：**
> * `scroll`: Scroll up, down, left, or right at the specified coordinates.

**翻译：**
* `scroll`：在指定坐标处向上、下、左或右滚动。

---

> **原文：**
> * `key`: Press a specific keyboard key.

**翻译：**
* `key`：按下特定的键盘按键。

---

> **原文：**
> * `left_click_drag`: Drag from start_coordinate to coordinate.

**翻译：**
* `left_click_drag`：从起始坐标拖动到目标坐标。

---

> **原文：**
> * `zoom`: Take a screenshot of a specific region for closer inspection.

**翻译：**
* `zoom`：对特定区域进行截图以便近距离检查。

---

> **原文：**
> * `scroll_to`: Scroll an element into view using its element reference ID from read_page or find tools.

**翻译：**
* `scroll_to`：使用从 read_page 或 find 工具获取的元素引用 ID，将元素滚动到可视区域内。

---

> **原文：**
> * `hover`: Move the mouse cursor to the specified coordinates or element without clicking. Useful for revealing tooltips, dropdown menus, or triggering hover states.

**翻译：**
* `hover`：将鼠标光标移动到指定坐标或元素处但不点击。适用于显示工具提示、下拉菜单或触发悬停状态。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 枚举式参数定义（Exhaustive Enumeration） | 13 个 `action` 值的完整列表 | 通过穷举所有合法操作类型，严格限定模型可选择的行为空间，避免模型生成无效的 action 值 |
| 2 | 统一结构化格式（Uniform Structured Format） | 每项均为 `` `动作名`: 一句话描述 `` | 保持一致的"名称: 描述"格式，使模型能快速定位和理解每个操作的语义，降低解析复杂度 |
| 3 | 语义分组（Implicit Semantic Grouping） | 点击类(4)→输入类(2)→视图控制类(5)→拖放类(1)→悬停类(1) | 操作按功能类型隐式分组排列，帮助模型建立操作类别的心智模型 |
| 4 | 使用场景补充（Use-case Annotation） | `hover`: "Useful for revealing tooltips, dropdown menus, or triggering hover states" | 对非直觉操作补充使用场景说明，帮助模型判断何时应选择该操作而非其他操作 |
| 5 | 工具链引用（Tool Chain Reference） | `scroll_to`: "using its element reference ID from read_page or find tools" | 说明参数值可能来源于其他工具的输出，建立工具间的数据流依赖关系 |
| 6 | 坐标系锚定（Coordinate System Anchoring） | 多个操作引用 "at the specified coordinates" | 反复强调操作基于坐标系统执行，与 [computer.md](computer.md) 中"先截图确定坐标再操作"的指令形成呼应 |

## 📌 补充说明

### 操作类型分类

| 类别 | 操作 | 数量 |
|------|------|------|
| 鼠标点击 | `left_click`, `right_click`, `double_click`, `triple_click` | 4 |
| 文本输入 | `type`, `key` | 2 |
| 视图控制 | `screenshot`, `zoom`, `scroll`, `scroll_to`, `wait` | 5 |
| 拖放操作 | `left_click_drag` | 1 |
| 悬停交互 | `hover` | 1 |

### 与 Computer 工具主描述的关系

本文件是 [computer.md](computer.md) 的参数级补充文档：

- **computer.md** 定义了工具的整体行为规范（先截图再操作、点击元素中心等）
- **本文件** 定义了 `action` 参数的所有合法值及其语义

两者共同构成 Chrome 浏览器自动化工具的完整指令集。

### 设计特点

1. **穷举式设计**：列出所有 13 种操作，不留歧义空间
2. **渐进式复杂度**：从基础操作（点击、输入）到高级操作（拖放、悬停），符合直觉的排列顺序
3. **跨工具引用**：`scroll_to` 操作引用了 `read_page` 和 `find` 工具的输出，体现了 Claude Code 工具间的协作设计
