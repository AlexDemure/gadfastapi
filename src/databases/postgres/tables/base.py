import typing

from src.databases.postgres.setup import Table as _Table

Table = typing.TypeVar("Table", bound=_Table)
