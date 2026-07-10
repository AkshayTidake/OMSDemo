from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.refresh_token import RefreshToken

class AuthRepository:

    def __init__(self,db: AsyncSession):
        self.db=db

    async def save_refresh_token(self, refresh_token: RefreshToken):
        self.db.add(refresh_token)

    async def get_refresh_token(self,token:str) -> RefreshToken | None:
        result = await self.db.execute(select(RefreshToken).where(RefreshToken.token == token))
        return result.scalar_one_or_none()
    
    async def delete_refresh_token(self,refresh_token: RefreshToken):

        await self.db.delete(refresh_token)
