from typing import TypeVar

from src.databases.postgres.setup import Table as _Table

Table = TypeVar("Table", bound=_Table)
