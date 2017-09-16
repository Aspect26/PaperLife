from typing import Tuple, Union

from pygame.rect import Rect
from pygame.surface import Surface

from ui.component import UIComponent


class RectangularComponent(UIComponent):

    def __init__(self, position: Rect, description: Union[str, None]):
        super().__init__(position, description)

    def render(self, screen: Surface) -> None:
        pass

    def handle_mouse_up(self, game, position: Tuple) -> None:
        pass

    def handle_mouse_down(self, game, position: Tuple) -> None:
        pass

    def is_at(self, position: Tuple) -> bool:
        return self.position.collidepoint(position)
