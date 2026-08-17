#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.player import Player
from code.background import Background


class Level:
    def __init__(self, difficulty, game):
        self.game = game

        # O tempo vem da dificuldade que o jogador escolheu no menu
        self.duration = difficulty.duration
        self.time_remaining = difficulty.duration

        self.player = Player()

        # Passamos a duração para o cenário
        self.background = Background(self.duration)

        self.zombies = []
        self.shots = []

        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            # 1. Captura de Eventos (Fechar janela)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # 2. Atualiza a lógica (Movimentação do jogador)
            self.player.update()

            # 3. Desenha na tela (Ordem de camadas)
            self.game.window.fill((0, 0, 0))        # 1º Limpa a tela com preto absoluto (Corrige o glitch)
            self.background.draw(self.game.window)  # 2º Desenha o fundo
            self.player.draw(self.game.window)      # 3º Desenha o jogador

            # 4. Atualiza o display e crava em 60 FPS
            pygame.display.flip()
            self.clock.tick(60)

    def spawn_zombie(self):
        pass

    def update(self):
        pass

    def check_collisions(self):
        pass