from src.domain.entities.base import Entity
from src.domain.value_objects.catalog_id import CatalogId
from src.domain.value_objects.catalog_name import CatalogName


class Catalog(Entity[CatalogId]):
    def __init__(
        self,
        id_: CatalogId,
        name: CatalogName,
        parent_id: CatalogId | None,
    ):
        super().__init__(id_)
        self.name = name
        self.parent_id = parent_id
