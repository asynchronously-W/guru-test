from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from dishka import make_async_container, AsyncContainer
from fastapi import FastAPI

from src.infrastructure.persistence_sqla.mappings.all import map_tables
from src.presentation.http.controllers.root_router import create_root_router
from src.setup.config.settings import AppSettings
from src.setup.ioc.registry import get_providers

def create_ioc_container(settings: AppSettings) -> AsyncContainer:
    return make_async_container(
        *get_providers(),
        context={AppSettings: settings},
    )

def create_web_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
    )

    app.include_router(create_root_router())

    return app

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    container = app.state.dishka_container
    try:
        map_tables()
        yield
    finally:
        await container.close()
