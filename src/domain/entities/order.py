from src.domain.entities.base import Entity
from src.domain.enums.order_status import OrderStatus
from src.domain.value_objects.customer_id import CustomerId
from src.domain.value_objects.order_id import OrderId
from src.domain.value_objects.order_total_price import OrderTotalPrice


class Order(Entity[OrderId]):
    def __init__(self, id_: OrderId, client_id: CustomerId, status: OrderStatus, total_price: OrderTotalPrice) -> None:
        super().__init__(id_)

        self.client_id = client_id
        self.status = status
        self.total_price = total_price
