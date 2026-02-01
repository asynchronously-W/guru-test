from fastapi import APIRouter

from src.presentation.http.controllers.general.router import create_general_router
from src.presentation.http.controllers.order.router import create_orders_router


def create_api_v1_router() -> APIRouter:
    router = APIRouter(prefix="/api/v1")
    router.include_router(create_general_router())
    router.include_router(create_orders_router())
    return router
