from functools import cached_property

from pydantic import BaseModel, PostgresDsn


class PostgresSettings(BaseModel):
    driver: str
    host: str
    port: int
    user: str
    password: str
    database: str

    @cached_property
    def dsn(self) -> str:
        return str(
            PostgresDsn.build(
                scheme=f"postgresql+{self.driver}",
                username=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                path=self.database,
            ),
        )