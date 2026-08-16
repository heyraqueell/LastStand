#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.background import Background


class Level(Background):
    def __init__(self):
        self.duration = None
        self.time_remaining = None
        self.player = None
        self.zombies = None
        self.shots = None

    def run(self, ):
        pass

    def spawn_zombie(self, ):
        pass

    def update(self, ):
        pass

    def check_collisions(self, ):
        pass
