from typing import Annotated
from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi.params import Path
from fastapi_error_map import ErrorAwareRouter, rule
from pydantic import BaseModel
from starlette import status

from src.application.commands.supplement_order import (
    SupplementOrderResponse,
    SupplementOrderCommand,
    SupplementOrderRequest,
)
from src.domain.exceptions.base import DomainTypeError
from src.domain.exceptions.order import OrderNotFoundByIdError
from src.domain.exceptions.product import ProductOutOfStockError, ProductNotFoundByIdError
from src.infrastructure.exceptions.gateway import DataMapperError, ReaderError
from src.presentation.http.errors.callbacks import log_error, log_info
from src.presentation.http.errors.translators import ServiceUnavailableTranslator


class SupplementOrderRequestPydantic(BaseModel):
    product_id: UUID
    quantity: int

def create_supplement_order_router() -> ErrorAwareRouter:
    router = ErrorAwareRouter()

    @router.post(
        "/{order_id}/items",
        error_map={
            DataMapperError: rule(
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
                translator=ServiceUnavailableTranslator(),
                on_error=log_error,
            ),
            ReaderError: rule(
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
                translator=ServiceUnavailableTranslator(),
                on_error=log_error,
            ),
            DomainTypeError: status.HTTP_400_BAD_REQUEST,
            OrderNotFoundByIdError: status.HTTP_404_NOT_FOUND,
            ProductNotFoundByIdError: status.HTTP_404_NOT_FOUND,
            ProductOutOfStockError: status.HTTP_409_CONFLICT,
        },
        default_on_error=log_info,
        status_code=status.HTTP_200_OK,
    )
    @inject
    async def supplement_order(
        order_id: Annotated[UUID, Path()],
        request_data_pydantic: SupplementOrderRequestPydantic,
        interactor: FromDishka[SupplementOrderCommand],
    ) -> SupplementOrderResponse:
        request_data = SupplementOrderRequest(
            order_id=order_id,
            product_id=request_data_pydantic.product_id,
            quantity=request_data_pydantic.quantity
        )

        return await interactor.execute(request_data=request_data)

    return router