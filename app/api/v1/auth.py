from fastapi import (APIRouter, Depends, HTTPException, status)
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.auth import (LoginRequest, TokenResponse)
from app.services.auth_service import AuthService
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    token = await AuthService.login(db,payload.email,payload.password)

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invaild credentials"
        )
    
    return{
        "access_token": token,
        "token_type": "bearer"
    }
class User(BaseModel):
    id: int
    username: str
    email: str
    fullname:str
    is_active: bool

    