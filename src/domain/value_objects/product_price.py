from dataclasses import dataclass
from decimal import Decimal

from src.domain.exceptions.base import DomainTypeError


@dataclass(frozen=True, slots=True)
class ProductPrice:
    value: Decimal

    def __post_init__(self) -> None:
        """:raises DomainTypeError:"""
        self._validate_price_value_non_negative(self.value)

    def _validate_price_value_non_negative(self, price_value: Decimal) -> None:
        """:raises DomainTypeError:"""

        if price_value < 0:
            raise DomainTypeError(
                "Product price must be non-negative value."
            )
