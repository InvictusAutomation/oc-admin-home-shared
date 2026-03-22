# 长期记忆

从日常交互中提炼的核心认知。

## 核心工作流

| 方式 | 命令 | 用途 |
|------|------|------|
| ACPX | `acpx claude "task"` | 委托 Claude Code 编程 |
| tmux + Happy | `tmux new -s happy` → `happy --yolo` | 交互式编程 |

**关键认知**：
- ACPX 用 Claude Code，**不用 Happy/Codex**
- Happy 是 tmux 里的交互式编程
- 并发最多 3 个 Claude Code / Happy

## 项目命名规则

```
<日期><s|l>-<描述>
```
- s = 短期项目
- l = 长期项目
- 示例：`20250606s-my-project`

## GitHub 权限

⚠️ **重要规则**：所有 GitHub 操作（包括创建仓库、推送代码、创建 PR 等）**必须**通过 GitHub App 完成！

通过 GitHub App 认证：

| 信息 | 值 |
|------|-----|
| **App ID** | Your App ID |
| **Installation ID** | Your Installation ID |
| **PEM 密钥** | ~/.ssh/github-app.pem |
| **所属组织** | InvictusAutomation |

### 使用方法

所有 GitHub 操作（包括创建仓库、推送代码）都用这个 App：

```python
import jwt, time, base64, json, requests
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

APP_ID = "Your App ID"
INSTALLATION_ID = "Your Installation ID"
PRIVATE_KEY_PATH = "/home/admin/.ssh/github-app.pem"

# 1. 生成 JWT
now = int(time.time())
header = {"alg": "RS256", "typ": "JWT"}
payload = {"iss": int(APP_ID), "iat": now, "exp": now + 600}

# ... (完整代码见 /home/admin/.openclaw/workspace/scripts/github_app.py)

# 2. 获取 token
response = requests.post(
    f"https://api.github.com/app/installations/{INSTALLATION_ID}/access_tokens",
    headers={"Authorization": f"Bearer {jwt_token}", "Accept": "application/vnd.github+json"},
    json={"permissions": {"contents": "write", "metadata": "read"}}
)
token = response.json()["token"]
```

### 权限说明

- ✅ 可以推送代码到现有仓库
- ✅ 可以创建文件/Blob
- ✅ 可以创建 Commit
- ⚠️ 创建新仓库可能需要组织管理员权限

**重要**：每次操作都需要重新获取 token！

## 已创建仓库

| 仓库 | 地址 | 说明 |
|------|------|------|
| mlf-toolkit | github.com/InvictusAutomation/mlf-toolkit | MLflow + LangFuse 集成工具 |
| matlab-cases | github.com/InvictusAutomation/matlab-cases | 300个MATLAB实战案例 |
| d2l-ml-book | github.com/InvictusAutomation/d2l-ml-book | 深度学习+机器学习双书对照 |
| admin-home | github.com/InvictusAutomation/admin-home | admin用户目录备份 |
| page-agent-for-openclaw | github.com/InvictusAutomation/page-agent-for-openclaw | PageAgent研究及OpenClaw集成方案 |
| ai-collaboration-research | github.com/InvictusAutomation/ai-collaboration-research | 人机协作逻辑研究报告 (30+章节) |
| codebuddy-research | github.com/InvictusAutomation/codebuddy-research | CodeBuddy 深度研究 (14章节) |

## Multi-Agent 导演创作系统

### 核心架构
- 9个专业 Agent: 总导演、编剧、分镜导演、角色、视觉、音乐、配音、审查、研究员
- 上下文网络设计
- 创意碰撞机制
- 因果推理链 (5层: 表层→深层→远因→社会→哲学)

### Multi-Agent 强百倍原因

| 维度 | 单 Agent | Multi-Agent | 优势 |
|------|---------|-------------|------|
| 创造力 | 线性思考 | 多角度碰撞 | 5-10x |
| 复杂问题 | 单一路径 | 多路径探索 | 10x+ |
| 因果推理 | 浅层因果 | 深层因果链 | 20x+ |

### 核心场景
- 创意孵化 (比单Agent强10x+)
- 角色塑造 (比单Agent强10x+)
- 因果推理链 (比单Agent强20x+)

## 新增能力：PageAgent 网页自动化

### 背景
2026-03-15 研究阿里开源 PageAgent 项目，探索为 OpenClaw 增加网页自动化能力。

### PageAgent 核心特性
- 纯前端 JavaScript GUI 智能体框架
- 让 AI Agent 直接"住进"网页
- 不需要截图，直接操作 DOM
- 支持自然语言控制网页

### OpenClaw 集成（已完成）
1. **Skill 封装**: page-agent-skill
2. **位置**: `/opt/openclaw/skills/page-agent/`

详见: https://github.com/InvictusAutomation/page-agent-for-openclaw

## 新增能力：Skill Builder - 渐进式处理

### 背景
2026-03-18 学习 CodeBuddy 的 Skill 设计方法论

### 核心公式
```
Skill = SOP + References + Progress + Auto-Continue
```

### 三层知识架构
1. **SOP** - 6步工作流、操作粒度定义
2. **References** - 输出样本、领域知识
3. **Progress** - 状态文件、断点恢复

