#!/usr/bin/env python3
"""
Generate Chinese documentation for all 73 tool-description files.
Reads each source file, extracts metadata, generates translations and analysis.
"""

import os
import re
import sys
import subprocess

SOURCE_DIR = "system-prompts"
TARGET_DIR = "docs/03-tool-descriptions"

def get_subcategory(name):
    if name.startswith("bash-"):
        return "Bash 工具"
    agent_names = {"taskcreate", "skill", "sendmessagetool", "sendmessagetool-non-agent-teams"}
    if name.startswith("agent-") or name in agent_names or name.startswith("tasklist-") or name.startswith("team"):
        return "Agent 工具"
    if name in ("edit", "write", "readfile", "notebookedit"):
        return "文件操作"
    if name in ("grep", "lsp") or name.startswith("toolsearch-"):
        return "搜索工具"
    if name in ("enterplanmode", "exitplanmode", "enterworktree", "exitworktree"):
        return "计划模式"
    if name.startswith("askuserquestion") or name.startswith("request_teach_access"):
        return "用户交互"
    return "通用工具"

def parse_frontmatter(content):
    match = re.search(r'<!--\s*(.*?)\s*-->', content, re.DOTALL)
    if not match:
        return {}, content
    fm_text = match.group(1)
    body = content[match.end():].strip()
    meta = {}
    name_match = re.search(r"name:\s*['\"]?(.*?)['\"]?\s*$", fm_text, re.MULTILINE)
    if name_match:
        meta['name'] = name_match.group(1).strip().rstrip("'\"")
    ver_match = re.search(r"ccVersion:\s*(\S+)", fm_text)
    if ver_match:
        meta['ccVersion'] = ver_match.group(1)
    variables = []
    in_vars = False
    for line in fm_text.split('\n'):
        line = line.strip()
        if line.startswith('variables:'):
            in_vars = True
            continue
        if in_vars:
            if line.startswith('- '):
                variables.append(line[2:].strip())
            elif line and not line.startswith('-') and not line.startswith('#'):
                in_vars = False
    meta['variables'] = variables
    return meta, body

