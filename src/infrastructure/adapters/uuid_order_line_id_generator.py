import uuid_utils.compat as uuid_utils

from src.domain.ports.order_line_id_generator import OrderLineIdGenerator
from src.domain.value_objects.order_line_id import OrderLineId


class UuidOrderLineIdGenerator(OrderLineIdGenerator):
    def generate(self) -> OrderLineId:
        return OrderLineId(uuid_utils.uuid7())