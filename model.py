from pydantic import BaseModel
from typing import Optional


class System(BaseModel):
    name:str
    code:str
    health_check_url:str
    check_frequency:int

class HealthStatus(BaseModel):
    system_name: str
    system_code: str
    is_healthy: bool          # 是否健康（True/False）
    last_check_time: float    # 最后检查时间（时间戳）
    message: Optional[str]    # 检查结果描述
