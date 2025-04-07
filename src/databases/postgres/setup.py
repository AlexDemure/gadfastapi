import enum
import json
from contextlib import asynccontextmanager
from datetime import date
from datetime import datetime
from decimal import Decimal
from functools import partial

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from src.framework import settings


class DatetimeAwareJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, enum.Enum):
            return obj.value
        elif isinstance(obj, Decimal):
            return str(obj)
        try:
            return json.JSONEncoder.default(self, obj)
        except TypeError:
            return str(obj)


custom_serializer = partial(json.dumps, cls=DatetimeAwareJSONEncoder, ensure_ascii=False)


_engine = create_async_engine(
    settings.POSTGRES_URL,
    echo=False,
    # echo_pool="debug",
    future=True,
    isolation_level="READ COMMITTED",  # Не изменять
    json_serializer=custom_serializer,
)

_sessionmaker = async_sessionmaker(_engine, expire_on_commit=False)

Table = declarative_base()


@asynccontextmanager
async def _read() -> AsyncSession:
    async with _sessionmaker() as session:
        await session.connection(execution_options={"isolation_level": "AUTOCOMMIT"})
        yield session


@asynccontextmanager
async def _write() -> AsyncSession:
    async with _sessionmaker() as session:
        try:
            async with session.begin():
                yield session
        except Exception as e:
            await session.rollback()
            raise e


@asynccontextmanager
async def pgconnect(transaction: bool = False) -> AsyncSession:
    if transaction:
        async with _write() as session:
            yield session
    else:
        async with _read() as session:
            yield session
