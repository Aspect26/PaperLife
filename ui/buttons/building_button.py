from typing import Tuple

import pygame
from pygame.surface import Surface

from game.data import BuildingData
from ui.component import UIComponent


class BuildingButton(UIComponent):
    def __init__(self, position: Tuple, building_type: BuildingData):
        self._SIZE = 85, 100
        self._BORDER_SIZE = 2
        super().__init__(position, self._SIZE)
        self._building_type = building_type

    def render(self, screen: Surface) -> None:
        self._render_building_image(screen)
        self._render_building_label(screen)
        self._render_border(screen)

    def _render_border(self, screen: Surface) -> None:
        pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.size[0], self.size[1]),
                         self._BORDER_SIZE)

    def _render_building_image(self, screen: Surface) -> None:
        picture = pygame.image.load(self._building_type.image_path)
        picture = pygame.transform.scale(picture, (self.size[0], self.size[0]))
        screen.blit(picture, (self.position[0], self.position[1]))

    def _render_building_label(self, screen: Surface) -> None:
        # TODO: move all fonts to one place
        font = pygame.font.SysFont('monospace', 10)
        label = font.render(self._building_type.title, 1, (5, 80, 200))
        screen.blit(label, (self.position[0] + 2, self.position[1] + self.size[0] + 2))
