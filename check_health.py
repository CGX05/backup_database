import requests
import json
import time
from model import System,HealthStatus

def load_json(file_path:str="config.json"):
    """加载json文件"""
    try:
        with open(file_path,'r',encoding='utf8') as file:
            data=json.load(file)
            systems=[System(**item) for item in data]
            print(f"加载{len(systems)}个配置")
            print(systems)
            return systems
    except Exception as e:
        return {f"配置文件出错{e}"}
# load_json()

def check_health(system:System):
    """执行检查"""
    try:
        request=requests.get(system.health_check_url,timeout=10)
        is_healthy=request.status_code==200
        return HealthStatus(
            system_name=system.name,
            system_code=system.code,
            is_healthy=is_healthy,
            last_check_time=time.time(),
            message=f"状态码{request.status_code}"
        )
    except Exception as e:
        return HealthStatus(
            system_name=system.name,
            system_code=system.code,
            is_healthy=False,
            last_check_time=time.time(),
            message=f"检查失败: {str(e)}"
        )





