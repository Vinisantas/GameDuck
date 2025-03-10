import pygame

from const import MENU_OPTION, W_HEIGHT, W_WIDTH
from Menu import Menu
from Level import Level

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((800, 600))
        self.score = 0
        self.lives = 3
        pygame.init()
        pygame.font.init()

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()  # Chama o método run() do menu

            if menu_return == [MENU_OPTION[0]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run(self.window)
            elif menu_return == [MENU_OPTION[2]]:
                pygame.quit()
                quit()
            else:
                pass