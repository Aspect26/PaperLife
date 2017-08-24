from pygame.rect import Rect

from city.buildings.building import Building
from city.growth import GrowthFactor


class TownHall(Building):

    def __init__(self, city):
        super().__init__(10, 3, GrowthFactor(50, 50), city, Rect(13, 9, 7, 7), 'town_hall.png', 'Town Hall')
        self._population = self.max_population
