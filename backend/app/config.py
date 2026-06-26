from pathlib import Path
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    APP_NAME: str = "VLineups"
    DATABASE_URL: PostgresDsn
    DEBUG: bool = False
    CORS_ORIGINS: list[str]
    CORS_METHODS: list[str]
    CORS_HEADERS: list[str]

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")


settings = Settings()  # type: ignore
