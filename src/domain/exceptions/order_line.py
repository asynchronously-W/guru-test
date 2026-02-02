from src.domain.exceptions.base import DomainError
from src.domain.value_objects.order_line_id import OrderLineId


class QuantityChangeIsNotPermitted(DomainError):
    def __init__(self, order_line_id: OrderLineId) -> None:
        msg = f"Order line '{order_line_id.value}' quantity change is not permitted."
        super().__init__(msg)