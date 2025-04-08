from typing import TypeVar, Union

from src.databases import postgres

Session = TypeVar("Session", bound=Union[postgres.Session])
