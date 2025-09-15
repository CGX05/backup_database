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
            "filename": f"backup_{create_time}_{file_path.name}",
            "create_time": create_time,
            "file_size": stat.st_size
        })
    return backup_files
# print(get_backup_files())