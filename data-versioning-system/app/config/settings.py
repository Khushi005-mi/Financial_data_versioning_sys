# app/config/settings.py

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # App
    APP_NAME: str
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"


    # Database
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    
    UPLOAD_DIR: str
    SNAPSHOT_DIR: str
@property
def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

class Config:
        env_file = ".env"
        case_sensitive = True


# Singleton settings object (important)
@lru_cache
def get_settings():
    return Settings()

