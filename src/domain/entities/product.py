from src.domain.entities.base import Entity
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
    ) -> None:
        super().__init__(id_)

        self.name = name
        self.stock = stock
        self.price = price