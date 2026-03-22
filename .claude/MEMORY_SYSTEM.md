# Claude Code 记忆体系架构

本项目采用 Claude Code 官方推荐的多层次记忆体系，实现了结构化的指令管理和自动学习机制。

## 📁 文件结构

### 用户级 (全局配置)
```
~/.claude/
├── CLAUDE.md                 # 个人编码偏好（适用于所有项目）
├── MEMORY_SYSTEM.md          # 本文档
├── QUICK_REFERENCE.md        # 快速参考手册
└── rules/
    ├── python.md            # Python 开发偏好
    ├── typescript.md        # TypeScript 开发偏好
    ├── code-style.md        # 代码风格规范
    ├── testing.md           # 测试约定
    ├── complex-projects.md  # 复杂项目文档模板
    └── plugin-development.md  # 插件开发指南 (路径特定)
```

**作用范围**：所有项目
**优先级**：中等（被项目级覆盖）
**用途**：个人编码风格、工具偏好、通用工作流程

### 项目级 (团队共享)
```
./
├── .claude/
│   ├── CLAUDE.md            # 项目主配置
│   └── rules/
│       └── *.md             # 项目特定规则
└── CLAUDE.local.md          # 本地配置（不提交到 git）
```

**作用范围**：当前项目
**优先级**：高（覆盖用户级配置）
**用途**：项目架构、团队规范、构建命令

### Auto Memory (自动学习)
```
~/.claude/projects/<project>/memory/
├── MEMORY.md                # 索引（前200行自动加载）
├── debugging.md             # 调试经验
├── api-conventions.md       # API 设计决策
└── ...                      # 其他主题文件（按需加载）
```

**作用范围**：当前项目（所有 worktree 共享）
**管理方式**：Claude 自动维护
**用途**：构建命令、调试洞察、代码风格模式

## 🎯 记忆系统对比

| 特性 | CLAUDE.md | Auto Memory |
|------|-----------|-------------|
| **编写者** | 人工编写 | Claude 自动 |
| **内容** | 指令和规则 | 学习和模式 |
| **作用域** | 项目/用户/组织 | 按工作树 |
| **加载方式** | 每次会话完整加载 | MEMORY.md 前200行 + 按需加载 |
| **用途** | 编码标准、工作流程 | 构建命令、调试洞察 |

## 📜 加载优先级

更具体的位置优先于更广泛的位置：

1. **Managed Policy** (组织级) - 无法排除
2. **Project** (./.claude/CLAUDE.md) - 项目配置
3. **User** (~/.claude/CLAUDE.md) - 用户配置
4. **Local** (./CLAUDE.local.md) - 本地配置

## 🔍 路径特定规则

使用 YAML frontmatter 限定规则作用范围：

```markdown
---
paths:
  - "plugins/**/*.py"
  - "src/plugins/**/*.py"
---

# 这些规则仅在编辑插件相关文件时加载
```

**优势**：
- 减少上下文噪音
- 节省 token 使用
- 提高指令相关性

## 🛠️ 使用指南

### 查看当前加载的配置
```bash
/memory
```

### 编辑配置
通过 `/memory` 命令打开文件，或直接编辑：
- 用户级：`~/.claude/CLAUDE.md`
- 项目级：`./.claude/CLAUDE.md`
- 本地：`./CLAUDE.local.md`

### 导入其他文件
使用 `@` 语法导入：
```markdown
# 项目概览
@README.md

# 可用命令
@package.json

# 工作流程
@docs/workflow.md
```

### 让 Claude 记住偏好
直接告诉 Claude："记住我总是使用 pnpm 而不是 npm"
- 会话级偏好 → Auto Memory
- 持久化指令 → 手动添加到 CLAUDE.md

## ⚠️ 最佳实践

### DO ✅
- 每个 CLAUDE.md 文件控制在 200 行以内
- 使用具体、可验证的指令
- 将大型配置拆分到 `.claude/rules/`
- 使用路径特定规则减少噪音
- 定期审查和更新配置

### DON'T ❌
- 避免模糊的指令（"格式化代码" → "使用 2 空格缩进"）
- 避免冲突的规则
- 不要在 CLAUDE.md 中包含临时信息
- 不要提交 CLAUDE.local.md

## 📊 文件大小建议

| 文件类型 | 目标大小 | 说明 |
|---------|---------|------|
| CLAUDE.md | < 200 行 | 超过后考虑拆分到 rules/ |
| Rules/*.md | < 100 行 | 每个主题一个文件 |
| MEMORY.md | 前 200 行 | 自动加载，详细内容链接到主题文件 |

## 🔄 更新记录

- 2026-03-03: 扩展到系统级 (~/.claude/)
- 2026-03-02: 初始化多层次记忆体系
- 基于官方文档 https://code.claude.com/docs/en/memory
