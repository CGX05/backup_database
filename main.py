from fastapi import FastAPI,HTTPException
import uvicorn

from backup import get_backup_files,backup_database_post
from model import Backup_Post

app=FastAPI(title="Mysql备份",
            version="1.0.0")

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


@app.post("/api/backup",summary="指定数据库备份接口")
async def backup_post(request:Backup_Post):
    if not request.database_name:
        raise HTTPException(
            status_code=400,
            detail="数据库名称不能为空")
    result=backup_database_post(request.database_name)
    if not result["success"]:
        raise HTTPException(status_code=500,
                            detail=result["message"])
    raise HTTPException(status_code=200,
                        detail=f"{request.database_name}备份成功!"
    )

if __name__ == "__main__":

    uvicorn.run(
        app="main:app",
        host='127.0.0.1',
        port=8080,
        reload=True
    )