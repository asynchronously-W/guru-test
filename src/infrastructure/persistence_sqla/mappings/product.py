import sqlalchemy as sa
from sqlalchemy.orm import composite

from src.domain.entities.product import Product
from src.domain.value_objects.catalog_id import CatalogId
from src.domain.value_objects.product_id import ProductId
from src.domain.value_objects.product_name import ProductName
from src.domain.value_objects.product_price import ProductPrice
from src.domain.value_objects.product_stock import ProductStock
from src.infrastructure.persistence_sqla.registry import mapper_registry

products_table = sa.Table(
    "products",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
    sa.Column("name", sa.String(ProductName.MAX_LEN), nullable=False),
    sa.Column("stock", sa.Integer(), nullable=False),
    sa.Column("price", sa.Numeric(precision=12, scale=2), nullable=False),
    sa.Column("catalog_id", sa.UUID(as_uuid=True), nullable=True)
)


def map_products_table() -> None:
    mapper_registry.map_imperatively(
        Product,
        products_table,
        properties={
            "id_": composite(ProductId, products_table.c.id),
            "name": composite(ProductName, products_table.c.name),
            "stock": composite(ProductStock, products_table.c.stock),
            "price": composite(ProductPrice, products_table.c.price),
            "catalog_id": composite(CatalogId, products_table.c.catalog_id)
        },
        column_prefix="_",
    )
