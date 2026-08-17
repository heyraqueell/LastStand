#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.player import Player
from code.background import Background


class Level:
    def __init__(self, difficulty):
        self.duration = difficulty.duration
        self.time_remaining = difficulty.duration

        self.player = Player()
        self.background = Background()

        self.zombies = []
        self.shots = []

    def run(self):
        pass

    def spawn_zombie(self):
        pass

    def update(self):
        pass

    def check_collisions(self):
        pass