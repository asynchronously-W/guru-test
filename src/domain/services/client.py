from src.domain.entities.client import Client
from src.domain.ports.client_id_generator import ClientIdGenerator
from src.domain.value_objects.client_address import ClientAddress
from src.domain.value_objects.client_name import ClientName


class ClientService:
    def __init__(self, client_id_generator: ClientIdGenerator) -> None:
        self._client_id_generator = client_id_generator

    def create_client(
        self,
        name: ClientName | None,
        address: ClientAddress | None,
    ) -> Client:
        client_id = self._client_id_generator.generate()

        return Client(
            id_=client_id,
            name=name,
            address=address,
        )
