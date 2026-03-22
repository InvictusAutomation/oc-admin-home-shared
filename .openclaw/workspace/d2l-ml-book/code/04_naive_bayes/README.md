# 朴素贝叶斯分类器 - 双书对照实现

本案例展示朴素贝叶斯分类器，对照西瓜书第7章。

---

## 1. 原理回顾

### 西瓜书 (7. 贝叶斯分类器)

**核心**: 贝叶斯定理 + 条件独立假设

**后验概率**:
$$P(c|\mathbf{x}) = \frac{P(c)P(\mathbf{x}|c)}{P(\mathbf{x})}$$

**朴素贝叶斯**:
$$P(c|\mathbf{x}) = P(c)\prod_{i=1}^d P(x_i|c)$$

---

## 2. Python 实现

### 2.1 高斯朴素贝叶斯

```python
from sklearn.naive_bayes import GaussianNB
import numpy as np

# 数据
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# 训练
clf = GaussianNB()
clf.fit(X, y)

# 预测
pred = clf.predict(X_test)
```

### 2.2 手动实现

```python
import numpy as np

class NaiveBayes:
    """朴素贝叶斯分类器 - 高斯假设"""
    
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.mean = {}
        self.var = {}
        self.prior = {}
        
        for c in self.classes:
            X_c = X[y == c]
            self.mean[c] = X_c.mean(axis=0)
            self.var[c] = X_c.var(axis=0) + 1e-9
            self.prior[c] = len(X_c) / len(X)
            
    def predict(self, X):
        predictions = []
        for x in X:
            posteriors = []
            for c in self.classes:
                prior = np.log(self.prior[c])
                likelihood = np.sum(
                    -0.5 * np.log(2 * np.pi * self.var[c])
                    - 0.5 * ((x - self.mean[c])**2) / self.var[c])
                )
                posteriors.append(prior + likelihood)
            predictions.append(self.classes[np.argmax(posteriors)])
        return np.array(predictions)
```

---

## 参考

- 西瓜书 7. 贝叶斯分类器
