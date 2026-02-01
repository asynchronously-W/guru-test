import sqlalchemy as sa
from sqlalchemy.orm import composite

from src.domain.entities.catalog import Catalog
from src.domain.value_objects.catalog_id import CatalogId
from src.domain.value_objects.catalog_name import CatalogName
from src.infrastructure.persistence_sqla.registry import mapper_registry

catalogs_table = sa.Table(
    "catalogs",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
    sa.Column("name", sa.String(CatalogName.MAX_LEN), nullable=False),
    sa.Column("parent_id", sa.UUID(as_uuid=True), nullable=True),
)


def map_catalogs_table() -> None:
    mapper_registry.map_imperatively(
        Catalog,
        catalogs_table,
        properties={
            "id_": composite(CatalogId, catalogs_table.c.id),
            "name": composite(CatalogName, catalogs_table.c.name),
            "parent_id": composite(CatalogId, catalogs_table.c.parent_id),
        },
        column_prefix="_",
    )
