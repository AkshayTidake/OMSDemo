from sqlalchemy import select
from models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):

    def __init__(self,db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str) -> User | None:

        result = await self.db.execute(
            select(User).where(User.email == email)
        )

        return result.scalar_one_or_none()
    

    async def get_by_id( self, user_id: int) -> User | None:

        result = await self.db.execute( select(User).where(User.id == user_id))

        return result.scalar_one_or_none()
    

    async def create_user(self, user: User):

        self.db.add(user)

        return user