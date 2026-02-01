from src.domain.exceptions.base import DomainError
from src.domain.value_objects.product_id import ProductId


class ProductOutOfStockError(DomainError):
    def __init__(self, product_id: ProductId) -> None:
        msg = f"Product '{product_id.value}' is out of stock."
        super().__init__(msg)

class ProductNotFoundByIdError(DomainError):
    def __init__(self, product_id: ProductId) -> None:
        msg = f"Product '{product_id.value}' is not found."
        super().__init__(msg)