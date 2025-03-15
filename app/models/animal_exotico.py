from app.models.animal import Animal


class Animal_Exotico(Animal):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos
        
    def calcular_flete(self) -> float:
        return self._impuestos * self._peso
    
    def obtener_pais_origen(self) -> str:
        return self._pais_origen
    
    def obtener_impuestos(self) -> float:
        return self._impuestos