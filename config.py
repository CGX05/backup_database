from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv("config.env")

class Settings:
    MYSQL_HOST=os.getenv("MYSQL_HOST","localhost")
    MYSQL_PORT=os.getenv("MYSQL_PORT",3306)
    MYSQL_USER=os.getenv("MYSQL_USER",'root')
    MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD",'')
    TOKEN_KEY=os.getenv("token_key",'')


    # 备份路径
    BACKUP_DIR=os.getenv("BACKUP_DIR","./backups")
    backup_path=Path(BACKUP_DIR)
    # 判断是否存在
    if not backup_path.exists():
        backup_path.mkdir(parents=True)
        print("目录不存在")
    elif not backup_path.is_dir():
        print(f"{BACKUP_DIR}存在，但不是目录")
    else:
        print(f"{BACKUP_DIR}存在")

settings=Settings()