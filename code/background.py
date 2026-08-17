import pygame
from code.const import WINDOW_WIDTH, WINDOW_HEIGHT

class Background:
    def __init__(self, duration):
        if duration == 20:  # Fácil
            image_path = './assets/fase1.png'
        elif duration == 40:  # Médio
            image_path = './assets/fase2.png'
        else:  # Difícil
            image_path = './assets/fase3.png'

        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def draw(self, window):
        window.blit(self.image, (0, 0))