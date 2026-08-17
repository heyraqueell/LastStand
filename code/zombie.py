import pygame
import random


class Zombie:
    def __init__(self):
        escala = 2.5

        # Sorteia qual dos 3 zumbis será criado
        tipo = random.choice(["homem", "mulher1", "mulher2"])

        if tipo == "homem":
            img_ori = pygame.image.load('./assets/zombies/Walk.png').convert_alpha()
            colunas = 10
        elif tipo == "mulher1":
            img_ori = pygame.image.load('./assets/zombies/WalkWoman.png').convert_alpha()
            colunas = 12  # Ajustado para 12 quadros da WalkWoman
        else:
            img_ori = pygame.image.load('./assets/zombies/WalkWoman2.png').convert_alpha()
            colunas = 10  # Ajustado para 10 quadros da WalkWoman2

        # Descobre o tamanho exato de 1 quadro
        largura_frame = img_ori.get_width() // colunas
        altura_frame = img_ori.get_height()

        # Recorta e amplia cada quadro de forma limpa (sem rastro)
        self.frames = []
        for i in range(colunas):
            frame_original = img_ori.subsurface(pygame.Rect(i * largura_frame, 0, largura_frame, altura_frame))
            frame_limpo = pygame.Surface((largura_frame, altura_frame), pygame.SRCALPHA).convert_alpha()
            frame_limpo.blit(frame_original, (0, 0))
            tamanho_escalado = (int(largura_frame * escala), int(altura_frame * escala))
            frame_ampliado = pygame.transform.scale(frame_limpo, tamanho_escalado)
            self.frames.append(frame_ampliado)

        # Variáveis de animação
        self.current_frame = 0
        self.animation_speed = 0.15
        self.image = self.frames[0]

        tela_largura = pygame.display.get_surface().get_width()
        tela_altura = pygame.display.get_surface().get_height()

        # Sorteia se nasce na Esquerda ou na Direita
        lado = random.choice(["esquerda", "direita"])

        if lado == "esquerda":
            self.rect = self.image.get_rect(midbottom=(-50, tela_altura - 70))
            self.speed = 2  # Anda para a direita
            self.facing_right = True
        else:
            self.rect = self.image.get_rect(midbottom=(tela_largura + 50, tela_altura - 70))
            self.speed = -2  # Anda para a esquerda
            self.facing_right = False

    def update(self):
        # Movimentação
        self.rect.x += self.speed

        # Animação de caminhada
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.frames):
            self.current_frame = 0

        frame_to_draw = self.frames[int(self.current_frame)]

        # Espelha a imagem dependendo do lado para onde ele está andando
        if not self.facing_right:
            self.image = pygame.transform.flip(frame_to_draw, True, False)
        else:
            self.image = frame_to_draw

    def draw(self, window):
        window.blit(self.image, self.rect)