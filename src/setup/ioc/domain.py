from dishka import Provider, Scope, provide, provide_all

from src.domain.ports.clock import Clock
from src.domain.ports.order_line_id_generator import OrderLineIdGenerator
from src.domain.services.order_line import OrderLineService
from src.infrastructure.adapters.system_clock import SystemClock
from src.infrastructure.adapters.uuid_order_line_id_generator import (
    UuidOrderLineIdGenerator,
)


class DomainProvider(Provider):
    scope = Scope.APP

    clock = provide(SystemClock, provides=Clock)

    order_line_id_generator = provide(
        UuidOrderLineIdGenerator, provides=OrderLineIdGenerator
    )

    services = provide_all(
        OrderLineService,
    )
