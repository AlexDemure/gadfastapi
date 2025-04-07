from enum import StrEnum
from enum import auto

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Env(StrEnum):
    develop = auto()
    production = auto()


class PostgresSettings(BaseSettings):
    POSTGRES_URL: str


# INCLUDE SETTINGS
configs = [
    PostgresSettings,
]


class Settings(*configs):  # type:ignore
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True, extra="ignore")

    ENV: Env


settings = Settings()
