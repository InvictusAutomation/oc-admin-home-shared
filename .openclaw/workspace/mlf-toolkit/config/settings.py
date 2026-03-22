"""配置管理模块"""
import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent.parent
load_dotenv(PROJECT_ROOT / "config" / "config.env")


class Settings:
    MLFLOW_TRACKING_URI: str = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
    MLFLOW_EXPERIMENT_NAME: str = os.getenv("MLFLOW_EXPERIMENT_NAME", "mlf_toolkit_default")
    LANGFUSE_PUBLIC_KEY: str = os.getenv("LANGFUSE_PUBLIC_KEY", "")
    LANGFUSE_SECRET_KEY: str = os.getenv("LANGFUSE_SECRET_KEY", "")
    LANGFUSE_HOST: str = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o")
    APP_TITLE: str = os.getenv("APP_TITLE", "MLF-Toolkit")
    APP_ICON: str = os.getenv("APP_ICON", "🤖")
    MEMORY_DIR: Path = PROJECT_ROOT / "memory"
    
    @classmethod
    def init_memory_dir(cls):
        cls.MEMORY_DIR.mkdir(parents=True, exist_ok=True)
        (cls.MEMORY_DIR / "sessions").mkdir(exist_ok=True)
        (cls.MEMORY_DIR / "projects").mkdir(exist_ok=True)
        
    @classmethod
    def is_mlflow_configured(cls) -> bool:
        return bool(cls.MLFLOW_TRACKING_URI)
    
    @classmethod
    def is_langfuse_configured(cls) -> bool:
        return bool(cls.LANGFUSE_PUBLIC_KEY and cls.LANGFUSE_SECRET_KEY)
    
    @classmethod
    def is_llm_configured(cls) -> bool:
        return bool(cls.OPENAI_API_KEY)


settings = Settings()
