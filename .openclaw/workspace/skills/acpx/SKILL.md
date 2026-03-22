---
name: acpx
description: 使用 acpx 通过 Agent Client Protocol 运行编码代理，支持会话管理、队列、权限控制和多种输出格式
metadata:
  {
    "openclaw": { "emoji": "🔧", "requires": { "anyBins": ["acpx", "npm"] } },
  }
---

# ACPX - Agent Client Protocol CLI

_无头、可脚本化的 ACP 客户端，用于 agent 间通信。_

## 什么时候用

- 需要运行编码代理时
- 管理持久化 ACP 会话
- 队列化 prompt 提交
- 从脚本中消费结构化 agent 输出

## 安装

```bash
npm install -g acpx@latest
```

## 命令结构

```
acpx [global_options] [command] [prompt...]
acpx [global_options] exec [prompt_options] [prompt...]
acpx [global_options] <agent> [prompt_options] [prompt...]
```

## 内置 Agent

| Agent | 命令 |
|-------|------|
| claude | `npx -y @zed-industries/claude-agent-acp` (ACPX 默认) |
| claude | `npx -y @zed-industries/claude-agent-acp` |
| pi | `npx pi-acp` |
| openclaw | `openclaw acp` |
| gemini | `gemini --acp` |
| kimi | `kimi acp` |
| opencode | `npx -y opencode-ai acp` |
| qwen | `qwen --acp` |

**默认 agent**: `claude`

## 命令详解

### Prompt (默认 - 持续会话)

```bash
# 默认用 claude
acpx "fix the auth module"

# 指定 agent
acpx claude "refactor the API"

# 命名会话
acpx -s myproject happy "add user auth"

# 等待正在运行的会话（队列）
acpx happy "next task"

# 不等待，立即返回
acpx --no-wait happy "background task"
```

**行为**：
- 使用已保存的会话
- 自动恢复之前的对话
- 如果会话不存在，提示创建新会话

### Exec (单次执行)

```bash
acpx exec "summarize this repo"
acpx happy exec "write a unit test for utils.js"
```

**行为**：
- 单次 prompt，不保存会话状态
- 适合简单任务

### Sessions 管理

```bash
acpx sessions list              # 列出所有会话
acpx sessions new --name test   # 创建新会话
acpx sessions show mysession   # 查看会话详情
acpx sessions history mysession # 查看历史
acpx sessions close mysession   # 关闭会话
```

### Cancel / Mode / Config

```bash
acpx happy cancel              # 取消当前任务
acpx happy set-mode auto       # 设置模式
acpx happy set approval_policy conservative  # 设置权限策略
acpx config show               # 显示配置
acpx config init               # 初始化配置
```

## 全局选项

| 选项 | 说明 |
|------|------|
| `--cwd <dir>` | 工作目录 (默认: workspace) |
| `--approve-all` | 自动批准所有权限请求 |
| `--approve-reads` | 自动批准读取，提示写入 |
| `--deny-all` | 拒绝所有权限请求 |
| `--format <fmt>` | 输出格式: text, json, quiet |
| `--model <id>` | 指定模型 |
| `--max-turns` | 最大回合数 |
| `--timeout` | 超时秒数 |
| `-s, --session` | 命名会话 |
| `--no-wait` | 队列模式，不等待 |
| `-f, --file` | 从文件读取 prompt |

## 工作流示例

### 日常开发

```bash
# 1. 开始一个任务
acpx happy "fix the login bug"

# 2. 继续之前的会话
acpx happy "now add unit tests"

# 3. 查看会话状态
acpx happy status

# 4. 取消任务
acpx happy cancel
```

### 复杂项目

```bash
# 创建命名会话
acpx -s myapp happy "build a REST API"

# 在项目中继续
cd projects/20250601s-myapp
acpx -s myapp happy "add CRUD endpoints"
```

### 后台任务

```bash
# 不等待，继续其他工作
acpx --no-wait happy "refactor the entire codebase"

# 之后查看
acpx sessions show myapp
```

## ACPX 用 Claude Code

ACPX 默认用 Claude Code：

```bash
# 基本用法
acpx "your prompt here"           # 默认 claude
acpx claude "fix the bug"

# 跳过权限验证
acpx --approve-all "make changes"

# 命名会话 + 工作目录
acpx -s myproject --cwd ./projects/myapp claude "code"
```

## 权限策略

| 策略 | 说明 |
|------|------|
| `skip` | 跳过认证 |
| `fail` | 需要认证否则失败 |
| `conservative` | 保守模式 |

---

## 在 OpenClaw 中使用

当需要委托编码工作时，使用 acpx：

```bash
# 启动编码代理
exec command="acpx happy 'refactor auth module'"

# 命名会话
exec command="acpx -s myproject happy 'add feature'"

# 查看状态
exec command="acpx happy status"
```

**注意**：开发必须在 `projects/` 目录下进行！
