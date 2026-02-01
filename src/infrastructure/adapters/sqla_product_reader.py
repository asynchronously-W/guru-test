from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.ports.product_query_gateway import ProductQueryGateway
from src.domain.entities.product import Product
from src.domain.value_objects.product_id import ProductId
from src.infrastructure.exceptions.gateway import ReaderError


class SqlaProductReader(ProductQueryGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def read_by_id(self, product_id: ProductId) -> Product | None:
        """:raises ReaderError:"""
        stmt = select(Product).where(Product.id_ == product_id)  # type: ignore

        try:
            product = (await self._session.execute(stmt)).scalar_one_or_none()
        except SQLAlchemyError as err:
            raise ReaderError() from err

        return product
