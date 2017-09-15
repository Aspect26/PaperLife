from events.game_event import GameEvent


class CollectRentEvent(GameEvent):

    def __init__(self, city):
        self._city = city

    def handle(self):
        total_income = 0
        for building in self._city.get_city_objects():
            total_income += building.income * building.population

        self._city.add_money(total_income)
        # TODO: make this constant a !named! constant
        self._city.enqueue_game_event(self, 10)
