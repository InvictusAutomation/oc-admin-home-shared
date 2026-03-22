"""
MLF-Toolkit 主应用程序
开箱即用的机器学习实验与大语言模型监控工具
"""
import streamlit as st
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from config.settings import settings
from core import get_mlflow_client, get_langfuse_client, get_memory_system

st.set_page_config(page_title=settings.APP_TITLE, page_icon=settings.APP_ICON, layout="wide")

# CSS
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: bold; text-align: center; padding: 20px; }
    .mode-selector { display: flex; justify-content: center; gap: 20px; padding: 20px; }
    .feature-card { background: #f0f2f6; padding: 20px; border-radius: 10px; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)


class ModeState:
    MODE = "mode"
    
    @staticmethod
    def init():
        if ModeState.MODE not in st.session_state:
            st.session_state[ModeState.MODE] = "home"
    
    @staticmethod
    def set_mode(mode: str):
        st.session_state[ModeState.MODE] = mode
    
    @staticmethod
    def get_mode():
        return st.session_state.get(ModeState.MODE, "home")


def render_sidebar():
    with st.sidebar:
        st.title("🛠️ 工具箱")
        
        st.subheader("🔄 模式切换")
        mode = st.radio("选择工作模式", ["🏠 首页", "🤖 MLflow 模式", "💬 LangFuse 模式", "🧠 记忆系统"])
        
        mode_map = {"🏠 首页": "home", "🤖 MLflow 模式": "mlflow", "💬 LangFuse 模式": "langfuse", "🧠 记忆系统": "memory"}
        ModeState.set_mode(mode_map.get(mode, "home"))
        
        st.divider()
        
        # 状态
        st.subheader("📌 状态")
        memory = get_memory_system()
        st.metric("会话ID", memory.session_id[:8])
        
        mlflow_status = "✅ 已配置" if settings.is_mlflow_configured() else "❌ 未配置"
        langfuse_status = "✅ 已配置" if settings.is_langfuse_configured() else "❌ 未配置"
        llm_status = "✅ 已配置" if settings.is_llm_configured() else "❌ 未配置"
        
        st.write(f"MLflow: {mlflow_status}")
        st.write(f"LangFuse: {langfuse_status}")
        st.write(f"LLM: {llm_status}")


def render_home():
    st.markdown('<p class="main-header">🤖 MLflow + LangFuse 集成工具箱</p>', unsafe_allow_html=True)
    
    st.markdown("""
    欢迎使用 **MLF-Toolkit**！这是一个开箱即用的机器学习实验与大语言模型监控一体化工具。
    
    ### 🎯 核心功能
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class="feature-card"><h3>🤖 MLflow 模式</h3><p>机器学习实验跟踪、模型管理、指标监控</p></div>""", unsafe_allow_html=True)
        if st.button("进入 MLflow 模式", key="btn_mlflow"): ModeState.set_mode("mlflow"); st.rerun()
    with col2:
        st.markdown("""<div class="feature-card"><h3>💬 LangFuse 模式</h3><p>LLM 应用监控、提示词工程与 token 分析</p></div>""", unsafe_allow_html=True)
        if st.button("进入 LangFuse 模式", key="btn_langfuse"): ModeState.set_mode("langfuse"); st.rerun()
    with col3:
        st.markdown("""<div class="feature-card"><h3>🧠 智能记忆</h3><p>全程跟踪分析过程，自动记录与复盘</p></div>""", unsafe_allow_html=True)
        if st.button("查看记忆系统", key="btn_memory"): ModeState.set_mode("memory"); st.rerun()


def render_mlflow_mode():
    st.title("🤖 MLflow 实验管理")
    
    if not settings.is_mlflow_configured():
        st.error("⚠️ MLflow 未配置！请在 config.env 中设置 MLFLOW_TRACKING_URI")
        return
    
    tab1, tab2, tab3 = st.tabs(["📈 实验列表", "🔬 运行详情", "⚡ 快速实验"])
    
    with tab1:
        st.subheader("实验列表")
        try:
            mlflow_client = get_mlflow_client()
            runs_df = mlflow_client.list_runs(max_results=20)
            if not runs_df.empty:
                st.dataframe(runs_df[["run_id", "status"]], use_container_width=True)
            else:
                st.info("暂无实验记录")
        except Exception as e:
            st.error(f"连接失败: {str(e)}")
    
    with tab3:
        st.subheader("⚡ 快速实验")
        exp_name = st.text_input("实验名称", "quick_experiment")
        metric_name = st.text_input("指标名称", "accuracy")
        metric_value = st.number_input("指标值", 0.0, 1.0, 0.85)
        
        if st.button("记录指标"):
            memory = get_memory_system()
            memory.record_analysis_step(f"记录指标 {metric_name}", {"value": metric_value})
            st.success(f"✅ 已记录: {metric_name} = {metric_value}")


def render_langfuse_mode():
    st.title("💬 LangFuse LLM 监控")
    
    if not settings.is_langfuse_configured():
        st.error("⚠️ LangFuse 未配置！请设置 LANGFUSE_PUBLIC_KEY 和 LANGFUSE_SECRET_KEY")
        return
    
    if not settings.is_llm_configured():
        st.error("⚠️ LLM 未配置！请设置 OPENAI_API_KEY")
        return
    
    tab1, tab2, tab3 = st.tabs(["🔍 Trace 追踪", "📊 统计分析", "💬 LLM 对话"])
    
    with tab1:
        st.subheader("Trace 追踪")
        try:
            langfuse = get_langfuse_client()
            traces = langfuse.list_traces(limit=10)
            if traces:
                for t in traces:
                    with st.expander(f"Trace: {t['id'][:8]}"):
                        st.write(f"**输入**: {str(t.get('input', ''))[:200]}")
            else:
                st.info("暂无 Trace")
        except Exception as e:
            st.error(f"获取失败: {str(e)}")
    
    with tab3:
        st.subheader("💬 LLM 对话")
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []
        
        for msg in st.session_state["chat_history"]:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        
        user_input = st.chat_input("输入您的问题...")
        if user_input:
            st.session_state["chat_history"].append({"role": "user", "content": user_input})
            
            try:
                langfuse = get_langfuse_client()
                response = langfuse.generate(prompt=user_input)
                st.session_state["chat_history"].append({"role": "assistant", "content": response.get("output", "无响应")})
                st.rerun()
            except Exception as e:
                st.error(f"调用失败: {str(e)}")


def render_memory_mode():
    st.title("🧠 智能记忆系统")
    
    memory = get_memory_system()
    history = memory.get_operation_history()
    
    st.subheader("📜 操作历史")
    
    if history:
        for op in reversed(history[-20:]):
            op_type = op.get("type", "unknown")
            emoji = {"create": "🟢", "update": "🔵", "analysis": "📊", "rollback": "⚠️"}.get(op_type, "⚪")
            with st.expander(f"{emoji} {op_type} - {op.get('timestamp', '')}"):
                st.write(f"**内容**: {op.get('content', '')}")
    else:
        st.info("暂无操作记录")
    
    st.divider()
    
    if st.button("📝 生成会话报告"):
        report = memory.generate_session_report()
        st.markdown(report)


def main():
    ModeState.init()
    render_sidebar()
    
    mode = ModeState.get_mode()
    if mode == "home": render_home()
    elif mode == "mlflow": render_mlflow_mode()
    elif mode == "langfuse": render_langfuse_mode()
    elif mode == "memory": render_memory_mode()
    else: render_home()


if __name__ == "__main__":
    settings.init_memory_dir()
    main()
