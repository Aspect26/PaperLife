from city.buildings.building import Building


class GameState(object):
    pass


class NormalState(GameState):
    pass


class PlacingNewBuildingState(GameState):

    def __init__(self, building: Building):
        self.building = building
