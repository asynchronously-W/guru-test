from src.domain.exceptions.base import DomainError
from src.domain.value_objects.order_id import OrderId


class OrderNotFoundByIdError(DomainError):
    def __init__(self, order_id: OrderId) -> None:
        msg = f"Order '{order_id.value}' is not found."
        super().__init__(msg)