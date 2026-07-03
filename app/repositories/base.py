from typing import Generic, TypeVar, Type
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):

    def __init__(
            self,
            model: Type[ModelType],
            db: AsyncSession,
    ):
            
        self.model = model
        self.db = db

    async def get(self, id: int):
        result = await self.db.execute(
            select(self.model).where(
                self.model.id == id
                )
            )
        return result.scalar_one_or_none()
    

    async def get_all(self):
        result = await self.db.execute(
            select(self.model)
        )

        return result.scalars().all()
    

    async def create(self, **kwargs):

        obj = self.model(**kwargs)

        self.db.add(obj)

        await self.db.commit()

        await self.db.refresh(obj)

        return obj
    
    async def delete(self, obj):

        await self.db.delete(obj)

        await self.db.commit()

    async def update(self, obj, **kwargs):
        
        for key, value in kwargs.items():
            setattr(obj,key,value)
            
        await self.db.commit()

        await self.db.refresh(obj)

        return obj