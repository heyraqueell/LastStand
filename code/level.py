#!/usr/init/python
# -*- coding: utf-8 -*-

import pygame

from code.player import Player
from code.background import Background
from code.shot import Shot
from code.zombie import Zombie
from code.victory import Victory
from code.game_over import GameOver


class Level:
    def __init__(self, difficulty, game):
        self.game = game
        self.difficulty_name = difficulty.name  # "EASY", "MEDIUM", "HARD"

        self.duration = difficulty.duration
        self.time_remaining = self.duration

        self.player = Player()
        self.background = Background(self.duration)

        self.zombies = []
        self.shots = []

        self.clock = pygame.time.Clock()

        # Configurações de velocidade e spawn ajustadas
        if self.difficulty_name == "EASY":
            self.zombie_speed = 2
            spawn_tempo = 2000  # A cada 2 segundos
        elif self.difficulty_name == "MEDIUM":
            # Usa a mesma velocidade e spawn do Hard, mas o tempo do Medium (30s) permanece o da classe difficulty
            self.zombie_speed = 5
            spawn_tempo = 1000  # A cada 1 segundo
        else:  # HARD
            self.zombie_speed = 5
            spawn_tempo = 1000  # A cada 1 segundo

        # Timer para contagem regressiva do nível
        self.TIMER_EVENT = pygame.USEREVENT + 2
        pygame.time.set_timer(self.TIMER_EVENT, 1000)

        # Cria um evento customizado para o tempo de spawn dos zumbis
        self.SPAWN_ZOMBIE = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWN_ZOMBIE, spawn_tempo)

    def run(self):
        while True:
            # 1. Captura de Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Evento do Timer: Nasce um zumbi
                if event.type == self.SPAWN_ZOMBIE:
                    z = Zombie()
                    z.speed = self.zombie_speed if z.speed > 0 else -self.zombie_speed
                    self.zombies.append(z)

                # Evento de Contagem Regressiva do Tempo de Sobrevivência
                if event.type == self.TIMER_EVENT:
                    self.time_remaining -= 1
                    if self.time_remaining <= 0:
                        # O tempo acabou e o player sobreviveu! Zera a pontuação para a próxima se quiser, ou mantém. Aqui vamos para a vitória.
                        Victory(self.game).run()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()
                        novo_tiro = Shot(self.player.rect.center, self.player.facing_right)
                        self.shots.append(novo_tiro)

            # 2. Atualiza a lógica do jogo
            self.player.update()

            for shot in self.shots[:]:
                shot.update()
                if shot.rect.x < 0 or shot.rect.x > pygame.display.get_surface().get_width():
                    self.shots.remove(shot)

            for zombie in self.zombies[:]:
                zombie.update()
                if zombie.is_dead:
                    self.zombies.remove(zombie)

            self.check_collisions()

            # 3. Desenha na tela
            self.game.window.fill((0, 0, 0))
            self.background.draw(self.game.window)

            for zombie in self.zombies:
                zombie.draw(self.game.window)

            for shot in self.shots:
                shot.draw(self.game.window)

            self.player.draw(self.game.window)

            # Placar e Cronômetro na tela
            fonte = pygame.font.Font(None, 36)
            texto_score = fonte.render(f"Score: {self.game.score}", True, (255, 255, 255))
            texto_tempo = fonte.render(f"Tempo: {self.time_remaining}s", True, (255, 255, 0))

            self.game.window.blit(texto_score, (20, 20))
            self.game.window.blit(texto_tempo, (20, 60))

            # 4. Atualiza o display e crava em 60 FPS
            pygame.display.flip()
            self.clock.tick(60)

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
                    GameOver(self.game).run()