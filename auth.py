from fastapi.security import OAuth2AuthorizationCodeBearer,OAuth2PasswordRequestForm
from model import token,user
from datetime import datetime,timedelta
from jose import JWSError,jwt
from config import settings

SECRET_KEY=settings.SECRET_KEY

