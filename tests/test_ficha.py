import unittest
from core.ficha import Ficha

class TestFicha(unittest.TestCase):
    def test_color_de_ficha(self):
        ficha = Ficha("negro")
        self.assertEqual(ficha.__color__, "negro")

if __name__ == "__main__":
    unittest.main()
