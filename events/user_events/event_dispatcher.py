import pygame
from pygame.event import Event

from events.user_events.exit_event import ExitEvent
from events.user_events.toggle_grid_event import ToggleGridEvent


class EventDispatcher(object):

    def __init__(self, game_object):
        self._game_object = game_object

    def dispatch(self, event: Event) -> None:
        if event.type == pygame.QUIT:
            ExitEvent().handle(self._game_object)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                ToggleGridEvent().handle(self._game_object)
