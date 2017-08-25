from typing import Tuple

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from game.constants import GameSettings
from rendering.colors import Colors
from rendering.fonts import Fonts
from ui.component import UIComponent


class TopToolbar(UIComponent):

    def __init__(self, city):
        super().__init__(Rect(0, 0, GameSettings.Screen.WIDTH, 40))
        self._INDENT = self.position.height
        self._BORDER_POINTS = [
            (self.position.x, self.position.y),
            (self.position.x + self._INDENT, self.position.y + self.position.height),
            (self.position.x + self.position.width - self._INDENT, self.position.y + self.position.height),
            (self.position.x + self.position.width, self.position.y),
        ]
        self._city = city

    def handle_mouse_up(self, game, position: Tuple) -> None:
        pass

    def handle_mouse_down(self, game, position: Tuple) -> None:
        pass

    def render(self, screen: Surface) -> None:
        self._render_background(screen)
        self._render_border(screen)
        self._render_money(screen)
        self._render_population(screen)
        self._render_growth_factor(screen)

    def _render_background(self, screen: Surface) -> None:
        pygame.draw.polygon(screen, (255, 255, 255), self._BORDER_POINTS)

    def _render_border(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, (0, 0, 0), self._BORDER_POINTS, 2)

    def _render_money(self, screen: pygame.Surface) -> None:
        label = Fonts.LARGE_FONT.render('Money: ' + str(self._city.get_money()) + '€', 1, Colors.Blue)
        screen.blit(label, (self.position.x + 50, self.position.y + 10))

    def _render_population(self, screen: pygame.Surface) -> None:
        label = Fonts.LARGE_FONT.render('Population: ' + str(self._city.get_population()), 1, Colors.Blue)
        screen.blit(label, (self.position.x + 180, self.position.y + 10))

    def _render_growth_factor(self, screen: pygame.Surface) -> None:
        gf = self._city.get_growth_factor()
        label = Fonts.LARGE_FONT.render('GF: {0:1.2f}, {1:1.2f}'.format(gf.food, gf.health_care), 1, Colors.Blue)
        screen.blit(label, (self.position.x + 340, self.position.y + 10))
