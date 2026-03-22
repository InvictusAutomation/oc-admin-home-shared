# OpenClaw User Preferences

> 本文件为 OpenClaw 用户级配置，适用于所有项目
> 参考：https://code.claude.com/docs/en/memory

## 项目开发范式

每个项目采用多层次文档体系，节省上下文：

```
<项目名>/
├── CLAUDE.md              # 主配置（项目规范、架构）
├── QUICK-INDEX.md         # 快速索引（各文档位置和用途）
├── .claude/
│   └── rules/            # 路径特定规则
├── specs/                 # 规范文档
├── changelogs/            # 变更日志
├── security/              # 安全文档
└── requirements/          # 需求文档
```

**工作流**：
1. 先读 `QUICK-INDEX.md` 了解项目结构
2. 编程时按需参考相关 md 文件
3. 避免把所有文档塞到一个文件

## Communication Style

- Be concise and direct
- Avoid emojis unless explicitly requested
- Provide context for decisions
- Use Chinese for explanations when appropriate

## Workflow Preferences

- 始终监控 tmux 会话状态：`tmux ls`
- 完成 tmux + Happy 开发后，输入 `exit` 退出 happy
- **不要杀 tmux**，保持会话以便后续复用
- 定期清理不用的 tmux 会话
- 最多同时运行 3 个 Claude Code / Happy 会话

## Tool Preferences

- 使用 `acpx` 进行代理开发
- 使用 GitHub App 进行 Git 操作
- 优先使用 ACPX（acpx claude）而非 tmux

## Memory System

- 使用 Bootstrap 体系：`/home/admin/.openclaw/workspace/bootstrap/`
- 重要记忆保存到：`/home/admin/.openclaw/workspace/memory/`
- 定期同步更新 Bootstrap

## Project Naming

- GitHub Org: InvictusAutomation
- 格式：`<日期><s|l>-<描述>`
- s = 短期项目，l = 长期项目
- 描述用 kebab-case

---

@~/.claude/rules/workflow.md
