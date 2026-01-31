from src.domain.entities.base import Entity
from src.domain.value_objects.customer_address import CustomerAddress
from src.domain.value_objects.customer_id import CustomerId
from src.domain.value_objects.customer_name import CustomerName


class Customer(Entity[CustomerId]):
    def __init__(
        self,
        id_: CustomerId,
        name: CustomerName | None,
        address: CustomerAddress | None,
    ) -> None:
        super().__init__(id_)

        self.name = name
        self.address = address
