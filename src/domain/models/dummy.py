from typing import Self

from src.utils import strings

from .base import Model


class Dummy(Model):
    id: int | None = None
    name: str

    @classmethod
    def init(cls, name: str) -> Self:
        return cls(name=strings.to_lower(name))
