import sqlalchemy as sa
from sqlalchemy.orm import composite

from src.domain.entities.order_line import OrderLine
from src.domain.value_objects.order_id import OrderId
from src.domain.value_objects.order_line_id import OrderLineId
from src.domain.value_objects.order_line_quantity import OrderLineQuantity
from src.domain.value_objects.product_id import ProductId
from src.domain.value_objects.product_name import ProductName
from src.infrastructure.persistence_sqla.registry import mapper_registry

order_lines_table = sa.Table(
    "order_lines",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
    sa.Column("quantity", sa.Integer(), nullable=False),
    sa.Column("order_id", sa.UUID(as_uuid=True), nullable=False),
    sa.Column("product_id", sa.UUID(as_uuid=True), nullable=False),
    sa.Column("product_name_snapshot", sa.String(ProductName.MAX_LEN), nullable=False),
)


def map_order_lines_table() -> None:
    mapper_registry.map_imperatively(
        OrderLine,
        order_lines_table,
        properties={
            "id_": composite(OrderLineId, order_lines_table.c.id),
            "quantity": composite(OrderLineQuantity, order_lines_table.c.quantity),
            "order_id": composite(OrderId, order_lines_table.c.order_id),
            "product_id": composite(ProductId, order_lines_table.c.product_id),
            "product_name_snapshot": composite(
                ProductName,
                order_lines_table.c.product_name_snapshot,
            ),
        },
        column_prefix="_",
    )
