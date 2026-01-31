from src.domain.entities.product import Product
from src.domain.ports.product_id_generator import ProductIdGenerator


class ProductService:
    def __init__(self, product_id_generator: ProductIdGenerator) -> None:
        self._product_id_generator = product_id_generator