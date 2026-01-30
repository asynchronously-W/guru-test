from src.domain.ports.order_id_generator import OrderIdGenerator


class OrderService:
    def __init__(self, order_id_generator: OrderIdGenerator) -> None:
        self._order_id_generator = order_id_generator

    