from src.databases import postgres
from src.domain import exceptions, models

from .base import Repository


class Dummy(Repository):
    orm = postgres.Dummy
    model = models.Dummy
    error = exceptions.DummyNotFoundError
