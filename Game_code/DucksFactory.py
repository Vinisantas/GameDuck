import random

from Game_code.Ducks import Duck
from Game_code.const import W_HEIGHT, W_WIDTH



class DuckFactory:
    @staticmethod
    def create_duck():
        # Pato começa na parte inferior da tela
        x = random.randint(100, W_WIDTH - 100)
        y = W_HEIGHT
        # O pato se move lentamente para cima (câmera lenta)
        speed_y = random.uniform(0.3 , 0.5)  # Velocidade variável e lenta
        speed_x = random.uniform(0.1, 0.5)  # Velocidade horizontal
        return Duck(x, y, speed_y, speed_x)