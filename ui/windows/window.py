from typing import Tuple

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from rendering.colors import Colors
from ui.component import UIComponent
from ui.rectangular_component import RectangularComponent


class Window(RectangularComponent):

    def __init__(self, position: Rect):
        super().__init__(position, None)
        self._components = []

    def add_component(self, component: UIComponent):
        component.position = self._fit_component_position(component.position)
        self._components.append(component)

    def handle_mouse_down(self, game, position: Tuple) -> None:
        for component in reversed(self._components):
            if component.position.collidepoint(position):
                component.handle_mouse_down(game, position)
                break

    def handle_mouse_up(self, game, position: Tuple) -> None:
        for component in reversed(self._components):
            if component.position.collidepoint(position):
                component.handle_mouse_up(game, position)
                break

    def handle_mouse_over(self, screen, position: Tuple) -> None:
        for component in reversed(self._components):
            if component.position.collidepoint(position):
                component.handle_mouse_over(screen, position)
                break

    def render(self, screen: Surface) -> None:
        self._render_background(screen)
        self._render_border(screen)
        for component in self._components:
            component.render(screen)

    def is_at(self, position: Tuple):
        if super().is_at(position):
            return True
        for child in self._components:
            if child.is_at(position):
                return True

    def _render_background(self, screen: Surface) -> None:
        pygame.draw.rect(screen, Colors.White,
                         (self.position.x, self.position.y, self.position.width, self.position.height), 0)

    def _render_border(self, screen: Surface) -> None:
        pygame.draw.rect(screen, Colors.Black,
                         (self.position.x, self.position.y, self.position.width, self.position.height), 3)

    def _fit_component_position(self, position: Rect) -> Rect:
        pos_x = self.position.x + self.position.width - position.width if (
            position.x + position.width > self.position.width) else position.x + self.position.x

        # TODO: finish this y coord if the x is working
        # TODO: Yes it is!
        pos_y = position.y + self.position.y
        return Rect(pos_x, pos_y, position.width, position.height)
