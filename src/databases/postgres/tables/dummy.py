from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy import String

from .base import Base


class Dummy(Base):
    __tablename__ = "dummy"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(), nullable=False)
