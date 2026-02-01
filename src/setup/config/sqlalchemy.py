from pydantic import BaseModel


class SqlalchemySettings(BaseModel):
    echo: bool
    echo_pool: bool
    pool_size: int
    max_overflow: int