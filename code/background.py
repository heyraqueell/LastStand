#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame


class Background:
    def __init__(self):
        self.image = pygame.image.load(
            './assets/background.png'
        ).convert()

        self.image = pygame.transform.scale(
            self.image,
            (800, 600)
        )

    def draw(self, window):
        window.blit(self.image, (0, 0))