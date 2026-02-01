from src.domain.entities.customer import Customer
from src.domain.ports.customer_id_generator import CustomerIdGenerator
from src.domain.value_objects.customer_address import CustomerAddress
from src.domain.value_objects.customer_name import CustomerName


class CustomerService:
    def __init__(self, customer_id_generator: CustomerIdGenerator) -> None:
        self._customer_id_generator = customer_id_generator

    def create_customer(
        self,
        name: CustomerName | None,
        address: CustomerAddress | None,
    ) -> Customer:
        customer_id = self._customer_id_generator.generate()

        return Customer(
            id_=customer_id,
            name=name,
            address=address,
        )
