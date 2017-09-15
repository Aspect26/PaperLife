import heapq
import time
from typing import List, Tuple

from pygame.rect import Rect

from city.growth import GrowthFactor
from city.objects.buildings.building import Building
from city.objects.buildings.buildings import TownHall, FlatHouse1, FlatHouse2, FlatHouse3
# The above imports need to be here because of 'reflection' loading
from city.objects.city_object import CityObject
from events.collect_rent_event import CollectRentEvent
from events.game_event import GameEvent
from events.population_growth_event import PopulationGrowthEvent
from game.json_keys import JsonKeys


class City(object):

    def __init__(self):
        self._money = 30000
        self._city_objects = []
        self._events_heap = []
        self._occupied_fields = []

        self.add_building(TownHall(self))
        self.enqueue_game_event(CollectRentEvent(self))
        self.enqueue_game_event(PopulationGrowthEvent(self))

    def get_money(self) -> int:
        return self._money

    def get_population(self) -> int:
        return sum(city_object.population for city_object in self._city_objects)

    def get_growth_factor(self) -> GrowthFactor:
        food_total = 0
        health_care_total = 0
        for city_object in self._city_objects:
            food_total += city_object.growth_factor.food
            health_care_total += city_object.growth_factor.health_care

        population = self.get_population()
        food_factor = 0.5 if food_total / population > 0.5 else food_total / population
        health_factor = 0.5 if health_care_total / population > 0.5 else health_care_total / population
        return GrowthFactor(food_factor, health_factor)

    def get_city_objects(self) -> List[CityObject]:
        return self._city_objects

    def _set_money(self, money: int) -> None:
        self._money = money

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
        self._city_objects.append(building)
        self._money -= building.cost
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

    def enqueue_game_event(self, event: GameEvent, event_time: int = 0, specific: bool = False) -> None:
        if not specific:
            event_time += round(time.time())
        heapq.heappush(self._events_heap, (event_time, event))

    def jsonify(self) -> dict:
        return {
            JsonKeys.City.TotalMoney: self.get_money(),
            JsonKeys.City.Objects: [city_object.jsonify() for city_object in self._city_objects],
            JsonKeys.City.Events: [{JsonKeys.Event.EventTime: event_time, JsonKeys.Event.Event: type(event).__name__}
                                   for event_time, event in self._events_heap],
        }

    def load(self, data: dict) -> None:
        self._set_money(data[JsonKeys.City.TotalMoney])
        self._city_objects = []
        for building in data[JsonKeys.City.Objects]:
            building_obj = globals()[building[JsonKeys.Building.Id]](self)
            building_obj.load(building)
            self._city_objects.append(building_obj)

        self._events_heap = []
        for event in data[JsonKeys.City.Events]:
            event_time = event[JsonKeys.Event.EventTime]
            event_obj = globals()[event[JsonKeys.Event.Event]](self)
            self.enqueue_game_event(event_obj, event_time, True)

        self._recompute_occupied_fields()

    def _recompute_occupied_fields(self):
        self._occupied_fields = []
        for city_object in self._city_objects:
            for x in range(city_object.x, city_object.x + city_object.width):
                for y in range(city_object.y, city_object.y + city_object.height):
                    self._occupied_fields.append((x, y))
