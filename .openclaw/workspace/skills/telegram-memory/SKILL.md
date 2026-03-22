---
name: telegram-memory
description: 持续记录 Telegram 群聊中用户与 OpenClaw 的对话历史。每个 group 的每个 topic 分开记录，并在 "all" topic 中标注消息来源 topic。
---

# Telegram 对话记忆备份

持续记录 Telegram 群聊中用户与 OpenClaw 的对话，保存到本地文件以便日后查阅和分析。

## 触发条件

当在 Telegram group chat 中收到任何消息时（无论是直接 @mentioned 还是被拉入群聊），自动触发记忆备份。

## 消息上下文

从消息元数据中提取以下信息：

| 字段 | 来源 | 说明 |
|------|------|------|
| `chat_type` | `channel` | 应为 "group" |
| `group_subject` | `conversation_label` 或元数据 | 群名称，如 "oc boost" |
| `topic_id` | `conversation_label` 或 topic identifier | Topic ID |
| `topic_title` | 群聊元数据 | Topic 名称 |
| `is_forum` | 元数据 | 是否为 Forum 模式 |
| `was_mentioned` | 元数据 | 是否被 @ 提及 |
| `sender_name` | 发送者元数据 | 用户名称 |
| `message_text` | 消息内容 | 消息正文 |

## 存储结构

```
memory/telegram/
├── {group_subject}/
│   ├── {topic_id}_{topic_title}/
│   │   └── conversation.md
│   └── all/
│       └── conversation.md
```

### 字段说明

- `{group_subject}`: 群名称，如 `oc-boost`
- `{topic_id}_{topic_title}`: Topic ID + 名称，如 `230_general`
- `all/`: 汇总所有 topic 的对话（仅 Forum 模式使用）

## 记录格式

### 普通 Topic 记录

```markdown
# Telegram 对话记录 - oc-boost #230_general

## 会话信息
- 群组: oc-boost
- Topic: #230_general
- 开始时间: 2026-03-12 00:00:00

---

### 2026-03-12 00:15:30
**[Rock Chen]**: 你好

### 2026-03-12 00:15:45
**[oc2]**: 你好！有什么可以帮你的？

```

### "all" Topic 记录

当在 Forum 群组的 "all" topic 中发言时，需要额外标注消息实际来自哪个 topic：

```markdown
# Telegram 对话记录 - oc-boost (all topic)

## 会话信息
- 群组: oc-boost
- Topic: all (汇总)
- 开始时间: 2026-03-12 00:00:00

---

### 2026-03-12 00:15:30 [from #230_general]
**[Rock Chen]**: 你好

### 2026-03-12 00:15:45 [from #230_general]
**[oc2]**: 你好！有什么可以帮你的？

### 2026-03-12 00:20:00 [from #231_random]
**[另一个用户]**: 随机话题

```

## 处理流程

1. **解析元数据**: 从消息中提取 group_subject、topic_id、topic_title
2. **判断 Topic 类型**: 
   - 如果是 "all" topic（topic_id 为 "all" 或 topic_title 包含 "all"）
   - 需要从 `reply_to_message` 或消息上下文获取原始 topic
3. **追加记录**: 
   - 找到对应的 Topic 目录
   - 追加消息到 `conversation.md`
   - 如果是 "all"，同时更新对应源 topic 的记录（可选）
4. **创建新文件**: 如果目录不存在，先创建目录结构

## 消息格式模板

```
### {timestamp}
{filters}[from #{topic_id}]
**[{sender_name}]**: {message_text}
```

字段说明：
- `{timestamp}`: ISO 8601 格式时间
- `{filters}`: "from #topic_id " 如果是 all topic
- `{sender_name}`: 发送者名称
- `{message_text}`: 消息内容（支持多行）

## 注意事项

1. **不记录敏感信息**: 如果消息包含密码、token 等敏感词，跳过或脱敏
2. **附件处理**: 记录附件类型和文件名，不记录内容
3. **引用回复**: 如果消息是回复，标注回复的是哪条消息
4. **中文支持**: 使用 UTF-8 编码，中文文件名需要 URL 编码或拼音替代
5. **文件名规范**: 
   - 群名: 小写字母、数字、横线
   - Topic: ID + 名称（横线分隔）
   - 特殊字符用横线替代

## 示例代码

```python
import os
from datetime import datetime

def save_message(group: str, topic_id: str, topic_title: str, 
                sender: str, text: str, is_all_topic: bool = False,
                source_topic: str = None):
    """保存 Telegram 消息到记忆文件"""
    
    # 清理文件名
    group = group.lower().replace(" ", "-")
    topic_title = topic_title.lower().replace(" ", "-")
    topic_id = str(topic_id)
    
    # 基础路径
    base = f"/home/admin/.openclaw/workspace/memory/telegram/{group}"
    
    if is_all_topic:
        # all topic: 记录到 all 目录，并标注来源
        topic_dir = f"{base}/all"
    else:
        topic_dir = f"{base}/{topic_id}_{topic_title}"
    
    os.makedirs(topic_dir, exist_ok=True)
    
    filepath = f"{topic_dir}/conversation.md"
    
    # 时间戳
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 构建消息行
    if is_all_topic and source_topic:
        line = f"\n### {ts} [from #{source_topic}]\n**[{sender}]**: {text}\n"
    else:
        line = f"\n### {ts}\n**[{sender}]**: {text}\n"
    
    # 追加写入
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(line)
    
    return filepath
```

## 配置

将对话记忆保存到：
```
/home/admin/.openclaw/workspace/memory/telegram/
```

如需修改存储路径，编辑 `TOOLS.md` 中的 `telegram_memory_path` 配置。
