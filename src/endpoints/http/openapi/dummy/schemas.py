from typing import Literal
from typing import Self

from pydantic import BaseModel
from pydantic import constr

from src.domain import models
from src.endpoints.http.schemas import Paginated
from src.endpoints.http.schemas import Pagination


class Dummy(BaseModel):
    id: int
    name: str

    @classmethod
    def serialize(cls, model: models.Dummy) -> Self:
        return cls(id=model.id, name=model.name)


class Dummies(Paginated):
    items: list[Dummy]

    @classmethod
    def serialize(cls, models: list[models.Dummy], total: int) -> Self:
        return cls(items=[Dummy.serialize(model) for model in models], total=total)


class Search(BaseModel):
    class Filter(BaseModel):
        name: constr(to_lower=True, min_length=1, max_length=256, strip_whitespace=True) | None

    class Sorting(BaseModel):
        field: Literal["id"]
        type: Literal["asc", "desc"]

    filters: Filter
    sorting: Sorting
    pagination: Pagination

    def deserialize(self) -> dict:
        return dict(
            filters=dict(self.filters),
            sorting=dict(self.sorting),
            pagination=self.pagination.deserialize,
        )
