"""
LangFuse 客户端封装
提供 LLM 应用监控和日志分析的统一接口
"""
from langfuse import Langfuse
from typing import Dict, List, Optional, Any
import time


class LangFuseClientWrapper:
    """LangFuse 客户端封装类"""
    
    def __init__(self, public_key: str, secret_key: str, host: str = "https://cloud.langfuse.com"):
        self.public_key = public_key
        self.secret_key = secret_key
        self.host = host
        self.langfuse = Langfuse(public_key=public_key, secret_key=secret_key, host=host)
        
    def generate(self, prompt: str, model: str = "gpt-4o", temperature: float = 0.7, 
                 max_tokens: Optional[int] = None, metadata: Optional[Dict] = None, **kwargs) -> Dict:
        """生成文本并自动跟踪"""
        start_time = time.time()
        
        from config.settings import settings
        if settings.OPENAI_API_KEY:
            import openai
            openai.api_key = settings.OPENAI_API_KEY
            
            response = openai.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs
            )
            
            result = response.choices[0].message.content
            latency = time.time() - start_time
            
            self.langfuse.trace(name=model, input=prompt, output=result, metadata=metadata or {})
            
            return {"output": result, "model": model, "latency": latency, "usage": response.usage.model_dump() if response.usage else {}}
        else:
            raise ValueError("No LLM provider configured")
    
    def chat(self, messages: List[Dict], model: str = "gpt-4o", temperature: float = 0.7) -> Dict:
        """聊天完成接口"""
        from config.settings import settings
        import openai
        openai.api_key = settings.OPENAI_API_KEY
        
        response = openai.chat.completions.create(model=model, messages=messages, temperature=temperature)
        
        return {"message": response.choices[0].message.model_dump(), "usage": response.usage.model_dump() if response.usage else {}}
    
    def list_traces(self, limit: int = 100) -> List[Dict]:
        traces = self.langfuse.traces.list(limit=limit)
        return [{"id": t.id, "name": t.name, "input": t.input, "output": t.output} for t in traces]
    
    def get_stats(self, start_date=None, end_date=None) -> Dict:
        from datetime import timedelta
        if not start_date:
            start_date = datetime.now() - timedelta(days=7)
        if not end_date:
            end_date = datetime.now()
        traces = self.langfuse.traces.list(start_date=start_date, end_date=end_date)
        return {"total_traces": len(traces)}


def get_langfuse_client() -> LangFuseClientWrapper:
    from config.settings import settings
    return LangFuseClientWrapper(public_key=settings.LANGFUSE_PUBLIC_KEY, secret_key=settings.LANGFUSE_SECRET_KEY, host=settings.LANGFUSE_HOST)
