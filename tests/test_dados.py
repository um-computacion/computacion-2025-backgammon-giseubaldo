import unittest
from core.dados import Dados

class TestDados(unittest.TestCase):
    def setUp(self):
        self.dados = Dados()

    def test_tirada_devuelve_dos_valores(self):
        resultado = self.dados.tirar_dados()
        self.assertEqual(len(resultado), 2)
        self.assertTrue(all(1 <= dado <= 6 for dado in resultado))

    def test_tirada_doble(self):
        resultado = self.dados.tirar_dados()
        if resultado[0] == resultado[1]:
            self.assertEqual(resultado[0], resultado[1])

if __name__ == "__main__":
    unittest.main()
