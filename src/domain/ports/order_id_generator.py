from abc import abstractmethod
from typing import Protocol

from src.domain.value_objects.order_id import OrderId


class OrderIdGenerator(Protocol):
    @abstractmethod
    def generate(self) -> OrderId:
        ...