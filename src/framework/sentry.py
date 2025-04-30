from gadfastsentry import Sentry

from .settings import settings

if settings.SENTRY:
    Sentry(dsn=settings.SENTRY_DSN, env=settings.ENV)
