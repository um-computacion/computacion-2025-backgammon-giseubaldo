from core.tablero import Tablero
from core.dados import Dados
from core.jugador import Jugador

class JuegoBackgammon:
    """Coordina el flujo general del juego."""

    def __init__(self, nombre1, nombre2):
        self.__tablero__ = Tablero()
        self.__dados__ = Dados()
        self.__jugador1__ = Jugador(nombre1, "blanco")
        self.__jugador2__ = Jugador(nombre2, "negro")
        self.__jugador_actual__ = self.__jugador1__

    def cambiar_turno(self):
        """Cambia el turno al otro jugador."""
        self.__jugador_actual__ = (
            self.__jugador2__ if self.__jugador_actual__ == self.__jugador1__ else self.__jugador1__
        )
