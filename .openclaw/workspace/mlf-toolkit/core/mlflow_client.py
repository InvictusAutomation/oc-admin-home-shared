"""
MLflow 客户端封装
提供机器学习实验跟踪的统一接口
"""
import mlflow
from mlflow.tracking import MlflowClient
from typing import Dict, List, Optional, Any
import pandas as pd


class MLflowClientWrapper:
    """MLflow 客户端封装类"""
    
    def __init__(self, tracking_uri: str, experiment_name: str = "mlf_toolkit_default"):
        self.tracking_uri = tracking_uri
        self.experiment_name = experiment_name
        self.client = MlflowClient(tracking_uri)
        self._setup_experiment()
        
    def _setup_experiment(self):
        """设置实验"""
        try:
            exp_id = mlflow.create_experiment(self.experiment_name)
        except mlflow.exceptions.MlflowException:
            exp_id = mlflow.get_experiment_by_name(self.experiment_name).experiment_id
        mlflow.set_experiment(self.experiment_name)
        self.experiment_id = exp_id
        
    def start_run(self, run_name: Optional[str] = None, nested: bool = False):
        return mlflow.start_run(run_name=run_name, nested=nested)
    
    def end_run(self, status: str = "FINISHED"):
        mlflow.end_run(status=status)
        
    def log_param(self, key: str, value: Any):
        mlflow.log_param(key, value)
        
    def log_params(self, params: Dict[str, Any]):
        mlflow.log_params(params)
        
    def log_metric(self, key: str, value: float, step: Optional[int] = None):
        mlflow.log_metric(key, value, step=step)
        
    def log_metrics(self, metrics: Dict[str, float], step: Optional[int] = None):
        mlflow.log_metrics(metrics, step=step)
        
    def log_artifact(self, local_path: str, artifact_path: Optional[str] = None):
        mlflow.log_artifact(local_path, artifact_path=artifact_path)
        
    def set_tag(self, key: str, value: str):
        mlflow.set_tag(key, value)
        
    def set_tags(self, tags: Dict[str, str]):
        mlflow.set_tags(tags)
        
    def get_experiment(self, experiment_name: Optional[str] = None) -> Dict:
        name = experiment_name or self.experiment_name
        exp = mlflow.get_experiment_by_name(name)
        if exp:
            return {
                "id": exp.experiment_id,
                "name": exp.name,
                "artifact_location": exp.artifact_location,
            }
        return {}
    
    def list_runs(self, max_results: int = 100, filter_string: Optional[str] = None) -> pd.DataFrame:
        return mlflow.search_runs(
            experiment_ids=[self.experiment_id],
            filter_string=filter_string,
            max_results=max_results
        )
    
    def get_run(self, run_id: str) -> Dict:
        run = mlflow.get_run(run_id)
        return {
            "run_id": run.info.run_id,
            "status": run.info.status,
            "params": run.data.params,
            "metrics": run.data.metrics,
            "tags": run.data.tags
        }
    
    def compare_runs(self, run_ids: List[str]) -> pd.DataFrame:
        runs_data = []
        for run_id in run_ids:
            run_info = self.get_run(run_id)
            runs_data.append({"run_id": run_id, **run_info.get("metrics", {}), **run_info.get("params", {})})
        return pd.DataFrame(runs_data)


def get_mlflow_client() -> MLflowClientWrapper:
    from config.settings import settings
    return MLflowClientWrapper(
        tracking_uri=settings.MLFLOW_TRACKING_URI,
        experiment_name=settings.MLFLOW_EXPERIMENT_NAME
    )
