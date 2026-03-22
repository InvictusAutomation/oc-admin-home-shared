# 10-lessons.md - 经验教训

从实际工作中提炼的经验教训。

## 开发经验

### ACPX vs Happy

- **ACPX**：适合后台委托任务，结果可预期
- **Happy**：适合交互式探索和快速原型

### 会话管理

- tmux 会复用，不要每次新建
- `tmux ls` 查看活跃会话
- `exit` 正常退出，不要 kill

### 上下文管理

- ACPX 会话久了上下文会膨胀
- 定期 `acpx exec` 开新会话
- 复杂任务拆分成多个小 acpx 调用

## GitHub 协作

### 权限问题

- GitHub App 不需要 SSH 公钥
- "Bad credentials" 多数是 IP 白名单问题
- 先 `curl -s ifconfig.me` 确认本机 IP

### 仓库命名

- 组织级项目用 `<org>/<repo>`
- 个人项目放 admin-home

## 故障排查

### GitHub API 403/401

```bash
# 1. 确认 IP
curl -s ifconfig.me

# 2. 检查 token 权限
gh auth status

# 3. 用 GitHub App token
export GH_TOKEN="Your GitHub Token"
```

### npm 包安装失败

- 清理缓存：`npm cache clean --force`
- 用 `npm install -g` 加 `--force`

## 文件管理

- Bootstrap 放在 `/home/admin/.openclaw/workspace/bootstrap/`
- 用户级配置放 `~/.claude/CLAUDE.md`
- 项目配置放 `<project>/CLAUDE.md`

## 协作规范

- 更新能力时同步 Bootstrap
- 不泄露用户机密数据
- 遇到冲突以当前逻辑为准
