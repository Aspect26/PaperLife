from pygame.rect import Rect

from city.growth import GrowthFactor
from city.objects.city_object import CityObject


class Road(CityObject):

    def __init__(self, city):
        position = Rect(0, 0, 1, 1)
        super().__init__(city, 100, position, 0, GrowthFactor(0, 0), 'road_2s.png', '')
