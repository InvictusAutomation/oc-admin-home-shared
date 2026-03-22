# 优化算法 - 双书对照实现

本案例展示深度学习优化算法，对照D2L第10章。

---

## 1. 原理回顾

### 梯度下降

$$w_{t+1} = w_t - \eta \nabla L(w_t)$$

### 动量法

$$v_{t+1} = \beta v_t + \eta \nabla L(w_t)$$
$$w_{t+1} = w_t - v_{t+1}$$

### Adam

$$m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t$$
$$v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2$$

---

## 2. 实现

```python
import numpy as np

class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr
        
    def update(self, w, grad):
        return w - self.lr * grad

class Momentum:
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None
        
    def update(self, w, grad):
        if self.v is None:
            self.v = np.zeros_like(w)
        self.v = self.momentum * self.v + self.lr * grad
        return w - self.v

class Adam:
    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.m = None
        self.v = None
        self.t = 0
        
    def update(self, w, grad):
        self.t += 1
        if self.m is None:
            self.m = np.zeros_like(w)
            self.v = np.zeros_like(w)
            
        self.m = self.beta1 * self.m + (1 - self.beta1) * grad
        self.v = self.beta2 * self.v + (1 - self.beta2) * (grad ** 2)
        
        m_hat = self.m / (1 - self.beta1 ** self.t)
        v_hat = self.v / (1 - self.beta2 ** self.t)
        
        return w - self.lr * m_hat / (np.sqrt(v_hat) + 1e-8)
```

---

## 参考

- D2L 10. Optimization Algorithms
