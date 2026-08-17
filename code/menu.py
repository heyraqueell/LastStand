#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WINDOW_WIDTH, COLOR_RED, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, game):
        self.game = game
        self.window = game.window
        self.surf = pygame.image.load('./assets/menuHeader.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.selected_option = 0

    def run(self):
        pygame.mixer.music.load('./assets/theme.mp3')
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(
                95,
                "LAST",
                COLOR_RED,
                ((WINDOW_WIDTH / 2), 150)
            )

            self.menu_text(
                90,
                "STAND",
                COLOR_RED,
                ((WINDOW_WIDTH / 2), 230)
            )

            for i in range(len(MENU_OPTION)):
                if i == self.selected_option:
                    self.menu_text(
                        30,
                        MENU_OPTION[i],
                        COLOR_RED,
                        ((WINDOW_WIDTH / 2), 340 + 45 * i)
                    )
                else:
                    self.menu_text(
                        30,
                        MENU_OPTION[i],
                        COLOR_WHITE,
                        ((WINDOW_WIDTH / 2), 340 + 45 * i)
                    )

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        self.selected_option += 1

                    if event.key == pygame.K_UP:
                        self.selected_option -= 1

                    if self.selected_option < 0:
                        self.selected_option = len(MENU_OPTION) - 1

                    if self.selected_option >= len(MENU_OPTION):
                        self.selected_option = 0

                    if event.key == pygame.K_RETURN:
                        self.select_difficulty()

            pygame.display.flip()

    def select_difficulty(self):
        pass

    def menu_text(
            self,
            text_size: int,
            text: str,
            text_color: tuple,
            text_center_pos: tuple
    ):
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter",
            size=text_size
        )

        text_surf: Surface = text_font.render(
            text,
            True,
            text_color
        ).convert_alpha()

        text_rect: Rect = text_surf.get_rect(
            center=text_center_pos
        )

        self.window.blit(
            source=text_surf,
            dest=text_rect
        )