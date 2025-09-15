from fastapi import FastAPI,HTTPException
import uvicorn
from backup import get_backup_files

app=FastAPI(title="Mysql备份",
            version="1.0.0")

@app.get('/')
async def hello():
    return {"message":"Hello"}

@app.get("/backup",summary="获取备份列表接口")
async def backup_list():
    try:
        backup_files=get_backup_files()
        return backup_files
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=f"获取备份文件信息失败：{e}")



if __name__ == "__main__":

    uvicorn.run(
        app="main:app",
        host='127.0.0.1',
        port=8080,
        reload=True
    )