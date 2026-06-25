# from pwdlib import PasswordHash
from passlib.context import CryptoContext
from datetime import datetime, timedelta
from jose import jwt
from app.core.config import settings


pwd_context = CryptoContext(schemes=["bycrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data: dict):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCES_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": expire})

    return jwt.encode(payload, settings.SECRET_KEY,
                      algorithm=settings.ALGORITHM)

# password_hash = PasswordHash.recommended()
# hashed = password_hash.hash(password)
# password_hash.verify(password,hashed)



