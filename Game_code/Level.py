import pygame as pg
from Game_code.DucksFactory import DuckFactory



class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode





    def run(self, screen):
        ducks = [DuckFactory.create_duck() for _ in range(3)]  # Cria 5 patos
        score = 0
        lives = 3  # O jogador começa com 3 vidas
        self.surf = pg.image.load('./assets/BgLevel1.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        running = True

        while running:
                screen.fill((255, 255, 255))  # Limpa a tela
                self.window.blit(self.surf, self.rect)
                # Loop de eventos
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False

                    # Detecção de clique do mouse (atirar)
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:  # Botão esquerdo do mouse
                            mouse_x, mouse_y = pg.mouse.get_pos()

                            # Verifica se algum pato foi atingido
                            for duck in ducks:
                                if duck.is_hit(mouse_x, mouse_y):
                                    ducks.remove(duck)  # Remove o pato atingido
                                    ducks.append(DuckFactory.create_duck())  # Cria um novo pato
                                    score += 1  # Atualiza o score
                                    break

                # Movimenta e desenha todos os patos
                for duck in ducks[:]:
                    duck.move()
                    duck.draw(screen)

                    if duck.is_off_screen():
                        # Se o pato sair da tela, perde uma vida
                        ducks.remove(duck)
                        ducks.append(DuckFactory.create_duck())  # Cria um novo pato
                        lives -= 1

                # Desenha a mira
                mouse_x, mouse_y = pg.mouse.get_pos()
                pg.mouse.set_visible(False)
                crosshair = pg.image.load('./assets/crosshair.png')
                screen.blit(crosshair, (mouse_x - crosshair.get_width() // 2, mouse_y - crosshair.get_height() // 2))

                # Verifica se o jogador perdeu todas as vidas
                if lives <= 0:
                    running = False
                    print("Game Over! Você perdeu todas as vidas.")

                # Atualiza a tela
                pg.display.update()


        return score, lives