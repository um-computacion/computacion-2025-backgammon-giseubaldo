import random

class Dados:

    """Clase que representa los dados del juego."""

    def tirar_dados(self):
        """Lanza dos dados de seis caras.
        Returns:
            tuple: Dos valores entre 1 y 6.
        """
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        return (dado1, dado2)