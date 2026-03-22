# 11-packaging.md - Bootstrap 打包指南

## 敏感信息清单

| 类别 | 敏感项 | 位置 |
|------|--------|------|
| API Token | ANTHROPIC_AUTH_TOKEN | `~/.bashrc`, `~/.profile`, 或 auth-profiles.json |
| API Token | alibaba-cloud-international key | auth-profiles.json |
| GitHub | GitHub App PEM | ~/.ssh/github-app.pem |
| GitHub | SSH 私钥 | ~/.ssh/id_ed25519 |
| OpenClaw | Gateway Token | auth-profiles.json |
| OpenClaw | 设备配对信息 | ~/.openclaw/devices/paired.json |

## 脱敏步骤

### 1. 环境变量脱敏

编辑 `bootstrap/00-env.md`，替换真实 Token：

```bash
# 原：ANTHROPIC_AUTH_TOKEN=Your API Key
# 改：ANTHROPIC_AUTH_TOKEN=<你的TOKEN>
```

### 2. GitHub 配置脱敏

编辑 `bootstrap/08-github.md`：

```bash
# App ID 和 Installation ID 可以保留
# PEM 路径保留，但说明需要用户自己生成
```

### 3. 其他配置脱敏

检查以下文件是否有敏感信息：
- `~/.openclaw/agents/main/agent/auth-profiles.json`
- `~/.bashrc` / `~/.profile`
- `~/.npmrc`

## 打包流程

```bash
# 1. 创建临时目录
mkdir -p /tmp/openclaw-bootstrap
cd /tmp/openclaw-bootstrap

# 2. 复制 Bootstrap 文件
cp -r ~/.openclaw/workspace/bootstrap ./

# 3. 复制必要技能（如需要）
cp -r ~/.openclaw/workspace/skills/ ./

# 4. 复制用户级配置（脱敏后）
cp ~/.claude/CLAUDE.md ./ 2>/dev/null || true

# 5. 打包
zip -r openclaw-bootstrap-opclw.zip bootstrap/ skills/ CLAUDE.md

# 6. 输出文件位置
ls -la openclaw-bootstrap-opclw.zip
```

## 分发

打包完成后，用户获取 .zip 文件，按 `07-onboarding-checklist.md` 说明配置。
