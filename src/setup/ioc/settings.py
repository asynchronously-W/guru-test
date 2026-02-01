from dishka import Provider, Scope, from_context, provide

from src.setup.config.logging import LoggingSettings
from src.setup.config.postgres import PostgresSettings
from src.setup.config.settings import AppSettings
from src.setup.config.sqlalchemy import SqlalchemySettings


class SettingsProvider(Provider):
    scope = Scope.APP

    settings = from_context(AppSettings)

    @provide
    def provide_sqlalchemy_settings(
        self,
        settings: AppSettings,
    ) -> SqlalchemySettings:
        return settings.sqlalchemy

    @provide
    def provide_postgres_settings(self, settings: AppSettings) -> PostgresSettings:
        return settings.postgres

    @provide
    def provide_logging_settings(self, settings: AppSettings) -> LoggingSettings:
        return settings.logging