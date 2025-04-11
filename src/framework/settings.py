import enum

import pydantic_settings


class Env(enum.StrEnum):
    develop = enum.auto()
    production = enum.auto()


class PostgresSettings(pydantic_settings.BaseSettings):
    POSTGRES_URL: str


configs = [
    PostgresSettings,
]


class Settings(*configs):  # type:ignore
    model_config = pydantic_settings.SettingsConfigDict(env_file=".env", case_sensitive=True, extra="ignore")

    ENV: Env


settings = Settings()
