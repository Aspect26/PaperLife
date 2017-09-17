from typing import Tuple

import pygame
from pygame.rect import Rect

from city.growth import GrowthFactor
from game.constants import GameSettings
from game.json_keys import JsonKeys
from rendering.image_cache import get_image


class CityObject(object):
    def __init__(self, city, cost: int, position: Rect, income, growth_factor: GrowthFactor, image_file: str,
                 title: str):
        self._income = income
        self._growth_factor = growth_factor
        self._cost = cost
        self._position = position
        self._city = city
        self._image_path = GameSettings.Paths.Images.CityObjects + image_file
        self._title = title

    @property
    def income(self) -> int:
        return self._income

    @property
    def growth_factor(self) -> GrowthFactor:
        return self._growth_factor

    @property
    def cost(self) -> int:
        return self._cost

    @property
    def city(self):
        return self._city

    @property
    def x(self) -> int:
        return self._position.x

    @property
    def y(self) -> int:
        return self._position.y

    @property
    def width(self) -> int:
        return self._position.width

    @property
    def height(self) -> int:
        return self._position.height

    @property
    def position(self) -> Rect:
        return self._position

    @property
    def image_path(self) -> str:
        return self._image_path

    @property
    def title(self) -> str:
        return self._title

    def set_position(self, position: Tuple) -> None:
        self._position.x = position[0]
        self._position.y = position[1]

    def is_populated(self):
        return False

    def render(self, screen: pygame.Surface) -> None:
        building_picture = get_image(self.image_path)
        building_picture = pygame.transform.scale(building_picture, (
            self.width * GameSettings.Game.FIELD_SIZE, self.height * GameSettings.Game.FIELD_SIZE))
        screen.blit(building_picture, (self.x * GameSettings.Game.FIELD_SIZE, self.y * GameSettings.Game.FIELD_SIZE))

    def jsonify(self) -> dict:
        return {
            JsonKeys.Building.Id: type(self).__name__,
            JsonKeys.Position.X: self.position.x,
            JsonKeys.Position.Y: self.position.y,
        }

    def load(self, data: dict) -> None:
        from city.objects.buildings.buildings import TownHall, FlatHouse1, FlatHouse2, FlatHouse3
        # NOTE: the above imports need to be here because of loading through 'reflection'
        self._position.x = data[JsonKeys.Position.X]
        self._position.y = data[JsonKeys.Position.Y]
