from src.domain.entities.base import Entity
from src.domain.value_objects.order_id import OrderId


class Order(Entity[OrderId]):
    def __init__(self, id_: OrderId, ) -> None:
        super().__init__(id_)