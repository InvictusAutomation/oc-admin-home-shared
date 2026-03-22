# 图神经网络 GNN
## 原理
消息传递神经网络

## PyG实现
```python
import torch_geometric.nn as pyg_nn
class GNN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super().__init__()
        self.conv1 = pyg_nn.GCNConv(in_channels, hidden_channels)
        self.conv2 = pyg_nn.GCNConv(hidden_channels, out_channels)
```

