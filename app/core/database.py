from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker, 
    AsyncSession)
from app.core.config import settings
from sqlalchemy.orm import DeclarativeBase


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=10, 
    max_overflow=20,
    pool_timeout=30,
    pool_pre_ping=True,
    pool_recycle=1800
    )

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

class Base(DeclarativeBase):
    pass


async def get_db():
   async with AsyncSessionLocal() as session:
       yield session

