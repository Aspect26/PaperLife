from typing import Tuple

from pygame.rect import Rect

from city.growth import GrowthFactor
from game.constants import GameSettings
from game.json_keys import JsonKeys


class Building(object):
    def __init__(self, rent: int, max_population: int, cost: int, growth_factor: GrowthFactor, city, position: Rect,
                 image_file: str, title: str):
        self._rent = rent
        self._max_population = max_population
        self._population = 0
        self._cost = cost
        self._growth_factor = growth_factor
        self._city = city
        self._position = position
        self._image_path = GameSettings.Paths.Images.Buildings + image_file
        self._title = title

    @property
    def rent(self) -> int:
        return self._rent

    @property
    def max_population(self) -> int:
        return self._max_population

    @property
    def population(self) -> int:
        return self._population

    @property
    def cost(self) -> int:
        return self._cost

    @property
    def growth_factor(self) -> GrowthFactor:
        return self._growth_factor

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

    def increase_population(self):
        if not self._population >= self._max_population:
            self._population += 1

    def jsonify(self) -> dict:
        return {
            JsonKeys.Building.Id: type(self).__name__,
            JsonKeys.Building.Population: self._population,
            JsonKeys.Position.X: self.position.x,
            JsonKeys.Position.Y: self.position.y,
        }

    def load(self, data: dict) -> None:
        self._population = data[JsonKeys.Building.Population]
        self._position.x = data[JsonKeys.Position.X]
        self._position.y = data[JsonKeys.Position.Y]
