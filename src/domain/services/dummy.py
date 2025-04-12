from gadutils import strings

from src.databases.postgres import pgconnect
from src.domain import exceptions
from src.domain import models
from src.domain import repositories


class Dummy:
    @classmethod
    async def page(cls, dummy_id: int) -> models.Dummy:
        async with pgconnect() as session:
            return await repositories.Dummy.relations(session, id=dummy_id)

    @classmethod
    async def search(cls, filters: dict, sorting: dict, pagination: dict) -> tuple[list[models.Dummy], int]:
        async with pgconnect() as session:
            return await repositories.Dummy.paginated(session, filters, sorting, pagination)

    @classmethod
    async def create(cls, name: str) -> models.Dummy:
        async with pgconnect(transaction=True) as session:
            if await repositories.Dummy.exists(session, name=strings.lower(name)):
                raise exceptions.DummyAlreadyExistsError
            return await repositories.Dummy.create(session, model=models.Dummy.init(name=name))
