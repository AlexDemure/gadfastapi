from typing import TypeVar
from typing import Union

from src.databases import postgres

Session = TypeVar("Session", bound=Union[postgres.Session])
