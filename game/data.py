from typing import List, Type

from city.buildings.building import Building
from city.buildings.town_hall import TownHall


class BuildingData(object):

    def __init__(self, building: Type[Building]):
        self.building = building
        building = building(None)
        self.title = building.title
        self.image_path = building.image_path

_ALL_BUILDINGS = [
    BuildingData(TownHall),
    BuildingData(TownHall),
]


def get_all_buildings() -> List[BuildingData]:
    return _ALL_BUILDINGS
