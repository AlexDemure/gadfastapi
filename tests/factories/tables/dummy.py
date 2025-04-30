from gadsqlalchemy.testing import Table
from src.databases.postgres import tables
from tests.faker import fake


class Dummy(Table):
    class Meta:
        model = tables.Dummy

    name = fake.name()
