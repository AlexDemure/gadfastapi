from datetime import date

from sqlalchemy import BinaryExpression, delete, exists, func, select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.sql import Select

from src.databases.exceptions import ObjectNotFoundError
from src.databases.postgres.setup import AsyncSession
from src.databases.postgres.tables import Table


class CRUD:
    table: Table

    @classmethod
    def filters(cls, fields: dict) -> list[BinaryExpression]:
        expressions = []

        for key in fields.keys():
            if fields[key] is not None:
                if isinstance(fields[key], list):
                    expressions.append(getattr(cls.table, key).in_(fields[key]))
                elif isinstance(fields[key], date):
                    expressions.append(func.DATE(getattr(cls.table, key)) == fields[key])
                else:
                    expressions.append(getattr(cls.table, key) == fields[key])

        return expressions

    @classmethod
    async def one(cls, session: AsyncSession, **kwargs) -> Table:
        query = select(cls.table).where(*cls.filters(kwargs))
        return await fetchone(session, query)

    @classmethod
    async def relations(cls, session: AsyncSession, **kwargs) -> Table:
        raise NotImplementedError

    @classmethod
    async def paginated(
        cls,
        session: AsyncSession,
        filters: dict,
        sorting: dict,
        pagination: dict,
    ) -> tuple[list[Table], int]:
        raise NotImplementedError

    @classmethod
    async def all(cls, session: AsyncSession, **kwargs) -> list[Table]:
        query = select(cls.table).where(*cls.filters(kwargs))
        return await fetchall(session, query)

    @classmethod
    async def count(cls, session: AsyncSession, **kwargs) -> int:
        query = select(cls.table).where(*cls.filters(kwargs))
        return await count(session, query)

    @classmethod
    async def exists(cls, session: AsyncSession, **kwargs) -> bool:
        query = exists().where(*cls.filters(kwargs)).select()
        return (await session.execute(query)).scalar()

    @classmethod
    async def create(cls, session: AsyncSession, row: dict) -> Table:
        columns = {k: v for k, v in row.items() if getattr(cls.table, k, None) is not None}
        instance = cls.table(**columns)
        session.add(instance)
        await session.flush()
        return instance

    @classmethod
    async def update(cls, session: AsyncSession, id: str | int, **kwargs) -> None:
        columns = {k: v for k, v in kwargs.items() if getattr(cls.table, k, None) is not None}
        query = update(cls.table).where(cls.table.id == id).values(**columns)
        await session.execute(query)
        await session.flush()

    @classmethod
    async def delete(cls, session: AsyncSession, **kwargs) -> None:
        query = delete(cls.table).where(*cls.filters(kwargs))
        await session.execute(query)
        await session.flush()


async def fetchone(session: AsyncSession, query: Select) -> Table:
    try:
        return (await session.execute(query)).unique().scalars().one()
    except NoResultFound:
        raise ObjectNotFoundError


async def fetchall(session: AsyncSession, query: Select) -> list[Table]:
    return (await session.execute(query)).scalars().all()  # type:ignore


async def count(session: AsyncSession, query: Select) -> int:
    return (await session.execute(select(func.count()).select_from(query.subquery()))).scalars().one()
