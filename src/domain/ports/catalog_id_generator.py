from abc import abstractmethod
from typing import Protocol

from src.domain.value_objects.catalog_id import CatalogId


class CatalogIdGenerator(Protocol):
    @abstractmethod
    def generate(self) -> CatalogId:
        ...