from dataclasses import dataclass

from src.domain.exceptions.base import DomainTypeError


@dataclass(frozen=True, slots=True)
class ProductStock:
    value: int

    def __post_init__(self) -> None:
        """:raises DomainTypeError:"""
        self._validate_stock_non_negative(self.value)

    def _validate_stock_non_negative(self, stock_value: int) -> None:
        """:raises DomainTypeError:"""
        if stock_value < 0:
            raise DomainTypeError(
                "Product stock value must be non-negative."
            )