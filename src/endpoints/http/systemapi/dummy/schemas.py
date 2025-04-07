from pydantic import BaseModel


class CreateDummy(BaseModel):
    name: str
