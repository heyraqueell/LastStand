#!/usr/python
# -*- coding: utf-8 -*-

import pygame
from code.const import WINDOW_WIDTH, WINDOW_HEIGHT


class Victory:
    def __init__(self, game):
        self.game = game
        self.window = game.window

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Pressione Enter para voltar ao menu
                        self.game.score = 0  # Zera a pontuação ao reiniciar
                        from code.menu import Menu
                        Menu(self.game).run()

            # Desenha a tela de Vitória
            self.window.fill((0, 0, 0))

            fonte_titulo = pygame.font.Font(None, 48)
            fonte_texto = pygame.font.Font(None, 36)

            texto_titulo = fonte_titulo.render("PARABÉNS, VOCÊ NÃO FOI INFECTADO!", True, (0, 255, 0))
            texto_score = fonte_texto.render(f"Pontuação Final: {self.game.score}", True, (255, 255, 255))
            texto_instrucao = fonte_texto.render("Pressione ENTER para voltar ao Menu", True, (200, 200, 200))

            # Centraliza os textos na tela
            self.window.blit(texto_titulo, (WINDOW_WIDTH // 2 - texto_titulo.get_width() // 2, WINDOW_HEIGHT // 2 - 80))
            self.window.blit(texto_score, (WINDOW_WIDTH // 2 - texto_score.get_width() // 2, WINDOW_HEIGHT // 2 - 10))
            self.window.blit(texto_instrucao,
                             (WINDOW_WIDTH // 2 - texto_instrucao.get_width() // 2, WINDOW_HEIGHT // 2 + 50))

            pygame.display.flip()
            clock.tick(60)