from functools import lru_cache
from pydantic import computed_field
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_ENV: str = "development"
    DEBUG: bool = False

    USERNAME: str
    PASSWORD: str
    DATABASE: str
    PORT: int = 5432
    HOST: str = "postgres"

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    REDIS_HOST: str
    REDIS_PORT: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}"

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
