import pygame

from city.city import City
from game.constants import GameSettings
from ui.window.buildings_window import BuildingsWindow


class UI:

    def __init__(self, city: City):
        self._GRID_LINE_COLOR = (230, 230, 230)
        self._FONT_NAME = 'monospace'
        self._LARGE_FONT = pygame.font.SysFont(self._FONT_NAME, 15)
        self._show_grid = False
        self._city = city
        self._active_ui_components = []

        self._buildings_window = None

    def render(self, screen: pygame.Surface) -> None:
        if self._show_grid:
            self._render_grid(screen)
        for ui_component in self._active_ui_components:
            ui_component.render(screen)
        self._render_money(screen)

    def toggle_grid(self) -> None:
        self._show_grid = not self._show_grid

    def toggle_buildings_window(self) -> None:
        if self._buildings_window is not None:
            self._active_ui_components.remove(self._buildings_window)
            self._buildings_window = None
        else:
            self._buildings_window = BuildingsWindow()
            self._active_ui_components.append(self._buildings_window)

    def _render_grid(self, screen: pygame.Surface) -> None:
        width = GameSettings.Screen.WIDTH
        height = GameSettings.Screen.HEIGHT
        size = GameSettings.Game.FIELD_SIZE

        for x in range(0, width, size):
            pygame.draw.line(screen, self._GRID_LINE_COLOR, (x, 0), (x, height))
        for y in range(0, height, size):
            pygame.draw.line(screen, self._GRID_LINE_COLOR, (0, y), (width, y))

    # TODO: this will be in top toolbar at some time
    def _render_money(self, screen: pygame.Surface) -> None:
        label = self._LARGE_FONT.render('Money: ' + str(self._city.get_money()) + '€', 1, (0, 80, 200))
        screen.blit(label, (10, 10))
