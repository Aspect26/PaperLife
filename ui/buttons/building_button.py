from typing import Tuple

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from game.data import CityObjectData
from game.state import PlacingNewBuildingState
from rendering.colors import Colors
from rendering.fonts import Fonts
from rendering.image_cache import get_image
from ui.rectangular_component import RectangularComponent


class BuildingButton(RectangularComponent):

    def __init__(self, position: Tuple, building_type: CityObjectData):
        self._WIDTH = 85
        self._HEIGHT = 100
        self._BORDER_SIZE = 2
        description = 'Cost: {0}'.format(building_type.cost)
        super().__init__(Rect(position[0], position[1], self._WIDTH, self._HEIGHT), description)
        self._building_type = building_type

    def handle_mouse_down(self, game, position: Tuple) -> None:
        pass

    def handle_mouse_up(self, game, position: Tuple) -> None:
        if self._building_type.cost <= game.get_city().get_money():
            game.set_state(PlacingNewBuildingState(self._building_type.city_object(game.get_city())))

    def render(self, screen: Surface) -> None:
        self._render_building_image(screen)
        self._render_building_label(screen)
        self._render_border(screen)

    def _render_border(self, screen: Surface) -> None:
        pygame.draw.rect(screen, Colors.Black,
                         (self.position.x, self.position.y, self.position.width, self.position.height),
                         self._BORDER_SIZE)

    def _render_building_image(self, screen: Surface) -> None:
        picture = get_image(self._building_type.image_path)
        picture = pygame.transform.scale(picture, (self.position.width, self.position.width))
        screen.blit(picture, (self.position.x, self.position.y))

    def _render_building_label(self, screen: Surface) -> None:
        font = Fonts.SMALL_FONT
        label = font.render(self._building_type.title, 1, Colors.Blue)
        screen.blit(label, (self.position.x + 2, self.position.y + self.position.width + 2))
