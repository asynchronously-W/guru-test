from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.ports.transaction_manager import TransactionManager
from src.infrastructure.exceptions.gateway import DataMapperError


class SqlaTransactionManager(TransactionManager):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        try:
            await self._session.commit()
        except SQLAlchemyError as err:
            raise DataMapperError("Database commit failed.") from err