VAR_DESCRIPTIONS = {
    'TOOL_BASE_DESCRIPTION': '工具的基础描述文本',
    'TOOL_PARAMETERS_DESCRIPTION': '工具参数的描述文本',
    'GET_TIER_FN': '获取用户订阅层级的函数',
    'IS_TRUTHY_FN': '判断值是否为真的辅助函数',
    'PROCESS_OBJECT': 'Node.js 进程对象，用于访问环境变量等',
    'IS_SUBAGENT_CONTEXT_FN': '判断当前是否在子智能体上下文中的函数',
    'HAS_SUBAGENT_TYPES': '是否有可用的子智能体类型定义',
    'SEND_MESSAGE_TOOL_NAME': '发送消息工具的名称',
    'TOOL_OBJECT': '工具对象引用',
    'IS_TEAMMATE_CONTEXT_FN': '判断当前是否在团队成员上下文中的函数',
    'ADDITIONAL_USAGE_NOTES': '附加的使用说明',
    'EXTRA_USAGE_NOTES': '额外的使用提示',
    'SUBAGENT_TYPE_DEFINITIONS': '子智能体类型的定义列表',
    'DEFAULT_AGENT_DESCRIPTION': '默认智能体描述文本',
    'BASH_TOOL_NAME': 'Bash 工具的名称',
    'COMPUTER_TOOL_NAME': '计算机操作工具的名称',
    'FILE_EDIT_TOOL_NAME': '文件编辑工具的名称',
    'FILE_WRITE_TOOL_NAME': '文件写入工具的名称',
    'FILE_READ_TOOL_NAME': '文件读取工具的名称',
    'GREP_TOOL_NAME': '搜索（grep）工具的名称',
    'LS_TOOL_NAME': '目录列表工具的名称',
    'GLOB_TOOL_NAME': '文件匹配（glob）工具的名称',
    'TASK_TOOL_NAME': '任务/智能体工具的名称',
    'TOOL_NAME': '当前工具的名称',
    'MCP_TOOL_NAME': 'MCP（Model Context Protocol）工具的名称',
    'NOTEBOOK_EDIT_TOOL_NAME': 'Notebook 编辑工具的名称',
    'READ_NOTEBOOK_TOOL_NAME': 'Notebook 读取工具的名称',
    'WEB_FETCH_TOOL_NAME': '网页获取工具的名称',
    'WEB_SEARCH_TOOL_NAME': '网页搜索工具的名称',
    'SEARCH_TOOL_NAME': '搜索工具的名称',
    'PLAN_MODE_TOOL_NAME': '计划模式工具的名称',
    'EXIT_PLAN_MODE_TOOL_NAME': '退出计划模式工具的名称',
    'TODO_TOOL_NAME': 'TODO 管理工具的名称',
    'CONFIG_TOOL_NAME': '配置工具的名称',
    'CRON_CREATE_TOOL_NAME': '定时任务创建工具的名称',
    'OPERATING_SYSTEM': '当前操作系统类型',
    'IS_EXTENDED_THINKING': '是否启用了扩展思考模式',
    'TOOL_USE_INSTRUCTIONS': '工具使用的指令说明',
    'MAX_TOOL_CALLS_PER_MESSAGE': '每条消息允许的最大工具调用次数',
    'MAX_CONCURRENT_TOOL_CALLS': '最大并发工具调用数',
    'REPO_DIR': '代码仓库的根目录路径',
    'WORKTREE_DIR': '工作树目录路径',
    'BASH_COMMAND_NAME': 'Bash 命令的名称',
    'SANDBOX_TYPE': '沙箱类型',
    'SANDBOX_CMD': '沙箱命令',
    'SANDBOX_DOCS_URL': '沙箱文档链接',
    'SANDBOX_CONFIG_FILE': '沙箱配置文件路径',
    'AVAILABLE_SANDBOX_MODES': '可用的沙箱模式列表',
    'SHELL': '当前使用的 Shell 类型',
    'IDLE_TIMEOUT_MS': '空闲超时时间（毫秒）',
    'COMBINED_DESCRIPTION': '组合描述文本',
    'ADDITIONAL_INSTRUCTIONS': '附加指令说明',
    'PLATFORM': '当前平台',
    'ORIGINAL_CWD': '原始工作目录路径',
    'TIMEOUT_SECONDS': '超时秒数',
    'TOOL_RESULT_TOO_LARGE_MESSAGE': '工具结果过大时的提示消息',
    'TMPDIR': '临时目录路径',
    'USER_FACING_SANDBOX_MODE': '用户可见的沙箱模式名称',
    'BASE_BRANCH': '基础分支名称',
    'LS_DESCRIPTION': '目录列表工具的描述',
    'FILE_EDIT_DESCRIPTION': '文件编辑工具的描述',
    'CONNECTED_MCP_SERVERS': '已连接的 MCP 服务器列表',
    'TOOL_SEARCH_DESCRIPTION': '工具搜索的描述',
    'TODO_WRITE_DESCRIPTION': 'TODO 写入工具的描述',
    'CRON_DESCRIPTION': '定时任务工具的描述',
    'LSP_DIAGNOSTICS_TOOL_NAME': 'LSP 诊断工具的名称',
    'LSP_DIAGNOSTICS_DESCRIPTION': 'LSP 诊断工具的描述',
    'CONFIG_DESCRIPTION': '配置工具的描述',
    'WORKTREE_DESCRIPTION': '工作树工具的描述',
    'EXIT_WORKTREE_TOOL_NAME': '退出工作树工具的名称',
    'ENTER_WORKTREE_TOOL_NAME': '进入工作树工具的名称',
    'CURRENT_WORKTREE_PATH': '当前工作树的路径',
    'SLASH_COMMAND_PREFIX': '斜杠命令前缀',
    'CURRENT_WORKING_DIR': '当前工作目录',
    'IS_PLAN_MODE_AVAILABLE': '计划模式是否可用',
    'LIST_ITEM_MARKER': '列表项标记符',
    'MAX_SLEEP_SECONDS': '最大休眠秒数',
    'TOOL_SEARCH_SECOND_PART': '工具搜索描述的第二部分',
    'SKILL_SEARCH_TOOL_DESCRIPTION': '技能搜索工具的描述',
}

