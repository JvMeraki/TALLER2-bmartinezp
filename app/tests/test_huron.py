import io
import unittest
from unittest.mock import patch

from models.huron import Huron


class TestHuron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Timon", 5, 3, "Estados Unidos", 10.5)

    def test_hacer_sonido(self):
        with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            self.huron.hacer_sonido()
            self.assertEqual(mock_stdout.getvalue().strip(), "¡Eek, Eek!")

    def test_calcular_flete(self):
        self.assertEqual(self.huron.calcular_flete(), 3 * 10.5)

if __name__ == "__main__":
    unittest.main()