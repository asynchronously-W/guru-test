from src.domain.entities.order_line import OrderLine
from src.domain.ports.order_line_id_generator import OrderLineIdGenerator
from src.domain.value_objects.order_id import OrderId
from src.domain.value_objects.order_line_quantity import OrderLineQuantity
from src.domain.value_objects.product_id import ProductId
from src.domain.value_objects.product_name import ProductName


class OrderLineService:
    def __init__(self, order_line_id_generator: OrderLineIdGenerator) -> None:
        self._order_line_id_generator = order_line_id_generator

    def change_quantity(
        self,
        order_line: OrderLine,
        quantity: OrderLineQuantity,
    ) -> None:
        order_line.quantity = quantity

    def create_order_line(
        self,
        quantity: OrderLineQuantity,
        order_id: OrderId,
        product_id: ProductId,
        product_name_snapshot: ProductName,
    ) -> OrderLine:
        order_line_id = self._order_line_id_generator.generate()

        return OrderLine(
            id_=order_line_id,
            quantity=quantity,
            order_id=order_id,
            product_id=product_id,
            product_name_snapshot=product_name_snapshot,
        )
