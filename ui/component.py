from abc import abstractmethod
from typing import Tuple

from pygame.surface import Surface


class UIComponent(object):

    def __init__(self, position: Tuple, size: Tuple):
        self.position = position
        self.size = size

    @abstractmethod
    def render(self, screen: Surface) -> None:
        pass
