from src.domain.entities.base import Entity
from src.domain.value_objects.client_address import ClientAddress
from src.domain.value_objects.client_id import ClientId
from src.domain.value_objects.client_name import ClientName


class Client(Entity[ClientId]):
    def __init__(
        self,
        id_: ClientId,
        name: ClientName | None,
        address: ClientAddress | None,
    ) -> None:
        super().__init__(id_)

        self.name = name
        self.address = address
