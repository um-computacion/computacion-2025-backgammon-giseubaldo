import unittest
from core.juego import JuegoBackgammon

class TestJuegoBackgammon(unittest.TestCase):
    def setUp(self):
        self.juego = JuegoBackgammon("Gisela", "Bot")

    def test_jugadores_iniciales(self):
        self.assertEqual(self.juego.__jugador1__.__nombre__, "Gisela")
        self.assertEqual(self.juego.__jugador2__.__nombre__, "Bot")

    def test_cambio_de_turno(self):
        jugador_inicial = self.juego.__jugador_actual__
        self.juego.cambiar_turno()
        self.assertNotEqual(self.juego.__jugador_actual__, jugador_inicial)

if __name__ == "__main__":
    unittest.main()
