from app.models.boa_constrictor import Boa_Constrictor
from app.models.huron import Huron


class Guarderia:
    def __init__(self):
        self.boa_1 = Boa_Constrictor("Black Mamba", 8, 30, "Brasil", 15.5)
        self.boa_2 = Boa_Constrictor("Anaconda", 10, 40, "Perú", 18.0)
        self.huron_1 = Huron("Timon", 5, 3, "Estados Unidos", 10.5)
        self.huron_2 = Huron("Pumba", 4, 2.5, "Canadá", 9.8)

    def alimentar_boa(self, boa: Boa_Constrictor, cantidad: int) -> str:
        if boa is None:
            return "Esta Boa no existe!"
        
        try:
            boa.comer_raton(cantidad)
            return "Éxito"
        except ValueError as e:
            return "La boa está llena"

# Ejemplo de uso
if __name__ == "__main__":
    guarderia = Guarderia()
    
    # Alimentando normalmente
    print(guarderia.alimentar_boa(guarderia.boa_1, 5))  # Salida esperada: "Éxito"
    
    # Intentando sobrealimentar la boa
    print(guarderia.alimentar_boa(guarderia.boa_1, 5))  # Salida esperada: "La boa está llena"
    
    # Probando con una boa inexistente
    print(guarderia.alimentar_boa(None, 3))  # Salida esperada: "Esta Boa no existe!"