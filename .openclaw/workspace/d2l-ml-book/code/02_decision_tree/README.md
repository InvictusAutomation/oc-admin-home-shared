# 决策树 - 双书对照实现

本案例展示决策树的实现，对照西瓜书第4章与D2L相关章节。

---

## 1. 原理回顾

### 西瓜书 (4. 决策树)

**核心思想**: 从根节点分裂，通过属性选择最优划分

**划分准则**:
- 信息增益 (ID3)
- 增益率 (C4.5)
- 基尼指数 (CART)

### D2L (5. 多层感知机基础)

决策树在D2L中作为数据预处理工具出现，核心算法相同。

---

## 2. NumPy 实现

```python
import numpy as np
from collections import Counter

class DecisionTree:
    """决策树 - 基于基尼指数"""
    
    def __init__(self, max_depth=10, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None
        
    def gini(self, y):
        """计算基尼指数"""
        classes, counts = np.unique(y, return_counts=True)
        probs = counts / len(y)
        return 1 - np.sum(probs ** 2)
    
    def best_split(self, X, y):
        """找到最优划分"""
        best_gain = -1
        best_feature = None
        best_threshold = None
        
        n_features = X.shape[1]
        parent_gini = self.gini(y)
        
        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                left_mask = X[:, feature] <= threshold
                right_mask = ~left_mask
                
                if np.sum(left_mask) < self.min_samples_split:
                    continue
                    
                # 计算加权基尼指数
                n = len(y)
                n_left, n_right = np.sum(left_mask), np.sum(right_mask)
                gini_left = self.gini(y[left_mask])
                gini_right = self.gini(y[right_mask])
                
                gain = parent_gini - (n_left/n * gini_left + n_right/n * gini_right)
                
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold
                    
        return best_feature, best_threshold, best_gain
    
    def fit(self, X, y):
        """训练决策树"""
        self.tree = self._build_tree(X, y, depth=0)
        
    def _build_tree(self, X, y, depth):
        n_samples = len(y)
        
        # 停止条件
        if (depth >= self.max_depth or 
            n_samples < self.min_samples_split or 
            len(np.unique(y)) == 1):
            return Counter(y).most_common(1)[0][0]
        
        # 找最优划分
        feature, threshold, gain = self.best_split(X, y)
        
        if gain <= 0:
            return Counter(y).most_common(1)[0][0]
        
        # 划分
        left_mask = X[:, feature] <= threshold
        right_mask = ~left_mask
        
        # 递归构建
        left_tree = self._build_tree(X[left_mask], y[left_mask], depth + 1)
        right_tree = self._build_tree(X[right_mask], y[right_mask], depth + 1)
        
        return {
            'feature': feature,
            'threshold': threshold,
            'left': left_tree,
            'right': right_tree
        }
    
    def predict_sample(self, x, tree):
        if isinstance(tree, dict):
            if x[tree['feature']] <= tree['threshold']:
                return self.predict_sample(x, tree['left'])
            else:
                return self.predict_sample(x, tree['right'])
        return tree
    
    def predict(self, X):
        return np.array([self.predict_sample(x, self.tree) for x in X])
```

---

## 3. sklearn 实现

```python
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn import tree

# 分类
clf = DecisionTreeClassifier(
    criterion='gini',  # 或 'entropy'
    max_depth=5,
    min_samples_split=10
)
clf.fit(X, y)

# 可视化
plt.figure(figsize=(20, 10))
tree.plot_tree(clf, filled=True)
plt.show()

# 预测
predictions = clf.predict(X_test)
```

---

## 4. 对照总结

| 实现 | 划分准则 | 特点 |
|------|----------|------|
| 纯NumPy | 基尼指数 | 原理清晰，适合学习 |
| sklearn | 基尼/信息熵 | 工业级实现 |

---

## 参考

- 西瓜书 4. 决策树
- sklearn DecisionTree
