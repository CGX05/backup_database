import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,HTTPException
import uvicorn
from backup import get_backup_files,backup_database_post
from check_health import execute_check_health,lifespan
from supervisord_API import get_processes,get_process_name,get_process_log
import logging
import logging.handlers

#配置日志目录
log_dir="logs"
os.makedirs(log_dir,exist_ok=True)

logger=logging.getLogger("DatabaseBackupApp")
logger.setLevel(logging.DEBUG)
logger.propagate=False
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
)
file_handler=logging.handlers.TimedRotatingFileHandler(
    os.path.join(log_dir,"backup.log"),
    when="midnight",
    interval=1,
    backupCount=7,
    encoding='utf-8'
)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)


app=FastAPI(lifespan=lifespan,
            title="Mysql备份",
            version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
async def hello():
    logger.info("/根目录被访问")
    return {"message":"Hello"}

@app.get("/health",summary="检查系统")
async def check_health():
    logger.info("健康检查接口被调用")
    raise HTTPException(status_code=200)


@app.get("/api/backups",summary="获取备份列表接口")
async def backup_list():
    try:
        logger.info("开始获取备份列表接口信息")
        backup_files=get_backup_files()
        logger.info(f"成功获取{len(backup_files)}个备份文件")
        return backup_files
    except Exception as e:
        logger.error(f"获取备份文件失败{e}",exc_info=True)
        raise HTTPException(status_code=500,
                            detail=f"获取备份文件信息失败：{e}")


@app.post("/api/backup/database",summary="执行数据库备份接口")
async def backup_post():
    logger.info("收到数据库备份请求")
    result=backup_database_post()
    if not result["success"]:
        raise HTTPException(status_code=500,
                            detail=result["message"])
    logger.info(f"备份成功：{result}")
    raise HTTPException(status_code=200,
                        detail=f"备份成功!"
    )

@app.get("/api/health",summary="返回系统健康状态接口")
async def get_health_status():
    """获取系统健康状态"""
    logger.info("检查系统健康")
    check=execute_check_health()
    logger.info(f"系统健康检查结果：{check}")
    return check

@app.get("/api/supervisord/processes",summary="获取supervisord管理的所有进程状态信息")
async def list_processes():
    try:
        processes=get_processes()
        return processes
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"获取失败：{str(e)}")

@app.get("/api/supervisord/process/{name}",summary="获取指定进程的状态")
async def process(name:str):
    try:
        process=get_process_name(name)
        return process
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"指定{name}进程状态获取失败：{str(e)}")

@app.get("/api/supervisord/process/log/{name}",summary="获取指定进程日志")
async def get_log(name:str):
    try:
        logs=get_process_log(name)
        return logs
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"指定{name}进程日志获取失败：{str(e)}")



# if __name__ == "__main__":
#
#     uvicorn.run(
#         app="main:app",
#         host='127.0.0.1',
#         port=8000,
#         reload=True
#     )