from queue import PriorityQueue

import time
from typing import List

from city.buildings.building import Building
from city.buildings.town_hall import TownHall
from events.game_events.collect_rent_event import CollectRentEvent
from events.game_events.game_event import GameEvent


class City(object):

    def __init__(self):
        self._events_queue = PriorityQueue()
        self._money = 0
        self._town_hall = TownHall(self)
        self._buildings = [self._town_hall]
        self.enqueue_game_event(CollectRentEvent(self._town_hall), 0)

    def get_money(self) -> int:
        return self._money

    def get_buildings(self) -> List[Building]:
        return self._buildings

    def add_money(self, amount: int) -> None:
        self._money += amount

    def simulate(self) -> None:
        current_seconds = round(time.time())
        while len(self._events_queue.queue) > 0:
            event_time, _ = self._events_queue.queue[0]
            if event_time < current_seconds:
                _, event = self._events_queue.get()
                event.handle()
            else:
                break

    def enqueue_game_event(self, event: GameEvent, after_time: int) -> None:
        in_time = round(time.time()) + after_time
        self._events_queue.put((in_time, event))
