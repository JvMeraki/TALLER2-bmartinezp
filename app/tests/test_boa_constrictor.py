import io
import unittest
from unittest.mock import patch

from models.boa_constrictor import Boa_Constrictor


class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        self.boa = Boa_Constrictor("Black Mamba", 8, 30, "Brasil", 15.5)

    def test_hacer_sonido(self):
        with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            self.boa.hacer_sonido()
            self.assertEqual(mock_stdout.getvalue().strip(), "¡Tsss!")

    def test_calcular_flete(self):
        self.assertEqual(self.boa.calcular_flete(), 30 * 15.5)

    def test_comer_raton(self):
        self.boa.comer_raton(5)
        self.assertEqual(self.boa.obtener_ratones_comidos(), 5)

    def test_comer_muchos_ratones(self):
        """Verifica que se lance ValueError si se intenta comer 10 o más ratones"""
        self.boa.comer_raton(8)  # Primero come 8
        with self.assertRaises(ValueError) as context:
            self.boa.comer_raton(2)  # Intenta comer 2 más (total 10)
        self.assertEqual(str(context.exception), "Demasiados Ratones!")

if __name__ == "__main__":
    unittest.main()