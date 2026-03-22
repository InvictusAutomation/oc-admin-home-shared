# Boosting 集成学习 - 双书对照实现

本案例展示 Boosting 集成学习方法，对照西瓜书第8章与D2L第7章。

---

## 1. 原理回顾

### 西瓜书 (8. 集成学习)

**核心**: 组合多个弱分类器形成强分类器

**AdaBoost 算法**:
1. 初始化样本权重 $D_1$
2. 训练弱分类器 $h_t$
3. 计算误差率 $\epsilon_t$
4. 更新权重 $D_{t+1}$
5. 最终 $H(x) = \text{sign}(\sum_t \alpha_t h_t(x))$

### D2L (7. 深度学习中的正则化)

- Dropout 可看作隐式的 Bagging
- 权重衰减是 L2 正则化

---

## 2. Python 实现

### 2.1 AdaBoost 手动实现

```python
import numpy as np

class AdaBoost:
    def __init__(self, n_estimators=10):
        self.n_estimators = n_estimators
        self.alphas = []
        self.classifiers = []
        
    def fit(self, X, y):
        n_samples = len(X)
        weights = np.ones(n_samples) / n_samples
        
        for _ in range(self.n_estimators):
            # 训练弱分类器 (决策树桩)
            clf = DecisionTreeClassifier(max_depth=1)
            clf.fit(X, y, sample_weight=weights)
            
            # 计算误差
            pred = clf.predict(X)
            err = np.sum(weights * (pred != y)) / np.sum(weights)
            
            # 计算 alpha
            alpha = 0.5 * np.log((1 - err) / (err + 1e-10))
            
            # 更新权重
            weights *= np.exp(-alpha * y * pred)
            weights /= np.sum(weights)
            
            self.alphas.append(alpha)
            self.classifiers.append(clf)
            
    def predict(self, X):
        pred = np.zeros(len(X))
        for alpha, clf in zip(self.alphas, self.classifiers):
            pred += alpha * clf.predict(X)
        return np.sign(pred)
```

### 2.2 使用 sklearn

```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

clf = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=10,
    random_state=42
)
clf.fit(X, y)
```

---

## 参考

- 西瓜书 8. 集成学习
- D2L 7. 深度学习中的正则化
