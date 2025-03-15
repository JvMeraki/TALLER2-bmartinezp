from app.models.animal_exotico import Animal_Exotico


class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float):
        super().__init__(nombre, edad, peso, pais_origen, impuestos)
        self._ratones_comidos = 0

    def hacer_sonido(self) -> str:
        return "¡Tsss!"

    def comer_raton(self, cantidad: int) -> None:
        if self._ratones_comidos + cantidad >= 20:
            raise ValueError("Demasiados Ratones!")
        self._ratones_comidos += cantidad

    def obtener_ratones_comidos(self) -> int:
        return self._ratones_comidos