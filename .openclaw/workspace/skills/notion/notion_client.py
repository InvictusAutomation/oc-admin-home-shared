"""
Notion API Python 客户端
用于 OpenClaw 的 Notion Skill
"""

import requests
import time
from typing import Dict, List, Any, Optional

# 配置
NOTION_API_KEY = "Your Notion Token"
NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}


class NotionClient:
    """Notion API 客户端"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or NOTION_API_KEY
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json"
        }
    
    # ==================== 用户 ====================
    
    def get_me(self) -> Dict:
        """获取当前用户信息"""
        return self._request("GET", "/users/me")
    
    # ==================== 搜索 ====================
    
    def search(self, query: str = "", filter_type: str = None, page_size: int = 100) -> Dict:
        """搜索页面或数据库"""
        data = {
            "query": query,
            "page_size": page_size
        }
        if filter_type:
            data["filter"] = {"property": "object", "value": filter_type}
        
        return self._request("POST", "/search", json=data)
    
    def search_pages(self, query: str = "") -> List[Dict]:
        """搜索页面"""
        result = self.search(query, filter_type="page")
        return result.get("results", [])
    
    def search_databases(self, query: str = "") -> List[Dict]:
        """搜索数据库"""
        result = self.search(query, filter_type="database")
        return result.get("results", [])
    
    # ==================== 页面 ====================
    
    def get_page(self, page_id: str) -> Dict:
        """获取页面"""
        return self._request("GET", f"/pages/{page_id}")
    
    def get_page_blocks(self, page_id: str) -> List[Dict]:
        """获取页面内容（块）"""
        result = self._request("GET", f"/blocks/{page_id}/children")
        return result.get("results", [])
    
    def create_page(
        self,
        parent_id: str,
        title: str,
        content: List[Dict] = None,
        properties: Dict = None,
        is_database: bool = False
    ) -> Dict:
        """创建页面"""
        if is_database:
            parent = {"database_id": parent_id}
        else:
            parent = {"page_id": parent_id}
        
        # 构建属性
        props = {}
        if title:
            props["title"] = [{"text": {"content": title}}]
        
        if properties:
            props.update(properties)
        
        data = {
            "parent": parent,
            "properties": props
        }
        
        if content:
            data["children"] = content
        
        return self._request("POST", "/pages", json=data)
    
    def update_page(self, page_id: str, properties: Dict) -> Dict:
        """更新页面属性"""
        return self._request("PATCH", f"/pages/{page_id}", json={
            "properties": properties
        })
    
    def delete_page(self, page_id: str) -> Dict:
        """删除页面（移至回收站）"""
        return self._request("DELETE", f"/pages/{page_id}")
    
    # ==================== 数据库 ====================
    
    def get_database(self, database_id: str) -> Dict:
        """获取数据库结构"""
        return self._request("GET", f"/databases/{database_id}")
    
    def query_database(
        self,
        database_id: str,
        filter_conditions: Dict = None,
        sorts: List[Dict] = None,
        page_size: int = 100
    ) -> Dict:
        """查询数据库"""
        data = {"page_size": page_size}
        
        if filter_conditions:
            data["filter"] = filter_conditions
        
        if sorts:
            data["sorts"] = sorts
        
        return self._request("POST", f"/databases/{database_id}/query", json=data)
    
    def create_database_item(self, database_id: str, properties: Dict) -> Dict:
        """创建数据库条目"""
        return self.create_page(
            parent_id=database_id,
            title=None,
            properties=properties,
            is_database=True
        )
    
    def create_database(
        self,
        parent_page_id: str,
        title: str,
        properties: Dict
    ) -> Dict:
        """创建数据库"""
        data = {
            "parent": {"page_id": parent_page_id},
            "title": [{"text": {"content": title}}],
            "properties": properties
        }
        
        return self._request("POST", "/databases", json=data)
    
    # ==================== 块操作 ====================
    
    def append_blocks(self, block_id: str, children: List[Dict]) -> Dict:
        """添加块"""
        return self._request("PATCH", f"/blocks/{block_id}/children", json={
            "children": children
        })
    
    def add_paragraph(self, block_id: str, text: str) -> Dict:
        """添加段落"""
        return self.append_blocks(block_id, [{
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"text": {"content": text}}]
            }
        }])
    
    def add_heading(self, block_id: str, text: str, level: int = 1) -> Dict:
        """添加标题"""
        heading_type = f"heading_{level}"
        return self.append_blocks(block_id, [{
            "object": "block",
            "type": heading_type,
            heading_type: {
                "rich_text": [{"text": {"content": text}}]
            }
        }])
    
    def add_bullet_list(self, block_id: str, items: List[str]) -> Dict:
        """添加无序列表"""
        children = []
        for item in items:
            children.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"text": {"content": item}}]
                }
            })
        return self.append_blocks(block_id, children)
    
    def add_todo(self, block_id: str, text: str, checked: bool = False) -> Dict:
        """添加待办事项"""
        return self.append_blocks(block_id, [{
            "object": "block",
            "type": "to_do",
            "to_do": {
                "rich_text": [{"text": {"content": text}}],
                "checked": checked
            }
        }])
    
    # ==================== 内部方法 ====================
    
    def _request(
        self,
        method: str,
        endpoint: str,
        json: Dict = None,
        params: Dict = None
    ) -> Dict:
        """发送请求"""
        url = f"{BASE_URL}{endpoint}"
        
        # 添加延迟避免速率限制
        time.sleep(0.35)  # Notion 限制 ~3 requests/sec
        
        if method == "GET":
            response = requests.get(url, headers=self.headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=self.headers, json=json)
        elif method == "PATCH":
            response = requests.patch(url, headers=self.headers, json=json)
        elif method == "DELETE":
            response = requests.delete(url, headers=self.headers)
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        if response.status_code >= 400:
            return {
                "error": True,
                "status": response.status_code,
                "message": response.text
            }
        
        return response.json()


# ==================== 便捷函数 ====================

def quick_search(query: str) -> List[Dict]:
    """快速搜索"""
    client = NotionClient()
    return client.search_pages(query)


def quick_create_task(database_id: str, title: str, status: str = "待处理") -> Dict:
    """快速创建任务"""
    client = NotionClient()
    return client.create_database_item(database_id, {
        "Name": {"title": [{"text": {"content": title}}]},
        "Status": {"select": {"name": status}}
    })


def quick_add_daily_log(database_id: str, content: str) -> Dict:
    """快速添加每日记录"""
    client = NotionClient()
    return client.create_database_item(database_id, {
        "Name": {"title": [{"text": {"content": content}}]},
        "日期": {"date": {"start": time.strftime("%Y-%m-%d")}}
    })


# ==================== 自定义 Agent ====================

class NotionTaskAgent:
    """任务管理 Agent"""
    
    def __init__(self, database_id: str):
        self.client = NotionClient()
        self.database_id = database_id
    
    def add_task(self, title: str, status: str = "待处理", tags: List[str] = None) -> Dict:
        """添加任务"""
        properties = {
            "Name": {"title": [{"text": {"content": title}}]},
            "Status": {"select": {"name": status}}
        }
        
        if tags:
            properties["Tags"] = {"multi_select": [{"name": tag} for tag in tags]}
        
        return self.client.create_database_item(self.database_id, properties)
    
    def complete_task(self, task_id: str) -> Dict:
        """完成任务"""
        return self.client.update_page(task_id, {
            "Status": {"select": {"name": "已完成"}}
        })
    
    def list_tasks(self, status: str = None) -> List[Dict]:
        """列出任务"""
        filter_cond = None
        if status:
            filter_cond = {
                "property": "Status",
                "select": {"equals": status}
            }
        
        result = self.client.query_database(self.database_id, filter_cond)
        return result.get("results", [])


class NotionDailyLogAgent:
    """每日记录 Agent"""
    
    def __init__(self, database_id: str):
        self.client = NotionClient()
        self.database_id = database_id
    
    def log(self, content: str, category: str = None) -> Dict:
        """记录每日"""
        properties = {
            "Name": {"title": [{"text": {"content": content}}]},
            "日期": {"date": {"start": time.strftime("%Y-%m-%d")}}
        }
        
        if category:
            properties["分类"] = {"select": {"name": category}}
        
        return self.client.create_database_item(self.database_id, properties)
    
    def today_logs(self) -> List[Dict]:
        """今日记录"""
        today = time.strftime("%Y-%m-%d")
        filter_cond = {
            "property": "日期",
            "date": {"equals": today}
        }
        
        result = self.client.query_database(self.database_id, filter_cond)
        return result.get("results", [])


# ==================== 主程序 ====================

if __name__ == "__main__":
    client = NotionClient()
    
    # 测试
    print("=" * 50)
    print("Notion API 测试")
    print("=" * 50)
    
    # 获取用户
    me = client.get_me()
    print(f"用户: {me.get('name', 'Unknown')}")
    print(f"类型: {me.get('type')}")
    
    # 搜索
    print("\n搜索页面...")
    pages = client.search_pages("项目")
    for page in pages[:5]:
        title = page.get("properties", {}).get("title", {}).get("title", [{}])[0].get("text", {}).get("content", "Untitled")
        print(f"  - {title}")
    
    print("\n搜索数据库...")
    dbs = client.search_databases("")
    for db in dbs[:5]:
        title = db.get("title", [{}])[0].get("text", {}).get("content", "Untitled")
        print(f"  - {title}")
