import pygame
from code.const import WINDOW_WIDTH


class Player:
    def __init__(self):
        # Carrega as planilhas de sprites
        self.run_sheet = pygame.image.load('./assets/Run.png').convert_alpha()
        self.idle_sheet = pygame.image.load('./assets/Idle.png').convert_alpha()

        # Recorta as planilhas em quadros (8 para Run, 6 para Idle)
        self.run_frames = self.cut_sprites(self.run_sheet, 8)
        self.idle_frames = self.cut_sprites(self.idle_sheet, 6)

        # Variáveis de animação
        self.current_frame = 0
        self.animation_speed = 0.2
        self.image = self.idle_frames[0]

        # Posição e física
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, 500))
        self.speed = 5
        self.facing_right = True
        self.is_moving = False

    def cut_sprites(self, sheet, columns):
        """Divide a sprite sheet em uma lista de imagens individuais."""
        frames = []
        width = sheet.get_width() // columns
        height = sheet.get_height()
        for i in range(columns):
            frame = sheet.subsurface(pygame.Rect(i * width, 0, width, height))
            frames.append(frame)
        return frames

    def update(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False

        # Movimentação e direção
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.facing_right = False
            self.is_moving = True

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.facing_right = True
            self.is_moving = True

        # Limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

        self.animate()

    def animate(self):
        self.current_frame += self.animation_speed

        # Escolhe a animação correta
        if self.is_moving:
            if self.current_frame >= len(self.run_frames):
                self.current_frame = 0
            frame_to_draw = self.run_frames[int(self.current_frame)]
        else:
            if self.current_frame >= len(self.idle_frames):
                self.current_frame = 0
            frame_to_draw = self.idle_frames[int(self.current_frame)]

        # Espelha a imagem se estiver andando para a esquerda
        if not self.facing_right:
            self.image = pygame.transform.flip(frame_to_draw, True, False)
        else:
            self.image = frame_to_draw

    def draw(self, window):
        window.blit(self.image, self.rect)