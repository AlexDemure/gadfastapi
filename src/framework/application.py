import contextlib

import fastapi.routing
from gadfastrouter import APIRoute
from gadfastrouter import APIRouter

fastapi.APIRouter = APIRouter
fastapi.routing.APIRoute = APIRoute

from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from gadfastopenapi import OpenAPI
from gadfastopenapi.extensions.affix import affix
from gadfastopenapi.extensions.errors import APIError
from gadfastopenapi.extensions.operationid import use_route_as_operation_id
from src.endpoints.http import router
from src.storages import etcd

from .asyncio import detector
from .cron import cron
from .health import health


@contextlib.asynccontextmanager
async def lifespan(_: FastAPI):
    detector.start()
    cron.start()
    yield
    cron.shutdown()
    detector.shutdown()


app = FastAPI(
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
    debug=True,
)


@app.get("/api/docs", include_in_schema=False)
async def swagger():
    return get_swagger_ui_html(openapi_url="/api/openapi.json", title=app.title)


@app.get("/api/redoc", include_in_schema=False)
async def redoc():
    return get_redoc_html(openapi_url="/api/openapi.json", title=app.title)


@app.get("/api/openapi.json", include_in_schema=False)
async def openapi():
    return OpenAPI(app, handlers=[affix, use_route_as_operation_id]).generate()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)

app.include_router(etcd.router)

app.include_router(router)

app.exclude_paths = []  # fastapi.routing.py

app.mount("/api/static", StaticFiles(directory="src/static"), name="static")


@app.exception_handler(APIError)
async def error_handler(_: Request, error: APIError) -> JSONResponse:
    return JSONResponse(status_code=error.status_code, content=error.to_dict())
