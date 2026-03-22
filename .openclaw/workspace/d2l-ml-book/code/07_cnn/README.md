# 卷积神经网络 CNN - 双书对照实现

本案例展示卷积神经网络的实现，对照D2L第6章。

---

## 1. 原理回顾

### CNN 核心概念

- **卷积层**: 局部连接 + 权值共享
- **池化层**: 下采样，减少参数量
- **全连接层**: 分类器

### 前向传播

$$y_{i,j,k} = \sum_{m}\sum_{n} x_{i+m, j+n, k} \cdot w_{m,n,k}$$

---

## 2. PyTorch 实现

```python
import torch
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(64 * 8 * 8, 256)
        self.fc2 = nn.Linear(256, num_classes)
        self.relu = nn.ReLU()
        
    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(-1, 64 * 8 * 8)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x
```

## 3. NumPy 实现

```python
import numpy as np

def conv2d(image, kernel, stride=1, padding=0):
    """2D 卷积"""
    # 填充
    if padding > 0:
        image = np.pad(image, padding, mode='constant')
    
    h, w = image.shape
    kh, kw = kernel.shape
    
    out_h = (h - kh) // stride + 1
    out_w = (w - kw) // stride + 1
    
    output = np.zeros((out_h, out_w))
    
    for i in range(0, out_h * stride, stride):
        for j in range(0, out_w * stride, stride):
            output[i//stride, j//stride] = np.sum(
                image[i:i+kh, j:j+kw] * kernel
            )
    return output
```

---

## 参考

- D2L 6. Convolutional Neural Networks
