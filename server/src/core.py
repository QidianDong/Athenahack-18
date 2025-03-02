from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Generator, Optional, Self

import asyncpg
from celery import Celery
from fastapi import Depends, FastAPI, status
from fastapi.openapi.utils import get_openapi
from fastapi.responses import ORJSONResponse

if TYPE_CHECKING:
    from utils.config import ServerConfig


__title__ = "py-rest-templte"
__description__ = "Performance-driven FastAPI template for MLH Hackathons"
__version__ = "0.1.0a"


class Server(FastAPI):
    pool: asyncpg.Pool

    def __init__(
        self,
        *,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        celery: Celery,
        config: ServerConfig,
    ):
        self.loop: asyncio.AbstractEventLoop = (
            loop or asyncio.get_event_loop_policy().get_event_loop()
        )
        super().__init__(
            title=__title__,
            description=__description__,
            version=__version__,
            dependencies=[Depends(self.get_db)],
            default_response_class=ORJSONResponse,
            loop=self.loop,
            redoc_url="/docs",
            docs_url=None,
            lifespan=self.lifespan,
        )
        self.config = config
        self.celery = celery

    async def send_task(self, name: str, collect: bool = False, *args):
        result = await self.loop.run_in_executor(
            None, self.celery.send_task, name, args
        )

        if collect:
            return [item for item in result.collect()]
        return result.get()

    ### Server-related utilities

    @asynccontextmanager
    async def lifespan(self, app: Self):
        async with asyncpg.create_pool(dsn=self.config["postgres_uri"]) as app.pool:
            yield

    def get_db(self) -> Generator[asyncpg.Pool, None, None]:
        yield self.pool

    def openapi(self) -> dict[str, Any]:
        if not self.openapi_schema:
            self.openapi_schema = get_openapi(
                title=self.title,
                version=self.version,
                openapi_version=self.openapi_version,
                description=self.description,
                terms_of_service=self.terms_of_service,
                contact=self.contact,
                license_info=self.license_info,
                routes=self.routes,
                tags=self.openapi_tags,
                servers=self.servers,
            )
            for path in self.openapi_schema["paths"].values():
                for method in path.values():
                    responses = method.get("responses")
                    if str(status.HTTP_422_UNPROCESSABLE_ENTITY) in responses:
                        del responses[str(status.HTTP_422_UNPROCESSABLE_ENTITY)]
        return self.openapi_schema
