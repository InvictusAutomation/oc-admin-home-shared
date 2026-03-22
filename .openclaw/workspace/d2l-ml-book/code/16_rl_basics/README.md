# 强化学习基础
## 核心概念
- State, Action, Reward
- Policy, Value Function

## Q-Learning实现
```python
import numpy as np
class QLearning:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.9):
        self.Q = np.zeros((n_states, n_actions))
        self.alpha = alpha
        self.gamma = gamma
    
    def update(self, s, a, r, s_next):
        self.Q[s,a] += self.alpha * (r + self.gamma * np.max(self.Q[s_next]) - self.Q[s,a])
```

