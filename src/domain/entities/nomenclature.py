from src.domain.entities.base import Entity
from src.domain.value_objects.nomenclature_id import NomenclatureId
from src.domain.value_objects.nomenclature_name import NomenclatureName
from src.domain.value_objects.nomenclature_price import NomenclaturePrice
from src.domain.value_objects.nomenclature_stock import NomenclatureStock


class Nomenclature(Entity[NomenclatureId]):
    def __init__(
        self,
        id_: NomenclatureId,
        name: NomenclatureName,
        stock: NomenclatureStock,
        price: NomenclaturePrice,
    ) -> None:
        super().__init__(id_)

        self.name = name
        self.stock = stock
        self.price = price