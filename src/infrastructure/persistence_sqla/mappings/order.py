import sqlalchemy as sa
from sqlalchemy.orm import composite

from src.domain.entities.order import Order
from src.domain.enums.order_status import OrderStatus
from src.domain.value_objects.customer_id import CustomerId
from src.domain.value_objects.order_id import OrderId
from src.domain.value_objects.order_total_price import OrderTotalPrice
from src.infrastructure.persistence_sqla.registry import mapper_registry

orders_table = sa.Table(
    "orders",
    mapper_registry.metadata,
    sa.Column("id", sa.Uuid(as_uuid=True), primary_key=True),
    sa.Column("customer_id", sa.Uuid(as_uuid=True), nullable=False),
    sa.Column("status", sa.Enum(OrderStatus), nullable=False),
    sa.Column("total_price", sa.Numeric(precision=12, scale=2), nullable=True),
)


def map_orders_table() -> None:
    mapper_registry.map_imperatively(
        Order,
        orders_table,
        properties={
            "id_": composite(OrderId, orders_table.c.id),
            "customer_id": composite(CustomerId, orders_table.c.customer_id),
            "status": orders_table.c.status,
            "total_price": composite(OrderTotalPrice, orders_table.c.total_price),
        },
        column_prefix="_",
    )
