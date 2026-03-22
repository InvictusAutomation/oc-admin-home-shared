"""
智能记忆系统
提供完整的分析过程跟踪和项目进展记录
"""
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
import uuid


class OperationType:
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    ROLLBACK = "rollback"
    ANALYSIS = "analysis"
    NOTE = "note"


class MemoryStore:
    """记忆存储管理"""
    
    def __init__(self, memory_dir: Path):
        self.memory_dir = memory_dir
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        
    def create_session(self, session_name: Optional[str] = None) -> str:
        session_id = str(uuid.uuid4())[:8]
        session_data = {"session_id": session_id, "session_name": session_name or f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}", 
                       "created_at": datetime.now().isoformat(), "operations": [], "projects": [], "notes": []}
        
        session_file = self.memory_dir / "sessions" / f"{session_id}.json"
        session_file.parent.mkdir(exist_ok=True)
        with open(session_file, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)
        return session_id
    
    def load_session(self, session_id: str) -> Dict:
        session_file = self.memory_dir / "sessions" / f"{session_id}.json"
        if session_file.exists():
            with open(session_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_session(self, session_id: str, data: Dict):
        session_file = self.memory_dir / "sessions" / f"{session_id}.json"
        with open(session_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def record_operation(self, session_id: str, operation_type: str, content: str, metadata: Optional[Dict] = None) -> str:
        session_data = self.load_session(session_id)
        operation = {"id": str(uuid.uuid4())[:8], "type": operation_type, "content": content, 
                     "timestamp": datetime.now().isoformat(), "metadata": metadata or {}}
        session_data.setdefault("operations", []).append(operation)
        self.save_session(session_id, session_data)
        return operation["id"]
    
    def get_operation_history(self, session_id: str) -> List[Dict]:
        session_data = self.load_session(session_id)
        return session_data.get("operations", [])
    
    def create_project(self, session_id: str, project_name: str) -> str:
        project_id = str(uuid.uuid4())[:8]
        project_data = {"project_id": project_id, "project_name": project_name, "created_at": datetime.now().isoformat(),
                       "milestones": [], "modifications": [], "status": "active"}
        
        project_file = self.memory_dir / "projects" / f"{project_id}.json"
        project_file.parent.mkdir(exist_ok=True)
        with open(project_file, 'w', encoding='utf-8') as f:
            json.dump(project_data, f, ensure_ascii=False, indent=2)
        
        session_data = self.load_session(session_id)
        session_data.setdefault("projects", []).append({"project_id": project_id, "project_name": project_name})
        self.save_session(session_id, session_id)
        return project_id
    
    def _get_all_projects(self) -> List[Dict]:
        projects_dir = self.memory_dir / "projects"
        if not projects_dir.exists():
            return []
        projects = []
        for f in projects_dir.glob("*.json"):
            with open(f, 'r', encoding='utf-8') as fp:
                projects.append(json.load(fp))
        return projects


class MemorySystem:
    """记忆系统主类"""
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, memory_dir: Optional[Path] = None):
        if self._initialized:
            return
        from config.settings import settings
        self.memory_dir = memory_dir or settings.MEMORY_DIR
        self.store = MemoryStore(self.memory_dir)
        self.current_session_id = self.store.create_session()
        self._initialized = True
    
    @property
    def session_id(self) -> str:
        return self.current_session_id
    
    def record_analysis_step(self, step_name: str, details: Dict):
        return self.store.record_operation(self.current_session_id, OperationType.ANALYSIS, step_name, details)
    
    def record_design_change(self, description: str, old_value: Any = None, new_value: Any = None):
        return self.store.record_operation(self.current_session_id, OperationType.UPDATE, description, 
                                          {"old_value": str(old_value), "new_value": str(new_value)})
    
    def create_project(self, project_name: str) -> str:
        return self.store.create_project(self.current_session_id, project_name)
    
    def get_operation_history(self) -> List[Dict]:
        return self.store.get_operation_history(self.current_session_id)
    
    def generate_session_report(self) -> str:
        session_data = self.store.load_session(self.current_session_id)
        ops = session_data.get("operations", [])
        report = [f"# 会话报告: {session_data.get('session_name', '未命名')}", 
                  f"- 创建时间: {session_data.get('created_at', '')}", f"- 操作数: {len(ops)}"]
        
        op_types = {}
        for op in ops:
            t = op.get("type", "unknown")
            op_types[t] = op_types.get(t, 0) + 1
        if op_types:
            report.append("\n### 操作类型分布")
            for t, count in op_types.items():
                report.append(f"- {t}: {count}")
        return "\n".join(report)


def get_memory_system() -> MemorySystem:
    return MemorySystem()
