from abc import abstractmethod
from typing import Tuple

from pygame.rect import Rect
from pygame.surface import Surface


class UIComponent(object):

    def __init__(self, position: Rect):
        self.position = position

    @abstractmethod
    def render(self, screen: Surface) -> None:
        pass

    @abstractmethod
    def handle_mouse_down(self, game, position: Tuple) -> None:
        pass

    @abstractmethod
    def handle_mouse_up(self, game, position: Tuple) -> None:
        pass
