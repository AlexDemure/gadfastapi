import contextlib
import functools
import json
import logging
import typing

from fastapi import APIRouter as _APIRouter
from fastapi import Request
from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi.exceptions import ValidationException
from fastapi.routing import APIRoute as _APIRoute
from gadify import dates
from starlette.responses import Response

logger = logging.getLogger("fastapi.route")


class Logging:
    REQUEST_MAX_LENGTH = 16384
    RESPONSE_MAX_LENGTH = 65536

    def __init__(self, request: Request):
        self.context = self.init_context(request)

    @classmethod
    def init_context(cls, request: Request) -> dict:
        headers = dict(request.headers.items())

        hidden_headers = [
            "authorization",
        ]

        for key in hidden_headers:
            if headers.get(key, None):
                headers[key] = "*"

        return {
            "debug": request.app.debug,
            "service": request.app.title,
            "version": request.app.version,
            "http-version": request.scope.get("http_version", None),
            "ip": f"{request.client.host}:{request.client.port}",
            "method": request.method.upper(),
            "url": str(request.url),
            "headers": headers,
            "query": dict(request.query_params),
            "body": {},
            "response": {},
            "code": None,
            "started": dates.now(),
            "ended": None,
            "elapsed": None,
        }

    @property
    def endpoint(self) -> str:
        return f"{self.context['method']} {self.context['url']}"

    def timing(self):
        self.context["ended"] = dates.now()
        self.context["elapsed"] = (self.context["ended"] - self.context["started"]).total_seconds()

    def accepted(self) -> None:
        _logger = logger.warning if self.context.get("body") == "-" else logger.info
        _logger(f"Request accepted: {self.endpoint}", extra=self.context)

    def processed(self) -> None:
        _logger = logger.warning if self.context.get("response") == "-" else logger.info
        _logger(f"Request processed: {self.endpoint}", extra=self.context)

    def error(self) -> None:
        logger.error(f"Request error: {self.endpoint}", extra=self.context, exc_info=True)


class JSON:
    @classmethod
    def parseresponse(cls, response: Response):
        with contextlib.suppress(json.JSONDecodeError):
            return json.loads(response.body.decode("utf-8").replace("\n", ""))
        return response.body

    @classmethod
    async def parsebody(cls, request: Request):
        body = await request.body()
        with contextlib.suppress(json.JSONDecodeError):
            return json.loads(body.decode("utf-8").replace("\n", ""))
        return body


class APIRoute(_APIRoute):
    def get_route_handler(self) -> typing.Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            if route := request.scope.get("route", None):  # noqa:SIM102
                if exclude_paths := getattr(request.app, "routing_exclude_paths", None):  # noqa:SIM102
                    if route.path_format in exclude_paths:
                        return await original_route_handler(request)

            log = Logging(request)

            if request.headers.get("Content-Type") == "application/json":
                with contextlib.suppress(ValueError):
                    log.context["body"] = (
                        await JSON.parsebody(request)
                        if int(request.headers.get("Content-Length", 0)) < log.REQUEST_MAX_LENGTH
                        else "-"
                    )

            log.accepted()

            try:
                response: Response = await original_route_handler(request)
                log.context["code"] = response.status_code
            except HTTPException as e:
                log.context["code"] = e.status_code
                log.context["response"] = e.detail
                log.timing()
                log.processed()
                raise e
            except ValidationException as e:
                log.context["code"] = status.HTTP_422_UNPROCESSABLE_ENTITY
                log.context["response"] = str(e)
                log.timing()
                log.processed()
                raise e
            except Exception as e:
                log.context["code"] = status.HTTP_500_INTERNAL_SERVER_ERROR
                log.timing()
                log.error()
                raise e

            if response.headers.get("Content-Type") == "application/json":
                log.context["response"] = (
                    JSON.parseresponse(response) if len(response.body) < log.RESPONSE_MAX_LENGTH else "-"
                )

            log.timing()
            log.processed()

            return response

        return custom_route_handler


APIRouter = functools.partial(_APIRouter, route_class=APIRoute)
