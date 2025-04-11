from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy import String

from src.databases.postgres.setup import Table


class Dummy(Table):
    __tablename__ = "city"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(), nullable=False)
