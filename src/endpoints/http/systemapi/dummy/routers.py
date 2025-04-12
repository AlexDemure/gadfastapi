from fastapi import Body
from fastapi import status
from gadfastopenapi.extensions.errors import openapi_errors

from src.domain import exceptions
from src.domain import services
from src.endpoints.http.const import tags
from src.endpoints.http.schemas import ID
from src.tools.fastapi import APIRouter

from .schemas import CreateDummy

router = APIRouter()


@router.post(
    "/dummy",
    summary=tags.SYSTEMAPI,
    status_code=status.HTTP_201_CREATED,
    response_model=ID,
    responses=openapi_errors(exceptions.DummyAlreadyExistsError),
)
async def create(body: CreateDummy = Body(...)) -> ID:
    dummy = await services.Dummy.create(**body.model_dump())
    return ID.serialize(dummy)
