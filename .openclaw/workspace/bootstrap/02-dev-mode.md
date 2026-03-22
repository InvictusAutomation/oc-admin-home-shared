# 02-dev-mode.md - 开发模式

## 开发方式

| 方式 | 命令 |
|------|------|
| ACPX | `acpx claude "task"` |
| tmux + Happy | `tmux new -s happy` → `happy --yolo` |

## 项目命名

```
<日期><s|l>-<描述>-opclw
```
- s = 短期项目
- l = 长期项目
- 描述用 kebab-case
- **必须加 -opclw 后缀**

示例：`20250606s-my-project-opclw`

## ACPX

```bash
npm install -g acpx@latest

# 基本
acpx "task"

# 命名会话
acpx -s name "task"

# 单次执行
acpx exec "task"
```

## HappyCoder

```bash
npm install -g happy-coder
```

### 认证
```bash
export ANTHROPIC_AUTH_TOKEN="Your API Key"
export ANTHROPIC_BASE_URL="https://api.minimaxi.com/anthropic"
```

### 首次认证
1. 启动 → 选 1 (Mobile App)
2. 发 happy:// URL 给用户
3. 用户协助验证

### 启动
```bash
cd projects/<项目>
tmux new -s happy
happy --yolo
```

### 会话管理
- 完成后 `exit` 退出 happy
- 不要杀 tmux
- `tmux ls` 查看会话
- 最多 3 个并发

## 项目文档范式

```
<项目>/
├── CLAUDE.md
├── QUICK-INDEX.md
├── specs/
├── changelogs/
└── ...
```

## 工具安装

```bash
npm install -g @anthropic-ai/claude-code
npm install -g acpx@latest
npm install -g happy-coder
```

## GitHub App

| 信息 | 值 |
|------|-----|
| App ID | Your App ID |
| Installation ID | Your Installation ID |
| PEM | ~/.ssh/github-app.pem |
