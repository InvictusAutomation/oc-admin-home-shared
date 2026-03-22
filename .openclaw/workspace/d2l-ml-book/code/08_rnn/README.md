# 循环神经网络 RNN - 双书对照实现

本案例展示循环神经网络的实现，对照D2L第8章。

---

## 1. 原理回顾

### RNN 结构

$$h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t)$$

$$y_t = W_{hy} h_t$$

### 梯度计算 (BPTT)

反向传播通过时间展开网络计算梯度。

---

## 2. PyTorch 实现

```python
import torch
import torch.nn as nn

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)
        
    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        out, _ = self.rnn(x, h0)
        out = self.fc(out[:, -1, :])
        return out
```

## 3. NumPy 实现

```python
import numpy as np

class SimpleRNN:
    def __init__(self, input_size, hidden_size, output_size, lr=0.01):
        self.lr = lr
        self.hidden_size = hidden_size
        
        # 初始化权重
        self.Wxh = np.random.randn(hidden_size, input_size) * 0.01
        self.Whh = np.random.randn(hidden_size, hidden_size) * 0.01
        self.Why = np.random.randn(output_size, hidden_size) * 0.01
        self.bh = np.zeros(hidden_size)
        self.by = np.zeros(output_size)
        
    def tanh(self, x):
        return np.tanh(x)
    
    def forward(self, x_sequence):
        T = len(x_sequence)
        h = np.zeros(self.hidden_size)
        hidden_states = []
        
        for t in range(T):
            h = self.tanh(np.dot(self.Wxh, x_sequence[t]) + np.dot(self.Whh, h) + self.bh)
            hidden_states.append(h)
            
        y = np.dot(self.Why, h) + self.by
        return y, hidden_states
```

---

## 参考

- D2L 8. Recurrent Neural Networks
