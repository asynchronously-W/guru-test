from dataclasses import dataclass

from src.domain.exceptions.base import DomainTypeError


@dataclass(frozen=True, slots=True)
class OrderLineQuantity:
    value: int

    def __post_init__(self) -> None:
        """:raises DomainTypeError:"""
        self._validate_greater_than_zero(self.value)

    def _validate_greater_than_zero(self, quantity_value: int) -> None:
        """:raises DomainTypeError:"""
        if quantity_value <= 0:
            raise DomainTypeError(
                "Quantity must be greater than 0."
            )