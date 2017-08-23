import pygame
from pygame.event import Event

from events.user_events.exit_event import ExitEvent
from events.user_events.toggle_buildings_window_event import ToggleBuildingsWindowEvent
from events.user_events.toggle_grid_event import ToggleGridEvent


class EventDispatcher(object):

    def __init__(self, game_object):
        self._game_object = game_object

    def dispatch(self, event: Event) -> None:
        event_handler = None
        if event.type == pygame.QUIT:
            event_handler = ExitEvent()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                event_handler = ToggleGridEvent()
            if event.key == pygame.K_b:
                event_handler = ToggleBuildingsWindowEvent()

        if event_handler is not None:
            event_handler.handle(self._game_object)
