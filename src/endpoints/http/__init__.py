from src.endpoints.http.openapi import router as openapi
from src.endpoints.http.systemapi import router as systemapi
from src.tools.fastapi import APIRouter

router = APIRouter(prefix="/api")

router.include_router(openapi)
router.include_router(systemapi, prefix="/-")
