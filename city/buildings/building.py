from typing import Tuple

from pygame.rect import Rect

from game.constants import GameSettings


class Building(object):

    def __init__(self, rent: int, rent_time: int, city, position: Rect, image_file: str, title: str):
        self._rent = rent
        self._rent_time = rent_time
        self._city = city
        self._position = position
        self._image_path = GameSettings.Paths.Images.Buildings + image_file
        self._title = title

    @property
    def rent(self) -> int:
        return self._rent

    @property
    def rent_time(self) -> int:
        return self._rent_time

    @property
    def city(self):
        return self._city

    @property
    def x(self) -> int:
        return self._position.x

    @property
    def y(self) -> int:
        return self._position.y

    @property
    def width(self) -> int:
        return self._position.width

    @property
    def height(self) -> int:
        return self._position.height

    @property
    def image_path(self) -> str:
        return self._image_path

    @property
    def title(self) -> str:
        return self._title

    def set_position(self, position: Tuple) -> None:
        self._position.x = position[0]
        self._position.y = position[1]
