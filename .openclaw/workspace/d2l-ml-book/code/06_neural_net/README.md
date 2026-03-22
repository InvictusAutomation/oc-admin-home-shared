# 神经网络基础 - 双书对照实现

本案例展示神经网络的基础实现，对照西瓜书第5章与D2L第6章。

---

## 1. 原理回顾

### 西瓜书 (5. 神经网络)

**神经元模型**:
$$y = f(\sum_{i=1}^n w_i x_i - b)$$

**激活函数**:
- Sigmoid: $\sigma(x) = \frac{1}{1+e^{-x}}$
- ReLU: $f(x) = \max(0, x)$

### D2L (6. 神经网络)

**多层感知机 (MLP)**:
$$H = \sigma(XW^{(1)} + b^{(1)})$$
$$O = HW^{(2)} + b^{(2)}$$

---

## 2. Python 实现

### 2.1 手动实现神经网络

```python
import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Xavier 初始化
        self.W1 = np.random.randn(input_size, hidden_size) * np.sqrt(2.0 / input_size)
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * np.sqrt(2.0 / hidden_size)
        self.b2 = np.zeros((1, output_size))
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2
    
    def backward(self, X, y, learning_rate=0.1):
        m = X.shape[0]
        
        # 输出层误差
        delta2 = (self.a2 - y) * self.sigmoid_derivative(self.a2)
        dW2 = self.a1.T @ delta2 / m
        db2 = np.sum(delta2, axis=0, keepdims=True) / m
        
        # 隐藏层误差
        delta1 = (delta2 @ self.W2.T) * self.sigmoid_derivative(self.a1)
        dW1 = X.T @ delta1 / m
        db1 = np.sum(delta1, axis=0, keepdims=True) / m
        
        # 更新权重
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
        
    def fit(self, X, y, epochs=1000, learning_rate=0.1):
        for _ in range(epochs):
            self.forward(X)
            self.backward(X, y, learning_rate)
            
    def predict(self, X):
        return (self.forward(X) > 0.5).astype(int)
```

### 2.2 PyTorch 实现

```python
import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        return self.net(x)
```

---

## 参考

- 西瓜书 5. 神经网络
- D2L 6. 神经网络
