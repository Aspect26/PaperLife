from typing import Tuple

import pygame

from city.objects.buildings.building import Building
from game.constants import GameSettings
from game.state import PlacingNewBuildingState
from rendering.colors import Colors
from ui.toolbars.top_toolbar import TopToolbar
from ui.windows.buildings_window import BuildingsWindow


class UI:
    def __init__(self, game):
        self._GRID_LINE_COLOR = Colors.LightGray
        self._show_grid = False
        self._game = game
        self._active_ui_components = [TopToolbar(self._game.get_city())]
        self._buildings_window = None

    def handle_mouse_down(self, position: Tuple) -> None:
        for component in reversed(self._active_ui_components):
            if component.position.collidepoint(position):
                component.handle_mouse_down(self._game, position)
                break

    def handle_mouse_up(self, position: Tuple) -> None:
        for component in reversed(self._active_ui_components):
            if component.position.collidepoint(position):
                component.handle_mouse_up(self._game, position)
                break

    def render(self, screen: pygame.Surface) -> None:
        if type(self._game.get_state()) is PlacingNewBuildingState:
            self._render_building_hitbox(screen, self._game.get_state().building)
        if self._show_grid or type(self._game.get_state()) is PlacingNewBuildingState:
            self._render_grid(screen)
        for ui_component in self._active_ui_components:
            ui_component.render(screen)
        mouse_position = pygame.mouse.get_pos()
        for ui_component in self._active_ui_components:
            if ui_component.is_at(mouse_position):
                ui_component.handle_mouse_over(screen, mouse_position)

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
        self._render_occupied_fields(screen)

    def _render_occupied_fields(self, screen: pygame.Surface) -> None:
        size = GameSettings.Game.FIELD_SIZE
        occupation_surface = pygame.Surface((GameSettings.Screen.WIDTH, GameSettings.Screen.HEIGHT))
        occupation_surface.set_alpha(128)
        for x in range(0, 50, 1):
            for y in range(0, 50, 1):
                if self._game.get_city().is_field_occupied((x, y)):
                    pygame.draw.rect(occupation_surface, Colors.Red, (x * size, y * size, size, size), 0)

        screen.blit(occupation_surface, (0, 0))

    def _render_building_hitbox(self, screen: pygame.Surface, building: Building):
        position = pygame.mouse.get_pos()
        field_size = GameSettings.Game.FIELD_SIZE
        grid_position = int(position[0] / field_size) * field_size, int(position[1] / field_size) * field_size

        hitbox_surface = pygame.Surface((building.width * field_size, building.height * field_size))
        hitbox_surface.fill(Colors.Green)
        hitbox_surface.set_alpha(128)
        building_picture = pygame.image.load(building.image_path)
        building_picture = pygame.transform.scale(building_picture, (
            building.width * GameSettings.Game.FIELD_SIZE, building.height * GameSettings.Game.FIELD_SIZE))
        hitbox_surface.blit(building_picture, (0, 0))
        screen.blit(hitbox_surface, (grid_position[0], grid_position[1]))
