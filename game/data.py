from typing import List, Type

from city.buildings.building import Building
from city.buildings.buildings import TownHall, FlatHouse1, FlatHouse3, FlatHouse2


class BuildingData(object):

    def __init__(self, building: Type[Building]):
        self.building = building
        building = building(None)
        self.title = building.title
        self.cost = building.cost
        self.image_path = building.image_path

_PURCHASABLE_BUILDINGS = [
    BuildingData(FlatHouse1),
    BuildingData(FlatHouse2),
    BuildingData(FlatHouse3),
]


def get_purchasable_buildings() -> List[BuildingData]:
    return _PURCHASABLE_BUILDINGS
