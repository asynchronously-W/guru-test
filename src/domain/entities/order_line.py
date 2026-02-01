from src.domain.entities.base import Entity
from src.domain.value_objects.order_id import OrderId
from src.domain.value_objects.order_line_id import OrderLineId
from src.domain.value_objects.order_line_quantity import OrderLineQuantity
from src.domain.value_objects.product_id import ProductId
from src.domain.value_objects.product_name import ProductName


class OrderLine(Entity[OrderLineId]):
    def __init__(
        self,
        id_: OrderLineId,
        quantity: OrderLineQuantity,
        order_id: OrderId,
        product_id: ProductId,
        product_name_snapshot: ProductName,
    ):
        super().__init__(id_=id_)

        self.quantity = quantity
        self.order_id = order_id
        self.product_id = product_id
        self.product_name_snapshot = product_name_snapshot