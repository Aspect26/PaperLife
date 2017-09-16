from pygame.rect import Rect

from city.growth import GrowthFactor
from city.objects.city_object import CityObject
from game.json_keys import JsonKeys


class Building(CityObject):

    def __init__(self, income: int, max_population: int, cost: int, growth_factor: GrowthFactor, city, position: Rect,
                 image_file: str, title: str):
        super().__init__(city, cost, position, income, growth_factor, image_file, title)
        self._max_population = max_population
        self._population = 0

    @property
    def max_population(self) -> int:
        return self._max_population

    @property
    def population(self) -> int:
        return self._population

    def is_populated(self):
        return True

    def increase_population(self):
        if not self._population >= self._max_population:
            self._population += 1

    def jsonify(self) -> dict:
        data = super().jsonify()
        data.update({
            JsonKeys.Building.Population: self._population,
        })
        return data

    def load(self, data: dict) -> None:
        super().load(data)
        self._population = data[JsonKeys.Building.Population]
