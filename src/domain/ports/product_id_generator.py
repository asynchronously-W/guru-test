from abc import abstractmethod
from typing import Protocol

from src.domain.value_objects.product_id import ProductId


class ProductIdGenerator(Protocol):
    @abstractmethod
    def generate(self) -> ProductId:
        ...
