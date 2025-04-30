from enum import StrEnum
from enum import auto

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Env(StrEnum):
    develop = auto()
    production = auto()


class PostgresSettings(BaseSettings):
    POSTGRES_URL: str


class S3Settings(BaseSettings):
    S3_HOST: str
    S3_BUCKET: str
    S3_ACCESS_KEY: str
    S3_SECRET_KEY: str


class EtcdSettings(BaseSettings):
    ETCD_HOST: str
    ETCD_STORAGE: str


class SentrySettings(BaseSettings):
    SENTRY: bool
    SENTRY_DSN: str | None


configs = [
    PostgresSettings,
    S3Settings,
    EtcdSettings,
    SentrySettings,
]


class Settings(*configs):  # type:ignore
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True, extra="allow")

    ENV: Env


settings = Settings()
