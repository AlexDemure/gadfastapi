import typing

from src.databases import postgres

Session = typing.TypeVar("Session", bound=typing.Union[postgres.Session])
