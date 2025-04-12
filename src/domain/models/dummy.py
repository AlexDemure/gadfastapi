from typing import Self

from gadutils import strings

from .base import Model


class Dummy(Model):
    id: int | None = None
    name: str

    @classmethod
    def init(cls, name: str) -> Self:
        return cls(name=strings.lower(name))
