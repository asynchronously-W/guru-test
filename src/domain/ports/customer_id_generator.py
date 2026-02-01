from abc import abstractmethod
from typing import Protocol

from src.domain.value_objects.customer_id import CustomerId


class CustomerIdGenerator(Protocol):
    @abstractmethod
    def generate(self) -> CustomerId:
        ...
    