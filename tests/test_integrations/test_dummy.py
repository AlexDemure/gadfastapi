import asyncio
import time

import pytest
from gadpytestprofiler import AsyncFunctionProfiler
from gadpytestprofiler import FunctionProfiler
from gadpytestprofiler import SqlalchemyProfiler
from sqlalchemy import select
from src.databases.postgres.tables import Dummy


def timesleep():
    time.sleep(1)


async def aiotimesleep():
    await asyncio.sleep(1)


@pytest.mark.asyncio
async def test_query_performance(session):
    query = select(Dummy)

    rows, results = await SqlalchemyProfiler(session, query, runs=1).analyze()
    print(len(rows))

    print(results.json())

    _, results = FunctionProfiler(timesleep).analyze()
    print(results.json())

    _, results = await AsyncFunctionProfiler(aiotimesleep).analyze()
    print(results.json())
