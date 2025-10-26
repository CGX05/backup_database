from fastapi import HTTPException,status,Depends
from fastapi.security import  HTTPAuthorizationCredentials,HTTPBearer
from config import settings

oauth2_schemes=HTTPBearer()
valid_token={
    f"{settings.TOKEN_KEY}"
}

def get_current_token(credentials: HTTPAuthorizationCredentials = Depends(oauth2_schemes)):
    token = credentials.credentials
    if token not in valid_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token