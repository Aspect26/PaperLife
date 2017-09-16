from typing import List, Type

from city.objects.buildings.buildings import FlatHouse1, FlatHouse3, FlatHouse2
from city.objects.city_object import CityObject
from city.objects.road import Road


class CityObjectData(object):

    def __init__(self, city_object: Type[CityObject]):
        self.city_object = city_object
        city_object = city_object(None)
        self.title = city_object.title
        self.cost = city_object.cost
        self.image_path = city_object.image_path

_PURCHASABLE_CITY_OBJECTS = [
    CityObjectData(Road),
    CityObjectData(FlatHouse1),
    CityObjectData(FlatHouse2),
    CityObjectData(FlatHouse3),
]


def get_purchasable_buildings() -> List[CityObjectData]:
    return _PURCHASABLE_CITY_OBJECTS
