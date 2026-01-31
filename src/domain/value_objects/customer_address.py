from dataclasses import dataclass
from typing import ClassVar, Final

from src.domain.exceptions.base import DomainTypeError


@dataclass(frozen=True, slots=True)
class CustomerAddress:
    MIN_LEN: ClassVar[Final[int]] = 10
    MAX_LEN: ClassVar[Final[int]] = 255

    value: str

    def __post_init__(self) -> None:
        """:raises: DomainTypeError"""
        self._validate_address_length(self.value)

    def _validate_address_length(self, address_value: str) -> None:
        """:raises DomainTypeError:"""
        if self.MIN_LEN < len(address_value) or len(address_value) > self.MAX_LEN:
            raise DomainTypeError(
                "Address must be between"
                f"{self.MIN_LEN} and"
                f"{self.MAX_LEN} characters."
            )