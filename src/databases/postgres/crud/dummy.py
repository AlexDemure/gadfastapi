from gadsqlalchemy import fetchall
from gadsqlalchemy import fetchcount
from gadsqlalchemy import fetchone
from sqlalchemy import BinaryExpression
from sqlalchemy import UnaryExpression
from sqlalchemy import select
from sqlalchemy.sql import asc
from sqlalchemy.sql import desc
from src.databases.postgres import tables
from src.databases.postgres.setup import Session

from .base import CRUD


class Dummy(CRUD):
    table = tables.Dummy

    @classmethod
    async def relations(cls, session: Session, **kwargs) -> tables.Dummy:
        query = select(cls.table).where(*cls.filters(kwargs))
        return await fetchone(session, query)

    @classmethod
    async def paginated(
        cls,
        session: Session,
        filters: dict,
        sorting: dict,
        pagination: dict,
    ) -> tuple[list[tables.Dummy], int]:
        def prepare_filters() -> list[BinaryExpression]:
            expressions = []

            if filters.get("name"):
                expressions.append(cls.table.name.ilike(f"%{filters['name']}%"))

            return expressions

        def prepare_sorting() -> list[UnaryExpression]:
            field = sorting.get("field")

            if field in ["id"]:
                expression = getattr(cls.table, field)
            else:
                expression = cls.table.id

            return (
                [desc(expression), desc(cls.table.id)]
                if sorting["type"] == "desc"
                else [asc(expression), desc(cls.table.id)]
            )

        def prepare_pagination() -> tuple[int, int]:
            return pagination.get("limit", 10), pagination.get("offset", 0)

        filters = prepare_filters()
        sorting = prepare_sorting()
        limit, offset = prepare_pagination()

        query = select(cls.table).where(*filters).order_by(*sorting)

        rows = await fetchall(session, query.limit(limit).offset(offset))
        total = await fetchcount(session, query)

        return rows, total
