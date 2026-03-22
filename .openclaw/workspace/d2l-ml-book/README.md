# 深度学习与机器学习 - 双书对照实践

> 《动手深度学习 (D2L)》+ 《机器学习 (西瓜书)》代码实践与原理详解

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)

---

## 项目简介

本项目整合《动手深度学习》与《机器学习》两本经典教材，提供：

- 📚 **双书对照** - D2L 实践 + 西瓜书原理
- 💻 **多框架实现** - PyTorch / TensorFlow / NumPy
- 📖 **详细原理讲解** - 公式推导 + 代码验证
- 🏋️ **配套数据集** - 开箱即用

---

## 内容结构

### 第一部分：机器学习基础 (西瓜书)

| 章节 | 主题 | D2L对应 | 状态 |
|------|------|---------|------|
| 1 | 绪论 | - | ⏳ |
| 2 | 模型评估与选择 | - | ⏳ |
| 3 | 线性模型 | D2L 3 | ⏳ |
| 4 | 决策树 | D2L 5 | ⏳ |
| 5 | 神经网络 | D2L 6 | ⏳ |
| 6 | 支持向量机 | D2L 5 | ⏳ |
| 7 | 贝叶斯分类器 | - | ⏳ |
| 8 | 集成学习 | D2L 7 | ⏳ |
| 9 | 聚类 | D2L 13 | ⏳ |
| 10 | 降维与度量学习 | D2L 11 | ⏳ |

### 第二部分：深度学习 (D2L)

| 章节 | 主题 | 西瓜书对应 | 状态 |
|------|------|-----------|------|
| 1 |  introduction | - | ⏳ |
| 2 | Preliminaries | - | ⏳ |
| 3 | Linear Neural Networks | 3章 | ⏳ |
| 4 | Multilayer Perceptrons | 5章 | ⏳ |
| 5 | Deep Learning Computation | - | ⏳ |
| 6 | Convolutional Neural Networks | - | ⏳ |
| 7 | Modern CNNs | - | ⏳ |
| 8 | Recurrent Neural Networks | - | ⏳ |
| 9 | Attention Mechanisms | - | ⏳ |
| 10 | Optimization Algorithms | - | ⏳ |
| 11 | Computational Performance | - | ⏳ |
| 12 | Computer Vision | - | ⏳ |
| 13 | Natural Language Processing | - | ⏳ |
| 14 | Generative Adversarial Networks | - | ⏳ |
| 15 | Transformers | - | ⏳ |

---

## 学习路径

### 入门路径

```
1. 机器学习基础 (西瓜书前3章)
   ↓
2. 线性模型与神经网络 (D2L 3-6章)
   ↓
3. CNN 与计算机视觉 (D2L 6-7章)
   ↓
4. RNN 与 NLP (D2L 8-9章)
   ↓
5. Transformer 与大模型 (D2L 15章)
```

---

## 代码示例

### 线性回归 (西瓜书 3章 / D2L 3章)

```python
import torch
import torch.nn as nn

# PyTorch 实现
class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)
    
    def forward(self, x):
        return self.linear(x)

model = LinearRegression()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 训练
for epoch in range(1000):
    optimizer.zero_grad()
    loss = criterion(model(x), y)
    loss.backward()
    optimizer.step()
```

### 对照：NumPy 实现

```python
import numpy as np

# 纯 NumPy 实现
class LinearRegressionNumPy:
    def __init__(self, lr=0.01):
        self.lr = lr
        self.weights = None
        
    def fit(self, X, y, epochs=1000):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        bias = 0
        
        for _ in range(epochs):
            y_pred = np.dot(X, self.weights) + bias
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            self.weights -= self.lr * dw
            bias -= self.lr * db
```

---

## 推荐阅读

### 主教材

| 书名 | 作者 | 出版社 |
|------|------|--------|
| 动手深度学习 | Aston Zhang, Zachary C. Brown 等 | 人民邮电出版社 |
| 机器学习 | 周志华 | 清华大学出版社 |

### 辅助资源

- [D2L 官网](https://d2l.ai/)
- [D2L PyTorch 版](https://zh.d2l.ai/)
- [西瓜书公式推导](https://github.com/datawhalechina/pumpkin-book)

---

## 许可证

MIT License
