import unittest
from core.jugador import Jugador

class TestJugador(unittest.TestCase):
    def setUp(self):
        self.jugador = Jugador("Gisela", "blanco")

    def test_atributos_iniciales(self):
        self.assertEqual(self.jugador.__nombre__, "Gisela")
        self.assertEqual(self.jugador.__color__, "blanco")
        self.assertEqual(self.jugador.__fichas__, 15)

if __name__ == "__main__":
    unittest.main()
