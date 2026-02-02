from src.domain.entities.order import Order
from src.domain.enums.order_status import OrderStatus
from src.domain.exceptions.order import OrderPlaceIsNotPermittedError
from src.domain.ports.clock import Clock
from src.domain.ports.order_id_generator import OrderIdGenerator
from src.domain.value_objects.customer_id import CustomerId
from src.domain.value_objects.order_total_price import OrderTotalPrice


class OrderService:
    def __init__(self, order_id_generator: OrderIdGenerator, clock: Clock) -> None:
        self._order_id_generator = order_id_generator
        self._clock = clock

    def create_order(
        self,
        customer_id: CustomerId,
        status: OrderStatus,
        total_price: OrderTotalPrice | None,
    ) -> Order:
        order_id = self._order_id_generator.generate()

        return Order(
            id_=order_id,
            customer_id=customer_id,
            status=status,
            total_price=total_price,
            created_at=self._clock.now()
        )

    def place_order(self, order: Order, total_price: OrderTotalPrice) -> None:
        if order.status != OrderStatus.DRAFT:
            raise OrderPlaceIsNotPermittedError(order.id_)

        order.total_price = total_price