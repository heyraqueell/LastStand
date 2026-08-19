import pygame
import random


class Zombie:
    def __init__(self):
        escala = 2.5

        # Sorteia qual dos 3 zumbis será criado
        self.tipo = random.choice(["homem", "mulher1", "mulher2"])

        if self.tipo == "homem":
            caminho_walk = './assets/zombies/Walk.png'
            caminho_dead = './assets/zombies/Dead.png'
            colunas_walk = 10
            colunas_dead = 5  # Ajuste Dead.png
        elif self.tipo == "mulher1":
            caminho_walk = './assets/zombies/WalkWoman.png'
            caminho_dead = './assets/zombies/DeadWoman.png'
            colunas_walk = 12
            colunas_dead = 5  # Ajuste DeadWoman.png
        else:
            caminho_walk = './assets/zombies/WalkWoman2.png'
            caminho_dead = './assets/zombies/DeadWoman2.png'
            colunas_walk = 10
            colunas_dead = 5  # Ajuste DeadWoman2.png

        # Carrega os frames de caminhada e de morte
        img_walk = pygame.image.load(caminho_walk).convert_alpha()
        img_dead = pygame.image.load(caminho_dead).convert_alpha()

        self.walk_frames = self.carregar_frames(img_walk, colunas_walk, escala)
        self.dead_frames = self.carregar_frames(img_dead, colunas_dead, escala)

        # Estados do zumbi
        self.frames = self.walk_frames
        self.current_frame = 0
        self.animation_speed = 0.15
        self.is_dying = False
        self.is_dead = False

        self.image = self.frames[0]

        tela_largura = pygame.display.get_surface().get_width()
        tela_altura = pygame.display.get_surface().get_height()

        # Sorteia se nasce na Esquerda ou na Direita
        lado = random.choice(["esquerda", "direita"])

        if lado == "esquerda":
            self.rect = self.image.get_rect(midbottom=(-50, tela_altura - 70))
            self.speed = 2
            self.facing_right = True
        else:
            self.rect = self.image.get_rect(midbottom=(tela_largura + 50, tela_altura - 70))
            self.speed = -2
            self.facing_right = False

    def carregar_frames(self, sheet, colunas, escala):
        frames = []
        largura = sheet.get_width() // colunas
        altura = sheet.get_height()

        for i in range(colunas):
            frame_original = sheet.subsurface(pygame.Rect(i * largura, 0, largura, altura))
            frame_limpo = pygame.Surface((largura, altura), pygame.SRCALPHA).convert_alpha()
            frame_limpo.blit(frame_original, (0, 0))
            tamanho_escalado = (int(largura * escala), int(altura * escala))
            frame_ampliado = pygame.transform.scale(frame_limpo, tamanho_escalado)
            frames.append(frame_ampliado)

        return frames

    def die(self):
        """Ativa a animação de morte"""
        if not self.is_dying:
            self.is_dying = True
            self.frames = self.dead_frames
            self.current_frame = 0
            self.speed = 0  # Para de andar imediatamente ao morrer

    def update(self):
        if self.is_dead:
            return

        # Movimentação (só anda se não estiver morrendo)
        if not self.is_dying:
            self.rect.x += self.speed

        # Animação
        self.current_frame += self.animation_speed

        if self.is_dying:
            # Se chegou ao último frame da morte, trava no chão
            if self.current_frame >= len(self.frames):
                self.current_frame = len(self.frames) - 1
                self.is_dead = True  # Marca que o zumbi terminou de cair e está morto no chão
        else:
            if self.current_frame >= len(self.frames):
                self.current_frame = 0

        frame_to_draw = self.frames[int(self.current_frame)]

        # Espelha a imagem dependendo do lado
        if not self.facing_right:
            self.image = pygame.transform.flip(frame_to_draw, True, False)
        else:
            self.image = frame_to_draw

    def draw(self, window):
        window.blit(self.image, self.rect)