from abc import abstractmethod
from typing import Protocol

from src.domain.value_objects.nomenclature_id import NomenclatureId


class NomenclatureIdGenerator(Protocol):
    @abstractmethod
    def generate(self) -> NomenclatureId:
        ...
