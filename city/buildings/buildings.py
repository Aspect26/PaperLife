from pygame.rect import Rect

from city.buildings.building import Building
from city.growth import GrowthFactor

"""
Common building cost is rent * population *  100
"""


class TownHall(Building):
    def __init__(self, city):
        super().__init__(10, 3, 0, GrowthFactor(50, 50), city, Rect(13, 9, 7, 7), 'town_hall.png', 'Town Hall')
        self._population = self.max_population


class FlatHouse1(Building):
    """The 2*8 flat house"""
    def __init__(self, city):
        super().__init__(3, 16, 4800, GrowthFactor(0, 0), city, Rect(0, 0, 1, 4), 'flat_1.png', 'Flat House #1')


class FlatHouse2(Building):
    """The 3*2 flat house"""
    def __init__(self, city):
        super().__init__(3, 6, 1800, GrowthFactor(0, 0), city, Rect(0, 0, 2, 1), 'flat_2.png', 'Flat House #2')


class FlatHouse3(Building):
    """The 4*6 flat house"""
    def __init__(self, city):
        super().__init__(3, 24, 7200, GrowthFactor(0, 0), city, Rect(0, 0, 3, 2), 'flat_3.png', 'Flat House #3')