def get_var_desc(var, name):
    return VAR_DESCRIPTIONS.get(var, f'用于 {name} 相关功能的配置变量')

def find_snippet(text, pattern):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        s = match.group(0).strip()
        return s[:100]
    return None

def analyze_techniques(body, name):
    techniques = []
    text = body.strip()
    if not text or len(text) < 10:
        techniques.append(("简洁指令（Concise Instruction）", text[:60] if text else "(空内容)", "极简指令直接传达单一明确要求，减少歧义"))
        return techniques

    # Role/behavior anchoring
    if re.search(r'\b(you (are|should|must|will|can))\b', text, re.IGNORECASE):
        s = find_snippet(text, r'[Yy]ou (?:are|should|must|will|can)[^.\n]{0,80}')
        if s:
            techniques.append(("角色/行为锚定（Role/Behavior Anchoring）", s, "通过明确指定行为预期，引导模型在特定框架内运作"))

    # Conditional logic with template vars
    if re.search(r'\$\{[^}]+\}.*[\?:]', text) or re.search(r'\?\s*`', text):
        s = find_snippet(text, r'\$\{[^}]+\}[^`\n]{0,60}')
        if s:
            techniques.append(("条件逻辑注入（Conditional Logic Injection）", s, "通过模板变量和条件表达式动态调整提示内容，适应不同运行环境"))

    # Negative constraints
    if re.search(r'\b(do not|don\'t|never|avoid|must not|NEVER|DO NOT|cannot|can\'t|should not|shouldn\'t)\b', text, re.IGNORECASE):
        s = find_snippet(text, r'(?:do not|don\'t|never|avoid|must not|NEVER|DO NOT|cannot|can\'t|should not|shouldn\'t)[^.\n]{0,80}')
        if s:
            techniques.append(("负面约束（Negative Constraint）", s, "明确禁止不期望的行为，防止常见错误模式"))

    # Structured lists
    if re.search(r'^\s*[-*]\s', text, re.MULTILINE) or re.search(r'^\s*\d+[\.)]\s', text, re.MULTILINE):
        s = find_snippet(text, r'[-*]\s[^\n]{0,80}')
        if s:
            techniques.append(("结构化列表（Structured Enumeration）", s, "使用列表格式组织多条指令，提高可读性和逐项执行的准确率"))

    # Examples
    if re.search(r'(example|e\.g\.|for instance|such as|like )', text, re.IGNORECASE):
        s = find_snippet(text, r'(?:example|e\.g\.|for instance|such as|like )[^.\n]{0,80}')
        if s:
            techniques.append(("示例引导（Example-driven Guidance）", s, "通过具体示例消除抽象指令的歧义，提供明确的参考模式"))

    # Priority/preference
    if re.search(r'(prefer|instead of|rather than|priority|first.*then|always.*before)', text, re.IGNORECASE):
        s = find_snippet(text, r'(?:prefer|instead of|rather than|priority|always)[^.\n]{0,80}')
        if s:
            techniques.append(("优先级排序（Priority Ordering）", s, "建立行为优先级，在多种可选方案中引导模型选择最优路径"))

    # Dynamic context injection
    if '${' in text and not any(t[0].startswith("条件") for t in techniques):
        s = find_snippet(text, r'\$\{[A-Z_]+\}')
        if s:
            techniques.append(("动态上下文注入（Dynamic Context Injection）", s, "通过模板变量在运行时注入环境特定信息，使提示词适应不同配置"))

    # Scope limitation
    if re.search(r'\b(only|exclusively|limited to|restrict|solely|specifically)\b', text, re.IGNORECASE):
        s = find_snippet(text, r'(?:only|exclusively|limited to|restrict|solely|specifically)[^.\n]{0,80}')
        if s:
            techniques.append(("范围限定（Scope Limitation）", s, "限定操作范围，防止模型过度扩展行为边界"))

    # Safety patterns
    if re.search(r'\b(safe|security|dangerous|risk|careful|caution|protect|sensitive)\b', text, re.IGNORECASE):
        s = find_snippet(text, r'(?:safe|security|dangerous|risk|careful|caution|protect|sensitive)[^.\n]{0,80}')
        if s:
            techniques.append(("安全防护指令（Safety Guard）", s, "嵌入安全意识指令，确保操作时考虑潜在风险"))

    # Conciseness
    if re.search(r'\b(concise|brief|short|efficient|minimal|terse|compact)\b', text, re.IGNORECASE):
        s = find_snippet(text, r'(?:concise|brief|short|efficient|minimal|terse|compact)[^.\n]{0,80}')
        if s:
            techniques.append(("简洁性约束（Conciseness Constraint）", s, "要求输出简洁，减少冗余信息，提升信息密度"))

    if not techniques:
        if len(text) < 80:
            techniques.append(("简洁指令（Concise Instruction）", text[:80], "极简指令减少歧义，直接传达明确要求"))
        else:
            techniques.append(("上下文约束（Contextual Constraint）", text[:80], "通过具体上下文信息约束模型的行为范围"))

    return techniques[:6]

