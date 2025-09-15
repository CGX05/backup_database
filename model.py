from pydantic import BaseModel

class Backup_Post(BaseModel):
    database_name:str
