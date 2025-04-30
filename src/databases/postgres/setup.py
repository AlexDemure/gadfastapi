from gadsqlalchemy import Sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession
from src.framework import settings

pg = Sqlalchemy(settings.POSTGRES_URL)

Session = AsyncSession
