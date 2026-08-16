import pygame
from code.level import Level
from code.difficulty import Difficulty
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.level = None
        self.difficulty = None

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

           # for event in pygame.event.get():
              #  if event.type == pygame.QUIT:
               #     pygame.quit()
                #    quit()

    def start_game(self):
        pass

    def game_over(self):
        pass

    def victory(self):
        pass