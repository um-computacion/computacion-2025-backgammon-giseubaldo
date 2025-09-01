
class Tablero:
    """Representa el tablero de Backgammon."""


    def __init__(self):
        self.__puntos__ = [[] for _ in range(24)]
        self.__barra__ = {"blanco": [], "negro": []}
        self.__home__ = {"blanco": [], "negro": []}

    def mover_ficha(self, punto_origen, punto_destino, color_jugador):
        """Mueve una ficha si es válido."""
        if not self.__puntos__[punto_origen]:
            return False

        ficha = self.__puntos__[punto_origen][-1]
        if ficha.__color__ != color_jugador:
            return False

        destino = self.__puntos__[punto_destino]
        if destino and destino[-1].__color__ != color_jugador and len(destino) == 1:
            capturada = destino.pop()
            self.__barra__[capturada.__color__].append(capturada)
        elif destino and destino[-1].__color__ != color_jugador and len(destino) > 1:
            return False

        self.__puntos__[punto_origen].pop()
        self.__puntos__[punto_destino].append(ficha)
        return True

    def reingresar_desde_barra(self, punto_entrada, color_jugador):
        """Reingresa una ficha desde la barra."""
        if not self.__barra__[color_jugador]:
            return False

        destino = self.__puntos__[punto_entrada]
        ficha = self.__barra__[color_jugador].pop()

        if destino and destino[-1].__color__ != color_jugador and len(destino) == 1:
            capturada = destino.pop()
            self.__barra__[capturada.__color__].append(capturada)
        elif destino and destino[-1].__color__ != color_jugador and len(destino) > 1:
            return False

        self.__puntos__[punto_entrada].append(ficha)
        return True

    def verificar_victoria(self, color_jugador):
        """Verifica si el jugador ha ganado."""
        return len(self.__home__[color_jugador]) == 15

