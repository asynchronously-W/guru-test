from fastapi import APIRouter

from src.presentation.http.controllers.general.healthcheck import (
    create_healthcheck_router,
)


def create_general_router() -> APIRouter:
    router = APIRouter()
    router.include_router(create_healthcheck_router())
    return router
