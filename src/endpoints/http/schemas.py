import typing

import pydantic

from src.domain import models


class ID(pydantic.BaseModel):
    id: typing.Union[int, str]

    @classmethod
    def serialize(cls, item: models.Model) -> typing.Self:
        return cls(id=item.id)


class Pagination(pydantic.BaseModel):
    page: pydantic.conint(gt=0, le=1000)
    size: pydantic.conint(gt=0, le=100)

    @property
    def deserialize(self) -> dict:
        return dict(limit=self.size, offset=(self.page - 1) * self.size if self.page > 0 else 0)


class Paginated(pydantic.BaseModel):
    total: int
    items: typing.List[typing.Any]
