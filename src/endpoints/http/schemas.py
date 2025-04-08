from typing import Any, Self, Union

from pydantic import BaseModel, conint

from src.domain import models


class ID(BaseModel):
    id: Union[int, str]

    @classmethod
    def serialize(cls, item: models.Model) -> Self:
        return cls(id=item.id)


class Pagination(BaseModel):
    page: conint(gt=0, le=1000)
    size: conint(gt=0, le=100)

    @property
    def deserialize(self) -> dict:
        return dict(limit=self.size, offset=(self.page - 1) * self.size if self.page > 0 else 0)


class Paginated(BaseModel):
    total: int
    items: list[Any]
