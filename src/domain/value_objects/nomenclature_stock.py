from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class NomenclatureStock:
    value: int