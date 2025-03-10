import pygame as pg
from const import C_BLUE, C_GREEN, C_RED, MENU_OPTION, W_WIDTH

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./assets/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.font = pg.font.Font(None, 36)

    def run(self):
        menu_option = 0
        pg.mixer.music.load('./assets/Menu.mp3')
        pg.mixer.music.play(-1)
        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(text_size=50, text="Ducks", text_color=C_RED, text_center_pos=(W_WIDTH / 2, 70))
            self.menu_text(text_size=50, text="Shooter", text_color=C_RED, text_center_pos=(W_WIDTH / 2, 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=C_GREEN, text_center_pos=(W_WIDTH / 2, 200 + 25 * i))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=C_BLUE, text_center_pos=(W_WIDTH / 2, 200 + 25 * i))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    elif event.key == pg.K_RETURN:  # Adicionado para selecionar a opção
                        pg.mixer.music.stop()
                        return [MENU_OPTION[menu_option]]

            pg.display.update()

    def menu_text(self, text_size, text, text_color, text_center_pos):
        text_font = pg.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_suf = text_font.render(text, True, text_color).convert_alpha() #remova o color=
        text_rect = text_suf.get_rect(center=text_center_pos)
        self.window.blit(text_suf, text_rect)