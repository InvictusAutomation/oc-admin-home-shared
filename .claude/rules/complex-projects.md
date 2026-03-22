# Complex Project Documentation Template

> 当构建复杂、多模块项目时，主动采用这个标准文档结构模板

## 触发条件

当遇到以下情况时，**主动建议**使用此模板：
- ✅ 多模块项目 (API + Frontend + Admin 等)
- ✅ 预计文档超过 1000 行
- ✅ 需要长期维护和团队协作
- ✅ 有多个子系统或规格文档

## 核心原则

1. **分层索引**: CLAUDE.md → QUICK-INDEX.md → 详细文档
2. **职责分离**: 入口文件只含核心规则和导航，详细内容在独立文档
3. **速查优化**: 为大型文档提供 quick-ref 版本
4. **历史追踪**: 使用 changelog 记录演进

## 标准目录结构

```
project_root/
├── CLAUDE.md                    # AI 入口（规则 + Top 20 速查 + 导航）
├── docs/
│   ├── QUICK-INDEX.md          # 完整索引合集（唯一完整列表来源）
│   ├── project-changelog.md    # 功能历史索引
│   ├── specs/                  # 详细规格文档
│   │   ├── api-spec.md        # API 完整规格
│   │   ├── api-quick-ref.md   # API 速查表（精简版）
│   │   ├── frontend-spec.md   # 前端架构
│   │   ├── backend-spec.md    # 后端架构
│   │   ├── database-spec.md   # 数据库设计
│   │   ├── uiux-spec.md       # 设计系统
│   │   └── ...
│   ├── changelogs/             # 每日/每周更新记录
│   ├── reports/                # 各类报告
│   │   └── security/
│   └── requirements/           # 需求文档
└── ...
```

## 文件职责

### CLAUDE.md (入口文件)
- **长度**: ≤ 200 行（超出移到专门文档）
- **内容**:
  - 核心开发规则 (10-20 条)
  - Top 20 速查信息（最常用端点、命令、配置）
  - 导航索引（链接到详细文档）

### docs/QUICK-INDEX.md (主索引)
- **唯一完整文档列表来源**
- 包含所有文档描述、状态、行数统计
- 文档间依赖关系

### docs/specs/ (规格文档)
- **模式**: 完整版 + 速查版
  - `{module}-spec.md` - 详细描述（可达数千行）
  - `{module}-quick-ref.md` - 精简速查
- **常见模块**:
  - API、Frontend、Backend、Database
  - UI/UX、Security、Deployment、Testing

### docs/changelogs/ (变更历史)
- 按日期或版本组织
- 记录功能添加、修改、删除

## 初始化步骤

当开始复杂项目时，执行以下步骤：

```bash
# 1. 创建目录结构
mkdir -p docs/specs docs/changelogs docs/reports/security docs/requirements

# 2. 创建基础文件
touch CLAUDE.md docs/QUICK-INDEX.md
```

然后：
1. 编写 CLAUDE.md - 添加核心规则和导航
2. 创建 QUICK-INDEX.md - 列出计划的所有文档
3. 按需创建 spec 文件 - 从核心模块开始
4. 建立 changelog 习惯 - 每日或每周更新

## 维护规则

1. **CLAUDE.md**: 超过 200 行时，将详细内容移到 specs/
2. **QUICK-INDEX.md**: 添加新文档时必须更新
3. **Specs**: 超过 500 行时考虑创建 quick-ref 版本
4. **Changelogs**: 重大变更后及时更新，链接到 spec 而非写详细实现

## 实战示例

### API 密集型项目
```
docs/specs/
├── api-spec.md (2400 行) - 完整 API 文档
├── api-quick-ref.md (74 端点速查)
├── api-authentication.md - 认证说明
└── api-rate-limiting.md - 限流策略
```

### 全栈 Web 应用
```
docs/specs/
├── frontend-spec.md (579 行)
├── admin-frontend-spec.md (280 行)
├── uiux-spec.md (686 行)
├── seo-spec.md (762 行)
└── server-config.md (528 行)
```

## 反模式

❌ 在 CLAUDE.md 中写详细实现（应该简洁）
❌ 跳过 QUICK-INDEX.md（失去全局视图）
❌ Spec 文件过大不拆分（>1000 行应拆分或加 quick-ref）
❌ Changelog 写得像 git commit（应面向用户/功能）

## Claude 使用提示

当用户开始复杂项目时：
1. **主动建议**使用此模板结构
2. 帮助创建初始目录和基础文件
3. 引导用户逐步完善文档，不要一次性全部创建
4. 提醒保持文档与代码同步
