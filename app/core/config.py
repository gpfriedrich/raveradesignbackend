from functools import lru_cache

from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Ravera API"
    debug: bool = False
    database_url: PostgresDsn = Field(
        default="postgresql+psycopg://ravera:senha_ficticia@localhost:5432/ravera"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
