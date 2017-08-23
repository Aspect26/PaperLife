import time
from queue import PriorityQueue
from typing import List, Tuple

from pygame.rect import Rect

from city.buildings.building import Building
from city.buildings.town_hall import TownHall
from events.collect_rent_event import CollectRentEvent
from events.game_event import GameEvent


class City(object):

    def __init__(self):
        self._events_queue = PriorityQueue()
        self._money = 0
        self._buildings = []
        self._occupied_fields = []

        self.add_building(TownHall(self))
        self.enqueue_game_event(CollectRentEvent(self))

    def get_money(self) -> int:
        return self._money

    def get_buildings(self) -> List[Building]:
        return self._buildings

    def is_field_occupied(self, field: Tuple):
        return field in self._occupied_fields

    def is_rectangle_ocuppied(self, rectangle: Rect):
        for x in range(rectangle.x, rectangle.x + rectangle.width, 1):
            for y in range(rectangle.y, rectangle.y + rectangle.height, 1):
                if self.is_field_occupied((x, y)):
                    return True

        return False

    def add_money(self, amount: int) -> None:
        self._money += amount

    def add_building(self, building: Building) -> None:
        self._buildings.append(building)
        for x in range(building.x, building.width + building.x):
            for y in range(building.y, building.height + building.y):
                self._occupied_fields.append((x, y))

    def simulate(self) -> None:
        current_seconds = round(time.time())
        while len(self._events_queue.queue) > 0:
            event_time, _ = self._events_queue.queue[0]
            if event_time < current_seconds:
                _, event = self._events_queue.get()
                event.handle()
            else:
                break

    def enqueue_game_event(self, event: GameEvent, after_time: int = 0) -> None:
        in_time = round(time.time()) + after_time
        self._events_queue.put((in_time, event))
