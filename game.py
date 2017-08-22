import pygame

from city.city import City
from constants import GameSettings
from events.user_events.event_dispatcher import EventDispatcher
from rendering.renderer import Renderer
from timing.game_timer import GameTimer


class Game(object):

    def __init__(self):
        self._done = False
        self._event_dispatcher = EventDispatcher(self)
        self._renderer = Renderer(GameSettings.SCREEN_WIDTH, GameSettings.SCREEN_HEIGHT)
        self._timer = GameTimer()
        self._city = City()  # TODO: this should be loaded from somewhere -> introduce save/load system

    def start(self) -> None:
        pygame.init()

        self._timer.reset()
        while not self._done:
            for user_event in pygame.event.get():
                self._event_dispatcher.dispatch(user_event)
            self._city.simulate()
            self._renderer.render(self._city)

    def save_game(self) -> None:
        pass

    def end_game(self) -> None:
        self.save_game()
        self._done = True
