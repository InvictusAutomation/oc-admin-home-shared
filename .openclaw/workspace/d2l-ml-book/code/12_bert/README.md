# BERT 预训练语言模型
## 原理
- Masked Language Model
- Next Sentence Prediction

## PyTorch实现
```python
from transformers import BertModel, BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
```

