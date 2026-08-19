import pygame

class Shot:
    def __init__(self, player_center, facing_right):
        # Cria um retângulo pequeno para representar o projétil
        self.image = pygame.Surface((12, 4))
        self.image.fill((255, 204, 0))

        # Define a direção e velocidade do disparo
        self.speed = 15 if facing_right else -15

        offset_x = 55 if facing_right else -55

        # player_center[1] + 30 abaixa o tiro em direção ao cano da arma
        self.rect = self.image.get_rect(center=(player_center[0] + offset_x, player_center[1] + 30))

    def update(self):
        # Desloca o tiro horizontalmente
        self.rect.x += self.speed

    def draw(self, window):
        window.blit(self.image, self.rect)