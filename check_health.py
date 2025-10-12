import requests
import json
from fastapi import FastAPI
from model import System,HealthStatus
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from contextlib import asynccontextmanager
import asyncio

def load_json(file_path:str="config.json"):
    """加载json文件"""
    try:
        with open(file_path,'r',encoding='utf8') as file:
            data=json.load(file)
            systems=[System(**item) for item in data]
            # print(f"加载{len(systems)}个健康检查配置")
            # print(systems)
            return systems
    except Exception as e:
        return {f"健康检查配置文件出错{e}"}
# load_json()

def check_health(system:System):
    """健康检查逻辑"""
    try:
        request=requests.get(system.health_check_url,timeout=30)
        is_healthy=request.status_code==200
        return HealthStatus(
            system_name=system.name,
            is_healthy=is_healthy,
            message=f"系统检查正常，状态码：{request.status_code}"
        )
    except Exception as e:
        return HealthStatus(
            system_name=system.name,
            is_healthy=False,
            message=f"系统检查异常: {str(e)}"
        )

def execute_check_health():
    # 执行检查
    all_check={}
    systems=load_json()
    if not systems:
        print("json没有配置可检查的系统信息")
    for system in systems:
        check=check_health(system)
        all_check[system.code]=check
        print(all_check)
    return all_check


# 定时执行的任务
systems_timr=load_json()
for system_t in systems_timr:
    check_time=system_t.check_frequency
@asynccontextmanager
async def lifespan(app:FastAPI):
    global check_time
    scheduler=AsyncIOScheduler()
    scheduler.add_job(execute_check_health,
                      trigger=IntervalTrigger(seconds=check_time),
                      id="check_time"
                      )

    scheduler.start()
    print("🚀 定时任务调度器已启动")

    yield

    scheduler.shutdown()
    print("定时任务 已关闭")


