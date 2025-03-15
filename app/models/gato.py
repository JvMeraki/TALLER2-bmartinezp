from app.models.animal import Animal


class Gato(Animal):
    def __init__(self, nombre: str, edad: int, peso: float):
        super().__init__(nombre, edad, peso)
        
    def hacer_sonido(self) -> str:
        return "Miau, Miau!"