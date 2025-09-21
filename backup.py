import os.path
import subprocess
from datetime import datetime
from pathlib import Path
from config import settings


def get_backup_files():
    """获取备份目录中的文件信息"""
    backup_files = list()
    backup_dir = Path(settings.BACKUP_DIR)

    for file_path in backup_dir.glob("*.sql"):
        stat = file_path.stat()
        create_time=datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
        backup_files.append({
            "filename": f"{file_path.name}",
            "create_time": create_time,
            "file_size": f"{round(stat.st_size / (1024 * 1024), 2)}MB"
        })
    return backup_files
# print(get_backup_files())

def backup_database_post():
    """数据库备份"""
    try:
        time_str=datetime.now().strftime("%Y-%m-%d %H时%M分%S")
        filename=f"backup_{time_str}.sql"
        backup_dir=settings.BACKUP_DIR
        backup_path=os.path.join(backup_dir,filename)
        cmd=[
            'mysqldump',
            f'-h{settings.MYSQL_HOST}',
            f'-P{settings.MYSQL_PORT}',
            f'-u{settings.MYSQL_USER}',
            f'-p{settings.MYSQL_PASSWORD}',
            '--all-databases'
        ]
        with open(backup_path,'w') as f:
            result=subprocess.run(cmd,stdout=f,text=True)
        if result.returncode != 0:
            os.remove(backup_path)
            return {
                "success":False,
                "message":f"备份失败，返回码{result.returncode}",
                "backup_file":None
            }
        return {
            "success": True,
            "message": "备份成功",
            "backup_file": str(backup_path)
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"备份异常: {str(e)}",
            "backup_file": None
        }
# print(backup_database_post())