from typing import Tuple

import pygame
from pygame.surface import Surface

from ui.component import UIComponent


class Window(UIComponent):
    def __init__(self, position: Tuple, size: Tuple):
        super().__init__(position, size)
        self._components = []

    def add_component(self, component: UIComponent):
        component.position = self._fit_component_position(component.position, component.size)
        self._components.append(component)

    def render(self, screen: Surface) -> None:
        self._render_background(screen)
        self._render_border(screen)
        for component in self._components:
            component.render(screen)

    def _render_background(self, screen: Surface) -> None:
        pygame.draw.rect(screen, (255, 255, 255), (self.position[0], self.position[1], self.size[0], self.size[1]), 0)

    def _render_border(self, screen: Surface) -> None:
        pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.size[0], self.size[1]), 3)

    def _fit_component_position(self, position: Tuple, size: Tuple) -> Tuple:
        pos_x = self.position[0] + self.size[0] - size[0] if (
            position[0] + size[0] > self.size[0]) else position[0] + self.position[0]
        pos_y = position[1] + self.position[1]
        return pos_x, pos_y
