from city.buildings.building import Building


class TownHall(Building):

    def __init__(self, city):
        super().__init__(10, 10, city, 5, 5, 'town_hall.jpg', 'Town Hall')
