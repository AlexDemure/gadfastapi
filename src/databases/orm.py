from typing import TypeVar, Union

from src.databases import postgres

ORM = TypeVar("ORM", bound=Union[postgres.CRUD])
