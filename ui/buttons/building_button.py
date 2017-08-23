from typing import Tuple

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from game.data import BuildingData
from game.state import PlacingNewBuildingState
from ui.component import UIComponent


class BuildingButton(UIComponent):

    def __init__(self, position: Tuple, building_type: BuildingData):
        self._WIDTH = 85
        self._HEIGHT = 100
        self._BORDER_SIZE = 2
        super().__init__(Rect(position[0], position[1], self._WIDTH, self._HEIGHT))
        self._building_type = building_type

    def handle_mouse_down(self, game, position: Tuple) -> None:
        pass

    def handle_mouse_up(self, game, position: Tuple) -> None:
        game.set_state(PlacingNewBuildingState(self._building_type.building(game.get_city())))

    def render(self, screen: Surface) -> None:
        self._render_building_image(screen)
        self._render_building_label(screen)
        self._render_border(screen)

    def _render_border(self, screen: Surface) -> None:
        pygame.draw.rect(screen, (0, 0, 0),
                         (self.position.x, self.position.y, self.position.width, self.position.height),
                         self._BORDER_SIZE)

    def _render_building_image(self, screen: Surface) -> None:
        picture = pygame.image.load(self._building_type.image_path)
        picture = pygame.transform.scale(picture, (self.position.width, self.position.width))
        screen.blit(picture, (self.position.x, self.position.y))

    def _render_building_label(self, screen: Surface) -> None:
        # TODO: move all fonts to one place
        font = pygame.font.SysFont('monospace', 10)
        label = font.render(self._building_type.title, 1, (5, 80, 200))
        screen.blit(label, (self.position.x + 2, self.position.y + self.position.width + 2))
