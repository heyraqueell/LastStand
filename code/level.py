#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.background import Background
from code.game_over import GameOver
from code.player import Player
from code.shot import Shot
from code.victory import Victory
from code.zombie import Zombie


class Level:
    def __init__(self, difficulty, game):
        self.game = game
        self.difficulty_name = difficulty.name

        self.duration = difficulty.duration
        self.time_remaining = self.duration

        self.player = Player()
        self.background = Background(self.duration)

        self.zombies = []
        self.shots = []

        self.clock = pygame.time.Clock()

        self.zombie_speed = 2
        spawn_interval = 2000

        if self.difficulty_name == "MEDIUM":
            self.zombie_speed = 5
            spawn_interval = 1000

        elif self.difficulty_name == "HARD":
            self.zombie_speed = 5
            spawn_interval = 1000

        self.timer_event = pygame.USEREVENT + 2
        pygame.time.set_timer(self.timer_event, 1000)

        self.spawn_zombie_event = pygame.USEREVENT + 1
        pygame.time.set_timer(
            self.spawn_zombie_event,
            spawn_interval
        )

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == self.spawn_zombie_event:
                self.spawn_zombie()

            if event.type == self.timer_event:
                self.time_remaining -= 1

                if self.time_remaining <= 0:
                    Victory(self.game).run()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()

                    shot = Shot(
                        self.player.rect.center,
                        self.player.facing_right
                    )

                    self.shots.append(shot)

    def update(self):
        self.player.update()

        self.update_shots()
        self.update_zombies()

        self.check_collisions()

    def update_shots(self):
        screen_width = pygame.display.get_surface().get_width()

        for shot in self.shots[:]:
            shot.update()

            if shot.rect.right < 0 or shot.rect.left > screen_width:
                self.shots.remove(shot)

    def update_zombies(self):
        for zombie in self.zombies[:]:
            zombie.update()

            if zombie.is_dead:
                self.zombies.remove(zombie)

    def spawn_zombie(self):
        zombie = Zombie()

        if zombie.speed > 0:
            zombie.speed = self.zombie_speed
        else:
            zombie.speed = -self.zombie_speed

        self.zombies.append(zombie)

    def check_collisions(self):
        self.check_shot_collisions()
        self.check_player_collisions()

    def check_shot_collisions(self):
        for shot in self.shots[:]:
            for zombie in self.zombies[:]:

                if zombie.is_dying:
                    continue

                if shot.rect.colliderect(zombie.rect):
                    if shot in self.shots:
                        self.shots.remove(shot)

                    zombie.die()
                    self.game.score += 100

    def check_player_collisions(self):
        for zombie in self.zombies:

            if zombie.is_dying:
                continue

            distance_x = abs(
                zombie.rect.centerx - self.player.rect.centerx
            )

            if distance_x < 30:
                GameOver(self.game).run()

    def draw(self):
        self.game.window.fill((0, 0, 0))
        self.background.draw(self.game.window)

        for zombie in self.zombies:
            zombie.draw(self.game.window)

        for shot in self.shots:
            shot.draw(self.game.window)

        self.player.draw(self.game.window)

        self.draw_hud()

    def draw_hud(self):
        font = pygame.font.Font(None, 36)

        score_text = font.render(
            f"Score: {self.game.score}",
            True,
            (255, 255, 255)
        )

        time_text = font.render(
            f"Tempo: {self.time_remaining}s",
            True,
            (255, 255, 0)
        )

        self.game.window.blit(score_text, (20, 20))
        self.game.window.blit(time_text, (20, 60))