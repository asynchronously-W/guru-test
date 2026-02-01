from typing import AsyncIterator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from src.setup.config.postgres import PostgresSettings
from src.setup.config.sqlalchemy import SqlalchemySettings


class PersistenceSqlaProvider(Provider):
    @provide(scope=Scope.APP)
    async def provide_async_engine(
        self,
        sqlalchemy_settings: SqlalchemySettings,
        postgres_settings: PostgresSettings,
    ) -> AsyncEngine:
        return create_async_engine(
            postgres_settings.dsn,
            echo=sqlalchemy_settings.echo,
            echo_pool=sqlalchemy_settings.echo_pool,
            pool_size=sqlalchemy_settings.pool_size,
            max_overflow=sqlalchemy_settings.max_overflow,
            pool_pre_ping=True,
        )

    @provide(scope=Scope.APP)
    async def provide_async_session_factory(
        self,
        engine: AsyncEngine,
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(engine, expire_on_commit=False)

    @provide(scope=Scope.REQUEST)
    async def provide_async_session(
        self,
        session_factory: async_sessionmaker[AsyncSession],
    ) -> AsyncIterator[AsyncSession]:
        async with session_factory() as session:
            yield session

def infrastructure_providers() -> tuple[Provider, ...]:
    return (
        PersistenceSqlaProvider(),
    )