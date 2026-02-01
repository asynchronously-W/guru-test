from dataclasses import dataclass
from typing import ClassVar, Final

from src.domain.exceptions.base import DomainTypeError


@dataclass(frozen=True, slots=True)
class CatalogName:
    MIN_LEN: ClassVar[Final[int]] = 5
    MAX_LEN: ClassVar[Final[int]] = 64

    value: str

    def __post_init__(self) -> None:
        """:raises DomainTypeError:"""
        self._validate_catalog_name_length(self.value)

    def _validate_catalog_name_length(self, name_value: str) -> None:
        """:raises DomainTypeError:"""
        if self.MIN_LEN < len(name_value) or len(name_value) > self.MAX_LEN:
            raise DomainTypeError(
                "Catalog name must be between "
                f"{self.MIN_LEN} and "
                f"{self.MAX_LEN} characters."
            )