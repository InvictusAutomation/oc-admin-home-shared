# 线性回归 - 双书对照实现

本案例展示线性回归的多种实现方式，对照西瓜书第3章与D2L第3章。

---

## 1. 原理回顾

### 西瓜书 (3.1 线性回归)

**目标**: 学得 $f(\mathbf{x}_i) = \mathbf{w}^T \mathbf{x}_i + b$

**最小二乘法**:
$$\mathbf{w}^* = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

### D2L (3.1 线性回归)

**损失函数**: 均方误差 (MSE)
$$\mathcal{L}(\mathbf{w}, b) = \frac{1}{n}\sum_{i=1}^n (y_i - \mathbf{w}^T\mathbf{x}_i - b)^2$$

---

## 2. NumPy 实现 (原理导向)

```python
import numpy as np

class LinearRegressionNumPy:
    """线性回归 - 基于梯度下降"""
    
    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        
        # 初始化参数
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # 梯度下降
        for _ in range(self.n_iters):
            # 预测
            y_pred = np.dot(X, self.weights) + self.bias
            
            # 计算梯度
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            
            # 更新参数
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


# 使用正规方程 (闭式解)
class LinearRegressionNormal:
    """线性回归 - 闭式解"""
    
    def fit(self, X, y):
        # 添加偏置项
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        
        # 正规方程: θ = (X^T X)^(-1) X^T y
        theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
        
        self.bias = theta[-1]
        self.weights = theta[:-1]
        
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
```

---

## 3. PyTorch 实现

```python
import torch
import torch.nn as nn

class LinearRegressionPyTorch(nn.Module):
    """线性回归 - PyTorch"""
    
    def __init__(self, input_dim):
        super().__init__()
        self.linear = nn.Linear(input_dim, 1)
        
    def forward(self, x):
        return self.linear(x)


def train_pytorch(X, y, lr=0.01, epochs=1000):
    model = LinearRegressionPyTorch(X.shape[1])
    criterion = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)
    
    X_tensor = torch.FloatTensor(X)
    y_tensor = torch.FloatTensor(y).reshape(-1, 1)
    
    for epoch in range(epochs):
        optimizer.zero_grad()
        predictions = model(X_tensor)
        loss = criterion(predictions, y_tensor)
        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 100 == 0:
            print(f'Epoch [{epoch+1}], Loss: {loss.item():.4f}')
            
    return model
```

---

## 4. sklearn 实现

```python
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 训练
model = LinearRegression()
model.fit(X_scaled, y)

# 预测
y_pred = model.predict(X_scaled)
```

---

## 5. 对照总结

| 实现方式 | 优点 | 缺点 | 适用场景 |
|----------|------|------|----------|
| NumPy 梯度下降 | 原理清晰 | 速度慢 | 学习原理 |
| NumPy 正规方程 | 快速准确 | 需要矩阵可逆 | 小数据集 |
| PyTorch | 自动求导 | 需要GPU | 深度学习 |
| sklearn | 简单易用 | 灵活性一般 | 快速原型 |

---

## 6. 运行示例

```python
# 生成示例数据
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 训练
model = LinearRegressionNumPy(lr=0.01, n_iters=1000)
model.fit(X, y)

# 预测
X_test = np.array([[1.5], [2.0]])
predictions = model.predict(X_test)
print(f"预测值: {predictions}")
```

---

## 参考

- 西瓜书 3.1 线性回归
- D2L 3.1 线性回归
