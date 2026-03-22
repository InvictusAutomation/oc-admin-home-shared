# CLI-Anything Skill

> 给专业软件自动生成 CLI 接口，让 AI 直接操作真实软件

## 项目信息

- **项目**: CLI-Anything
- **机构**: 香港大学数据智能实验室 (HKUDS)
- **GitHub**: https://github.com/HKUDS/CLI-Anything
- **核心功能**: 自动给专业软件生成 CLI 接口

---

## 解决的问题

**AI 很聪明，但用不了专业软件**

| 传统方案 | 问题 |
|---------|------|
| UI 自动化 | 太脆弱，界面一改脚本就挂 |
| API 接入 | API 往往只开放一部分能力 |

**核心痛点**: AI 能把流程规划得很好，但真正执行时工具接不上

---

## 解决方案

```
给专业软件补一层 AI 接口

┌─────────────────────────────────────────────────────────────┐
│                     CLI-Anything 架构                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   源码分析 → CLI接口规划 → 代码生成 → 测试+文档            │
│                                                             │
│   专业软件 (如 GIMP, Blender, LibreOffice)                 │
│         ↓                                                  │
│   自动生成 CLI 接口 (无需修改原软件)                        │
│         ↓                                                  │
│   AI Agent 可以直接调用                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 支持环境

- ✅ **OpenClaw** (Claude Code)
- ✅ OpenCode
- ✅ Qodercli
- ✅ Codex
- ✅ 其他支持 CLI 的环境

---

## 使用方法

### 1. 安装 CLI-Anything

```bash
# 添加插件市场
/plugin marketplace add HKUDS/CLI-Anything

# 安装插件
/plugin install cli-anything
```

### 2. 生成 CLI 接口

```bash
# 为 GIMP 生成 CLI
/cli-anything:cli-anything ./gimp

# 为 Blender 生成 CLI
/cli-anything:cli-anything ./blender

# 为 LibreOffice 生成 CLI
/cli-anything:cli-anything ./libreoffice
```

### 3. 优化 CLI (可选)

```bash
# 针对特定功能精炼
/cli-anything:refine ./gimp "图像批处理和滤镜"
```

### 4. 使用生成的 CLI

```bash
# 创建新项目
cli-anything-gimp project new --width 1920 --height 1080

# 添加图层 (JSON格式)
cli-anything-gimp --json layer add -n "Background" --type solid --color "#1a1a2e"

# 进入交互式 REPL
cli-anything-gimp repl
```

---

## 支持的软件

| 软件 | 功能 |
|------|------|
| GIMP | 图像编辑、批处理 |
| Blender | 3D渲染、建模 |
| LibreOffice | PDF生成、文档处理 |
| Audacity | 音频处理 |
| ... | 更多软件支持中 |

---

## 技术细节

### 自动生成流水线

```
1. 源码分析
   └→ 理解软件结构

2. 接口规划
   └→ 设计 CLI 命令

3. 代码生成
   └→ 生成 CLI 实现

4. 测试补全
   └→ 单元测试 + 端到端测试

5. 文档生成
   └→ 自动生成 SKILL.md
```

### 测试覆盖

- **1500+** 测试用例
- **10+** 真实应用程序
- 单元测试 + 端到端测试 + CLI 子进程测试

---

## 未来展望

> 在面向人类的 UI 界面之外，会再多出一套专门给 AI 使用的接口层

```
软件 = 人类UI + AI-CLI接口

AI Agent 能做的事情，可能会比现在多得多
```

---

## 相关资源

- GitHub: https://github.com/HKUDS/CLI-Anything
- 公众号: AI开源前哨

---

## OpenClaw 集成

在 OpenClaw 中使用：

```bash
# 确保 CLI-Anything 已安装
/plugin list | grep cli-anything

# 查看可用命令
/help cli-anything

# 为新软件生成 CLI
/cli-anything /path/to/software
```

---

*了解更多: 直接问 AI 如何为特定软件生成 CLI 接口*
