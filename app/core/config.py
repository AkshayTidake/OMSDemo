from pydantic import computed_field
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    USERNAME: str
    PASSWORD: str
    DATABASE: str
    PORT: int = 5432
    HOST: str = "postgres"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}"


settings = Settings()
