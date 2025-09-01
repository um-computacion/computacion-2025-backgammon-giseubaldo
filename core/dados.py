import random

class Dados:
    

    def tirar_dados(self):
        
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        return (dado1, dado2)
 