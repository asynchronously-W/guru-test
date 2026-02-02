from dataclasses import dataclass
from decimal import Decimal

from src.domain.exceptions.base import DomainTypeError


@dataclass(frozen=True, slots=True)
class OrderTotalPrice:
    value: Decimal

    def __new__(cls, value: Decimal | None) -> OrderTotalPrice | None:
        if value is None:
            return None
        
        return super().__new__(cls)

    def __post_init__(self) -> None:
        """:raises DomainTypeError:"""
        self._validate_total_price_non_negative(self.value)

    def _validate_total_price_non_negative(self, total_price_value: Decimal) -> None:
        """:raises DomainTypeError:"""

        if total_price_value < 0:
            raise DomainTypeError(
                "Order total price must be non-negative value."
            )