from fastapi import APIRouter

from src.presentation.http.controllers.order.supplement_order import create_supplement_order_router


def create_orders_router() -> APIRouter:
    router = APIRouter(prefix="/orders", tags=["Orders"])
    router.include_router(create_supplement_order_router())
    return router
