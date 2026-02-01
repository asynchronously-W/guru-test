from src.infrastructure.persistence_sqla.mappings.catalog import map_catalogs_table
from src.infrastructure.persistence_sqla.mappings.customer import map_customers_table
from src.infrastructure.persistence_sqla.mappings.order import map_orders_table
from src.infrastructure.persistence_sqla.mappings.order_line import map_order_lines_table
from src.infrastructure.persistence_sqla.mappings.product import map_products_table


def map_tables() -> None:
    map_catalogs_table()
    map_customers_table()
    map_orders_table()
    map_order_lines_table()
    map_products_table()