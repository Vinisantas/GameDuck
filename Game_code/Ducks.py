
import random
import pygame as pg

from Game_code.const import W_WIDTH

class Duck:
    def __init__(self, x, y, speed_y, speed_x):
        self.x = x
        self.y = y
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.direction = 1  # Direção inicial: direita
        self.image = pg.image.load('./assets/duck.png')
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        # Movendo o pato para cima (da parte inferior para a superior da tela)
        largura_personagem = self.image.get_width()
        self.y -= self.speed_y  # Movimento vertical
        self.x += self.speed_x * self.direction  # Movimento horizontal

        # Inverta a direção ao atingir as bordas horizontais
        if self.x <= 0 or self.x >= W_WIDTH - largura_personagem:
            self.direction *= -1

        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_hit(self, mouse_x, mouse_y):
        return self.rect.collidepoint(mouse_x, mouse_y)

    def is_off_screen(self):
        # Verifica se o pato saiu da tela (se chegou na parte superior)
        return self.y < 0
        
