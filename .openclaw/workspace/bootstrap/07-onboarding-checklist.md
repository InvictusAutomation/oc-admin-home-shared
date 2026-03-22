# 07-onboarding-checklist.md - 新手入门清单

## 第一阶段：获取 Bootstrap

### 1.1 获取安装包

从分发者获取 `openclaw-bootstrap-opclw.zip`，解压到任意目录：

```bash
unzip openclaw-bootstrap.zip
cd openclaw-bootstrap
```

### 1.2 目录结构

```
openclaw-bootstrap/
├── bootstrap/           # Bootstrap 文档体系
│   ├── BOOTSTRAP.md   # 主索引
│   ├── 00-env.md      # 环境变量
│   ├── 01-user.md     # 用户信息
│   └── ...
├── skills/             # 技能（可选）
└── CLAUDE.md          # 用户级配置（可选）
```

---

## 第二阶段：环境准备

### 2.1 安装 OpenClaw

参考官方文档安装 OpenClaw：https://docs.openclaw.ai

### 2.2 部署 Bootstrap

```bash
# 1. 复制 Bootstrap 到工作区
cp -r bootstrap/ ~/.openclaw/workspace/

# 2. 复制技能（可选）
cp -r skills/ ~/.openclaw/workspace/

# 3. 复制用户配置（可选）
cp CLAUDE.md ~/.claude/ 2>/dev/null || mkdir -p ~/.claude && cp CLAUDE.md ~/.claude/
```

---

## 第三阶段：配置敏感信息

### 3.1 配置 API Token

编辑 `~/.openclaw/workspace/bootstrap/00-env.md`，填入你的 Token：

| 变量 | 获取方式 |
|------|----------|
| ANTHROPIC_AUTH_TOKEN | MiniMax/ Anthropic API |
| alibaba-cloud-international | 阿里云国际站 |

### 3.2 配置 GitHub

#### 生成 GitHub App 密钥

1. 打开 GitHub → Settings → Developer settings → GitHub Apps
2. 创建新 App 或使用现有 App
3. 生成私钥（Private key）
4. 记录 App ID 和 Installation ID

#### 配置 PEM

```bash
# 1. 创建 SSH 目录
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# 2. 复制 PEM 密钥
cp <你的-github-app.pem> ~/.ssh/github-app.pem
chmod 600 ~/.ssh/github-app.pem
```

### 3.3 配置认证文件

编辑 `~/.openclaw/agents/main/agent/auth-profiles.json`，填入你的 API 密钥。

---

## 第四阶段：验证

### 4.1 启动检查

```bash
# 检查工作区
ls -la ~/.openclaw/workspace/bootstrap/

# 检查模型
session_status

# 测试工具
gateway config.get
```

### 4.2 检查清单

- [ ] Bootstrap 文件已部署到正确位置
- [ ] 环境变量已配置
- [ ] GitHub App 已配置
- [ ] 认证文件已配置
- [ ] OpenClaw 服务正常运行
- [ ] 可以发送消息

---

## 第五阶段：个性化

### 5.1 设置用户信息

编辑 `bootstrap/01-user.md`，填入你的信息。

### 5.2 更新记忆

```bash
# 创建今日记忆文件
touch ~/.openclaw/workspace/memory/$(date +%Y-%m-%d).md
```

### 5.3 连接 EvoMap（可选）

参考 `bootstrap/03-evomap.md` 连接 EvoMap。

---

## 常见问题

| 问题 | 解决 |
|------|------|
| Token 无效 | 检查 00-env.md 是否脱敏后未填入真实值 |
| GitHub 权限不足 | 确认 GitHub App 有 administration 权限 |
| 工具不可用 | 检查 auth-profiles.json 配置 |
