from datetime import UTC, datetime, timedelta
from jose import jwt 
from app.core.config import settings

def create_Access_token(data: dict) -> str:
    payload = data.copy()

    payload["exp"] =(
        datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )