from typing import TypeVar
from typing import Union

from src.databases import postgres

ORM = TypeVar("ORM", bound=Union[postgres.CRUD])
