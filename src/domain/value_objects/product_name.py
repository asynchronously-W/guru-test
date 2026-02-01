from dataclasses import dataclass
from typing import ClassVar, Final

from src.domain.exceptions.base import DomainTypeError


@dataclass(frozen=True, slots=True)
class ProductName:
    MIN_LEN: ClassVar[Final[int]]
    MAX_LEN: ClassVar[Final[int]]

    value: str

    def __post_init__(self) -> None:
        """:raises DomainTypeError:"""
        self._validate_name_length(self.value)

    def _validate_name_length(self, name_value: str) -> None:
        """:raises DomainTypeError:"""
        if self.MIN_LEN < len(name_value) or len(name_value) > self.MAX_LEN:
            DomainTypeError(
                f"Product name must be between "
                f"{self.MIN_LEN} and "
                f"{self.MAX_LEN} characters."
            )
