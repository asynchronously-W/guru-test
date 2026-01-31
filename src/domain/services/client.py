from src.domain.entities.customer import Customer
from src.domain.ports.customer_id_generator import ClientIdGenerator
from src.domain.value_objects.customer_address import CustomerAddress
from src.domain.value_objects.customer_name import CustomerName


class ClientService:
    def __init__(self, client_id_generator: ClientIdGenerator) -> None:
        self._client_id_generator = client_id_generator

    def create_client(
        self,
        name: CustomerName | None,
        address: CustomerAddress | None,
    ) -> Customer:
        client_id = self._client_id_generator.generate()

        return Customer(
            id_=client_id,
            name=name,
            address=address,
        )