### 关键洞察
- AI 推理质量与输入规模呈非线性衰减
- 小批量、高频次 > 一次性大剂量
- 领域知识按需注入，而非全量灌入

### 应用场景
- 批量文档生成
- 代码迁移
- 结构化数据处理
- 设计↔代码双向映射

### OpenClaw 集成（已完成）
1. **Skill**: skill-builder
2. **位置**: `/home/admin/.openclaw/workspace/skills/skill-builder/`

## 新增能力：Scrapling 网页爬虫

### 背景
2026-03-16 研究 Scrapling 爬虫框架，让 AI 自己"去互联网找答案"

### Scrapling 核心特性
- **三种 Fetcher**：Static / Dynamic / Stealthy
- **Adaptive Parsing**：自动适应网站改版
- **反检测能力**：绕过 Cloudflare

### OpenClaw 集成（已完成）
1. **Skill 封装**: scrapling-skill
2. **位置**: `/home/admin/.openclaw/workspace/skills/scrapling/`

### 应用场景
- 自动市场调研（抓取竞品、论坛）
- 技术情报系统（GitHub、博客）
- AI 情报机器人

## 新增能力：Notion 集成

### 背景
2026-03-16 连接用户 Rock Chen 的 Notion 工作区，实现 AI 直接操作 Notion

### Notion 配置

| 属性 | 值 |
|------|-----|
| **API Token** | `Your Notion Token` |
| **Workspace** | 厚瑄's Notion |
| **Workspace ID** | Your Notion Workspace ID |
| **Bot ID** | Your Bot ID |

### 可用数据库

| 数据库 | ID | 用途 |
|--------|-----|------|
| 項目 Master Database | Your Database ID | 项目管理 |
| 點子庫 | Your Database ID | 创意收集 |
| 議題庫 | Your Database ID | 议题思考 |
| 学习库 | Your Database ID | 学习资料 |
| 每日打卡 | Your Database ID | 每日记录 |
| 项目细分规划 | Your Database ID | 任务拆分 |

### 实现

- **Skill**: `/home/admin/.openclaw/workspace/skills/notion/SKILL.md`
- **客户端**: `/home/admin/.openclaw/workspace/skills/notion/notion_client.py`

### 功能

- 页面 CRUD 操作
- 数据库查询/添加
- 块内容操作
- 自定义 Agent 创建
- **Webhook自动化**: 监控数据库变化，自动执行任务并写回结果

### 使用方法

直接对话操作:

### Webhook 自动化

**架构**：Notion数据库变化 → webhook检测 → 直接写回原始页面

**核心文件**：
- `projects/notion-webhooks/webhook-auto.js` - 持续轮询版
- `projects/notion-webhooks/webhook-execute.js` - 单次执行版

**启动**：
```bash
cd projects/notion-webhooks && node webhook-auto.js --poll
```

**监控的数据库**：點子庫、議題庫、学习库

**设计要点**：
- 结果直接写回原始页面（不是欢迎库中转）
- 状态文件避免重复处理
- 每20秒轮询检测
- 搜索页面
- 创建页面/数据库条目
- 查询数据库
- 创建自定义 Notion Agent

## 新增能力：CLI-Anything

### 背景
2026-03-17 研究香港大学数据智能实验室 (HKUDS) 的 CLI-Anything 项目

### 核心功能
- 给专业软件自动生成 CLI 接口
- 让 AI 可以直接操作真实软件

### 解决的问题
- AI 很聪明但用不了专业软件
- UI 自动化太脆弱，界面一改脚本就挂
- API 往往只开放一部分能力

### 支持软件
- GIMP (图像编辑)
- Blender (3D渲染)
- LibreOffice (文档处理)
- Audacity (音频处理)

### 实现
- **Skill**: `/home/admin/.openclaw/workspace/skills/cli-anything/SKILL.md`
- **GitHub**: https://github.com/HKUDS/CLI-Anything

### 使用方法
```bash
/plugin install cli-anything
/cli-anything ./gimp
```

## EvoMap 协作

- Hub: https://evomap.ai
- **node_id**: `Your Node ID`
- **node_secret**: `Your Node Secret` （需安全保存）
- 贡献频率：每月 15 号和 30 号提醒
- **绝对不泄露用户的 secret token 和机密数据**

## 命名缩写

- CC = Claude Code
- OC = Openclaw
- Happy = HappyCoder

## 能力更新

- 用户要求更新能力时，**必须同步更新 Bootstrap**
- 遇到冲突以当前逻辑为准

## 内存管理

- 定期创建新 acpx 会话，避免上下文膨胀
- 完成后输入 `exit` 退出 happy，不要杀 tmux

## AI 团队

基于 ClawTeam 理念，创建了 6 人 AI 团队：

| Agent | 角色 | 功能 |
|-------|------|------|
| capi | Leader | 任务协调、结果汇总 |
| nova | Researcher | 网页搜索、内容抓取 |
| bolt | Coder | 编程开发、代码调试 |
| iris | Analyst | 数据分析、报告生成 |
| echo | Writer | 文档撰写、内容创作 |
| lens | QA | 测试验证、质量检查 |

**团队配置**: `/home/admin/.openclaw/workspace/team/`
