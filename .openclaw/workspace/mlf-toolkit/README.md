# MLF-Toolkit

**MLflow + LangFuse 集成工具包** - 开箱即用的机器学习实验与大语言模型监控工具

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![MLflow](https://img.shields.io/badge/MLflow-2.x-green)
![LangFuse](https://img.shields.io/badge/LangFuse-2.x-orange)

---

## 功能特性

### 🔄 双模式切换
- **MLflow 模式**: 机器学习实验跟踪、模型管理、指标监控
- **LangFuse 模式**: LLM 应用监控、提示词工程、token 分析

### 🧠 智能记忆系统
- 实时跟踪分析过程（修改、设计、撤回操作）
- 项目进展全程记录
- 自动复盘与报告生成

### 📊 报告导出
- 一键生成精美研究报告
- 对话记录智能总结
- Markdown/HTML/PDF 多格式支持

---

## 快速开始

### 安装

```bash
# 克隆
git clone https://github.com/InvictusAutomation/mlf-toolkit.git
cd mlf-toolkit

# 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 配置

```bash
cp config/template.env config.env
# 编辑 config.env 填入 API Keys
```

### 启动

```bash
# Docker 启动服务
docker-compose up -d

# 启动 Web 界面
streamlit run app.py
```

访问 http://localhost:8501

---

## 项目结构

```
mlf-toolkit/
├── app.py                    # Streamlit 主应用
├── core/                     # 核心模块
│   ├── mlflow_client.py      # MLflow 客户端
│   ├── langfuse_client.py   # LangFuse 客户端
│   ├── memory_system.py      # 记忆系统
│   └── report_generator.py  # 报告生成
├── config/                   # 配置
├── docs/                     # 文档
├── docker-compose.yml        # Docker 配置
└── requirements.txt          # 依赖
```

---

## 文档目录

| 文档 | 描述 |
|------|------|
| [快速开始](docs/01-quickstart.md) | 5分钟快速上手 |
| [MLflow 指南](docs/02-mlflow-guide.md) | 实验跟踪 |
| [LangFuse 指南](docs/03-langfuse-guide.md) | LLM 监控 |
| [记忆系统](docs/04-memory-system.md) | 智能记忆 |
| [API 申请指南](docs/00-api-keys.md) | API Key 申请 |
| [视频教程](docs/09-video-tutorials.md) | 学习资源 |

---

## 相关项目

- **[MATLAB 案例集](https://github.com/InvictusAutomation/matlab-cases)** - 300个MATLAB实战案例的Python实现

---

## 许可证

MIT License
