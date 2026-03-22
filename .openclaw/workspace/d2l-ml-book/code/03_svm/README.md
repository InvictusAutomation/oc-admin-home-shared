# SVM 支持向量机 - 双书对照实现

本案例展示支持向量机的实现，对照西瓜书第6章与D2L相关章节。

---

## 1. 原理回顾

### 西瓜书 (6. 支持向量机)

**核心**: 找到最大间隔的分类超平面

**目标函数**:
$$\min_{\mathbf{w}, b} \frac{1}{2}\|\mathbf{w}\|^2$$
$$s.t. \quad y_i(\mathbf{w}^T\mathbf{x}_i + b) \geq 1$$

**对偶问题**:
$$\max_{\alpha} \sum_{i=1}^m \alpha_i - \frac{1}{2}\sum_{i=1}^m\sum_{j=1}^m\alpha_i\alpha_jy_iy_j\mathbf{x}_i^T\mathbf{x}_j$$

---

## 2. Python 实现

### 2.1 线性 SVM

```python
import numpy as np
from sklearn.svm import SVC

# 线性核 SVM
clf = SVC(kernel='linear', C=1.0)
clf.fit(X, y)
predictions = clf.predict(X_test)
```

### 2.2 高斯核 SVM (RBF)

```python
# 高斯核 SVM
clf = SVC(kernel='rbf', C=1.0, gamma='scale')
clf.fit(X, y)
```

### 2.3 手动实现 (简化版)

```python
class SimpleSVM:
    """简化版 SVM - 使用梯度下降"""
    
    def __init__(self, lr=0.01, epochs=1000, C=1.0):
        self.lr = lr
        self.epochs = epochs
        self.C = C
        self.w = None
        self.b = None
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        y_ = np.where(y <= 0, -1, 1)
        
        self.w = np.zeros(n_features)
        self.b = 0
        
        for _ in range(self.epochs):
            for i, x_i in enumerate(X):
                condition = y_[i] * (np.dot(x_i, self.w) + self.b) >= 1
                if condition:
                    self.w -= self.lr * (2 * self.w / n_samples)
                else:
                    self.w -= self.lr * (2 * self.w / n_samples - np.dot(x_i, y_[i]))
                    self.b -= self.lr * y_[i]
                    
    def predict(self, X):
        return np.sign(np.dot(X, self.w) + self.b)
```

---

## 3. 对照总结

| 实现 | 特点 | 适用场景 |
|------|------|----------|
| sklearn SVC | 工业级实现 | 生产环境 |
| 手写简化版 | 原理清晰 | 学习原理 |

---

## 参考

- 西瓜书 6. 支持向量机
- D2L 5. 多层感知机基础
