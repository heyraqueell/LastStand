#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.player import Player
from code.background import Background
from code.shot import Shot

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
            # 1. Captura de Eventos (Fechar janela e Teclado)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Detecta o clique único na barra de espaço para atirar
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()  # Correção 1: Ativa a animação
                        # Cria um novo tiro baseado na posição e direção atual do player
                        novo_tiro = Shot(self.player.rect.center, self.player.facing_right)
                        self.shots.append(novo_tiro)

            # 2. Atualiza a lógica do jogador e dos tiros
            self.player.update()

            for shot in self.shots[:]:  # Correção 2: O [:] evita bugs ao remover
                shot.update()
                # Remove o tiro da lista se ele sair da tela para poupar memória
                if shot.rect.x < 0 or shot.rect.x > pygame.display.get_surface().get_width():
                    self.shots.remove(shot)

            # 3. Desenha na tela (Ordem de camadas)
            self.game.window.fill((0, 0, 0))
            self.background.draw(self.game.window)

            # Desenha todos os tiros ativos
            for shot in self.shots:
                shot.draw(self.game.window)

            self.player.draw(self.game.window)

            # 4. Atualiza o display e crava em 60 FPS
            pygame.display.flip()
            self.clock.tick(60)

    def spawn_zombie(self):
        pass

    def update(self):
        pass

    def check_collisions(self):
        pass