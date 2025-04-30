import pytest
from src.framework import settings
from tests.factories.tables import Dummy


@pytest.fixture(scope="package", autouse=True)
def dsn() -> str:
    return settings.POSTGRES_URL


@pytest.fixture(scope="package", autouse=True)
def tables() -> list:
    return [Dummy]


@pytest.fixture(scope="package", autouse=True)
async def initdb(scopesession):
    for i in range(10000):
        Dummy()
