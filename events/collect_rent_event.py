from city.buildings.building import Building
from events.game_event import GameEvent


class CollectRentEvent(GameEvent):

    def __init__(self, building: Building):
        self._building = building

    def handle(self):
        rent = self._building.rent
        repeat_time = self._building.rent_time
        self._building.city.add_money(rent)
        self._building.city.enqueue_game_event(self, repeat_time)