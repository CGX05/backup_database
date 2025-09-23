from pydantic import BaseModel

class System(BaseModel):
    name:str
    code:str
    health_check_url:str
    check_frequency:int

class HealthStatus(BaseModel):
    system_name: str
    is_healthy: bool # 是否健康（True/False）
    message: str     # 检查结果描述
