from src.domain.entities.base import Entity
from src.domain.value_objects.catalog_id import CatalogId
from src.domain.value_objects.product_id import ProductId
from src.domain.value_objects.product_name import ProductName
from src.domain.value_objects.product_price import ProductPrice
from src.domain.value_objects.product_stock import ProductStock


class Product(Entity[ProductId]):
    def __init__(
        self,
        id_: ProductId,
        name: ProductName,
        stock: ProductStock,
        price: ProductPrice,
        catalog_id: CatalogId | None,
    ) -> None:
        super().__init__(id_)

        self.name = name
        self.stock = stock
        self.price = price
        self.catalog_id = catalog_id