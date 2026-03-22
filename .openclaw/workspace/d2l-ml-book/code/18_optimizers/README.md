# 优化算法进阶
## 高级优化器
- AdamW (权重衰减)
- LAMB (Layer-wise Adaptive)
- RAdam (Rectified Adam)

## AdamW实现
```python
class AdamW(torch.optim.Adam):
    def step(self, closure=None):
        for group in self.param_groups:
            for p in group['params']:
                if p.grad is None: continue
                grad = p.grad
                state = self.state[p]
                
                if len(state) == 0:
                    state['exp_avg'] = torch.zeros_like(p)
                    state['exp_avg_sq'] = torch.zeros_like(p)
                
                exp_avg, exp_avg_sq = state['exp_avg'], state['exp_avg_sq']
                self._update_one_step(p, grad, exp_avg, exp_avg_sq, group)
```

