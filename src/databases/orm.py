import typing

from src.databases import postgres

ORM = typing.TypeVar("ORM", bound=typing.Union[postgres.CRUD])
