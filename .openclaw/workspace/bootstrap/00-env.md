# 00-env.md - 环境

## 基础

- 工作目录：/home/admin/.openclaw/workspace
- 系统：Linux (Alibaba Cloud)
- 主机：iZk1a1rkpph2sifr6agsxyZ

## 工具

| 工具 | 描述 |
|------|------|
| exec | Shell 命令 |
| read/write/edit | 文件操作 |
| browser | 浏览器控制 |
| message | 多渠道消息 |
| cron | 定时任务 |
| nodes | 设备节点 |
| web_search/fetch | 网络 |
| memory_search/get | 记忆 |
| tts | 语音 |
| image | 图像 |
| gateway | 网关管理 |

## 模型

| 模型 | 值 |
|------|-----|
| 默认 | MiniMax-M2.1 |
| Opus | MiniMax-M2.1 |
| Sonnet | MiniMax-M2.1 |
| Haiku | MiniMax-M2.1 |

## 渠道

Telegram（当前活跃）

## 路径

```
/home/admin/.openclaw/workspace/    # 工作区
/opt/openclaw/                      # 安装目录
/opt/openclaw/skills/              # 技能
/home/admin/.openclaw/workspace/skills/  # 用户技能
/home/admin/.openclaw/extensions/        # 插件
/home/admin/.local/bin/                   # CLI 工具
```

## 环境变量

### Anthropic / MiniMax

| 变量 | 值 |
|------|-----|
| ANTHROPIC_BASE_URL | https://api.minimaxi.com/anthropic |
| ANTHROPIC_AUTH_TOKEN | Your API Key |
| ANTHROPIC_MODEL | MiniMax-M2.1 |
| ANTHROPIC_DEFAULT_OPUS_MODEL | MiniMax-M2.1 |
| ANTHROPIC_DEFAULT_SONNET_MODEL | MiniMax-M2.1 |
| ANTHROPIC_DEFAULT_HAIKU_MODEL | MiniMax-M2.1 |

### Anthropic (官方)

| 变量 | 值 |
|------|-----|
| anthropic:default | Your Anthropic Token |

### OpenClaw

| 变量 | 值 |
|------|-----|
| OPENCLAW_HOST | iZk1a1rkpph2sifr6agsxyZ |
| OPENCLAW_GATEWAY_PORT | 17969 |
| OPENCLAW_GATEWAY_TOKEN | test |
| OPENCLAW_PATH_BOOTSTRAPPED | 1 |
| OPENCLAW_SERVICE_VERSION | 2026.2.9 |

### Alibaba Cloud

| 变量 | 值 |
|------|-----|
| alibaba-cloud-international | Your API Key |
