from src.domain.entities.nomenclature import Nomenclature
from src.domain.ports.nomenclature_id_generator import NomenclatureIdGenerator


class NomenclatureService:
    def __init__(self, nomenclature_id_generator: NomenclatureIdGenerator) -> None:
        self._nomenclature_id_generator = nomenclature_id_generator