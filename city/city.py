import heapq
import time
from typing import List, Tuple

from pygame.rect import Rect

from city.buildings.building import Building
from city.buildings.town_hall import TownHall
from city.growth import GrowthFactor
from events.collect_rent_event import CollectRentEvent
from events.game_event import GameEvent
from events.population_growth_event import PopulationGrowthEvent
from game.json_keys import JsonKeys


class City(object):
    def __init__(self):
        self._events_heap = []
        self._money = 0
        self._buildings = []
        self._occupied_fields = []

        self.add_building(TownHall(self))
        self.enqueue_game_event(CollectRentEvent(self))
        self.enqueue_game_event(PopulationGrowthEvent(self))

    def get_money(self) -> int:
        return self._money

    def get_population(self) -> int:
        return sum(building.population for building in self.get_buildings())

    def get_growth_factor(self) -> GrowthFactor:
        food_total = 0
        health_care_total = 0
        for building in self.get_buildings():
            food_total += building.growth_factor.food
            health_care_total += building.growth_factor.health_care

        population = self.get_population()
        food_factor = 0.5 if food_total / population > 0.5 else food_total / population
        health_factor = 0.5 if health_care_total / population > 0.5 else health_care_total / population
        return GrowthFactor(food_factor, health_factor)

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
        while len(self._events_heap) > 0:
            event_time, _ = self._events_heap[0]
            if event_time < current_seconds:
                _, event = heapq.heappop(self._events_heap)
                event.handle()
            else:
                break

    def enqueue_game_event(self, event: GameEvent, after_time: int = 0) -> None:
        in_time = round(time.time()) + after_time
        heapq.heappush(self._events_heap, (in_time, event))

    def jsonify(self) -> dict:
        return {
            JsonKeys.City.TotalMoney: self.get_money(),
            JsonKeys.City.Buildings: [building.jsonify() for building in self.get_buildings()],
            JsonKeys.City.Events: [{JsonKeys.Event.EventTime: event_time, JsonKeys.Event.Event: type(event).__name__}
                                   for event_time, event in self._events_heap],
        }
