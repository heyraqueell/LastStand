#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.entity import Entity
from code.shot import Shot


class Player(Entity):
    def __init__(self):
        super().__init__()

        self.vida = 100
        self.velocidade = 5
        self.direcao = 1

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.velocidade
            self.direcao = -1

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.velocidade
            self.direcao = 1

    def shoot(self):
        return Shot(self.x, self.y, self.direcao)

    def take_damage(self, dano):
        self.vida -= dano