from fastapi import APIRouter

from .dummy import router as dummy_router

router = APIRouter()

router.include_router(dummy_router, tags=["Dummy"])
