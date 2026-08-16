from fastapi.security import HTTPAuthorizationCredentials
from jose import jwt
from datetime import datetime, timedelta, UTC

from jwt import InvalidTokenError

from app.core.config import get_settings


ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7
ALGORITHM = "HS256"

def create_access_token(user_id: str):
    payload = {
        "sub": user_id,
        "type": "access",
        "exp": datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }

    return jwt.encode(payload, get_settings().secret_key, algorithm=ALGORITHM)

def create_refresh_token(user_id: str):
    payload = {
        "sub": user_id,
        "type": "refresh",
        "exp": datetime.now(UTC) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    }

    return jwt.encode(payload, get_settings().secret_key, algorithm=ALGORITHM)

def verify_token(token):


    return jwt.decode(token, get_settings().secret_key, algorithms=[ALGORITHM])
