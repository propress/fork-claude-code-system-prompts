# config

| 属性 | 值 |
|------|-----|
| 原始名称 | Tool Description: Config |
| 分类 | Tool Descriptions → 通用工具 |
| 文件路径 | `system-prompts/tool-description-config.md` |
| CC 版本 | 2.1.88 |
| 模板变量 | `${GLOBAL_SETTINGS_LIST}`, `${PROJECT_SETTINGS_LIST}`, `${ADDITIONAL_SETTINGS_NOTE}` |

## 原文

> Get or set Claude Code configuration settings.
>
>   View or change Claude Code settings. Use when the user requests configuration changes, asks about current settings, or when adjusting a setting would benefit them.
>
>
> ## Usage
> - **Get current value:** Omit the "value" parameter
> - **Set new value:** Include the "value" parameter
>
> ## Configurable settings list
> The following settings are available for you to change:
>
> ### Global Settings (stored in ~/.claude.json)
> ${GLOBAL_SETTINGS_LIST.join(`
> `)}
>
> ### Project Settings (stored in settings.json)
> ${PROJECT_SETTINGS_LIST.join(`
> `)}
>
> ${ADDITIONAL_SETTINGS_NOTE}
> ## Examples
> - Get theme: { "setting": "theme" }
> - Set dark theme: { "setting": "theme", "value": "dark" }
> - Enable vim mode: { "setting": "editorMode", "value": "vim" }
> - Enable verbose: { "setting": "verbose", "value": true }
> - Change model: { "setting": "model", "value": "opus" }
> - Change permission mode: { "setting": "permissions.defaultMode", "value": "plan" }

## 中文翻译

> **原文：**
> Get or set Claude Code configuration settings.

**翻译：**
获取或设置 Claude Code 配置项。

---

> **原文：**
>   View or change Claude Code settings. Use when the user requests configuration changes, asks about current settings, or when adjusting a setting would benefit them.

**翻译：**
查看或更改 Claude Code 设置。当用户请求更改配置、询问当前设置，或者调整某项设置对用户有利时使用此工具。

---

> **原文：**
> ## Usage
> - **Get current value:** Omit the "value" parameter
> - **Set new value:** Include the "value" parameter

**翻译：**
## 用法
- **获取当前值：** 省略 "value" 参数
- **设置新值：** 包含 "value" 参数

---

> **原文：**
> ## Configurable settings list
> The following settings are available for you to change:
>
> ### Global Settings (stored in ~/.claude.json)
> ${GLOBAL_SETTINGS_LIST.join(` `)}
>
> ### Project Settings (stored in settings.json)
> ${PROJECT_SETTINGS_LIST.join(` `)}
>
> ${ADDITIONAL_SETTINGS_NOTE}

**翻译：**
## 可配置设置列表
以下是你可以更改的设置：

### 全局设置（存储在 ~/.claude.json）
${GLOBAL_SETTINGS_LIST.join(` `)}

### 项目设置（存储在 settings.json）
${PROJECT_SETTINGS_LIST.join(` `)}

${ADDITIONAL_SETTINGS_NOTE}

---

> **原文：**
> ## Examples
> - Get theme: { "setting": "theme" }
> - Set dark theme: { "setting": "theme", "value": "dark" }
> - Enable vim mode: { "setting": "editorMode", "value": "vim" }
> - Enable verbose: { "setting": "verbose", "value": true }
> - Change model: { "setting": "model", "value": "opus" }
> - Change permission mode: { "setting": "permissions.defaultMode", "value": "plan" }

**翻译：**
## 示例
- 获取主题：{ "setting": "theme" }
- 设置暗色主题：{ "setting": "theme", "value": "dark" }
- 启用 vim 模式：{ "setting": "editorMode", "value": "vim" }
- 启用详细输出：{ "setting": "verbose", "value": true }
- 更改模型：{ "setting": "model", "value": "opus" }
- 更改权限模式：{ "setting": "permissions.defaultMode", "value": "plan" }

## 📋 模板变量说明

| 变量名 | 说明 |
|--------|------|
| `${GLOBAL_SETTINGS_LIST}` | 全局设置列表（存储在用户主目录下的配置文件中） |
| `${PROJECT_SETTINGS_LIST}` | 项目级别设置列表（存储在项目的 settings.json 中） |
| `${ADDITIONAL_SETTINGS_NOTE}` | 附加设置说明文本 |

## 🔧 提示词技巧分析

| # | 技巧名称 | 原文片段（关键部分） | 分析：为什么在这里有效 |
|---|---------|-------------------|---------------------|
| 1 | 结构化列表（Structured Enumeration） | `## Usage / ## Configurable settings list / ## Examples` | 通过清晰的章节结构将使用方法、可配置项和示例分开，让 LLM 能快速定位不同类型的信息，减少混淆。 |
| 2 | 示例引导（Example-driven Guidance） | `Get theme: { "setting": "theme" }` 等多个 JSON 示例 | 提供具体的 JSON 参数格式示例，确保 LLM 生成正确的工具调用参数，避免格式错误。 |
| 3 | 条件逻辑注入（Conditional Logic Injection） | `Use when the user requests configuration changes, asks about current settings, or when adjusting a setting would benefit them` | 明确列出三种触发条件，指导 LLM 在正确的场景下主动使用此工具，而不是被动等待。 |
| 4 | 动态上下文注入（Dynamic Context Injection） | `${GLOBAL_SETTINGS_LIST}`, `${PROJECT_SETTINGS_LIST}`, `${ADDITIONAL_SETTINGS_NOTE}` | 通过模板变量动态注入可用的设置列表，使提示词能适应不同的配置环境，保持灵活性。 |
| 5 | 范围限定（Scope Limitation） | `Global Settings (stored in ~/.claude.json)` / `Project Settings (stored in settings.json)` | 将设置分为全局和项目两个层级，并标注存储位置，帮助 LLM 理解设置的作用范围和影响。 |
