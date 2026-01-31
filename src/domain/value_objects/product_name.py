from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProductName:
    value: str