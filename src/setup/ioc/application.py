from dishka import Provider, Scope, provide_all, provide

from src.application.commands.supplement_order import SupplementOrderCommand
from src.application.common.ports.order_line_command_gateway import OrderLineCommandGateway
from src.application.common.ports.order_query_gateway import OrderQueryGateway
from src.application.common.ports.product_query_gateway import ProductQueryGateway
from src.application.common.ports.transaction_manager import TransactionManager
from src.infrastructure.adapters.sqla_order_line_data_mapper import SqlaOrderLineDataMapper
from src.infrastructure.adapters.sqla_order_reader import SqlaOrderReader
from src.infrastructure.adapters.sqla_product_reader import SqlaProductReader
from src.infrastructure.adapters.sqla_transaction_manager import SqlaTransactionManager


class ApplicationProvider(Provider):
    scope = Scope.REQUEST

    order_line_command_gateway = provide(
        SqlaOrderLineDataMapper, provides=OrderLineCommandGateway
    )

    order_query_gateway = provide(
        SqlaOrderReader, provides=OrderQueryGateway
    )

    product_query_gateway = provide(
        SqlaProductReader, provides=ProductQueryGateway
    )

    transaction_manager = provide(
        SqlaTransactionManager, provides=TransactionManager
    )

    commands = provide_all(
        SupplementOrderCommand,
    )