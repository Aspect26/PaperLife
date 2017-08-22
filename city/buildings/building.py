from constants import GameSettings


class Building(object):

    def __init__(self, rent, rent_time, city, x, y, image_file):
        self._rent = rent
        self._rent_time = rent_time
        self._city = city
        self._x = x
        self._y = y
        self._image_path = GameSettings.Paths.Images.Buildings + image_file

    @property
    def rent(self):
        return self._rent

    @property
    def rent_time(self):
        return self._rent_time

    @property
    def city(self):
        return self._city

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def image_path(self):
        return self._image_path
