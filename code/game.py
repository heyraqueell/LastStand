import pygame

from code.const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.level import Level
from code.difficulty import Difficulty
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        self.level = None
        self.difficulty = None

    def run(self):
        menu = Menu(self)
        menu.run()

    def start_game(self):
        self.level = Level(self.difficulty, self)
        self.level.run()

    def game_over(self):
        pass

    def victory(self):
        pass