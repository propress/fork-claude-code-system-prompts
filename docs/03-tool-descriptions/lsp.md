# lsp

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: LSP |
| 分类 | Tool Descriptions → 搜索工具 |
| 文件路径 | `system-prompts/tool-description-lsp.md` |
| CC 版本 | 2.0.73 |
| 模板变量 | 无 |

## 原文

> Interact with Language Server Protocol (LSP) servers to get code intelligence features.
>
> Supported operations:
> - goToDefinition: Find where a symbol is defined
> - findReferences: Find all references to a symbol
> - hover: Get hover information (documentation, type info) for a symbol
> - documentSymbol: Get all symbols (functions, classes, variables) in a document
> - workspaceSymbol: Search for symbols across the entire workspace
> - goToImplementation: Find implementations of an interface or abstract method
> - prepareCallHierarchy: Get call hierarchy item at a position (functions/methods)
> - incomingCalls: Find all functions/methods that call the function at a position
> - outgoingCalls: Find all functions/methods called by the function at a position
>
> All operations require:
> - filePath: The file to operate on
> - line: The line number (1-based, as shown in editors)
> - character: The character offset (1-based, as shown in editors)
>
> Note: LSP servers must be configured for the file type. If no server is available, an error will be returned.

## 中文翻译

> **原文：**
> Interact with Language Server Protocol (LSP) servers to get code intelligence features.

**翻译：**
与语言服务器协议（LSP）服务器交互以获取代码智能功能。

---

> **原文：**
> Supported operations:
> - goToDefinition: Find where a symbol is defined
> - findReferences: Find all references to a symbol
> - hover: Get hover information (documentation, type info) for a symbol
> - documentSymbol: Get all symbols (functions, classes, variables) in a document
> - workspaceSymbol: Search for symbols across the entire workspace
> - goToImplementation: Find implementations of an interface or abstract method
> - prepareCallHierarchy: Get call hierarchy item at a position (functions/methods)
> - incomingCalls: Find all functions/methods that call the function at a position
> - outgoingCalls: Find all functions/methods called by the function at a position

**翻译：**
支持的操作：
- goToDefinition：查找符号的定义位置
- findReferences：查找符号的所有引用
- hover：获取符号的悬停信息（文档、类型信息）
- documentSymbol：获取文档中的所有符号（函数、类、变量）
- workspaceSymbol：在整个工作区中搜索符号
- goToImplementation：查找接口或抽象方法的实现
- prepareCallHierarchy：获取某个位置（函数/方法）的调用层级项
- incomingCalls：查找所有调用该位置函数/方法的函数/方法
- outgoingCalls：查找该位置函数/方法调用的所有函数/方法

---

> **原文：**
> All operations require:
> - filePath: The file to operate on
> - line: The line number (1-based, as shown in editors)
> - character: The character offset (1-based, as shown in editors)

**翻译：**
所有操作都需要：
- filePath：要操作的文件
- line：行号（从 1 开始，与编辑器中显示的一致）
- character：字符偏移量（从 1 开始，与编辑器中显示的一致）

---

> **原文：**
> Note: LSP servers must be configured for the file type. If no server is available, an error will be returned.

**翻译：**
注意：必须为文件类型配置 LSP 服务器。如果没有可用的服务器，将返回错误。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 结构化列表（Structured Enumeration） | 9 个操作名称及其说明的列表 | 通过完整枚举所有支持的 LSP 操作，让 LLM 准确知道可用的功能范围，便于在不同代码导航场景中选择正确的操作。 |
| 2 | 范围限定（Scope Limitation） | `All operations require: filePath, line, character` | 统一说明所有操作的共同必填参数，避免在每个操作中重复，同时确保 LLM 在调用任何操作时都提供完整的定位信息。 |
| 3 | 安全防护指令（Safety Guard） | `LSP servers must be configured for the file type. If no server is available, an error will be returned` | 提前告知可能的失败场景，帮助 LLM 在收到错误时正确理解原因，而不是反复重试或误报问题。 |
| 4 | 简洁指令（Concise Instruction） | `Interact with Language Server Protocol (LSP) servers to get code intelligence features` | 用一句话精确概括工具的核心功能，建立 LLM 对工具用途的正确认知。 |
