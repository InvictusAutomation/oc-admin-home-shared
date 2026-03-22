# 正则化技术
## 深度学习中的正则化
- Dropout
- Batch Normalization
- Label Smoothing
- Mixup / CutMix

## 实现
```python
# Dropout
self.dropout = nn.Dropout(p=0.5)

# Label Smoothing
def label_smoothing(y, classes, smoothing=0.1):
    return y * (1 - smoothing) + smoothing / classes
```

