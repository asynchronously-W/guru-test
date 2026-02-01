from abc import abstractmethod
from typing import Protocol

from src.domain.entities.order import Order
from src.domain.value_objects.order_id import OrderId


class OrderQueryGateway(Protocol):
    @abstractmethod
    async def read_by_id(self, order_id: OrderId) -> Order | None:
        """:raises ReaderError:"""
