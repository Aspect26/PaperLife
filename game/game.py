import pygame

from city.city import City
from events.user_events.event_dispatcher import EventDispatcher
from game.constants import GameSettings
from rendering.renderer import Renderer
from timing.game_timer import GameTimer
from ui.ui import UI


class Game(object):

    def __init__(self):
        pygame.init()
        self._done = False
        self._event_dispatcher = EventDispatcher(self)
        self._renderer = Renderer(GameSettings.Screen.WIDTH, GameSettings.Screen.HEIGHT)
        self._timer = GameTimer()
        self._city = City()  # TODO: this should be loaded from somewhere -> introduce save/load system
        self._ui = UI(self._city)

    def start(self) -> None:
        self._timer.reset()
        while not self._done:
            for user_event in pygame.event.get():
                self._event_dispatcher.dispatch(user_event)
            self._city.simulate()
            self._renderer.render(self._city, self._ui)

    def toggle_grid(self) -> None:
        self._ui.toggle_grid()

    def toggle_buildings_window(self) -> None:
        self._ui.toggle_buildings_window()

    def save_game(self) -> None:
        pass

    def end_game(self) -> None:
        self.save_game()
        self._done = True
