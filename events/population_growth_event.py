from random import randint

from events.game_event import GameEvent


class PopulationGrowthEvent(GameEvent):

    def __init__(self, city):
        self._city = city

    def handle(self):
        growth_factor = self._city.get_growth_factor()
        for building in self._city.get_buildings():
            for empty_apartment in range(building.population, building.max_population, 1):
                if randint(0, 100) / 100.0 < growth_factor.food and randint(0, 100) / 100.0 < growth_factor.health_care:
                    building.increase_population()

        self._city.enqueue_game_event(self, 60 * 5)
