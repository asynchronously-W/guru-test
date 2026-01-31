from enum import StrEnum


class OrderStatus(StrEnum):
    DRAFT = "draft"
    CONFIRMED = "confirmed"