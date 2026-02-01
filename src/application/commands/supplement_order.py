from dataclasses import dataclass
from typing import TypedDict
from uuid import UUID

from src.application.common.ports.order_line_command_gateway import (
    OrderLineCommandGateway,
)
from src.application.common.ports.order_query_gateway import OrderQueryGateway
from src.application.common.ports.product_query_gateway import ProductQueryGateway
from src.application.common.ports.transaction_manager import TransactionManager
from src.domain.exceptions.order import OrderNotFoundByIdError
from src.domain.exceptions.product import ProductOutOfStockError, ProductNotFoundByIdError
from src.domain.services.order_line import OrderLineService
from src.domain.value_objects.order_id import OrderId
from src.domain.value_objects.order_line_quantity import OrderLineQuantity
from src.domain.value_objects.product_id import ProductId


@dataclass
class SupplementOrderRequest:
    order_id: UUID
    product_id: UUID
    quantity: int


class SupplementOrderResponse(TypedDict):
    order_id: UUID


class SupplementOrderCommand:
    def __init__(
        self,
        order_query_gateway: OrderQueryGateway,
        product_query_gateway: ProductQueryGateway,
        order_line_command_gateway: OrderLineCommandGateway,
        order_line_service: OrderLineService,
        transaction_manager: TransactionManager,
    ) -> None:
        self._order_query_gateway = order_query_gateway
        self._product_query_gateway = product_query_gateway
        self._order_line_command_gateway = order_line_command_gateway
        self._order_line_service = order_line_service
        self._transaction_manager = transaction_manager

    async def execute(self, request_data: SupplementOrderRequest) -> SupplementOrderResponse:
        """
        :raises DataMapperError:
        :raises ReaderError:
        :raises DomainTypeError:
        :raises OrderNotFoundByIdError:
        :raises ProductNotFoundByIdError:
        :raises ProductOutOfStockError:
        """
        order_id = OrderId(request_data.order_id)
        product_id = ProductId(request_data.product_id)
        supplement_quantity = OrderLineQuantity(request_data.quantity)

        order = await self._order_query_gateway.read_by_id(order_id)

        if not order:
            raise OrderNotFoundByIdError(order_id)

        product = await self._product_query_gateway.read_by_id(product_id)

        if not product:
            raise ProductNotFoundByIdError(product_id)

        order_line = await self._order_line_command_gateway.read_by_order_and_product(
            order_id=order_id,
            product_id=product_id,
            for_update=True,
        )

        current_quantity_value = order_line.quantity.value if order_line else 0
        total_quantity_value = current_quantity_value + supplement_quantity.value

        if product.stock.value < total_quantity_value:
            raise ProductOutOfStockError(product.id_)

        if order_line:
            self._order_line_service.change_quantity(
                order_line,
                OrderLineQuantity(total_quantity_value),
            )
        else:
            new_order_line = self._order_line_service.create_order_line(
                quantity=supplement_quantity,
                order_id=order.id_,
                product_id=product.id_,
                product_name_snapshot=product.name,
            )
            self._order_line_command_gateway.add(new_order_line)

        await self._transaction_manager.commit()

        return SupplementOrderResponse(
            order_id=request_data.order_id
        )
