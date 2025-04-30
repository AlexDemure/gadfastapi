from typing import TypeVar
from typing import Union

from src.databases import postgres

Table = TypeVar("Table", bound=Union[postgres.Table])
