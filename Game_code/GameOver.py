
import pygame as pg

from Game_code.const import C_BLACK, C_WHITE, MENU_OPTION, W_WIDTH

class Gameover:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./assets/GameOver.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.font = pg.font.Font(None, 36)

    def run(self):
        pg.mixer.music.load('./assets/Menu.mp3')
        pg.mixer.music.play(-1)
        while True:

            for event in pg.event.get():
                if event.type == pg.QUIT:  # Se o jogador fechar a janela
                    pg.mixer.music.stop()
                    pg.quit()
                    return  # Encerra o jogo
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        pg.mixer.music.stop()
                        return [MENU_OPTION]


            # Desenha a tela de "Game Over"
            self.window.blit(self.surf, self.rect)
            self.menu_text(text_size=50, text="Press enter to return", text_color=C_WHITE, text_center_pos=(W_WIDTH / 2, 500))

            # Atualiza a tela
            pg.display.flip()

    def menu_text(self, text_size, text, text_color, text_center_pos, background=C_BLACK):
        text_font = pg.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_suf = text_font.render(text, True, text_color, background).convert_alpha()
        text_rect = text_suf.get_rect(center=text_center_pos)
        self.window.blit(text_suf, text_rect)