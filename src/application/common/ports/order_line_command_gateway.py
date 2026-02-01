from abc import abstractmethod
from typing import Protocol

from src.domain.entities.order_line import OrderLine
from src.domain.value_objects.order_id import OrderId
from src.domain.value_objects.product_id import ProductId


class OrderLineCommandGateway(Protocol):
    @abstractmethod
    def add(self, order_line: OrderLine) -> None:
        """:raises DataMapperError:"""

    @abstractmethod
    async def read_by_order_and_product(
        self,
        order_id: OrderId,
        product_id: ProductId,
        for_update: bool,
    ) -> OrderLine | None:
        """:raises DataMapperError:"""
