from enum import StrEnum


class OrderStatus(StrEnum):
    DRAFT = "draft"
    PLACED = "placed"