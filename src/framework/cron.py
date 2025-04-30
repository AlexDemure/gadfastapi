from gadfastcron import Cron
from gadfastcron import jobstores

from .settings import settings

store = jobstores.Sqlalchemy(settings.POSTGRES_URL.replace("asyncpg", "psycopg2")).store

cron = Cron(store)
