#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity


class Shot(Entity):
    def __init__(self, x, y, direcao):
        super().__init__()

        self.x = x
        self.y = y
        self.velocidade = 10
        self.dano = 50
        self.direcao = direcao

    def move(self):
        self.x += self.velocidade * self.direcao