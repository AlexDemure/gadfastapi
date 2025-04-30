from typing import Union

from gadutils import dates
from src.databases import ORM
from src.databases import ObjectNotFoundError
from src.databases import Session
from src.domain.models import Model


class Repository:
    orm: ORM
    model: Model
    error: Exception

    @classmethod
    async def id(cls, session: Session) -> int:
        return await cls.orm.id(session)

    @classmethod
    async def one(cls, session: Session, **kwargs) -> "Repository.model":
        try:
            row = await cls.orm.one(session, **kwargs)
        except ObjectNotFoundError:
            raise cls.error

        return cls.model.from_orm(row)

    @classmethod
    async def relations(cls, session: Session, **kwargs) -> "Repository.model":
        try:
            row = await cls.orm.relations(session, **kwargs)
        except ObjectNotFoundError:
            raise cls.error

        return cls.model.from_orm(row)

    @classmethod
    async def paginated(
        cls,
        session: Session,
        filters: dict,
        sorting: dict,
        pagination: dict,
    ) -> tuple[list["Repository.model"], int]:
        rows, total = await cls.orm.paginated(session, filters, sorting, pagination)
        return [cls.model.from_orm(row) for row in rows], total

    @classmethod
    async def all(cls, session: Session, **kwargs) -> list["Repository.model"]:
        rows = await cls.orm.all(session, **kwargs)
        return [cls.model.from_orm(row) for row in rows]

    @classmethod
    async def count(cls, session: Session, **kwargs) -> int:
        return await cls.orm.count(session, **kwargs)

    @classmethod
    async def exists(cls, session: Session, **kwargs) -> bool:
        return await cls.orm.exists(session, **kwargs)

    @classmethod
    async def create(cls, session: Session, model: Model) -> "Repository.model":
        row = await cls.orm.create(session, row=model.dict())
        return cls.model.from_orm(row)

    @classmethod
    async def update(cls, session: Session, id: Union[str, int], **kwargs) -> None:
        await cls.orm.update(session=session, id=id, updated_at=dates.now(), **kwargs)

    @classmethod
    async def delete(cls, session: Session, **kwargs) -> None:
        return await cls.orm.delete(session, **kwargs)
