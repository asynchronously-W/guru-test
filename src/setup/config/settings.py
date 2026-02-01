import os
from functools import cache
from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    PydanticBaseSettingsSource,
    TomlConfigSettingsSource,
)

from src.setup.config.logging import LoggingSettings
from src.setup.config.postgres import PostgresSettings
from src.setup.config.sqlalchemy import SqlalchemySettings


class AppSettings(BaseSettings):
    postgres: PostgresSettings
    logging: LoggingSettings
    sqlalchemy: SqlalchemySettings

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            TomlConfigSettingsSource(settings_cls),
            file_secret_settings,
        )

@cache
def create_settings(app_env: str | None = None) -> AppSettings:
    app_env = app_env or os.getenv("APP_ENV", "local")

    config_path = (Path.cwd() / "config" / app_env / "config.toml").resolve()  # type: ignore[operator]

    if not config_path.is_file():
        raise RuntimeError(f"Config file not found: {config_path}")

    AppSettings.model_config = SettingsConfigDict(
        toml_file=str(config_path),
    )

    return AppSettings()  # type: ignore[call-arg]