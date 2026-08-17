#!/usr/bin/python
# -*- coding: utf-8 -*-


class Difficulty:
    def __init__(self):
        self.name = None
        self.duration = None
        self.zombie_count = None
        self.spawn_interval = None

    def configure(self, name):
        self.name = name

        if name == "EASY":
            self.duration = 20
            self.zombie_count = 5
            self.spawn_interval = 4

        elif name == "MEDIUM":
            self.duration = 40
            self.zombie_count = 7
            self.spawn_interval = 3.5

        elif name == "HARD":
            self.duration = 60
            self.zombie_count = 9
            self.spawn_interval = 3
