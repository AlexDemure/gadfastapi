from fastapi import Body
from fastapi import Path
from fastapi import status
from gadfastopenapi.extensions.errors import openapi_errors

from src.domain import exceptions
from src.domain import services
from src.endpoints.http.const import tags
from src.tools.fastapi import APIRouter

from .schemas import Dummies
from .schemas import Dummy
from .schemas import Search

router = APIRouter()


@router.get(
    "/dummy:id",
    summary=tags.OPENAPI,
    status_code=status.HTTP_200_OK,
    response_model=int,
)
async def id() -> int:
    return await services.Dummy.id()


@router.get(
    "/dummy:{id:int}",
    summary=tags.OPENAPI,
    status_code=status.HTTP_200_OK,
    response_model=Dummy,
    responses=openapi_errors(exceptions.DummyNotFoundError),
)
async def page(dummy_id: int = Path(..., ge=1, alias="id")) -> Dummy:
    dummy = await services.Dummy.page(dummy_id)
    return Dummy.serialize(dummy)


@router.post(
    "/dummy:search",
    summary=tags.OPENAPI,
    status_code=status.HTTP_200_OK,
    response_model=Dummies,
)
async def search(body: Search = Body(...)) -> Dummies:
    dummies, total = await services.Dummy.search(**body.deserialize())
    return Dummies.serialize(dummies, total)
