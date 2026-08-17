#!/usr/init/python
# -*- coding: utf-8 -*-

import pygame

from code.player import Player
from code.background import Background
from code.shot import Shot
from code.zombie import Zombie


class Level:
    def __init__(self, difficulty, game):
        self.game = game

        self.duration = difficulty.duration
        self.time_remaining = difficulty.duration

        self.player = Player()
        self.background = Background(self.duration)

        self.zombies = []
        self.shots = []

        self.clock = pygame.time.Clock()

        # Cria um evento customizado para o tempo de spawn dos zumbis
        self.SPAWN_ZOMBIE = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWN_ZOMBIE, 2000)  # A cada 2 segundos

    def run(self):
        while True:
            # 1. Captura de Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Evento do Timer: Nasce um zumbi
                if event.type == self.SPAWN_ZOMBIE:
                    self.zombies.append(Zombie())

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()
                        novo_tiro = Shot(self.player.rect.center, self.player.facing_right)
                        self.shots.append(novo_tiro)

            # 2. Atualiza a lógica do jogo (Apenas UMA vez cada)
            self.player.update()

            for shot in self.shots[:]:
                shot.update()
                if shot.rect.x < 0 or shot.rect.x > pygame.display.get_surface().get_width():
                    self.shots.remove(shot)

            for zombie in self.zombies[:]:
                zombie.update()
                # Se o zumbi terminou de cair (morreu), removemos ele da lista
                if zombie.is_dead:
                    self.zombies.remove(zombie)

            # Verifica as colisões dos tiros com os zumbis
            self.check_collisions()

            # 3. Desenha na tela (Ordem de camadas)
            self.game.window.fill((0, 0, 0))
            self.background.draw(self.game.window)

            for zombie in self.zombies:
                zombie.draw(self.game.window)

            for shot in self.shots:
                shot.draw(self.game.window)

            self.player.draw(self.game.window)

            # --- ADICIONE ESTAS LINHAS AQUI PARA EXIBIR O PLACAR ---
            fonte = pygame.font.Font(None, 36)
            texto_score = fonte.render(f"Score: {self.game.score}", True, (255, 255, 255))
            self.game.window.blit(texto_score, (20, 20))
            # ------------------------------------------------------

            # 4. Atualiza o display e crava em 60 FPS
            pygame.display.flip()
            self.clock.tick(60)

    def spawn_zombie(self):
        pass

    def update(self):
        pass

    def check_collisions(self):
        for shot in self.shots[:]:
            for zombie in self.zombies[:]:
                if not zombie.is_dying and shot.rect.colliderect(zombie.rect):
                    if shot in self.shots:
                        self.shots.remove(shot)
                    zombie.die()
                    self.game.score += 100

        # Verifica se o zumbi chegou perto o suficiente do player
        for zombie in self.zombies:
            if not zombie.is_dying:
                distancia_x = abs(zombie.rect.centerx - self.player.rect.centerx)
                if distancia_x < 30:
                    from code.game_over import GameOver
                    GameOver(self.game).run()