from abc import abstractmethod
from typing import Tuple, Union

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from rendering.colors import Colors
from rendering.fonts import Fonts


class UIComponent(object):

    def __init__(self, position: Rect, description: Union[str, None]):
        self.position = position
        self.description = description

    @abstractmethod
    def render(self, screen: Surface) -> None:
        pass

    def render_description(self, screen: Surface, position: Tuple) -> None:
        font = Fonts.MEDIUM_FONT
        font_size = font.size(self.description)
        position_rectangle = (position[0], position[1] - font_size[1], font_size[0] + 4, font_size[1] + 4)
        pygame.draw.rect(screen, Colors.White, position_rectangle, 0)
        pygame.draw.rect(screen, Colors.Black, position_rectangle, 1)

        label = font.render(self.description, 1, Colors.Blue)
        screen.blit(label, (position[0] + 2, position[1] - font_size[1] + 2))

    @abstractmethod
    def handle_mouse_down(self, game, position: Tuple) -> None:
        pass

    def handle_mouse_over(self, screen: Surface, position: Tuple) -> None:
        if self.description is not None:
            self.render_description(screen, position)

    @abstractmethod
    def handle_mouse_up(self, game, position: Tuple) -> None:
        pass

    @abstractmethod
    def is_at(self, position: Tuple) -> bool:
        pass
