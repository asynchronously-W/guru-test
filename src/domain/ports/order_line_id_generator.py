from abc import abstractmethod
from typing import Protocol

from src.domain.value_objects.order_line_id import OrderLineId


class OrderLineIdGenerator(Protocol):
    @abstractmethod
    def generate(self) -> OrderLineId:
        ...