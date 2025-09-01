

class Jugador:
    """Representa a un jugador."""

    def __init__(self, nombre, color):
        """Inicializa el jugador.
        Args:
            nombre (str): Nombre del jugador.
            color (str): Color de sus fichas.
        """
        self.__nombre__ = nombre
        self.__color__ = color
        self.__fichas__ = 15
