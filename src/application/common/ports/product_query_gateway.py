from abc import abstractmethod
from typing import Protocol

from src.domain.entities.product import Product
from src.domain.value_objects.product_id import ProductId


class ProductQueryGateway(Protocol):
    @abstractmethod
    async def read_by_id(self, product_id: ProductId) -> Product | None:
        """:raises ReaderError:"""
