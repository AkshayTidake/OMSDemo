from sqlalchemy.ext.asyncio import (create_async_engine,async_sessionmaker, AsyncSession)
from app.core.config import settings
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv

# Load variables from .env into the system environment
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(settings.DATABASE_URL,pool_size=20, max_overflow=40,pool_timeout=30,pool_pre_ping=True,pool_recycle=1800)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass


async def get_db():
   async with AsyncSessionLocal() as session:
       yield session

