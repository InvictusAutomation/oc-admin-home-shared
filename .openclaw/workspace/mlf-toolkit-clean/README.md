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

---

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 配置
cp config/template.env config.env

# 启动
streamlit run app.py
```

访问 http://localhost:8501

## 相关项目

- **[MATLAB 案例集](https://github.com/InvictusAutomation/matlab-cases)** - 300个MATLAB实战案例

## 许可证

MIT
