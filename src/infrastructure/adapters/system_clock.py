from datetime import datetime, UTC

from src.domain.ports.clock import Clock


class SystemClock(Clock):
    def now(self) -> datetime:
        return datetime.now(tz=UTC).replace(microsecond=0)