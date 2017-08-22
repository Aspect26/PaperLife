import pygame
from pygame.event import Event

from events.user_events.exit_event import ExitEvent


class EventDispatcher(object):

    def __init__(self, game_object):
        self._game_object = game_object

    def dispatch(self, event: Event) -> None:
        if event.type == pygame.QUIT:
            ExitEvent().handle(self._game_object)
