# Notion Skill - AI 操作 Notion 的能力

> 让 AI 直接操作 Notion，实现创建页面、管理数据库、自动化任务

## 功能列表

### 1. 页面操作
- 📄 创建新页面
- 📝 更新页面内容
- 🗑️ 删除页面
- 🔍 搜索页面

### 2. 数据库操作
- 📊 查询数据库
- ➕ 添加数据库条目
- ✏️ 更新数据库条目
- 🔍 筛选和排序

### 3. 块操作
- 📝 添加块内容
- ✏️ 编辑块
- 🗑️ 删除块

### 4. 高级功能
- 🤖 创建自定义 Agent
- 📋 批量操作
- 🔄 自动化工作流

---

## 使用方法

### 基本连接

```bash
# 设置 Notion API Token
export NOTION_API_KEY="你的 API Secret"
```

### API 调用示例

```python
import requests

NOTION_API_KEY = "Your Notion Token"
NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"

headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}
```

---

## 常用操作

### 1. 获取当前用户

```python
def get_me():
    response = requests.get(
        f"{BASE_URL}/users/me",
        headers=headers
    )
    return response.json()
```

### 2. 搜索页面/数据库

```python
def search(query="", filter_type=None):
    data = {
        "query": query,
        "page_size": 100
    }
    if filter_type:
        data["filter"] = {"property": "object", "value": filter_type}
    
    response = requests.post(
        f"{BASE_URL}/search",
        headers=headers,
        json=data
    )
    return response.json()
```

### 3. 获取数据库内容

```python
def get_database(database_id):
    response = requests.get(
        f"{BASE_URL}/databases/{database_id}",
        headers=headers
    )
    return response.json()

def query_database(database_id, filter_conditions=None):
    data = {"page_size": 100}
    if filter_conditions:
        data["filter"] = filter_conditions
    
    response = requests.post(
        f"{BASE_URL}/databases/{database_id}/query",
        headers=headers,
        json=data
    )
    return response.json()
```

### 4. 创建页面

```python
def create_page(parent_id, title, content=None, properties=None):
    data = {
        "parent": {"page_id": parent_id},
        "properties": {
            "title": [
                {
                    "text": {"content": title}
                }
            ]
        }
    }
    
    if content:
        data["children"] = content
    
    if properties:
        data["properties"].update(properties)
    
    response = requests.post(
        f"{BASE_URL}/pages",
        headers=headers,
        json=data
    )
    return response.json()
```

### 5. 创建数据库条目

```python
def create_database_item(database_id, properties):
    data = {
        "parent": {"database_id": database_id},
        "properties": properties
    }
    
    response = requests.post(
        f"{BASE_URL}/pages",
        headers=headers,
        json=data
    )
    return response.json()
```

### 6. 添加块内容

```python
def append_blocks(block_id, children):
    data = {"children": children}
    
    response = requests.patch(
        f"{BASE_URL}/blocks/{block_id}/children",
        headers=headers,
        json=data
    )
    return response.json()
```

---

## 常用属性类型

### 标题 (title)
```python
"Name": {
    "title": [{"text": {"content": "页面标题"}}]
}
```

### 文本 (rich_text)
```python
"Description": {
    "rich_text": [{"text": {"content": "描述内容"}}]
}
```

### 数字 (number)
```python
"Price": {
    "number": 99
}
```

### 日期 (date)
```python
"Due Date": {
    "date": {"start": "2026-03-20"}
}
```

### 复选框 (checkbox)
```python
"Done": {
    "checkbox": True
}
```

### 单选 (select)
```python
"Status": {
    "select": {"name": "进行中"}
}
```

### 多选 (multi_select)
```python
"Tags": {
    "multi_select": [{"name": "AI"}, {"name": "重要"}]
}
```

### 人员 (people)
```python
"Assign": {
    "people": [{"id": "user_id"}]
}
```

### 关系 (relation)
```python
"Related Page": {
    "relation": [{"id": "related_page_id"}]
}
```

---

## 你的 Notion 工作区信息

| 属性 | 值 |
|------|-----|
| Workspace | 厚瑄's Notion |
| Workspace ID | Your Notion Workspace ID |
| Bot ID | Your Bot ID |

### 可用数据库

| 数据库 | ID | 说明 |
|--------|-----|------|
| 歡迎使用厚瑄's Notion! | Your Bot ID | 问答数据库 |
| Getting started with Feed | e9d42e77-f235-476b-b97f-90c6d3c83cac | Feed入门 |
| 学习库 | Your Database ID | 学习资料库 |
| 點子庫 | Your Database ID | 创意库 |
| 議題庫 | Your Database ID | 议题库 |
| 項目 Master Database | Your Database ID | 项目数据库 |
| 項目細分規劃 | Your Database ID | 项目细分 |
| 項目縫 | 1fe5d4f1-bcda-4340-a3c3-958dbfdd0654 | 项目缝 |
| 每日打卡 | Your Database ID | 每日打卡 |
| Library | 258b9bef-f736-81c3-9edf-d3514f74572f | 文档库 |

---

## 示例：创建自定义 Notion Agent

```python
class NotionAgent:
    """自定义 Notion Agent"""
    
    def __init__(self, name, role, database_id=None):
        self.name = name
        self.role = role
        self.database_id = database_id
        self.api_key = NOTION_API_KEY
    
    def add_item(self, title, **properties):
        """添加数据库条目"""
        props = {"Name": {"title": [{"text": {"content": title}}]}}
        props.update(properties)
        return create_database_item(self.database_id, props)
    
    def query_items(self, filter_conditions=None):
        """查询数据库"""
        return query_database(self.database_id, filter_conditions)
    
    def daily_report(self, task_summary):
        """生成每日汇报"""
        return self.add_item(
            title=f"{self.name} - 每日汇报",
            Status={"select": {"name": "已完成"}},
            Description={"rich_text": [{"text": {"content": task_summary}}]}
        )
```

---

## 常用命令

你可以通过对话让我执行以下操作：

1. **搜索** - "搜索 Notion 中关于 X 的内容"
2. **创建页面** - "在 Notion 创建一个新页面，标题是 XXX"
3. **添加任务** - "在项目数据库添加一个新任务：XXX"
4. **查询** - "查询学习库中所有标记为 AI 的条目"
5. **更新** - "把任务 XXX 的状态改为已完成"
6. **创建 Agent** - "创建一个 Notion Agent 专门管理我的学习任务"

---

## 注意事项

1. **API 限制**: Notion API 每秒最多 3 个请求
2. **权限范围**: 当前是 Bot 账号，只能访问已分享的页面
3. **速率限制**: 大量操作需要添加延迟

---

*更多功能请直接告诉我你需要做什么！*
