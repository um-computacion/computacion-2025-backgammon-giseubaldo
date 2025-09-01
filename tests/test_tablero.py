import unittest
from core.tablero import Tablero
from core.ficha import Ficha

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()
        self.ficha_blanca = Ficha("blanco")
        self.ficha_negra = Ficha("negro")
        self.tablero.__puntos__[0].append(self.ficha_blanca)
        self.tablero.__puntos__[5].append(self.ficha_negra)

    def test_mover_ficha_valida(self):
        resultado = self.tablero.mover_ficha(0, 3, "blanco")
        self.assertTrue(resultado)
        self.assertEqual(len(self.tablero.__puntos__[3]), 1)

    def test_mover_ficha_color_incorrecto(self):
        resultado = self.tablero.mover_ficha(5, 3, "blanco")
        self.assertFalse(resultado)

    def test_captura_de_ficha(self):
        self.tablero.__puntos__[3].append(self.ficha_negra)
        self.tablero.__puntos__[0].append(self.ficha_blanca)
        resultado = self.tablero.mover_ficha(0, 3, "blanco")
        self.assertTrue(resultado)
        self.assertEqual(len(self.tablero.__barra__["negro"]), 1)

    def test_punto_bloqueado(self):
        self.tablero.__puntos__[3].extend([self.ficha_negra, self.ficha_negra])
        self.tablero.__puntos__[0].append(self.ficha_blanca)
        resultado = self.tablero.mover_ficha(0, 3, "blanco")
        self.assertFalse(resultado)

    def test_reingreso_desde_barra(self):
        self.tablero.__barra__["blanco"].append(self.ficha_blanca)
        resultado = self.tablero.reingresar_desde_barra(3, "blanco")
        self.assertTrue(resultado)
        self.assertEqual(len(self.tablero.__puntos__[3]), 1)

    def test_verificar_victoria(self):
        self.tablero.__home__["blanco"] = [self.ficha_blanca] * 15
        resultado = self.tablero.verificar_victoria("blanco")
        self.assertTrue(resultado)

if __name__ == "__main__":
    unittest.main()
