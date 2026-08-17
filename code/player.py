import pygame
from code.const import WINDOW_WIDTH


class Player:
    def __init__(self):
        escala = 2.5

        # 1. Carrega a imagem no tamanho ORIGINAL
        img_run_ori = pygame.image.load('./assets/Run.png').convert_alpha()
        img_idle_ori = pygame.image.load('./assets/Idle.png').convert_alpha()

        # 2. Descobre o tamanho exato de 1 quadro (original)
        largura_frame_run = img_run_ori.get_width() // 8
        altura_frame_run = img_run_ori.get_height()

        largura_frame_idle = img_idle_ori.get_width() // 7
        altura_frame_idle = img_idle_ori.get_height()

        # 3. Usa a nova função que RECORTA primeiro e AMPLIA depois
        self.run_frames = self.recortar_e_ampliar(img_run_ori, 8, largura_frame_run, altura_frame_run, escala)
        self.idle_frames = self.recortar_e_ampliar(img_idle_ori, 7, largura_frame_idle, altura_frame_idle, escala)

        # Variáveis de animação
        self.current_frame = 0
        self.animation_speed = 0.2
        self.image = self.idle_frames[0]

        # 4. Posição inicial adaptada para a largura REAL da sua tela
        tela_largura = pygame.display.get_surface().get_width()
        tela_altura = pygame.display.get_surface().get_height()

        self.rect = self.image.get_rect(midbottom=(tela_largura / 2, tela_altura - 70))

        self.speed = 5
        self.facing_right = True
        self.is_moving = False

    def recortar_e_ampliar(self, sheet, colunas, largura, altura, escala):
        """Recorta o quadro no tamanho original e depois amplia de forma limpa."""
        frames = []
        for i in range(colunas):
            # Recorta o quadro original
            frame_original = sheet.subsurface(pygame.Rect(i * largura, 0, largura, altura))

            # Cria uma superfície limpa para evitar rastro
            frame_limpo = pygame.Surface((largura, altura), pygame.SRCALPHA).convert_alpha()
            frame_limpo.blit(frame_original, (0, 0))

            # Só então amplia a imagem isolada
            tamanho_escalado = (int(largura * escala), int(altura * escala))
            frame_ampliado = pygame.transform.scale(frame_limpo, tamanho_escalado)

            frames.append(frame_ampliado)
        return frames

    def update(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False

        # Pega a largura real da tela para que o limite funcione de ponta a ponta
        tela_largura = pygame.display.get_surface().get_width()

        # Movimentação e direção
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.facing_right = False
            self.is_moving = True

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.facing_right = True
            self.is_moving = True

        # Limites da tela dinâmicos (Fim da parede invisível)
        margem = 40  # Distância que o centro do jogador pode chegar da borda

        if self.rect.centerx < margem:
            self.rect.centerx = margem

        if self.rect.centerx > tela_largura - margem:
            self.rect.centerx = tela_largura - margem

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
