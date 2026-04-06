# notebookedit

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: NotebookEdit |
| 分类 | Tool Descriptions → 文件操作 |
| 文件路径 | `system-prompts/tool-description-notebookedit.md` |
| CC 版本 | 2.0.14 |
| 模板变量 | 无 |

## 原文

> Completely replaces the contents of a specific cell in a Jupyter notebook (.ipynb file) with new source. Jupyter notebooks are interactive documents that combine code, text, and visualizations, commonly used for data analysis and scientific computing. The notebook_path parameter must be an absolute path, not a relative path. The cell_number is 0-indexed. Use edit_mode=insert to add a new cell at the index specified by cell_number. Use edit_mode=delete to delete the cell at the index specified by cell_number.

## 中文翻译

> **原文：**
> Completely replaces the contents of a specific cell in a Jupyter notebook (.ipynb file) with new source. Jupyter notebooks are interactive documents that combine code, text, and visualizations, commonly used for data analysis and scientific computing. The notebook_path parameter must be an absolute path, not a relative path. The cell_number is 0-indexed. Use edit_mode=insert to add a new cell at the index specified by cell_number. Use edit_mode=delete to delete the cell at the index specified by cell_number.

**翻译：**
将 Jupyter notebook（.ipynb 文件）中特定单元格的内容完全替换为新的源代码。Jupyter notebook 是结合了代码、文本和可视化的交互式文档，常用于数据分析和科学计算。notebook_path 参数必须是绝对路径，不能是相对路径。cell_number 从 0 开始索引。使用 edit_mode=insert 在 cell_number 指定的索引处添加新单元格。使用 edit_mode=delete 删除 cell_number 指定索引处的单元格。

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 负面约束（Negative Constraint） | `must be an absolute path, not a relative path` | 明确排除相对路径的使用，防止因路径解析问题导致操作错误的文件。 |
| 2 | 简洁指令（Concise Instruction） | `Completely replaces the contents of a specific cell` | 开头即明确工具的核心行为是"完全替换"，让 LLM 理解这是一个覆盖操作而非追加操作。 |
| 3 | 结构化列表（Structured Enumeration） | `edit_mode=insert` / `edit_mode=delete` 两种模式说明 | 在紧凑的描述中列出所有操作模式及其语义，确保 LLM 知道除了默认替换外还有插入和删除选项。 |
| 4 | 范围限定（Scope Limitation） | `Jupyter notebooks are interactive documents that combine code, text, and visualizations` | 提供上下文说明 Jupyter notebook 的性质，帮助 LLM 理解此工具适用于什么类型的文件。 |
