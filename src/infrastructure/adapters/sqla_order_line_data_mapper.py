from sqlalchemy import and_, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.ports.order_line_command_gateway import (
    OrderLineCommandGateway,
)
from src.domain.entities.order_line import OrderLine
from src.domain.value_objects.order_id import OrderId
from src.domain.value_objects.product_id import ProductId
from src.infrastructure.exceptions.gateway import DataMapperError


class SqlaOrderLineDataMapper(OrderLineCommandGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def add(self, order_line: OrderLine) -> None:
        """:raises DataMapperError:"""
        try:
            self._session.add(order_line)
        except SQLAlchemyError as err:
            raise DataMapperError() from err

    async def read_by_order_and_product(
        self,
        order_id: OrderId,
        product_id: ProductId,
        for_update: bool,
    ) -> OrderLine | None:
        """:raises DataMapperError:"""

        stmt = select(OrderLine).where(
            and_(
                OrderLine.order_id == order_id,      # type: ignore
                OrderLine.product_id == product_id,  # type: ignore
            )
        )

        if for_update:
            stmt.with_for_update()

        try:
            return (await self._session.execute(stmt)).scalar_one_or_none()
        except SQLAlchemyError as err:
            raise DataMapperError() from err
