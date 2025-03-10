
import pygame as pg
from const import W_WIDTH, W_HEIGHT

class Duck:
    def __init__(self, x, y, speed_y):
        self.x = x
        self.y = y
        self.speed_y = speed_y
        self.image = pg.image.load('./assets/duck.png')
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        # Movendo o pato para cima (da parte inferior para a superior da tela)
        self.y -= self.speed_y
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_hit(self, mouse_x, mouse_y):
        return self.rect.collidepoint(mouse_x, mouse_y)

    def is_off_screen(self):
        # Verifica se o pato saiu da tela (se chegou na parte superior)
        return self.y < 0
        
