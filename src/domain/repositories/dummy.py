from src.databases import postgres
from src.domain import exceptions
from src.domain import models

from .base import Repository


class Dummy(Repository):
    orm = postgres.Dummy
    model = models.Dummy
    error = exceptions.DummyNotFoundError
