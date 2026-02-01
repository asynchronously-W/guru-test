from typing import Literal

from pydantic import BaseModel


class LoggingSettings(BaseModel):
    level: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ]
