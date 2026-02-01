from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.ports.order_query_gateway import OrderQueryGateway
from src.domain.entities.order import Order
from src.domain.value_objects.order_id import OrderId
from src.infrastructure.exceptions.gateway import ReaderError


class SqlaOrderReader(OrderQueryGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def read_by_id(self, order_id: OrderId) -> Order | None:
        """:raises ReaderError:"""
        stmt = select(Order).where(Order.id_ == order_id)  # type: ignore

        try:
            order = (await self._session.execute(stmt)).scalar_one_or_none()
        except SQLAlchemyError as err:
            raise ReaderError() from err

        return order
