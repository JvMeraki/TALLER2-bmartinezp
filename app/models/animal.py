from app.models.ianimal import iAnimal


class Animal(iAnimal):
    def __init__(self, nombre: str, peso: float, edad: int):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = 0
        
    def comer(self, kilos: float) -> float:
        self._kilos_comidos += kilos
    
    def obtener_kilos_comidos(self) -> float:
        return self._kilos_comidos
    
    def hacer_sonido(self) -> str:
        pass

    def obtener_nombre(self) -> str:
        return self._nombre
    
    def obtener_peso(self) -> float:
        return self._peso
    
    def obtener_edad(self) -> int:
        return self._edad