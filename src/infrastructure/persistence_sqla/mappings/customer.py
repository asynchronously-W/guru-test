import sqlalchemy as sa
from sqlalchemy.orm import composite

from src.domain.entities.customer import Customer
from src.domain.value_objects.customer_address import CustomerAddress
from src.domain.value_objects.customer_id import CustomerId
from src.domain.value_objects.customer_name import CustomerName
from src.infrastructure.registry import mapper_registry

customers_table = sa.Table(
    "customers",
    mapper_registry.metadata,
    sa.Column("id", sa.Uuid(as_uuid=True), primary_key=True),
    sa.Column("name", sa.String(CustomerName.MAX_LEN), nullable=True),
    sa.Column("address", sa.String(CustomerAddress.MAX_LEN), nullable=True)
)

def map_customers_table() -> None:
    mapper_registry.map_imperatively(
        Customer,
        customers_table,
        properties={
            "id_": composite(CustomerId, customers_table.c.id),
            "name": composite(CustomerName, customers_table.c.name),
            "address": composite(CustomerAddress, customers_table.c.address),
        },
        column_prefix="_",
    )
