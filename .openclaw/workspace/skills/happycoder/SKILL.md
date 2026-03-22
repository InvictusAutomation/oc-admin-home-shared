---
name: happycoder
description: HappyCoder - 通过移动设备远程使用 Claude Code/Codex 进行编程
metadata:
  {
    "openclaw": { "emoji": "📱", "requires": { "anyBools": ["tmux", "ssh"] } },
  }
---

# HappyCoder - 移动端编程工具

_用手机也能写代码。通过 SSH 连接电脑，在手机上运行 Claude Code。_

## 安装

```bash
npm install -g happy-coder
happy --help
```

## 认证

```bash
# 方式一：设置环境变量
export ANTHROPIC_AUTH_TOKEN="Your API Key"
export ANTHROPIC_BASE_URL="https://api.minimaxi.com/anthropic"

# 方式二：使用 happy auth
happy auth login --force
```

## 首次认证流程（新终端）

1. 首次启动 HappyCoder → 提示选择认证方式
2. **永远选 1** (Mobile App)
3. 把 `happy://` 开头的 URL 通过 Telegram 发送给用户
4. 用户会协助完成验证

**重要**：首次认证必须通过用户协助完成。

## 什么是 HappyCoder

HappyCoder 是一种工作方式：通过手机 SSH 到运行 Claude Code/Codex 的电脑，用手机进行编程。

```
手机 (Termius) ──SSH──> 电脑 (Claude Code + tmux)
```

## 快速命令

```bash
# 启动 HappyCoder (跳过权限验证)
happy --yolo

# 或
happy --dangerously-skip-permissions

# 常用选项
happy --resume          # 继续上次对话
happy codex             # 进入 Codex 模式
```

## 核心组件

| 组件 | 作用 |
|------|------|
| **Termius** | 手机上的 SSH 客户端 |
| **SSH** | 安全连接到电脑 |
| **tmux** | 保持会话不断开 |
| **Claude Code** | 编程代理 |
| **happy** | 启动命令，`--yolo` 跳过权限验证 |

## 使用场景

- 在外面用手机写代码
- 通勤时修复 bug
- 躺床上审批 Claude 的 PR
- 随时随地监控长时间运行的任务

## 快速开始

### 1. 电脑端：确保有 tmux

```bash
# 检查是否已安装
which tmux

# 安装 tmux (如未安装)
brew install tmux
```

### 2. 电脑端：启动 tmux 会话

```bash
# 创建名为 happy 的 tmux 会话
tmux new -s happy

# 方式一：直接运行 Claude Code (需要配置环境变量)
claude

# 方式二：跳过权限验证 (常用)
happy --dangerously-skip-permissions

# 或者直接 echo 传送命令
tmux send-keys -t happy 'happy --dangerously-skip-permissions' C-m
```

### 3. 手机端：SSH 连接

```
# 使用 Termius 连接
ssh your-username@your-mac-ip

# 重新连接之前的 tmux 会话
tmux attach -t claude
```

## tmux 常用命令

| 操作 | 命令 |
|------|------|
| 创建新会话 | `tmux new -s <name>` |
| 分离会话 (保持运行) | `Ctrl+B` 然后按 `D` |
| 重新连接 | `tmux attach -t <name>` |
| 列出所有会话 | `tmux ls` |
| 杀掉会话 | `tmux kill-session -t <name>` |

## 从任何地方连接 (Tailscale)

默认 SSH 只能在家庭 Wi-Fi 用。用 Tailscale 可以从任何地方连接：

1. Mac 和手机都安装 Tailscale
2. 登录同一账户
3. 使用 Tailscale IP (100.x.x.x) 连接

```bash
# 获取 Tailscale IP
/Applications/Tailscale.app/Contents/MacOS/Tailscale ip -4
```

## HappyCoder 工作流

```
1. 用户说 "用 HappyCoder" 或 "用 Happy" 或 "用 tmux 开发"
   ↓
2. 在 projects/ 下创建项目文件夹 (命名: <日期><s|l>-<项目描述>)
   ↓
3. 创建 tmux 会话 (tmux new -s happy)
   ↓
4. 进入项目目录，启动 HappyCoder (happy --yolo)
   ↓
5. 通过 tmux 会话进行编程
   ↓
6. 用户可以通过手机 Termius 随时连接
```

## OpenClaw 中的使用

当用户说 "用 Happy" 或 "用 HappyCoder" 时：

```bash
# 检查是否有现成会话
tmux ls | grep claude

# 如果没有，创建新会话并启动 Claude Code
tmux new -s claude
claude

# 或者连接到现有会话
tmux attach -t claude
```

## 手机使用技巧

### 语音输入
启用手机键盘的语音输入，可以说：
> "Create a function that validates email addresses"

### 保存常用命令
在 Termius 中保存 snippets：
- `tmux attach -t claude` - 重新连接
- `claude --resume` - 继续上次对话

### 蓝牙键盘
长时间工作可以用蓝牙键盘

---

_ HappyCoder = 手机 + SSH + Claude Code + tmux _
