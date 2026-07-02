from pwdlib import PasswordHash
from datetime import datetime, timedelta
from jose import jwt
from app.core.config import settings


password_hash = PasswordHash.recommended()


def get_password_hash(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

def create_access_token(data: dict):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": expire})

    return jwt.encode(payload, settings.SECRET_KEY,
                      algorithm=settings.ALGORITHM)

# password_hash = PasswordHash.recommended()
# hashed = password_hash.hash(password)
# password_hash.verify(password,hashed)



