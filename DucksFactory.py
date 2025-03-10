import random

from Ducks import Duck
from const import W_HEIGHT, W_WIDTH


class DuckFactory:
    @staticmethod
    def create_duck():
        # Pato começa na parte inferior da tela
        x = random.randint(100, W_WIDTH - 100)
        y = W_HEIGHT
        # O pato se move lentamente para cima (câmera lenta)
        speed_y = random.uniform(0.5, 1.0)  # Velocidade variável e lenta
        return Duck(x, y, speed_y)