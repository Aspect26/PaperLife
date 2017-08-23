from constants import GameSettings
from ui.window.window import Window


class BuildingsWindow(Window):
    def __init__(self):
        self._MARGIN = 10
        self._WIDTH = 200
        super().__init__((GameSettings.Screen.WIDTH - self._MARGIN - self._WIDTH, self._MARGIN),
                         (self._WIDTH, GameSettings.Screen.HEIGHT - 2 * self._MARGIN))
