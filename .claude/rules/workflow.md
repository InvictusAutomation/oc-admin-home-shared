# Workflow Rules

## 项目文档范式

每个项目应建立多层次文档体系：

1. **CLAUDE.md** - 主配置（项目规范、架构）
2. **QUICK-INDEX.md** - 快速索引（各文档位置）
3. **specs/** - 规范文档（API、前端、服务器）
4. **changelogs/** - 变更日志
5. **security/** - 安全文档
6. **requirements/** - 需求文档

**工作流**：先读 QUICK-INDEX，按需参考具体文档。

## Development Workflow

1. **ACPX** (默认)
   - 用 `acpx claude "task"` 委托任务
   - 适合大多数开发场景

2. **tmux + Happy** (交互式)
   - 用 `tmux new -s happy` 创建会话
   - 用 `happy --yolo` 启动
   - 开发完成后输入 `exit` 退出 happy
   - 不要杀 tmux，保持复用

## Session Management

- 最多同时 3 个 Claude Code / Happy
- 定期检查会话：`tmux ls`
- 用 `acpx sessions list` 检查 acpx 会话

## Git Workflow

- 使用 GitHub App 认证
- 遵循项目命名规范
- 提交前确认变更
