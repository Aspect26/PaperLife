from pygame.rect import Rect

from game.constants import GameSettings
from game.data import get_purchasable_buildings
from ui.buttons.building_button import BuildingButton
from ui.windows.window import Window


class BuildingsWindow(Window):
    def __init__(self):
        self._MARGIN = 10
        self._WIDTH = 200
        super().__init__(Rect(GameSettings.Screen.WIDTH - self._MARGIN - self._WIDTH, self._MARGIN, self._WIDTH,
                              GameSettings.Screen.HEIGHT - 2 * self._MARGIN))

        self._create_building_buttons()

    def _create_building_buttons(self):
        current_y = 10
        current_index = 0
        for building_type in get_purchasable_buildings():
            current_x = 10 if (current_index % 2) == 0 else 105
            button = BuildingButton((current_x, current_y), building_type)
            self.add_component(button)
            current_y += 95 * (current_index % 2)
            current_index += 1
