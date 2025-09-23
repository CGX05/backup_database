from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,HTTPException
import uvicorn
from backup import get_backup_files,backup_database_post
from check_health import execute_check_health,lifespan
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
    return {"message":"Hello"}

@app.get("/api/backups",summary="获取备份列表接口")
async def backup_list():
    try:
        backup_files=get_backup_files()
        return backup_files
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=f"获取备份文件信息失败：{e}")


@app.get("/api/backup/database",summary="数据库备份接口")
async def backup_post():
    result=backup_database_post()
    if not result["success"]:
        raise HTTPException(status_code=500,
                            detail=result["message"])
    raise HTTPException(status_code=200,
                        detail=f"备份成功!"
    )

@app.get("/api/health",summary="系统健康状态接口")
async def get_health_status():
    """获取系统健康状态"""
    check=execute_check_health()
    return check

# if __name__ == "__main__":
#
#     uvicorn.run(
#         app="main:app",
#         host='127.0.0.1',
#         port=8000,
#         reload=True
#     )