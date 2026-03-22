# 09-init-checklist.md - 初始化配置

## 1. 默认模型

```bash
openclaw config set agents.defaults.model.primary "minimax-portal/MiniMax-M2.1"
```

## 2. 消息频道

Telegram / Discord / 飞书 / 钉钉

```bash
openclaw configure --channel telegram
```

## 3. GitHub App

- PEM 密钥
- App ID: Your App ID

## 4. EvoMap

- 注册节点
- 设置心跳

## 5. 工具

```bash
npm install -g acpx@latest
npm install -g happy-coder
npm install -g @anthropic-ai/claude-code
```

## 6. 模型 API

```bash
export ANTHROPIC_AUTH_TOKEN="Your API Key"
export ANTHROPIC_BASE_URL="https://api.minimaxi.com/anthropic"
```

## 7. Bootstrap

复制到 /home/admin/.openclaw/workspace/bootstrap/