def split_paragraphs(text):
    if not text.strip():
        return [""]
    lines = text.split('\n')
    paragraphs = []
    current = []
    for line in lines:
        if line.strip() == '' and current:
            paragraphs.append('\n'.join(current))
            current = []
        else:
            current.append(line)
    if current:
        paragraphs.append('\n'.join(current))
    return [p for p in paragraphs if p.strip()]

def esc(text):
    return text.replace('|', '\\|')

def generate_doc(name):
    source_path = os.path.join(SOURCE_DIR, f"tool-description-{name}.md")
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    meta, body = parse_frontmatter(content)
    subcategory = get_subcategory(name)
    orig_name = meta.get('name', f'Tool Description: {name}')
    cc_version = meta.get('ccVersion', '未知')
    variables = meta.get('variables', [])
    vars_display = ", ".join(f"`${{{v}}}`" for v in variables) if variables else "无"

    doc = []
    doc.append(f"# {name}\n")
    doc.append("| 属性 | 值 |")
    doc.append("|------|-----|")
    doc.append(f"| 原始名称 | {orig_name} |")
    doc.append(f"| 分类 | Tool Descriptions → {subcategory} |")
    doc.append(f"| 文件路径 | `system-prompts/tool-description-{name}.md` |")
    doc.append(f"| CC 版本 | {cc_version} |")
    doc.append(f"| 模板变量 | {vars_display} |")
    doc.append("")

    # 原文 section
    doc.append("## 原文\n")
    if body.strip():
        for line in body.split('\n'):
            if line.strip():
                doc.append(f"> {line}")
            else:
                doc.append(">")
    else:
        doc.append("> （空内容）")
    doc.append("")

    # Return the partial doc + body for translation
    return '\n'.join(doc), body, meta, variables, name

def write_doc_file(name, doc_content):
    target_path = os.path.join(TARGET_DIR, f"{name}.md")
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(doc_content)
    return target_path

# Output all source file contents for processing
if __name__ == '__main__':
    names = []
    for f in sorted(os.listdir(SOURCE_DIR)):
        if f.startswith('tool-description-') and f.endswith('.md'):
            name = f[len('tool-description-'):-len('.md')]
            names.append(name)
    
    # Output each file's metadata in a parseable format
    for name in names:
        source_path = os.path.join(SOURCE_DIR, f"tool-description-{name}.md")
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
        meta, body = parse_frontmatter(content)
        print(f"### FILE: {name}")
        print(f"NAME: {meta.get('name', '')}")
        print(f"VERSION: {meta.get('ccVersion', '')}")
        print(f"VARS: {','.join(meta.get('variables', []))}")
        print(f"BODY_START")
        print(body)
        print(f"BODY_END")
        print()
    
    print(f"TOTAL: {len(names)}")
