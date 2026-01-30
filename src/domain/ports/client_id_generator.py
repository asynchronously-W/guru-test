from abc import abstractmethod
from typing import Protocol

from src.domain.value_objects.client_id import ClientId


class ClientIdGenerator(Protocol):
    @abstractmethod
    def generate(self) -> ClientId:
        ...
    